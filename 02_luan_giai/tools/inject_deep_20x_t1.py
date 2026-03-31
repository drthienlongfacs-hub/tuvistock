#!/usr/bin/env python3
"""Inject 20x Deep Impact for T1 (Mão-Quan). SOT-verified."""
import re
from pathlib import Path

TARGET = '/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md'

OLD_T1 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Mão) là cung Quan Lộc gốc, có Triệt đóng. Mão tam hợp Hợi (Mệnh) — kênh 20% liên kết nguyệt hạn thẳng về Mệnh. Đại Vận hiện tại (Dần-Điền) kề sát bên trái Mão, tạo cấu trúc **Giáp cung ĐV-NH** cực kỳ mạnh.
> **Kết luận:** Triệt tại Mão (Quan) là cấu trúc CỐ ĐỊNH 10 năm ĐV4 — sự nghiệp chính thống bị cắt ngang KHÔNG phải do vận xấu nhất thời, mà do *thiết kế* của Đại Vận Điền Trạch: 10 năm này yêu cầu anh dồn sức xây TÀI SẢN (Dần), không phải leo thang chức vụ (Mão). Gốc Mệnh Phủ Đắc (Hợi) tam hợp Mão = vẫn hậu thuẫn ngầm, nhưng Phủ bị Tuần phong nên lộc chỉ rỉ chảy, không xối.
> **Hành động:** Không cướp đường sự nghiệp chính thống. Cứ xây hạ tầng (CDMS, AI Agent, BĐS) — Đại Vận Điền hỗ trợ tối đa cho tài sản tích lũy."""

NEW_T1 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — BẢN ĐỒ KẾT NỐI NGUYỆT HẠN T1 (MÃO — QUAN LỘC)**
>
> | Kênh | Đích | Tinh bàn đích (SOT) | Nhận định |
> |---|---|---|---|
> | **Xung chiếu** | Dậu (Phu Thê) | Liêm Hãm + Phá Hãm + Linh H + Đào V + L.Khoa + L.Kỵ | ⛔ Dậu BẮN THẲNG ↔ Mão — xung Thê↔Quan |
> | **Tam hợp 1** | **Hợi (GỐC MỆNH)** | Phủ Đắc + Lộc Tồn + Khoa + Tuần | ⭐⭐ Mệnh HẬU THUẪN sự nghiệp |
> | **Tam hợp 2** | Mùi (Tài Bạch) | VCD + Hình Hãm + Quốc Ấn | 🟡 Tài gắn Quan — tiền từ sự nghiệp |
> | **Nhị hợp** | Tuất (Huynh) | VCD + Tuần + Không H + Đà Đ + Khốc + Tang | ⚠️ Anh em rỗng — kênh nhị hợp yếu |
> | **Giáp trái** | **Dần (Điền = ĐV4!)** | Cự V + Dương V + Triệt + Mã Đ | ⭐⭐⭐ **ĐẠI VẬN KỀ SÁT bên trái** — Giáp ĐV-NH mạnh nhất |
> | **Giáp phải** | Thìn (Nô Bộc) | Cơ M + Lương M + Hóa Lộc V | ⭐ Brain Trust kề bên phải — nguồn cứu sinh |
> | **Lục hại** | Thìn (Nô Bộc) | (trùng giáp phải) | Mài mòn ngầm từ mạng lưới — có giúp nhưng có mệt |
>
> **📐 Kết luận Hình học (3 nhận định then chốt):**
>
> **① Giáp ĐV-NH cực mạnh:** ĐV (Dần-Điền) giáp TRÁI Mão = khoảng cách 1 cung = MỐI LIÊN HỆ MẬT NHẤT có thể. Toàn bộ năng lượng "quản trị tài sản" 10 năm ĐV4 TRÀN ngay bên cạnh sự nghiệp. Cơ Lương Lộc (Thìn-Nô) giáp PHẢI = Brain Trust hỗ trợ phía còn lại. **Mão bị kẹp giữa 2 lực CÁT (ĐV+Nô) mặc kệ bản thân Mão hung.**
>
> **② Xung chiếu Thê-Quan (Dậu↔Mão):** Mọi vấn đề sự nghiệp T1 đều có BÓNG DÁNG HÔN NHÂN/ĐỐI TÁC phía đối diện. Liêm Phá Hãm Linh bắn xung = đối tác/vợ chồng tạo nhiễu loạn, nhưng Đào + L.Khoa cũng kèm = bên cạnh xung có hòa.
>
> **③ Tam hợp Mão-Hợi-Mùi (MỘC CỤC):** NH trùng cung Quan + tam hợp Mệnh + Tài = **Trục Quan-Mệnh-Tài kích hoạt**. Sự nghiệp gắn trực tiếp bản mệnh và dòng tiền. MỌI quyết định sự nghiệp T1 đều có tác động tài chính.
>
> ---
> **II. NGŨ HÀNH CƠ HỌC — BẢN MỆNH KIM vs CUNG MÃO MỘC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh **KIM** vs Cung Mão **MỘC** | Kim khắc Mộc = **CHỦ ĐỘNG CẮT** | Anh CẮT BỎ quy trình cũ, tái cấu trúc sự nghiệp — không bị cung ép, anh ÉP cung |
> | Tướng **THỦY** vs Mão **MỘC** | Thủy sinh Mộc = **Sinh xuất** | Tướng nuôi cung = hao kiệt → "Ấn hết mực" — có tài phò tá nhưng thiếu dấu đóng |
> | Hỏa Đắc **HỎA** vs Mão **MỘC** | Mộc sinh Hỏa = **Hỏa cực vượng** | Hỏa tại Mộc cung = bùng nổ bất ngờ — "lửa rèn kiếm" |
> | Triệt **KIM** vs Mão **MỘC** | Kim khắc Mộc = **cắt đứt** | Sự nghiệp chính thống bị cắt ngang — cấu trúc 10 năm ĐV4 |
>
> **🔄 Chuỗi phản ứng:** Anh (Kim) → khắc cung Mão (Mộc) → Tướng (Thủy) bị rút cạn nuôi cung → Hỏa Đắc bùng lên từ Mộc cung → Triệt (Kim) cắt thêm → **Hệ quả: sự nghiệp chính thống GÃY, nhưng LỬA PHI TRUYỀN THỐNG bùng nổ.** Y khoa truyền thống không lên chức, nhưng CDMS/AI Agent bùng sáng.
>
> ---
> **III. ĐẠI VẬN (DẦN-ĐIỀN) × NGUYỆT HẠN (MÃO-QUAN) — GIÁP CUNG**
>
> ĐV Dần **giáp trái** Mão = khoảng cách 1 cung = **Liên kết mật nhất.**
> - ĐV Điền (tài sản) giáp Quan (sự nghiệp) = 10 năm này, SỰ NGHIỆP PHỤC VỤ TÀI SẢN, không ngược lại. Mỗi quyết định sự nghiệp phải hỏi: "Nó có tạo tài sản tích lũy không?"
> - Cự Nhật Vượng (ĐV) soi sáng Tướng Hãm (Mão) qua giáp = "Mặt Trời rọi kho ấn hết mực" → tri thức + ánh sáng THAY THẾ dấu ấn chính thống.
> - **Song Triệt Dần-Mão** = Triệt đóng cả ĐV lẫn NH liền 2 cung = đường chính thống bị KHÓA KÉP. NHƯNG Triệt nhả ~70-80% ở tuổi 34 → đường phi truyền thống BẮT ĐẦU MỞ.
>
> ---
> **IV. NIÊN HẠN 2026 (DẦN) × NH (MÃO) — GIÁP CUNG**
>
> Niên Hạn TRÙNG ĐV tại Dần → Cự Nhật x2. Dần giáp Mão = **BA TẦNG (ĐV + Niên + Nguyệt) kề nhau liền mạch Dần-Mão.** Năng lượng truyền liên tục qua kênh giáp cung ~5%.
>
> ---
> **V. TUẦN — TRIỆT XUYÊN TẦNG**
>
> | Tầng | Cung | Tuần/Triệt? | Tác động lên T1 (Mão-Quan) |
> |---|---|---|---|
> | **Gốc Mệnh** | Hợi | **TUẦN** ☁️ | Phủ Lộc bị phong → hậu thuẫn Mệnh cho Quan chỉ RỈ CHẢY, không xối |
> | **Gốc Thân** | Sửu | Không | Pháo Đài THÔNG SUỐT — tài chính không bị phong tỏa |
> | **Đại Vận 4** | Dần | **TRIỆT** ⚡ | Cự Nhật V bị Triệt = tài sản xây trong áp lực. Giáp Mão = Song Triệt Dần-Mão |
> | **Niên Hạn** | Dần | **TRIỆT** (trùng ĐV) | Triệt x2 → nén kép. Nhị hợp Hợi(Tuần) = "Triệt gặp Tuần" → triệt tiêu phần |
> | **Nguyệt Hạn T1** | **Mão** | **TRIỆT** ⚡ | ⛔ NH TRÙNG CUNG TRIỆT — sự nghiệp bị cắt TRỰC TIẾP, không gián tiếp |
> | **Cung chức gốc** | Mão (Quan) | **TRIỆT** ⚡ | NH trùng khít cung chức = Triệt tác động 100%. **THÁNG NẶNG NHẤT VỀ TRIỆT** |
>
> **🔑 Kết luận Tuần-Triệt T1:**
>
> **① NH ĐÚNG cung Triệt:** T1 là tháng duy nhất NH rơi ĐÚNG vào Mão (Triệt) — sự nghiệp bị cắt TRỰC TIẾP, không qua trung gian. ĐV cũng ở Dần (Triệt kề) → **Song Triệt Dần-Mão bao trùm cả ĐV lẫn NH.** Đây là tháng nặng Triệt nhất năm.
>
> **② Tuần Mệnh (Hợi) tam hợp Mão (NH):** Kênh tam hợp kết nối Tuần (Mệnh) với Triệt (NH) = **2 lực phong ấn CỘNG HƯỞNG qua tam hợp** → cảm giác bế tắc LAN TỪ SỰ NGHIỆP VÀO BẢN MỆNH.
>
> **③ Lối thoát:** Gốc Thân (Sửu) KHÔNG Tuần/Triệt → Pháo Đài tài chính là VÙNG TỰ DO duy nhất. **Tiền bạc + đầu tư là nơi an toàn T1 — sự nghiệp chính thống thì cứ để yên.**
>
> ---
> **VI. PHI TINH KÍCH HOẠT — Can Canh (T1)**
>
> | Phi | Sao | Phi vào | Hiện tượng |
> |---|---|---|---|
> | Lộc | Thái Dương | Dần (Điền=ĐV) | ⭐ Lộc BƠM ĐV Điền → tài sản tăng giá trị ngầm |
> | Quyền | Vũ Khúc | Sửu (Thân=Pháo Đài) | ⭐ Pháo Đài NÂNG QUYỀN — tài chính cứng cáp |
> | Khoa | Thái Âm | Tý (Phụ Mẫu) | Lời khuyên sáng suốt từ cấp trên/mẹ |
> | Kỵ | Thiên Đồng | Tý (Phụ Mẫu) | ⚠️ Song Khoa-Kỵ Phụ → mẹ/sếp giúp NHƯNG kèm phiền |
>
> **Tương tác Phi-NH:** KHÔNG có Phi Tinh nào rơi vào Mão (NH). NH T1 chạy "khô" — không có năng lượng Phi Tinh trực tiếp. Phải mượn sức Giáp (Dần-Thìn). **Song Lộc+Quyền đánh ĐV+Thân = tài sản và tài chính được bơm mạnh dù sự nghiệp bế tắc.**
>
> ---
> **VII. TRÀNG SINH: THAI 🤰 (2/10) — MẦM THAI NGHÉN**
>
> Kim tại Mão = **Thai** = ý tưởng mới đang thai nghén, chưa có gì cụ thể. "Gieo hạt trong bóng tối" — T1 không ra kết quả, nhưng gieo đúng sẽ NỞ ở T5-T9.
>
> ---
> **VIII. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động | Hành động |
> |---|---|---|
> | **Y khoa (BVBĐ)** | Tướng Hãm + Triệt = KHÔNG thăng chức, không giao quyền mới. Hỏa Đắc = khi case khó, anh tỏa sáng → Khôi (quý nhân) ghi nhận | Mổ robot, giải case khó. KHÔNG đòi thăng chức |
> | **AI/CDMS** | ĐV Điền giáp Quan = xây CDMS là ĐÚNG đường ĐV4. Triệt cắt "deploy chính thức" → chạy ngầm | Xây module, test UAT. KHÔNG ép deadline deploy official |
> | **CK/Đầu tư** | Thai = chưa hình thành. Triệt NÉN. Lộc→ĐV Điền = ngầm tốt | ❌ HOLD CHẶT. KHÔNG mua/bán. SHB bị nén = đúng chu kỳ |
>
> ---
> **IX. 🗣️ DIỄN GIẢI TỰ NHIÊN — NÓI BẰNG NGÔN NGỮ ĐỜI THƯỜNG**
>
> Anh Long ơi, tháng 1 Âm lịch (khoảng tháng 2-3 Dương lịch) nói thật là tháng khó chịu nhất năm về sự nghiệp — vì Nguyệt Hạn rơi ĐÚNG vào cung Quan Lộc, mà cung này bị Triệt phong tỏa từ lúc sinh. Hình dung thế này: cái cổng vào công sở bị xích khóa, anh đứng ngoài nhìn vào thấy rõ mọi thứ, biết mình có tài hơn nhiều người bên trong, nhưng chìa khóa lại không nằm trong tay anh. Tướng Hãm là "ấn hết mực" — tài phò tá có, nhưng con dấu để đóng quyết định thì hết.
>
> NHƯNG — cái hay là Đại Vận Điền Trạch (Dần) đang đứng ngay kề bên trái, và Brain Trust Cơ Lương (Thìn) kề bên phải. Giống như anh bị khóa cổng chính, nhưng hai bên hàng xóm mở cửa hông mời vào ăn cơm. ĐV bảo: "Thôi đừng đập cổng làm gì, qua nhà tôi xây tài sản." Brain Trust bảo: "Qua bên này, có dự án hay." Đó là lý do tháng này không phải lúc đòi hỏi sự nghiệp chính thống, mà là lúc ĐÀO HẦM — xây CDMS, code Agent, nghiên cứu đề cương NCS dưới radar.
>
> Về tiền: Phi Tinh Can Canh đổ Song Lộc+Quyền thẳng vào ĐV (Dần) và Pháo Đài (Sửu) = tài sản và tài chính ngầm TĂNG dù bề mặt bế tắc. SHB có thể đang âm thầm tích lũy giá rẻ. Tràng Sinh ở vị trí Thai = mọi thứ đang ấp ủ, chưa nở. Nếu anh gieo hạt đúng tháng này — viết spec CDMS, lên kế hoạch module mới, mở tài khoản margin mới — thì hạt sẽ nở tháng 5-9.
>
> **Một câu duy nhất:** *Tháng đào hầm — đừng đập cổng chính, qua cửa hông mà vào.*"""

content = Path(TARGET).read_text('utf-8')
if OLD_T1 in content:
    content = content.replace(OLD_T1, NEW_T1)
    Path(TARGET).write_text(content, 'utf-8')
    print("[T1 ✅] Injected 20x Deep Impact for T1 (Mão-Quan)")
else:
    print("[T1 ⚠️] Old T1 text not found — may already be replaced")
