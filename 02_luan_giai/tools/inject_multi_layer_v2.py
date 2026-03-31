import re
import sys
from pathlib import Path
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file

MONTHLY_DATA = {
    1: {"cung": "Mão", "house": "Quan Lộc", "sao": "Tướng Hãm + Triệt"},
    2: {"cung": "Thìn", "house": "Nô Bộc", "sao": "Cơ Lương Miếu + Lộc Vượng"},
    3: {"cung": "Tỵ", "house": "Thiên Di", "sao": "Tử Sát Vượng"},
    4: {"cung": "Ngọ", "house": "Tật Ách", "sao": "VCD (mượn Đồng Âm)"},
    5: {"cung": "Mùi", "house": "Tài Bạch", "sao": "VCD + Hình Hãm"},
    6: {"cung": "Thân", "house": "Tử Tức", "sao": "VCD + Đại Hao"},
    7: {"cung": "Dậu", "house": "Phu Thê", "sao": "Liêm Phá Hãm"},
    8: {"cung": "Tuất", "house": "Huynh Đệ", "sao": "VCD + Không + Đà Đắc"},
    9: {"cung": "Hợi", "house": "Mệnh", "sao": "Thiên Phủ Đắc + Tuần"},
    10: {"cung": "Tý", "house": "Phụ Mẫu", "sao": "Đồng Âm Vượng + Kiếp Kình Hãm"},
    11: {"cung": "Sửu", "house": "Phúc / Thân", "sao": "Vũ Tham Miếu + Hóa Kỵ"},
    12: {"cung": "Dần", "house": "Điền Trạch", "sao": "Cự Dương Vượng + Triệt"}
}

