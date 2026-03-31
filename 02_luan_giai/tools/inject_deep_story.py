import re
import sys
from pathlib import Path
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file

DEEP_NARRATIVES = {
    1: "> **Lớp 1 (Nền & Ngoại cảnh):** Khởi động năm Bính Ngọ, anh đối diện ngay với cung Quan Lộc bị Triệt án ngữ cùng Tướng Hãm. Về mặt sự nghiệp (lâm sàng BVBĐ lẫn tiến độ CDMS), anh sẽ cảm nhận rõ một sự 'bị nén' — năng lực chuyên môn có thừa nhưng cơ chế, hoàn cảnh chưa cho phép bung sức. Điểm Thái Tuế rơi vào Tuế Phá cộng hưởng với khí hậu Hàn (lạnh lẽo), sinh ra cảm giác bất mãn ngầm, 'chủ lấn khách' khao khát khẳng định thế chủ động nhưng lại thiếu sân phô diễn.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Tuy nhiên, ở lớp sâu hơn, sự kích hoạt của Hỏa Tinh Đắc Địa và Thiên Khôi cho thấy: chính trong lúc bế tắc nhất của dự án hay khó khăn của một ca mổ phức tạp, một vị quý nhân cấp cao (có thể là sếp lớn hoặc chuyên gia lão làng) sẽ đột ngột xuất hiện mở đường tắt rọi sáng giải pháp.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Điểm NPL 4.9 khuyên anh: Đừng vội tung dòng tiền vào chứng khoán (SHB, VN-Index lúc này đang ở phase tích lũy nén chặt), hãy lẳng lặng củng cố nền tảng hệ thống AI Agent bên dưới. Sự nghiệp đang ở thế 'lửa ủ trong băng', không được nóng vội phá vỡ quy trình mà phải tỉ mẩn 'lấy nhu thắng cương'.",
    
    2: "> **Lớp 1 (Nền & Ngoại cảnh):** Bước sang tháng 2 Âm Lịch, cung Nô Bộc được kích hoạt với bộ Cơ Lương Miếu và Hóa Lộc, mở khóa toàn diện lớp lang về 'Mạng lưới chuyên gia' và Brain Trust. Các mảng liên kết (cộng sự phát triển AI Agent, ê-kíp mổ, partner đầu tư) sẽ bùng nổ nhờ sự hỗ trợ từ những cộng sự lành nghề. Điểm Thái Tuế ở thế Long Đức (Chịu Thiệt) kết hợp khí Ấm — anh có thể phải chấp nhận nhường bước, đi cửa dưới, san sẻ quyền lợi trong team, nhưng sự 'thiết thòi' về mặt danh nghĩa này lại đẻ ra kim cương.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Lớp Tứ Hóa (L.Hóa Quyền) âm thầm trao cho anh quyền định đoạt ngầm trong tập thể. Mạng lưới này sẽ đẩy về tay anh những phím hàng chứng khoán chuẩn xác (như cổ phiếu ngành thép/ngân hàng) hoặc giải pháp đột phá gỡ nút thắt kĩ thuật cho codebase CDMS.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Mức NPL 4.9 cho thấy dòng tiền bắt đầu rục rịch chuyển mình. Lời khuyên tối thượng: Trải lòng, hạ cái tôi, dùng Đức để thu phục nhân tâm. Đừng giành công, cứ hào sảng chia sẻ credit trong các báo cáo, anh sẽ thu được một tập thể trung thành chết sống.",

    3: "> **Lớp 1 (Nền & Ngoại cảnh):** Đây là tháng anh bước ra ánh sáng rực rỡ và quyền lực nhất (Điểm nhảy vọt chạm 6.4 - đỉnh cao nửa đầu năm). Cung Thiên Di với Đế tinh Tử Vi và Thất Sát Vượng đặt anh vào ghế của người cầm trịch thiết lập luật chơi. Điểm Chủ-Khách 9/10 kết hợp với khí chất Bạch Hổ (Chính Danh): các buổi báo cáo hội chẩn Ban Giám Đốc, bàn giao dự án CDMS cho bộ phận IT, hay thuyết trình trước cổ đông sẽ hoàn toàn nằm dưới sự thao túng của anh.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Khí sắc đạt 7/10 (Mộc sinh Hỏa) cung cấp cho anh nền tảng thể lực và tốc độ tư duy cực kỳ sắc bén. Tuy nhiên, Thất Sát đi cùng Hỏa (tại Tỵ) là hình tượng thanh Kiếm Phong Kim (bản mệnh) bị đưa thẳng vào lò nung — áp lực cường độ làm việc là không tưởng. Sức ép từ mọi phía dồn mài sắc lưỡi kiếm của anh.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Về đầu tư (TuViStock): Đây là timing nhạy bén nhất, hệ thống bot báo tín hiệu chính xác. Hãy quyết đoán 'vung kiếm' chốt hạ các danh mục chiến lược. Đánh nhanh thắng nhanh, sự chần chừ sẽ làm mất 'tính thiêng' của tháng đế vượng.",

    4: "> **Lớp 1 (Nền & Ngoại cảnh):** Rời khỏi đỉnh cao bùng cháy của tháng 3, tháng 4 dìm anh xuống cung Tật Ách (VCD mượn Đồng Âm). Lớp lang năng lượng sinh lý và tinh thần đồng thanh báo động sự quá tải. Khí Hậu bốc lên mức 'Nóng' nhưng Khí Sắc anh hạ đột ngột xuống 2/10. Tinh thần đối ngoại chuyển sang trạng thái Phúc Đức (nhún nhường, khôn ngoan lùi lại).\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Anh sẽ cảm nhận sâu sắc các triệu chứng stress dạng ẩn, sự mệt mỏi khó định danh từ việc ôm đồm liên miên 3 mặt trận: lâm sàng y khoa cường độ cao, code AI thâu đêm, và rình rập bảng điện chứng khoán. Sự tương tác Ngũ Hành (Hỏa khắc Kim bản mệnh) ép buộc bộ máy sinh học của anh phải đình chỉ tự động (rút phích cắm).\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Thực tế: Hãy ngưng kiểm soát vi mô. Bàn giao công việc cho hệ thống auto-agent chạy tự định tuyến, hủy bỏ/lùi lịch những ca phẫu thuật không khẩn cấp, tuyệt đối nghiêm cấm việc lướt sóng T+ trong chứng khoán. Điểm NPL 4.8 cảnh báo rõ ràng: Dừng cày cuốc. Giữ tiền và giữ gìn sinh mạng là ưu tiên tuyệt đối.",

    5: "> **Lớp 1 (Nền & Ngoại cảnh):** ⛔ **THÁNG NGUY HIỂM NHẤT NĂM 2026** với điểm số lao dốc xuống vùng tử địa (3.8/10). Lớp lang Tài Bạch (VCD) đi kèm Thiên Hình Hãm và Điếu Khách (Nghịch Cảnh) lập tức kích hoạt chuỗi báo động đỏ về dòng tiền hoặc rủi ro pháp lý. Môi trường Cực Nóng đang đốt cháy Khí Sắc kiệt quệ về mốc 1/10.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Đối chiếu với bối cảnh của anh, các rủi ro cụ thể có thể là: Các điều khoản hợp đồng liên quan tới CDMS/phần mềm có lỗ hổng gây phạt, sai sót/nhầm lẫn tài liệu trên hồ sơ bệnh án gây phiền phức y khoa, hoặc bị kẹt trong bẫy 'bull trap' (giá tăng giả rồi xả lũ) thảm khốc trên thị trường cổ phiếu. Điểm Chủ-Khách 2/10 báo hiệu anh triệt để mất quyền kiểm soát tình hình, ngoại cảnh chèn ép.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Phương thức sinh tồn duy nhất: 'Bế quan tỏa cảng'. Đóng bảng điện chứng khoán, ôm khư khư tiền mặt, rà soát văn bản thật kĩ. Làm việc đúng quy trình tiêu chuẩn viện, tuyệt đối không có sự 'linh hoạt' hay 'sáng tạo' ngoài luồng nào trong tháng này. Tránh va chạm, nuốt giận vào trong để bảo toàn mạng lưới.",

    6: "> **Lớp 1 (Nền & Ngoại cảnh):** Tháng 6 mang năng lượng của sự dọn dẹp và chuyển giao hệ thống. Cung Tử Tức (VCD) với Đại Hao Đắc địa cho thấy một sự 'thay máu' cấu trúc về dòng tiền. Anh có thể phải chốt lời cắt lỗ một số tài sản mua sai nhịp, hoặc rót ngân sách mạnh tay cho việc mua sắm hạ tầng (hệ thống server, hardware mới cho Agent).\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Điểm Thái Tuế vướng Trực Phù (buồn bực rỉ rả, cào cấu nhẹ nội tâm) do di chứng tồn đọng của tháng 5 vừa qua. Rất may mắn, Khí sắc đã lội dòng sinh quy hồi lên mức 6/10 do môi trường Nóng Ẩm dung hòa. Tháng này anh tốn kém tiền bạc và công sức cho 'đứa con tinh thần' (chỉnh sửa repo CDMS, debug lỗi bot TuViStock, hoặc việc gia đình).\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Dòng tiền NPL 4.6 vẫn đang trong chu kỳ tích lũy làm lại từ đầu. Lời khuyên: Đừng nóng lòng gỡ gạc hay vội vã săn lùng cơ hội mới. Hãy xắn tay áo tái cấu trúc hệ thống, dọn sạch bugs, thiết lập quy chuẩn mới cho nửa cuối năm tung hoành.",

    7: "> **Lớp 1 (Nền & Ngoại cảnh):** Một tháng đối mặt với sự va đập đối ngã đặc biệt gay gắt. Nguyệt hạn đổ về cung Phu Thê (Liêm Phá Hãm) lại gồng mình tải trọn vòng Thái Tuế (Chính Danh). Lớp lang này dự đoán: Xung đột lợi ích, rạn nứt quan điểm sẽ nổ ra trực diện và khốc liệt với đối tác 'ruột' (có thể là người phối ngẫu, Co-founder dự án, hoặc đồng nghiệp kề vai sát cánh).\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Điểm Khí Sắc vút lên mạnh (9/10) tạo ra một đợt bùng nổ cái tôi rất lớn (Bản mệnh Kim gặp cung tháng Kim = Cương gặp Cương). Lớp Giáp Cung báo Cự Dương tương trợ, nghĩa là bên ngoài có sếp hoặc quý nhân che chở, nhưng bên trong nội bộ nhóm cốt lõi lại 'Liêm Phá' tàn phá lẫn nhau.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Ứng xử với tháng này: Trong các cuộc tranh luận nâng cấp phần mềm hoặc chuyện gia đình, anh cần tuyệt đối kềm tỏa sự phán xét (đặc tính sắc bén của Cự Môn mệnh anh). Khi đối phương đẩy không khí lên đỉnh điểm, hãy vận dụng lý trí máu lạnh của một bác sĩ ngoại khoa — bóc tách vấn đề một cách cơ học thay vì sa đà vào ăn thua cảm xúc. Lùi một bước để giữ trọn hệ sinh thái.",

    8: "> **Lớp 1 (Nền & Ngoại cảnh):** Xuyên thủng những ồn ào lộ liễu, tháng 8 được mệnh danh là vương quốc của 'Dark Pool' (Dòng tiền ngầm) và cơ hội ẩn. Nhập cung Huynh Đệ gặp Tuần, Không Vong và Đà La Đắc — lớp vỏ ngoài thể hiện sự lùng bùng, trì trệ, thiếu minh bạch và có tin gây chán nản. Mọi thứ dường như đi vào ngõ cụt.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Tuy nhiên, ở tầng sâu nhất (nơi Khí Sắc đạt đỉnh hoàn hảo 10/10 với khí Mát mẻ thanh tĩnh), tư duy phân tích của anh lại thăng hoa sắc bén nhất. Khí chất Thiếu Dương (Khôn Ngoan) cho anh nhãn quan lách qua các quy chế cứng nhắc hoặc định kiến đám đông. Những thỏa thuận ngầm, cái gật đầu phía sau hậu trường, hoặc các mã chứng khoán bị ruồng bỏ rớt thảm mà anh gom nhặt... sẽ bắt đầu đắp móng cho chuỗi lợi nhuận vĩ đại.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Điểm NPL (5.6) tăng mạnh: Hãy thả hệ thống AI vào các mảng tối của thị trường cào quét dữ liệu, nhặt nhạnh hàng chiến lược khi F0 bi quan. Nguyên tắc làm việc: Kín kẽ, thâm sâu, hạn chế phát ngôn và chỉ chia sẻ cơ hội với 1-2 cộng sự 'vào sinh ra tử'.",

    9: "> **Lớp 1 (Nền & Ngoại cảnh):** Tháng 9 đưa quy luật tuần hoàn trở về chính cung gốc (Hợi - Mệnh: Thiên Phủ Đắc + Tuần). Điểm tụt nhẹ (4.7) do sự gò bó từ sức vây hãm của Tuần Không chặn cứng nắp Thiên Phủ (Kho chứa tài năng/Tiền). Ở lớp lang thực tiễn, trạng thái này là: Dự án CDMS hoặc phác đồ nghiên cứu khoa học của anh đã chín muồi, nhân lực sẵn sàng bung lụa, nhưng bị ách tắc tức tưởi bởi giấy tờ thủ tục, sự chậm trễ của ban bệ hành chính.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Tâm thế Tang Môn (Nghịch cảnh) khiến hệ thần kinh anh sốt ruột, lo âu, muốn bùng phát. Tuy nhiên, Mệnh Kim sinh Thủy (cung Hợi) thiết lập cục 'Sinh Xuất' — tháng này định mệnh yêu cầu anh phải cống hiến, nhả năng lượng ra ngoài không toan tính.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Lời khuyên cốt tử: Phải học cách bao dung sự chậm trễ (latency) của cái guồng máy nhà nước/viện. Nó không chống lại anh, nó chỉ là quá trình thử lửa. Hãy duy trì nhịp điệu phẫu thuật thật chuẩn, code auto-agent đều đặn, không được đốt cháy giai đoạn hòng đi tắt đón đầu.",

    10: "> **Lớp 1 (Nền & Ngoại cảnh):** Tháng 10 điều hướng trọng tâm về trách nhiệm hệ sinh thái thượng tầng. Cung Phụ Mẫu rực sáng (Đồng Âm Vượng) về mặt vị thế nhưng lại kéo theo bè lũ Không, Kiếp, Kình Hãm. Ở lớp lang này, anh phải cáng đáng áp lực trực tiếp từ các Sếp lớn (BGĐ, Trưởng khoa) dội xuống, hoặc các vấn đề sức khỏe/hành chính lắt nhắt của phụ huynh trong gia đình gia tộc.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Có thể bố mẹ gặp sự cố sức khỏe nhỏ cần chính bác sĩ Long dốc sức xử lý, hoặc cấp trên đẩy xuống tay anh nhiều chỉ tiêu giám sát gắt gao. Điểm Thái Tuế Thiếu Âm (nhẫn nhịn, chịu thiệt) yêu cầu anh sắm vai anh hùng gánh vác rủi ro trong thầm lặng, không được ghi nhận công lao ngay lúc đó.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Năng lượng bị xén mỏng ra nhiều phía (Chủ-Khách 3/10 cho thấy Khách lấn Chủ triệt để). Chiến thuật: Bỏ qua ý định vung lệnh đầu tư mạnh tay hay khởi động project phần mềm cá nhân. Trích quỹ thời gian cho việc báo hiếu và dải quyết trơn tru các vấn đề gia đình, tạo vùng đệm hậu phương an toàn.",

    11: "> **Lớp 1 (Nền & Ngoại cảnh):** ⭐ **ĐỈNH CAO TÀI CHÍNH NGẦM 2026.** Vận khí sấm sét nổ tung tại cung Phúc/Thân (Vũ Tham Miếu + Hóa Kỵ). Sự giao thoa của Vũ Tham thiết lập một cỗ máy in xèng khổng lồ, đặc biệt năng lượng từ can Nhâm bản mệnh làm bùng nổ Hóa Kỵ ôm Thân, giật đứt mọi rào cản tài chính.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Lớp lang này cho thấy: Các khoản đầu tư ôm mòn mỏi từ T6-T8, các sản phẩm code/AI, hoặc các ca can thiệp thu dịch vụ giờ đây đổ bể tiền bạc và tiếng tăm ập vào túi anh (Cộng tiệp Điểm Quan Phù Chính Danh 9/10). Tuy nhiên, Hóa Kỵ (sự thị phi) dính Thân báo động chân thực: Dòng tiền vào ồ ạt tỷ lệ thuận tuyệt đối với sự săm soi, đố kỵ, báo cáo thọc gậy bánh xe từ đám đồng nghiệp/đối thủ ganh ghét.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Lời khuyên mang tính sinh tử: 'Mặc áo giáp, kiếm tiền trong sương mù, thu hoạch trên sa trường trong tĩnh lặng'. Có thể chốt các hợp đồng kinh tế lớn nhất năm, tài khoản xn lần, nhưng tuyệt đối không rêu rao mua xe tậu nhà hay khoe khoang tín hiệu trên mạng xã hội. Trí mạng nằm ở việc giấu bài.",

    12: "> **Lớp 1 (Nền & Ngoại cảnh):** Khép lại năm 2026, dòng năng lượng đi vào cung Điền Trạch (Cự Dương Vượng + Triệt). Trọng lực của vòng xoay xoáy vào khối tài sản tích lũy, chiến lược không gian sống và hệ thống nền tảng lâu dài. Nhát chém của Triệt án ngữ làm thanh khoản nhà đất hoặc kế hoạch mở rộng quy mô máy chủ bị khựng lại một nhịp độ.\n> \n> **Lớp 2 (Kích Hoạt & Sự Kiện):** Tuy nhiên, tính đặc thù vương giả của Mặt Trời (Thái Dương) phối với Cự Môn Vượng tại Dần là minh chứng cho một đế chế khối tài sản cá nhân đồ sộ đã được đắp lên và danh tiếng mang ánh sáng quang minh. Lực lượng Chủ đẩy ép Khách mốc 9/10, anh một tay thâu tóm toàn bộ sự kiểm soát tổng thể trước thềm năm mới.\n> \n> **Lớp 3 (Tổng Hợp & Hành Động):** Khí hậu chuyển mức Hàn Ẩm, năng lượng đang thu lại tích dưỡng. Đây là thời điểm tuyệt mĩ để tổng kết danh mục chứng khoán, tái cơ cấu đánh giá rủi ro tài sản, rà soát lại source code/kiến trúc Agent từ cấp hệ điều hành... và sau cùng là dành toàn bộ mùa đông ấm áp thưởng thức thành quả với những người yêu thương nhất. Một trạm dừng chân tĩnh lặng và kiêu hãnh chuẩn bị bước sang chương sách 2027."
}

