import os
import re

# Dữ liệu Khách-Chủ và Thái Tuế của Mệnh Nhâm Thân (Kiếm Phong Kim) qua 12 tháng (Dần -> Sửu)
CLASSIC_DATA = {
    1: {
        "thai_tue": "**Thế Tuế Phá (Nghịch Cảnh):** Bất mãn, nhiều trở ngại, cần kiên nhẫn chống đối lại nghịch cảnh.",
        "chu_khach": "**Chủ lấn Khách:** Bản cung (Cự Dương Vượng) đè bẹp đối cung (VCD). Nắm hoàn toàn lợi thế chủ động đàm phán."
    },
    2: {
        "thai_tue": "**Thế Long Đức (Chịu Thiệt):** Nhẫn nhịn, hiền hòa, lấy đức thu phục người, chấp nhận thiệt thòi bước đầu.",
        "chu_khach": "**Chủ Khách giằng co:** Bản cung (Tướng Hãm) và đối cung (Liêm Phá Hãm) đều bất ổn. Hoàn cảnh và đối tác đều mang mầm mống phá hoại."
    },
    3: {
        "thai_tue": "**Thế Bạch Hổ (Chính Danh):** Hành động quang minh chính đại, oai phong nhưng gánh vác nhiều mệt mỏi, áp lực.",
        "chu_khach": "**Chủ lấn Khách:** Bản cung (Cơ Lương Vượng) thắng thế đối cung (VCD). Nguồn lực nội tại của tháng vượt trội."
    },
    4: {
        "thai_tue": "**Thế Phúc Đức (Khôn Ngoan):** Hoàn cảnh ưu ái, thông minh sắc sảo nhưng cẩn trọng Thiên Không làm cho ảo tưởng.",
        "chu_khach": "**Chủ lấn cực mạnh Khách:** Bản cung (Tử Sát Miếu) áp đảo đối cung (Thiên Phủ Bình). Ngoại cảnh tháng này ép người, sức ép quyền lực khổng lồ."
    },
    5: {
        "thai_tue": "**Thế Điếu Khách (Nghịch Cảnh):** Bất mãn, nghịch lý, dễ lao tâm khổ tứ hoặc tiêu hao vì bất đồng quan điểm.",
        "chu_khach": "**Khách lấn Chủ:** Bản cung (VCD) bị đối cung (Đồng Âm Vượng) lấn lướt. Bị động, đối tác/người khác nắm quyền định đoạt."
    },
    6: {
        "thai_tue": "**Thế Trực Phù (Chịu Thiệt):** Mệt mỏi, nhân nhượng, làm nhiều hưởng ít nhưng an toàn, tránh bão.",
        "chu_khach": "**Khách lấn Chủ:** Bản cung (VCD) bị đối cung (Vũ Tham Miếu) chi phối. Dòng tiền đến từ ngoại lực, thụ động phụ thuộc hoàn cảnh."
    },
    7: {
        "thai_tue": "**Thế Thái Tuế (Chính Danh):** Danh chính ngôn thuận, cực kỳ thuận lý. Hành động được trời đất ủng hộ, tự tin quyết đoán.",
        "chu_khach": "**Khách lấn Chủ:** Bản cung (VCD) lép vế trước đối cung (Cự Dương Vượng). Cần dựa mượn lực từ người khác, không tự quyết được."
    },
    8: {
        "thai_tue": "**Thế Thiếu Dương (Khôn Ngoan):** Thông minh xuất chúng, nắm bắt cơ hội nhanh, nhưng đề phòng cái bẫy của Thiên Không dòm ngó.",
        "chu_khach": "**Khách Chủ giằng co:** Bản cung (Liêm Phá Hãm) đối chọi (Tướng Hãm). Hoàn cảnh hỗn loạn, không bên nào áp đảo hoàn toàn."
    },
    9: {
        "thai_tue": "**Thế Tang Môn (Nghịch Cảnh):** Tâm lý u buồn, chống đối, nghịch thiên lý. Đòi hỏi nghị lực lớn để vượt qua áp lực.",
        "chu_khach": "**Khách lấn Chủ:** Bản cung (VCD) phụ thuộc đối cung (Cơ Lương Vượng). Đối tác hoặc hoàn cảnh quyết định cuộc chơi, bản thân bị kéo theo."
    },
    10: {
        "thai_tue": "**Thế Thiếu Âm (Chịu Thiệt):** Nhường nhịn, hiền từ, không bon chen. Đôi khi chấp nhận lùi một bước để tiến ba bước.",
        "chu_khach": "**Khách lấn Chủ:** Bản cung (Thiên Phủ Bình) bị đối cung (Tử Sát Miếu) đè ép. Khách hàng/đối thủ mang tính sát phạt, bản thân phải cố thủ."
    },
    11: {
        "thai_tue": "**Thế Quan Phù (Chính Danh):** Hành động dựa trên lý trí, pháp lý, sự rõ ràng. Rất thuận lợi cho giấy tờ, hợp đồng.",
        "chu_khach": "**Chủ lấn Khách:** Bản cung (Đồng Âm Vượng) nắm lợi thế trước đối cung (VCD). Sự mềm mỏng, linh hoạt làm chủ cục diện."
    },
    12: {
        "thai_tue": "**Thế Tử Phù / Đào Hoa (Khôn Ngoan):** Cẩn trọng đào hoa hoặc những lợi ích phù phiếm. Thông minh nhưng dễ lạc lối, sai định hướng.",
        "chu_khach": "**Chủ lấn Khách:** Bản cung (Vũ Tham Miếu) đè bẹp (VCD). Quyền lực tài chính và dục vọng kiểm soát hoàn toàn tháng này."
    }
}

def inject_theory(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out_lines = []
    current_month = None
    
    for i, line in enumerate(lines):
        # Xác định tháng hiện tại (Header có chữ Tháng 1, Tháng 2, ...)
        month_match = re.search(r'THÁNG\s+(\d+)', line)
        if month_match:
            current_month = int(month_match.group(1))
            
        out_lines.append(line)
        
        # Nếu gặp dòng Phi Tinh Kích Hoạt, ta sẽ chèn System Kinh Diển vào NGAY TRƯỚC nó
        # Với điều kiện chưa được báo cáo (tránh lặp)
        if line.startswith("##### PHI TINH KÍCH HOẠT") and current_month:
            # Check xem trước đó đã có HỆ QUY CHIẾU KINH ĐIỂN chưa
            if i > 5 and "##### HỆ QUY CHIẾU KINH ĐIỂN" in "".join(lines[i-15:i]):
                pass
            else:
                data = CLASSIC_DATA.get(current_month)
                if data:
                    inject_text = "\n##### HỆ QUY CHIẾU KINH ĐIỂN (Trần Đoàn & Thiên Lương)\n"
                    inject_text += f"- **Thiên Lương (Vòng Thái Tuế):** {data['thai_tue']}\n"
                    inject_text += f"- **Trần Đoàn (Chủ - Khách):** {data['chu_khach']}\n\n"
                    
                    # Insert right before the current line (which is already appended, so inject BEFORE the last appended element)
                    out_lines.pop()
                    out_lines.append(inject_text)
                    out_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print(f"✅ Đã inject lý thuyết Kinh Điển vào: {os.path.basename(filepath)}")

# Run for both files
base_dir = "/Users/mac/Desktop/TuViStock/02_luan_giai/core"
inject_theory(os.path.join(base_dir, "luan_giai_12_thang_2026.md"))
inject_theory(os.path.join(base_dir, "luan_giai_12_thang_2027.md"))