IMPACT_ANALYSIS = {
    1: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Nguyệt hạn trùng phùng Đại Vận (Mão), kích hoạt toàn bộ năng lượng \"Phá cũ lập mới\" (Triệt). Dù tháng 1 khởi đầu bế tắc (Tướng Hãm), nhưng nhờ sự chống lưng của Lưu Niên (Cự Dương) ban phát cơ hội và Gốc Mệnh (Thiên Phủ) lo hậu cần tài chính vững chắc, sự bế tắc này thực chất là bước đà để anh đập bỏ luồng quy trình cũ (của dự án hoặc tư duy lâm sàng) nhằm xây lại hệ thống lớn hơn. Hạn trùng phùng nên động lực chuyển mình không thể cưỡng chế. Đau đớn trước, kiến thiết sau.",
    2: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Nguyệt hạn đi vào Nô Bộc (Cơ Lương Miếu + Lộc), kết nối hoàn hảo với Mệnh (Thủy sinh Mộc) tạo thành sức mạnh cộng hưởng dòng tiền từ đối tác. Đại Vận (Triệt) đang phá bỏ cái cũ, bắt buộc anh phải bấu víu vào mạng lưới Nô Bộc (Thìn) để tái thiết. Lưu niên (Cự Dương) soi rọi sinh khí toàn cục. Lực lượng cá nhân (Mệnh/Thân) đang bị Đại Vận (Triệt) kìm kẹp, do đó \"mượn lực\" bạn bè/cộng sự là chiến lược sinh tồn thông minh và hợp vi lượng tự nhiên nhất để bung Lộc Vượng.",
    3: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Tử Sát tại Tỵ là thế cờ Đế Vương xuất chinh. Tỵ (Thiên Di) xung chiếu trực tiếp với Hợi (Mệnh). Thiên Phủ (Mệnh) phùng Không/Tuần bị Tử Sát lấn lướt dữ dội. Nhìn quy chiếu: Đại Vận đang đập (Triệt), Gốc Mệnh đang thủ (Tuần), mà Nguyệt Hạn lại bung ra mãnh liệt (Tử Sát) tạo ra sự lệch pha không gian cực đoan. Lực đánh ra ngoài tháng này cực sắc bén, thu đoạt được ấn tín, nhưng Gốc (nội lực) đang rỗng do Triệt-Tuần kìm hãm. Áp lực dội ngược về sức khỏe sinh học là vô giá. Tuân thủ luật lệ: Đánh nhanh, thu quân gọn.",
    4: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Trục Tý-Ngọ. Tật Ách VCD vốn nhẹ gánh, nhưng do Đại Vận ở thế \"Tướng Hãm Triệt\" buộc anh hao tâm tổn trí liên miên các tháng trước, cộng thêm dư chấn bốc hoả từ Tử Sát (T3), sức bền của Mệnh (Kiếm Phong Kim) bị ngọn lửa cung Ngọ nung chảy. Lưu niên Dần (Cự Dương) hợp Hỏa cục (Dần-Ngọ-Tuất) thiêu đốt thêm. Bức tranh quy chiếu chỉ ra cấu trúc chốt chặn sinh học của anh đã quá tải. Bệnh tật ngầm hoặc stress tinh thần sẽ chớp lấy thời cơ Đại vận rỗng để bùng phát. Phải kích hoạt hạ nhiệt ngay lập tức.",
    5: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Gốc Thân (Sửu - Vũ Tham) xung chiếu rực lửa trực tiếp với Mùi. Khi Nguyệt hạn rơi thẳng vào Mùi, nó chọc ngoáy trục Sửu-Mùi (Mũi khoan Vũ Tham Kỵ đâm thẳng xuyên vào Gốc VCD Hình Hãm). Đại Vận (Mão Triệt) đứt gãy đòn bẩy không thể tải lực. Sự mất mát thanh khoản hoặc phiền phức pháp lý tháng 5 không phải xúi quẩy ngẫu nhiên, mà là sự kích nổ có toán học của trục Tài-Phúc gốc do Đại Vận không đủ lực che chắn. Lệnh phòng thủ thanh khoản bằng tiền mặt sẽ phát huy tác dụng đoạt lại sinh cơ mạng lưới.",
    6: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Cung Thân (Tử Tức) tạo Lục Hợp với cung Mão (Đại Vận). Việc thời gian dịch chuyển từ Mùi sang Thân chính thức cắt đứt rủi ro xung chiếu khốc liệt Sửu-Mùi (tháng 5). Thân là cung Đại Hao (năng lượng tái thiết). Mệnh (Hợi) và Đại Vận (Mão) gián tiếp quy tụ giúp phục hồi. Dấu vết Đại Hao ở đây được Gốc nâng đỡ chứng minh rằng: Đây là dòng tiền bung chi ra có chủ đích (đầu tư server, mua linh kiện AI, chi chắt nhóm đệ tử) chứ không phải mất mát vùi dập (Hình Hãm) như tháng 5. Chi tiền để kiến thiết hạ tầng Đại Vận lớn.",
    7: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Dậu xung chiếu trực diện và không nhân nhượng với Quan Lộc (Mão) - vốn là cung Đại Vận hiện tại (Tướng, Triệt). Sự kích hoạt của Nguyệt Hạn Dậu đánh dội sức sát thương thẳng vào Đại Vận Quan Lộc! Sự bất ổn về tình cảm/đối tác ruột (Liêm Phá) ở tháng này thực chất là hệ lụy dây chuyền nảy sinh gián tiếp từ việc Đại Vận Quan (Mão) đang bị Triệt phá cấu trúc làm lại, khiến đối tác hoang mang, hoài nghi anh. Lối thoát mâu thuẫn không cãi vã ở Dậu, mà nằm tại việc anh minh bạch hóa tiến trình đập-xây ở Mão để đối tác yên tâm.",
    8: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Tuất thuộc vòng Dần-Ngọ-Tuất, hợp cục Tam Hợp hùng mạnh với Niên Hạn 2026 (Dần - Cự Dương). Dù bản thân cung Tuất là VCD Không Vong tăm tối mờ mịt, nhưng được đại dương ánh sáng từ Lưu Niên rót thẳng vào. Mệnh (Thiên Phủ) vốn kín kẽ, Thân (Vũ Tham) ưa hành động trong bóng tối. Sự giao thoa này kích nổ: Ánh sáng Lưu Niên sẽ bí mật giải mã và bơm sức mạnh cho mạng lưới (Huynh Đệ) đánh những trận chiến ngầm. Gốc rễ Vũ Tham giật dây thu lợi nhuận trong sương mù. Dark Pool giao dịch chính thức kích hoạt.",
    9: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Nguyệt Hạn trùng khít Gốc Mệnh. Năng lượng lưu thông hồi quy 100%. Tuyệt sát: Mệnh có Tuần (kìm hãm) giáp lá cà với Đại Vận có Triệt (phá vỡ). Cục diện \"Tuần Triệt đương đầu\". Tuần ra sức dán chặt nắp kho Thiên Phủ bảo vệ, trong khi Triệt ép vỡ tư duy lột xác lôi ra. Tháng 9 trở thành \"Ground Zero\" giao tranh dữ dội nhất giữa Nội tại thủ thế an toàn (Phủ Tuần) và Yêu cầu của Đại vận quy mô lớn (Tướng Triệt thay máu). Tình trạng rườm rà hành chính, độ trễ và sốt ruột chỉ là hệ quả văng ra vì lớp giáp Tuần bị cào xé. Anh phải nhẫn nại đợi Triệt xuyên thủng xong vỏ bọc.",
    10: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Trục chiến lược Tý-Ngọ. Mệnh Hợi nhị hợp Dần (Niên hạn cự dương). Bộ Không Kiếp Kình ở cung Tý dội đồn dập áp lực cực lớn mệt mỏi từ tầng lớp lãnh đạo/sếp/phụ huynh. Nhưng bù trừ lại, Đồng Âm bản chất chứa đựng bộ rễ phân hóa mâu thuẫn gia đạo. Thân (Vũ Tham Sửu) nhị hợp khóa chặt cung Tý. Nhờ lực lượng Lưu Niên ánh sáng bảo phủ và phòng thủ nhị hợp Thân vững chãi, anh hội tụ đủ đinh lực để giải khuất mọi tàn dư bế tắc. Áp lực máu lửa tháng này chính là khoản vốn đổ vào rèn đúc tín nhiệm quyền lực thập kỷ.",
    11: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Nguyệt hạn đổ bộ trực tiếp thẳng xuống đỉnh đầu Gốc Thân. Vũ Tham Miếu vượng cất tiếng rú phát động toàn lực cỗ máy cày tiền, Hóa Kỵ (ám khí kích hoạt dội vào từ can Nhâm) tháp tùng khơi dậy sự phán xét hằn học của cộng đồng. Lưu niên Dần kề bên dốc sức tỏa hào quang. Khi nhát chém Triệt của Đại Vận đã dọn phẳng bãi chướng ngại vật mìn bẫy ở các tháng trước, vương quốc tài phiệt Vũ Tham chính thức bung lụa. Kỵ ở đây được tinh hóa thành \"chất xúc tác/Gió bão\" để hỏa tiễn Vũ Tham cất cánh bay lên. Thành quả tài chính đạt mốc kinh hoàng.",
    12: "> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:** Nguyệt hạn trùng khít song song Lưu Niên 2026 (Dần - Cự Dương) và nhị hợp sinh khí chặt nghẽn Mệnh (Hợi). Toàn bộ nỗ lực, đập phá càn quét, dịch chuyển luân hồi xuyên suốt năm nay của Lưu Niên đều quy tụ sinh linh đổ nhập vào đích đến cuối cùng tại cung này: Tài sản vô hình (Danh tiếng BVBĐ/AI) và hữu hình (BĐS, Server, Hạ Tầng Phần mềm đỉnh cao). Triệt tại Dần làm chững lại đà mua bán lướt sóng nhưng vĩnh viễn khóa chặt cố định lại nền tảng vững cữu cho khối tài sản. Cấp độ đập-xây tàn khốc của Đại Vận Mão nghỉ đông khép lại bằng một đế chế vững như bàn thạch tại Dần."
}

