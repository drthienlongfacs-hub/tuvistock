import re
import sys
from pathlib import Path

# Add tools to sys.path to import tuvi_engine
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

def process_file(file_path):
    print(f"Processing {file_path}...")
    content = Path(file_path).read_text(encoding='utf-8')
    
    # We will find all blocks starting from '##### 5-CHIỀU ĐỊNH LƯỢNG' to the end of the table
    # Pattern: ##### 5-CHIỀU ĐỊNH LƯỢNG\n\n| Chiều | Cung | Sao chính | Điểm | NET |\n... (up to 'TỔNG')
    
    # We will iterate and replace them one by one. But wait, each month corresponds to a specific month number.
    # To find the month number, we can look backwards for 'THÁNG (\d+)' or assume sequential.
    
    # We can use regex to find the blocks
    pattern = r'##### \d-CHIỀU ĐỊNH LƯỢNG.*?\n\n(.*?)(\n\n|$)' # Match until double newline
    # Wait, the table might have a line with TỔNG.
    
    # Let's split by '##### 5-CHIỀU ĐỊNH LƯỢNG' or '##### 9-CHIỀU ĐỊNH LƯỢNG'
    # Actually finding the month number is better.
    # Let's read the file line by line and track the current month.
    
    lines = content.split('\n')
    new_lines = []
    
    current_month = None
    in_table = False
    table_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect month header
        # ### C.2 🟢 THÁNG 2 ÂM LỊCH ...
        # Or ### A.1 🟢 THÁNG 1 ...
        m = re.search(r'THÁNG (\d+) ÂM LỊCH', line, re.IGNORECASE)
        if not m:
            m = re.search(r'THÁNG (\d+)', line, re.IGNORECASE)
        if m and line.startswith('### '):
            current_month = int(m.group(1))
        
        if line.startswith('##### 5-CHIỀU ĐỊNH LƯỢNG'):
            in_table = True
            table_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith('##### '):
                table_lines.append(lines[i])
                i += 1
            
            if current_month is None:
                current_month = 1 # Fallback
            
            # Parse table_lines
            s1 = s2 = s3_old = s4_old = s5_old = 5.0
            r1 = r2 = r3 = r4 = r5 = "..."
            for tl in table_lines:
                if 'Bản cung' in tl:
                    s1 = extract_score(tl)
                    r1 = tl.split('|')[3].strip()
                elif 'Xung chiếu' in tl:
                    s2 = extract_score(tl)
                    r2 = tl.split('|')[3].strip()
                elif 'Tam hợp' in tl:
                    s3_old = extract_score(tl)
                    r3 = tl.split('|')[3].strip()
                elif 'Nhị hợp' in tl:
                    s4_old = extract_score(tl)
                    r4 = tl.split('|')[3].strip()
                elif 'Giáp' in tl:
                    s5_old = extract_score(tl)
                    r5 = tl.split('|')[3].strip()
            
            # Compute new base dimensions
            base1 = s1
            base2 = round((s2 + s3_old) / 2, 1) # Tam chiếu
            base5 = s4_old # Use old Nhị hợp for Tứ Hóa LN as proxy
            base6 = 5.0 # Lưu Nguyệt baseline
            base7 = s5_old # Giáp cung
            
            base_scores = {
                1: base1,
                2: base2,
                5: base5,
                6: base6,
                7: base7
            }
            
            # Run engine
            res = te.compute_month_score(current_month, base_scores)
            
            s = res['scores']
            
            # Reconstruct Details
            d1 = r1
            d2 = f"{r2} (Xung), {r3} (Tam)"
            d3 = "..." # Chu khach text (from old or generic)
            d4 = "..."
            d5 = r4 # Proxy
            d6 = "Cần inject từ SOT scan"
            d7 = r5
            
            # Try to populate d3, d4 from engine data
            thai_tue_txt = res['thai_tue']
            chu_khach_txt = "Chủ suy Khách thịnh" if s[3] < 5 else "Chủ lấn Khách" if s[3] > 5 else "Chủ Khách cân bằng"
            
            d8 = f"{res['climate']} → {res['dung_than']} (EA09 ⚠️)"
            d9 = f"(EA11 ⚠️)"
            
            # Build new table
            new_table = f"""##### 9-CHIỀU ĐỊNH LƯỢNG (Engine v3.0)

| # | Chiều | Trọng số | Điểm | Chi tiết |
|:---:|---|:---:|:---:|---|
| **①** | **Bản Cung** | 20% | **{s[1]}/10** | {d1} |
| **②** | **Tam Chiếu** | 15% | **{s[2]}/10** | {d2} |
| **③** | **Chủ-Khách** | 12% | **{s[3]}/10** | {chu_khach_txt} |
| **④** | **Thái Tuế** | 12% | **{s[4]}/10** | {thai_tue_txt} |
| **⑤** | **Tứ Hóa LN** | 10% | **{s[5]}/10** | Dựa trên Nhị Hợp cũ: {d5} |
| **⑥** | **Lưu Nguyệt** | 8% | **{s[6]}/10** | Cần inject từ SOT scan |
| **⑦** | **Giáp cung** | 3% | **{s[7]}/10** | {d7} |
| **⑧** | **Điều Hầu** 🆕 | 10% | **{s[8]}/10** | {d8} |
| **⑨** | **Khí Sắc** 🆕 | 10% | **{s[9]}/10** | {d9} |
| | **TỔNG Additive** | 100% | **{res['additive_total']:.1f}/10** | Phương pháp cộng tuyến tính |
| | **TỔNG NPL** | — | **{res['multiplicative_total']:.1f}/10** | Phương pháp nhân lũy thừa [experimental] |
| | **Confidence** | — | `[{res['confidence']}]` | Rule R-16 Anti-Bias |

> ⚠️ **Evidence gate:** TVĐS core = provisional (EA10 pending), NPL = experimental (VN01 pending)
> 📌 Scores ①②⑤⑥⑦ được lấy từ dữ liệu 5-chiều SOT cũ, tích hợp vào engine.
"""
            new_lines.extend(new_table.split('\n'))
            continue
            
        new_lines.append(line)
        i += 1
        
    Path(file_path).write_text('\n'.join(new_lines), encoding='utf-8')
    print(f"Done upgrading {file_path}")

process_file('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md')
process_file('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md')

