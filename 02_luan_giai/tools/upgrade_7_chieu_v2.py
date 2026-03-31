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
        "chu_khach_score": 9.0, "chu_khach_desc": "Chủ lấn cực mạnh Khách (Áp lực bủa vây)"},
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
        "chu_khach_score": 3.0, "chu_khach_desc": "Khách lấn Chủ (Sức ép từ sát phạt)"},
    11: {"thai_tue_score": 9.0, "thai_tue_desc": "Quan Phù (Lý trí, pháp lý soi đường)", 
        "chu_khach_score": 9.0, "chu_khach_desc": "Chủ lấn Khách (Quyền chủ động 100%)"},
    12: {"thai_tue_score": 5.0, "thai_tue_desc": "Tử Phù (Cẩn thận sa đà phù phiếm)", 
        "chu_khach_score": 9.0, "chu_khach_desc": "Chủ lấn Khách (Đè bẹp đối thủ)"}
}

def extract_score(col_str):
    m = re.search(r'\*\*([\d\.]+)/10\*\*', col_str)
    if m:
        return float(m.group(1))
    return 5.0

def upgrade_7_chieu_v2(original_file, output_file):
    # Dọn dẹp HỆ QUY CHIẾU KINH ĐIỂN cũ nếu lỡ inject từ P.Án B
    with open(original_file, 'r', encoding='utf-8') as f:
        raw_lines = f.readlines()
        
    lines = []
    skip = 0
    for line in raw_lines:
        if skip > 0:
            skip -= 1
            continue
        if "##### HỆ QUY CHIẾU KINH ĐIỂN" in line:
            skip = 2
            continue
        lines.append(line)

    out_lines = []
    current_month = None
    in_table = False
    row_idx = 0
    table_scores = {}

    for i, line in enumerate(lines):
        # Month detection
        month_match = re.search(r'THÁNG\s+(\d+)', line)
        if month_match:
            current_month = int(month_match.group(1))
            
        if "##### 5-CHIỀU ĐỊNH LƯỢNG" in line:
            line = line.replace("5-CHIỀU ĐỊNH LƯỢNG", "BẢNG 7-CHIỀU ĐỊNH LƯỢNG KINH ĐIỂN")
            in_table = True
            row_idx = 0
            table_scores = {}
            out_lines.append(line)
            continue

        if in_table:
            if "#####" in line and "7-CHIỀU" not in line:
                in_table = False
            else:
                parts = line.split('|')
                if len(parts) >= 4 and "---" not in line and "Tỉ trọng" not in line and "Chiều" not in line and "TỔNG" not in line:
                    row_idx += 1
                    table_scores[row_idx] = extract_score(line)
                    
                    if row_idx == 1:
                        line = re.sub(r'40%', '25%', line)
                    elif row_idx == 2:
                        line = re.sub(r'30%', '20%', line)
                    elif row_idx == 3:
                        line = re.sub(r'20%', '15%', line)
                    elif row_idx == 4:
                        line = re.sub(r'10%', '5%', line)
                    elif row_idx == 5:
                        # Ghi dòng số 5 hiện tại ra trước
                        out_lines.append(line)
                        
                        # Chèn thêm dòng 6 và 7
                        c_data = CLASSIC_DATA[current_month]
                        table_scores[6] = c_data["chu_khach_score"]
                        table_scores[7] = c_data["thai_tue_score"]
                        num_cols = len(parts) - 2
                        
                        if num_cols == 3:
                            row6 = f"| **(+) Chủ-Khách** | 15% | **{c_data['chu_khach_score']}/10** | {c_data['chu_khach_desc']} |\n"
                            row7 = f"| **(+) Thái Tuế** | 15% | **{c_data['thai_tue_score']}/10** | {c_data['thai_tue_desc']} |\n"
                        else:
                            row6 = f"| **(+) Chủ-Khách (15%)** | Trần Đoàn | Lợi thế | **{c_data['chu_khach_score']}/10** | {c_data['chu_khach_desc']} |\n"
                            row7 = f"| **(+) Thái Tuế (15%)** | Thiên Lương | Hành động | **{c_data['thai_tue_score']}/10** | {c_data['thai_tue_desc']} |\n"
                        out_lines.append(row6)
                        out_lines.append(row7)
                        line = None
                        
                elif "TỔNG" in line:
                    s1 = table_scores.get(1, 5.0)
                    s2 = table_scores.get(2, 5.0)
                    s3 = table_scores.get(3, 5.0)
                    s4 = table_scores.get(4, 5.0)
                    s5 = table_scores.get(5, 5.0)
                    s6 = table_scores.get(6, 5.0)
                    s7 = table_scores.get(7, 5.0)
                    
                    total = 0.25*s1 + 0.20*s2 + 0.15*s3 + 0.05*s4 + 0.05*s5 + 0.15*s6 + 0.15*s7
                    
                    # Thay thế giá trị tổng bằng regex
                    old_score_match = re.search(r'\*\*([\d\.]+)/10\*\*', line)
                    if old_score_match:
                        line = line.replace(old_score_match.group(0), f"**{total:.1f}/10**")
                    else:
                        for idx, p in enumerate(parts):
                            if "10" in p and "**" in p:
                                parts[idx] = f" **{total:.1f}/10** "
                                line = "|".join(parts)
                                break
                                
        if line is not None:
            out_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print(f"✅ Đã tạo Master: {os.path.basename(output_file)}")

base_dir = "/Users/mac/Desktop/TuViStock/02_luan_giai/core"
# Use original files to generate v7
upgrade_7_chieu_v2(os.path.join(base_dir, "luan_giai_12_thang_2026.md"), os.path.join(base_dir, "luan_giai_12_thang_2026_master_7_chieu.md"))
upgrade_7_chieu_v2(os.path.join(base_dir, "luan_giai_12_thang_2027.md"), os.path.join(base_dir, "luan_giai_12_thang_2027_master_7_chieu.md"))
