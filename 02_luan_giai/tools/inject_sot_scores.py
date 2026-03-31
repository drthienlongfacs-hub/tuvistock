import re
import sys
from pathlib import Path

# Add tools to sys.path to import tuvi_engine
scripts_dir = Path(__file__).resolve().parent
sys.path.append(str(scripts_dir))
import tuvi_engine as te
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file, score_tu_hoa_context

CUNG_TO_MONTH = {
    'Mão': 1, 'Thìn': 2, 'Tỵ': 3, 'Ngọ': 4, 'Mùi': 5, 'Thân': 6,
    'Dậu': 7, 'Tuất': 8, 'Hợi': 9, 'Tý': 10, 'Sửu': 11, 'Dần': 12
}

def parse_sot(sot_path):
    content = Path(sot_path).read_text(encoding='utf-8')
    cung_data = {}
    
    # Split by ### CUNG
    blocks = re.split(r'### CUNG \d+:', content)
    for block in blocks[1:]:
        m = re.match(r'\s*.*?—\s*([A-Z-À-Ỹa-z-à-ỹ]+)\s*\(', block)
        if not m: continue
        cung_name = m.group(1).strip()
        month = CUNG_TO_MONTH.get(cung_name)
        if not month: continue
        
        # Extract Hóa Tinh / Lưu Tinh
        hoa_luu = []
        lines = block.split('\n')
        for line in lines:
            if '|' in line and ('Hóa Tinh' in line or 'L.Hóa' in line or 'L.' in line):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) > 3:
                    star = parts[2]
                    # Clean markdown
                    star = star.replace('**', '').strip()
                    if 'Hóa ' in star or 'L.' in star:
                        hoa_luu.append(star)
        
        # Extract Ngũ Hành tương tác:
        ngu_hanh_match = re.search(r'\*\*Ngũ Hành(?: tương tác)?:\*\*\s*(.*?)(?=\n\n|$)', block, re.DOTALL)
        ngu_hanh_text = ngu_hanh_match.group(1).replace('\n', ' ').strip() if ngu_hanh_match else ""
        
        cung_data[month] = {
            'cung': cung_name,
            'hoa_luu': hoa_luu,
            'ngu_hanh': ngu_hanh_text
        }
    return cung_data

def score_tu_hoa(hoa_luu_list):
    return score_tu_hoa_context(hoa_luu_list)

def score_ngu_hanh(ngu_hanh_text):
    if not ngu_hanh_text: return 5.0, "Tương tác trung tính"
    score = 5.0
    txt = ngu_hanh_text.lower()
    
    if 'sinh xuất' in txt or 'hao lực' in txt or 'bị khắc' in txt:
        score -= 1.0
    if 'sinh kim' in txt or 'cực vượng' in txt or 'được dưỡng' in txt or 'được sinh' in txt:
        score += 2.0
    if 'khắc' in txt and 'bị lừa' in txt:
        score -= 2.0
        
    score = max(1.0, min(10.0, score))
    # Summarize text
    summary = ngu_hanh_text[:60] + "..." if len(ngu_hanh_text) > 60 else ngu_hanh_text
    return score, summary

def inject_sot_into_file(file_path, sot_data):
    print(f"Injecting SOT data into {file_path}...")
    content = Path(file_path).read_text(encoding='utf-8')
    lines = content.split('\n')
    out_lines = []
    
    i = 0
    current_month = 1
    
    while i < len(lines):
        line = lines[i]
        
        m = re.search(r'THÁNG (\d+) ÂM LỊCH', line, re.IGNORECASE)
        if not m:
            m = re.search(r'THÁNG (\d+)', line, re.IGNORECASE)
        if m and line.startswith('### '):
            current_month = int(m.group(1))
            
        if line.startswith('##### 9-CHIỀU ĐỊNH LƯỢNG'):
            # Read block
            block_lines = []
            while i < len(lines) and not line.startswith('##### HỆ QUY CHIẾU'):
                block_lines.append(lines[i])
                i += 1
                if i < len(lines):
                    line = lines[i]
            
            # Now modify the block lines directly
            new_block = []
            s_dict = {}
            for l in block_lines:
                # Store old base scores for 1,2,3,4,7,8,9
                for dim in range(1, 10):
                    match = re.search(f'\\| \\*\\*(.)\\*\\* \\|.*?\\| \\*\\*(.*?)\/10', l)
                    if match and match.group(1) == chr(0x2460 + dim - 1): # ① is 0x2460
                        s_dict[dim] = float(match.group(2))
                
                if '| **⑤** |' in l:
                    # Inject 5
                    data = sot_data.get(current_month, {})
                    score5, txt5 = score_tu_hoa(data.get('hoa_luu', []))
                    s_dict[5] = score5
                    new_l = re.sub(r'\| \*\*([\d.]+)\/10\*\* \| (.*?)$', f'| **{score5:.1f}/10** | Tứ Hóa/Lưu tinh SOT: {txt5} |', l)
                    new_block.append(new_l)
                elif '| **⑥** |' in l:
                    # Inject 6
                    data = sot_data.get(current_month, {})
                    score6, txt6 = score_ngu_hanh(data.get('ngu_hanh', ''))
                    s_dict[6] = score6
                    new_l = re.sub(r'\| \*\*([\d.]+)\/10\*\* \| (.*?)$', f'| **{score6:.1f}/10** | Tương tác SOT: {txt6} |', l)
                    new_block.append(new_l)
                elif '| **TỔNG Additive** |' in l or '| **TỔNG NPL** |' in l or '| **Confidence** |' in l:
                    # Skip for now, will recalculate at the end of block
                    pass
                else:
                    new_block.append(l)
                    
            # Recalculate
            base_scores = {
                1: s_dict.get(1, 5.0),
                2: s_dict.get(2, 5.0),
                5: s_dict.get(5, 5.0),
                6: s_dict.get(6, 5.0),
                7: s_dict.get(7, 5.0)
            }
            res = te.compute_month_score(current_month, base_scores)
            
            # Append trailing table elements
            new_block.append(f"| | **TỔNG Additive** | 100% | **{res['additive_total']:.1f}/10** | Phương pháp cộng tuyến tính |")
            new_block.append(f"| | **TỔNG NPL** | — | **{res['multiplicative_total']:.1f}/10** | Phương pháp nhân lũy thừa [experimental] |")
            new_block.append(f"| | **Confidence** | — | `[{res['confidence']}]` | Rule R-16 Anti-Bias |")
            
            # Add existing notes trailing
            # Find index where table ends
            for l in block_lines:
                if l.startswith('>'):
                    new_block.append(l)
                elif l.strip() == '' and block_lines.index(l) > len(block_lines) - 4:
                    new_block.append(l)
                    
            out_lines.extend(new_block)
            continue

        out_lines.append(line)
        i += 1
        
    Path(file_path).write_text('\n'.join(out_lines), encoding='utf-8')
    apply_hoa_ky_guardrails_to_file(file_path)
    print(f"Done injecting SOT into {file_path}")

sot_path = '/Users/mac/Desktop/TuViStock/01_data_inventory/kiem_ke_tinh_ban_12_cung.md'
sot_data = parse_sot(sot_path)

inject_sot_into_file('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md', sot_data)
inject_sot_into_file('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md', sot_data)
