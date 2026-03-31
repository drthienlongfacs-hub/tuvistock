import os
import re
import shutil

CLASSIC_DATA = {
    1: {"thai_tue_score": 3.0, "thai_tue_desc": "Tuế Phá (Nghịch cảnh, chống đối)", 
        "chu_khach_score": 9.0, "chu_khach_desc": "Chủ lấn Khách (Tuyệt đối chủ động)"},
    2: {"thai_tue_score": 6.0, "thai_tue_desc": "Long Đức (Nhẫn nhịn, nhân từ)", 
        "chu_khach_score": 5.0, "chu_khach_desc": "Chủ Khách giằng co (Hỗn loạn)"},
    3: {"thai_tue_score": 9.0, "thai_tue_desc": "Bạch Hổ (Chính Danh, Quang minh)", 
        "chu_khach_score": 9.0, "chu_khach_desc": "Chủ lấn Khách (Ngoại lực yếu hơn nội lực)"},
    4: {"thai_tue_score": 5.0, "thai_tue_desc": "Phúc Đức (Khôn ngoan, coi chừng ảo tưởng)", 
        "chu_khach_score": 9.0, "chu_khach_desc": "Chủ lấn cực mạnh Khách (Áp lực bủa vây)"}, # Note: In TuVi, month is Chu, Di is Khach. Ty is Di -> Ty is Chu. Ty (Tu Sat) > Hoi (Phu)
    5: {"thai_tue_score": 3.0, "thai_tue_desc": "Điếu Khách (Bất mãn, tiêu hao)", 
        "chu_khach_score": 2.0, "chu_khach_desc": "Khách lấn Chủ (Bị động vòng ngoài)"},
    6: {"thai_tue_score": 6.0, "thai_tue_desc": "Trực Phù (Làm nhiều hưởng ít, an thân)", 
        "chu_khach_score": 2.0, "chu_khach_desc": "Khách lấn Chủ (Ngoại cảnh quyết định)"},
    7: {"thai_tue_score": 9.0, "thai_tue_desc": "Thái Tuế (Chính Danh, Thuận Thiên lý)", 
        "chu_khach_score": 2.0, "chu_khach_desc": "Khách lấn Chủ (Phải dựa vào người khác)"},
    8: {"thai_tue_score": 5.0, "thai_tue_desc": "Thiếu Dương (Thông minh bộc phát)", 
        "chu_khach_score": 5.0, "chu_khach_desc": "Chủ Khách giằng co (Thiếu dứt khoát)"},
    9: {"thai_tue_score": 3.0, "thai_tue_desc": "Tang Môn (Buồn lo, nghịch cảnh)", 
        "chu_khach_score": 2.0, "chu_khach_desc": "Khách lấn Chủ (Bản thân yếu thế)"},
    10: {"thai_tue_score": 6.0, "thai_tue_desc": "Thiếu Âm (Lùi 1 bước tiến 3 bước)", 
        "chu_khach_score": 3.0, "chu_khach_desc": "Khách lấn Chủ (Sức ép từ đối tượng sát phạt)"},
    11: {"thai_tue_score": 9.0, "thai_tue_desc": "Quan Phù (Lý trí, pháp lý soi đường)", 
        "chu_khach_score": 9.0, "chu_khach_desc": "Chủ lấn Khách (Quyền chủ động 100%)"},
    12: {"thai_tue_score": 5.0, "thai_tue_desc": "Tử Phù (Cẩn thận sa đà phù phiếm)", 
        "chu_khach_score": 9.0, "chu_khach_desc": "Chủ lấn Khách (Đè bẹp đối thủ)"}
}

def extract_score(col_str):
    m = re.search(r'([\d\.]+)/10', col_str)
    if m:
        return float(m.group(1))
    return 5.0 # fallback

