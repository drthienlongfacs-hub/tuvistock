import re
import sys
from pathlib import Path

scripts_dir = Path(__file__).resolve().parent
sys.path.append(str(scripts_dir))
import tuvi_engine as te

def extract_score(text):
    match = re.search(r'\*\*([\d.]+)\/10\*\*', text)
    if match:
        return float(match.group(1))
    match = re.search(r'([\d.]+)\/10', text)
    if match:
        return float(match.group(1))
    return 5.0

def fix_file(file_path):
    print(f"Fixing {file_path}...")
    content = Path(file_path).read_text(encoding='utf-8')
    
    # We need to find the blocks that look like this:
    # ##### 9-CHIỀU ĐỊNH LƯỢNG (Engine v3.0)\n...\n| | | | **TỔNG** | | ...
    # Wait, the new 9-chiều table has a line starting with '| | **TỔNG Additive** |'
    # The old table has a line starting with '| | | | **TỔNG** |'
    # Actually, we can use a more robust approach. We can split the file by months.
    
    out_lines = []
    lines = content.split('\n')
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
            # Collect lines until we see the end of the old table
            block_lines = []
            while i < len(lines) and not line.startswith('##### HỆ QUY CHIẾU'):
                block_lines.append(lines[i])
                i += 1
                if i < len(lines):
                    line = lines[i]
            
            # Now we have the whole block. Unless it's Month 1 which is already correct.
            block_text = '\n'.join(block_lines)
            if 'TỔNG Additive' in block_text and 'TỔNG NPL' in block_text and '| Chiều | Cung | Sao chính |' not in block_text:
                # This is already a clean 9-chiều table (like T1)
                out_lines.extend(block_lines)
                continue
                
            # Otherwise, we parse the old table from this block to get the 5 scores
            s1 = s2 = s3_old = s4_old = s5_old = 5.0
            r1 = r2 = r3 = r4 = r5 = "..."
            
            for l in block_lines:
                if 'Bản cung' in l:
                    s1 = extract_score(l)
                    parts = l.split('|')
                    if len(parts) > 3: r1 = parts[3].strip()
                elif 'Xung chiếu' in l:
                    s2 = extract_score(l)
                    parts = l.split('|')
                    if len(parts) > 3: r2 = parts[3].strip()
                elif 'Tam hợp' in l:
                    s3_old = extract_score(l)
                    parts = l.split('|')
                    if len(parts) > 3: r3 = parts[3].strip()
                elif 'Nhị hợp' in l:
                    s4_old = extract_score(l)
                    parts = l.split('|')
                    if len(parts) > 3: r4 = parts[3].strip()
                elif 'Giáp' in l:
                    s5_old = extract_score(l)
                    parts = l.split('|')
                    if len(parts) > 3: r5 = parts[3].strip()
            
            base1 = s1
            base2 = round((s2 + s3_old) / 2, 1) # Tam chiếu
            base5 = s4_old # Proxy for Tứ Hóa LN
            base6 = 5.0
            base7 = s5_old # Giáp cung
            
            base_scores = {1: base1, 2: base2, 5: base5, 6: base6, 7: base7}
            
            # Compute new engine scores
            res = te.compute_month_score(current_month, base_scores)
            s = res['scores']
            
            d1 = r1
            d2 = f"{r2} (Xung), {r3} (Tam)"
            chu_khach_txt = "Chủ suy Khách thịnh" if s[3] < 5 else "Chủ lấn Khách" if s[3] > 5 else "Chủ Khách cân bằng"
            thai_tue_txt = res['thai_tue']
            d5 = f"Nhị Hợp phụ trợ: {r4}"
            d7 = r5
            d8 = f"{res['climate']} → {res['dung_than']} (EA09 ⚠️)"
            d9 = f"(EA11 ⚠️)"
            
            new_table = f"""##### 9-CHIỀU ĐỊNH LƯỢNG (Engine v3.0)

| # | Chiều | Trọng số | Điểm | Chi tiết |
|:---:|---|:---:|:---:|---|
| **①** | **Bản Cung** | 20% | **{s[1]:.1f}/10** | {d1} |
| **②** | **Tam Chiếu** | 15% | **{s[2]:.1f}/10** | {d2} |
| **③** | **Chủ-Khách** | 12% | **{s[3]:.1f}/10** | {chu_khach_txt} |
| **④** | **Thái Tuế** | 12% | **{s[4]:.1f}/10** | {thai_tue_txt} |
| **⑤** | **Tứ Hóa LN** | 10% | **{s[5]:.1f}/10** | {d5} |
| **⑥** | **Lưu Nguyệt** | 8% | **{s[6]:.1f}/10** | Cần inject từ SOT scan |
| **⑦** | **Giáp cung** | 3% | **{s[7]:.1f}/10** | {d7} |
| **⑧** | **Điều Hầu** 🆕 | 10% | **{s[8]:.1f}/10** | {d8} |
| **⑨** | **Khí Sắc** 🆕 | 10% | **{s[9]:.1f}/10** | {d9} |
| | **TỔNG Additive** | 100% | **{res['additive_total']:.1f}/10** | Phương pháp cộng tuyến tính |
| | **TỔNG NPL** | — | **{res['multiplicative_total']:.1f}/10** | Phương pháp nhân lũy thừa [experimental] |
| | **Confidence** | — | `[{res['confidence']}]` | Rule R-16 Anti-Bias |

> ⚠️ **Evidence gate:** TVĐS core = provisional (EA10 pending), NPL = experimental (VN01 pending)
> 📌 Scores ①②⑤⑥⑦ được lấy từ dữ liệu 5-chiều SOT cũ, tích hợp vào engine.

"""
            out_lines.extend(new_table.split('\n'))
            continue
            
        out_lines.append(line)
        i += 1
        
    Path(file_path).write_text('\n'.join(out_lines), encoding='utf-8')
    print(f"Successfully fixed {file_path}")

fix_file('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md')
fix_file('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md')