def generate_table_and_analysis(month):
    data = MONTHLY_DATA[month]
    cung = data["cung"]
    house = data["house"]
    sao = data["sao"]
    analysis = IMPACT_ANALYSIS[month]
    
    block = [
        "##### 🌐 QUY CHIẾU ĐA TẦNG (Nguyệt Hạn ⊂ Niên Hạn ⊂ Đại Vận ⊂ Gốc)",
        "| Cấp Độ | Cung Vị | Tình Trạng / Tinh Bàn | Mức Chi Phối |",
        "|---|---|---|---|",
        "| **Gốc (Mệnh/Thân)** | Hợi (Phủ) / Sửu (Vũ Tham) | Tích lũy nền tảng vững chắc, quyền bính ngầm | ⭐⭐⭐ Hệ quy chiếu tối hậu |",
        f"| **Gốc ({house})** | {cung} | {sao} | ⭐⭐⭐ Năng lượng cội nguồn |",
        "| **Đại Vận (33-42)** | Mão (Quan Lộc) | Tướng Hãm + Triệt (Đập đi xây lại hệ thống) | ⭐⭐⭐ Định hình thập kỷ |",
        "| **Niên Hạn 2026** | Dần (Điền Trạch) | Cự Dương Vượng (Sáng sủa, thâu tóm tài sản) | ⭐⭐ Chủ đề của năm |",
        f"| **Nguyệt Hạn T{month}** | {cung} ({house}) | Chịu tác động đồng thời từ 4 lớp trên | ⭐ Biến động ngắn hạn |",
        "",
        analysis,
        ""
    ]
    return block

def inject_multi_layer_v2(file_path):
    print(f"Executing Deep Impact rewrite on {file_path}...")
    content = Path(file_path).read_text(encoding='utf-8')
    lines = content.split('\n')
    out_lines = []
    
    i = 0
    current_month = 1
    skip_mode = False
    
    while i < len(lines):
        line = lines[i]
        
        m = re.search(r'THÁNG (\d+) ÂM LỊCH', line, re.IGNORECASE)
        if not m:
            m = re.search(r'THÁNG (\d+)', line, re.IGNORECASE)
        if m and line.startswith('### '):
            current_month = int(m.group(1))

        if skip_mode:
            # We are skipping the old table lines until we hit HỆ QUY CHIẾU 
            if line.startswith('##### HỆ QUY CHIẾU KINH ĐIỂN'):
                skip_mode = False
                # Insert the new block
                block = generate_table_and_analysis(current_month)
                out_lines.extend(block)
                out_lines.append(line)
            i += 1
            continue

        if line.startswith('##### 🌐 QUY CHIẾU ĐA TẦNG'):
            skip_mode = True
            i += 1
            continue
            
        out_lines.append(line)
        i += 1
        
    Path(file_path).write_text('\n'.join(out_lines), encoding='utf-8')
    apply_hoa_ky_guardrails_to_file(file_path)
    print(f"Deep Impact rewrite complete: {file_path}")

inject_multi_layer_v2('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md')
inject_multi_layer_v2('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md')