def inject_deep_story(file_path):
    print(f"Injecting deep narrative stories into {file_path}...")
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
            # We skip lines until we hit an empty line or a non-text line
            # Wait, the previous block was:
            # ##### 🗣️ TỔNG LUẬN NHANH (Human-Readable)
            # > **🗣️ Tóm lại:** [Paragraph]
            # [Empty Line]
            # ##### HỆ QUY CHIẾU
            if line.startswith('##### HỆ QUY CHIẾU KINH ĐIỂN'):
                skip_mode = False
                # Insert the deep narrative
                story = DEEP_NARRATIVES.get(current_month, "")
                if story:
                    out_lines.append("##### 🗣️ TỰ SỰ DIỄN GIẢI CHUYÊN SÂU (Personal Profile: Long 1992, Y Khoa - AI - Đầu tư)")
                    out_lines.extend(story.split('\n'))
                    out_lines.append("")
                out_lines.append(line)
            i += 1
            continue
            
        if line.startswith('##### 🗣️ TỔNG LUẬN NHANH (Human-Readable)'):
            skip_mode = True
            i += 1
            continue
            
        out_lines.append(line)
        i += 1
        
    Path(file_path).write_text('\n'.join(out_lines), encoding='utf-8')
    apply_hoa_ky_guardrails_to_file(file_path)
    print(f"Done injecting deep stories into {file_path}")

inject_deep_story('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md')
inject_deep_story('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md')