def upgrade_7_chieu(original_file, output_file):
    with open(original_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out_lines = []
    current_month = None
    in_table = False
    skip_mode = False
    table_scores = {}
    table_buffer = []

    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Remove HỆ QUY CHIẾU KINH ĐIỂN injected earlier
        if "##### HỆ QUY CHIẾU KINH ĐIỂN" in line:
            # Skip this line and the next 4 lines
            i += 4
            continue
            
        # Detect month
        month_match = re.search(r'THÁNG\s+(\d+)', line)
        if month_match:
            current_month = int(month_match.group(1))
            
        # Transform Title
        if "##### 5-CHIỀU ĐỊNH LƯỢNG" in line:
            line = line.replace("5-CHIỀU ĐỊNH LƯỢNG", "7-CHIỀU TOÀN TRI (MASTER)")
            in_table = True
            table_scores = {}
            table_buffer = []

        if in_table:
            # Check if we hit the end of table
            if line.strip() == "" or "#####" in line and "7-CHIỀU" not in line:
                in_table = False
            else:
                parts = line.split('|')
                if len(parts) >= 4:
                    col1 = parts[1]
                    # Rewrite rows based on old indices
                    if "① Bản Cung" in col1:
                        table_scores[1] = extract_score(parts[3])
                        parts[2] = " 25% "
                        line = "|".join(parts)
                    elif "② Tam Chiếu" in col1:
                        table_scores[2] = extract_score(parts[3])
                        parts[2] = " 20% "
                        line = "|".join(parts)
                        out_lines.append(line)
                        
                        # INJECT NEW ROWS (3 and 4)
                        c_data = CLASSIC_DATA[current_month]
                        table_scores[3] = c_data["chu_khach_score"]
                        table_scores[4] = c_data["thai_tue_score"]
                        row3 = f"| **③ Chủ-Khách** (Trần Đoàn) | 15% | **{c_data['chu_khach_score']}/10** | {c_data['chu_khach_desc']} |\n"
                        row4 = f"| **④ Thái Tuế** (Thiên Lương) | 15% | **{c_data['thai_tue_score']}/10** | {c_data['thai_tue_desc']} |\n"
                        out_lines.append(row3)
                        out_lines.append(row4)
                        line = None # Prevent appending original line again at the end
                    elif "③ Tứ Hóa LN" in col1:
                        table_scores[5] = extract_score(parts[3])
                        line = line.replace("③ Tứ", "⑤ Tứ")
                        parts = line.split('|')
                        parts[2] = " 10% "
                        line = "|".join(parts)
                    elif "④ NH Can" in col1:
                        table_scores[6] = extract_score(parts[3])
                        line = line.replace("④ NH", "⑥ Lưu Nguyệt")
                        parts = line.split('|')
                        parts[2] = " 10% "
                        line = "|".join(parts)
                    elif "⑤ Giáp" in col1:
                        table_scores[7] = extract_score(parts[3])
                        line = line.replace("⑤ Giáp", "⑦ Giáp")
                        parts = line.split('|')
                        parts[2] = " 5% "
                        line = "|".join(parts)
                    elif "TỔNG" in col1:
                        # Recalculate
                        s1 = table_scores.get(1, 5.0)
                        s2 = table_scores.get(2, 5.0)
                        s3 = table_scores.get(3, 5.0)
                        s4 = table_scores.get(4, 5.0)
                        s5 = table_scores.get(5, 5.0)
                        s6 = table_scores.get(6, 5.0)
                        s7 = table_scores.get(7, 5.0)
                        
                        total = 0.25*s1 + 0.20*s2 + 0.15*s3 + 0.15*s4 + 0.10*s5 + 0.10*s6 + 0.05*s7
                        # Format total to 1 decimal place
                        parts[3] = f" **{total:.1f}/10** "
                        if "⭐" in line:
                            parts[3] += "⭐ "
                            parts[4] = parts[4].replace("⭐", "") # Clean up extra stars
                        line = "|".join(parts)
                        
        if line is not None:
            out_lines.append(line)
        i += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print(f"✅ Đã xuất bản Master 7-Chiều: {os.path.basename(output_file)}")

base_dir = "/Users/mac/Desktop/TuViStock/02_luan_giai/core"
upgrade_7_chieu(os.path.join(base_dir, "luan_giai_12_thang_2026.md"), os.path.join(base_dir, "luan_giai_12_thang_2026_master.md"))
upgrade_7_chieu(os.path.join(base_dir, "luan_giai_12_thang_2027.md"), os.path.join(base_dir, "luan_giai_12_thang_2027_master.md"))
