#!/usr/bin/env python3
"""Inject 20x Deep Impact for T11 (Sửu-Thân) and T12 (Dần-Điền). SOT-verified.
RCA: Kỵ Đắc tại Sửu = Mộ Khố tích trữ, NOT bế tắc."""
from pathlib import Path
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file
TARGET = '/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md'

OLD_T11 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn trùng khít Gốc Thân (Sửu-Vũ Tham Kỵ Miếu). Năng lượng tài chính hồi quy 100% về nguồn Pháo Đài. Sửu tam hợp Tỵ(Di-Tử Quyền)+Dậu(Thê-Đế Vượng) = toàn bộ Kim cục KÍCH HOẠT. Sửu giáp trái ĐV Điền (Dần) = Pháo Đài kề ngay Đại Vận xây tài sản. Nhật Nguyệt Giáp Sửu trực tiếp (Dương V Dần + Âm V Tý) = cách cục CÁT CỰC ĐẠI.
> **Kết luận:** Vũ Tham Miếu + Kỵ Đắc Phản Vi Giai + NH trùng Thân + Kim cục kích hoạt + Nhật Nguyệt Giáp = ĐỈNH CAO TÀI CHÍNH NĂM. Tuy nhiên, Kỵ đi kèm thị phi (Hóa Kỵ ôm Thân = bản thân gánh chịu tiếng nói đố kỵ). Gốc Mệnh (Phủ Hợi) nhị hợp Dần (ĐV) đang dõi theo, nhưng không kiểm soát trực tiếp Sửu → anh ở thế solo.
> **Hành động:** Thu hoạch tài chính trong tĩnh lặng. 'Mặc áo giáp, kiếm tiền trong sương mù.' Tuyệt đối không khoe khoang."""

NEW_T11 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — NGUYỆT HẠN T11 (SỬU — GỐC THÂN/PHÚC ĐỨC) — ⭐⭐⭐ ĐỈNH CAO TÀI CHÍNH**
>
> | Kênh | Đích | Tinh bàn đích (SOT) | Nhận định |
> |---|---|---|---|
> | **Xung chiếu** | Mùi (Tài Bạch) | VCD + Hình H + Quốc Ấn | ⭐ Trục Thân-Tài xung chiếu = tài chính TRÀN 2 CHIỀU |
> | **Tam hợp 1** | Tỵ (Thiên Di) | Tử Vi M + Sát V + Quyền | ⭐⭐ **Kim Cục kích hoạt LẦN 3** — cao trào cuối năm |
> | **Tam hợp 2** | Dậu (Phu Thê) | Liêm Phá H + Linh H + Đào V | ⚠️ Thê trong Kim Cục — hôn nhân gắn tài chính |
> | **Nhị hợp** | Tý (Phụ Mẫu) | Đồng V + Âm V + Kiếp H + Kình H | ⚠️ Phụ nhị hợp Thân — cha mẹ gắn tài chính (tiếp nối T10) |
> | **Giáp trái** | Tý (Phụ Mẫu) | (trùng nhị hợp) | Phụ kề bên |
> | **Giáp phải** | **Dần (Điền = ĐV4!)** | Cự V + Dương V + Triệt + Mã Đ | ⭐⭐⭐ **ĐV GIÁP PHẢI = Pháo Đài KỀ ĐV** |
> | **Lục hại** | Ngọ (Tật Ách) | VCD + xung chiếu | ⚠️ Ách hại Thân — sức khỏe mài mòn tài chính |
>
> **📐 Kết luận Hình học:**
>
> **① NH TRÙNG GỐC THÂN = Hồi Quy 100% VỀ PHÁO ĐÀI:** Giống T9 (hồi quy Mệnh), T11 hồi quy THÂN. Vũ Khúc Miếu + Tham Lang Miếu + Hóa Kỵ Đắc = bộ ba chiến đấu tài chính ĐỈNH NHẤT lá số — tất cả được kích hoạt 100%.
>
> **② Kim Cục tam hợp (Sửu-Tỵ-Dậu) lần 3:** Lần 1 (T3-Di), lần 2 (T7-Thê), lần 3 (T11-Thân) = đỉnh kim tự tháp. NH tại GỐC Kim Cục (Sửu) = **năng lượng Kim NGUYÊN THỦY nhất.**
>
> **③ Nhật Nguyệt Giáp Sửu:** Thái Dương Vượng (Dần, giáp phải) + Thái Âm Vượng (Tý, giáp trái) = **MẶT TRỜI + MẶT TRĂNG kẹp 2 bên Pháo Đài** = cách cục CÁT CỰC ĐẠI. Ánh sáng soi rọi kho vàng từ 2 phía.
>
> **④ ĐV giáp phải (Dần kề Sửu):** Đại Vận xây tài sản (Điền) nằm ngay kề Pháo Đài tài chính. ĐV + NH giáp nhau = **chiến lược tài sản 10 năm + bản mệnh tài chính GẶP NHAU chỉ cách 1 bức tường.**
>
> ---
> **II. NGŨ HÀNH CƠ HỌC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh **KIM** vs Sửu **THỔ** | Thổ sinh Kim = **ĐƯỢC NUÔI** | Cung Thân NUÔI bản mệnh — tháng THUẬN nhất |
> | Vũ **KIM** Miếu vs Sửu **THỔ** | Thổ sinh Kim, Vũ đắc vị | Kim CỰC VƯỢNG — tài chính đạt đỉnh cơ học |
> | Tham **MỘC** Miếu vs Sửu **THỔ** | Mộc khắc Thổ = "đào đất" | Tham KHAI MỎ — khả năng đào vàng từ đất = BĐS, tài sản ẩn |
>
> ---
> **III. ĐẠI VẬN (DẦN) × NH (SỬU) — GIÁP CUNG TRỰC TIẾP**
>
> ĐV (Dần) giáp phải Sửu = **khoảng cách 1 cung = liên kết mật nhất.** Cự Nhật V (ĐV) soi thẳng vào Vũ Tham Kỵ (Thân) qua khe cửa giáp = "Mặt Trời rọi kho vàng từ cửa sổ kề bên". **ĐV xây tài sản + NH tại kho tiền = PERFECT ALIGNMENT.**
>
> ---
> **IV. NIÊN HẠN (DẦN) × NH (SỬU)** — Trùng ĐV. Giáp phải kép.
>
> ---
> **V. TUẦN — TRIỆT XUYÊN TẦNG**
>
> | Tầng | Cung | Tuần/Triệt? | Tác động lên T11 (Sửu-Thân) |
> |---|---|---|---|
> | **Gốc Mệnh** | Hợi | **TUẦN** ☁️ | Cách 2 cung — Tuần Mệnh KHÔNG ảnh hưởng trực tiếp Sửu |
> | **Gốc Thân** | **Sửu** | **KHÔNG** ✅ | ⭐ **Sửu SẠCH — Pháo Đài KHÔNG bị phong tỏa** |
> | **ĐV4** | Dần | **TRIỆT** ⚡ | Giáp phải NH — Triệt kề bên nhưng KHÔNG LAN sang Sửu |
> | **NH T11** | **Sửu** | **KHÔNG** ✅ | Sạch — tài chính HIỆN RÕ 100% |
> | **Cung chức** | Sửu (Thân) | **KHÔNG** | 100% kích hoạt |
>
> **🔑 Kết luận:** **Sửu SẠCH + Kim Cục + Nhật Nguyệt Giáp + ĐV giáp = CÁT CỰC ĐẠI không bị phong tỏa.** Triệt nằm ở ĐV (Dần kề bên) nhưng KHÔNG lan sang Sửu. **Tháng tài chính tốt nhất năm.**
>
> ---
> **VI. PHI TINH — Can Canh (T11) — ⚡ TRÙNG CAN CANH NĂM!**
>
> | Phi | Sao | Vào | Hiện tượng |
> |---|---|---|---|
> | Lộc | Thái Dương | Dần (ĐV giáp) | ⭐ Lộc bơm ĐV kề bên → tài sản tăng |
> | Quyền | Vũ Khúc | **Sửu (Thân = NH!)** | ⭐⭐ **QUYỀN ĐÚNG NH** — Pháo Đài nắm QUYỀN tuyệt đối |
> | Khoa | Thái Âm | Tý (Phụ giáp trái) | ✅ Mẹ sáng suốt — lời khuyên đúng |
> | Kỵ | Thiên Đồng | Tý (Phụ giáp trái) | ⚠️ Song Khoa-Kỵ Phụ — mẹ giúp NHƯNG lo lắng quá |
>
> ---
> **VII. HÓA KỴ ĐẮC TẠI SỬU — LUẬN CHUYÊN SÂU (RCA-FIX)**
>
> ⚠️ **QUAN TRỌNG — Hóa Kỵ tại Sửu KHÔNG phải "bế tắc tài chính":**
>
> | Yếu tố | Phân tích | Kết luận |
> |---|---|---|
> | **Kỵ Đắc Địa** | Vũ Khúc Miếu tại Sửu — Kỵ ĐẮC = Phản Vi Giai | Kỵ ĐẢNG NGHỊCH = càng khóa càng giá trị |
> | **Tứ Mộ (Sửu)** | Sửu = ĐẤT, MỘ, KHO = nơi CHÔN GIỮ | Kỵ tại Tứ Mộ = **vùi vàng dưới đất = MỘ KHỐ** |
> | **Chuỗi Tứ Hóa** | Lộc→Quyền→Khoa→**Kỵ** = chốt cuối | Kỵ = NƠI NĂNG LƯỢNG TẬP TRUNG, không phải chặn |
> | **Thanh Long + Nguyệt Đức** | Phúc tinh bảo vệ | Kỵ được phúc tinh che chở → *hung hóa cát* |
> | **Vũ Phúc + Tham** | Vũ = vàng, Tham = đào mỏ, Phúc = may mắn | Bộ ba **KHAI MỎ VÀNG** — Kỵ khóa lại = giữ vàng trong mỏ |
> | **Song Kỵ (Kỵ gốc + Kỵ lưu)** | 2 ổ khóa = khóa kép | **Càng khóa chặt, kho càng an toàn** — không ai lấy được |
>
> **🔑 Kết luận Kỵ Đắc:** "Song Kỵ Thân" tại Sửu = **KHO MỘ KHỐ KHÓA KÉP** — tài sản vùi sâu dưới đất (Tứ Mộ), được Phúc tinh (Thanh Long + Nguyệt Đức) bảo hộ, Vũ Tham đào giữ. **KHÔNG BÁN, KHÔNG RÚT, KHÔNG LỘ.** Để yên = tự tăng giá trị. Đây là cách giàu CỦA NGƯỜI GIÀU THẬT SỰ — giấu vàng dưới nền nhà, mặt ngoài bình thường.
>
> ---
> **VIII. TRÀNG SINH: MỘ ⚰️ (1/10) — CHÔN GIỮ = MỘ KHỐ**
>
> Kim tại Sửu = **Mộ** = "vào mồ". NHƯNG Mộ trong Tràng Sinh = **KHO CHỨA, HANG ĐỘNG VÀNG** — KHÔNG phải chết. Giống như rượu vang: càng ủ trong hầm (Mộ) càng quý. **Mộ + Tứ Mộ (Sửu) + Kỵ Đắc = TRIPLE MỘ KHỐ** — tài sản PHẢI ĐƯỢC CHÔN mới có giá trị. Anh thu hoạch NHƯNG đừng tiêu — CHÔN lại.
>
> ---
> **IX. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động | Hành động |
> |---|---|---|
> | **Y khoa** | Nhật Nguyệt Giáp = uy tín đỉnh | Publish bài, nhận case lớn, build legacy |
> | **AI/CDMS** | ĐV giáp Thân = hạ tầng tài chính × tài sản | Deploy production, chốt hợp đồng |
> | **CK** | ⭐⭐⭐ **MỘ KHỐ MONTH** — Kim Cục lần 3 + Kỵ Đắc | 🟢 THU HOẠCH im lặng. GIỮ vị thế từ T9. Không khoe. **Mặc áo giáp, kiếm tiền trong sương mù** |
>
> ---
> **X. 🗣️ DIỄN GIẢI TỰ NHIÊN**
>
> Anh Long ơi, tháng 11 là tháng "VỀ KHO" — Nguyệt Hạn rơi đúng Gốc Thân, nơi Pháo Đài Vũ Tham Kỵ đã chờ sẵn 34 năm. Nếu T9 là "kho vàng Mệnh hé cửa", thì T11 là "kho vàng Thân MỞ TOÀN BỘ". Kim Cục (Sửu-Tỵ-Dậu) kích hoạt lần thứ 3 — cao trào cuối năm. Nhật Nguyệt Giáp (Mặt Trời Dần kề phải + Mặt Trăng Tý kề trái) soi rọi kho vàng từ 2 phía = không còn bóng tối.
>
> Cái quan trọng nhất tháng này là hiểu ĐÚNG Hóa Kỵ Đắc. Nhiều người thấy "Kỵ" là hoảng, nhưng Kỵ tại Sửu (Đắc Địa, Tứ Mộ) = **chìa khóa chôn vàng.** Hình dung: Vũ Khúc = vàng, Tham Lang = người đào mỏ, Hóa Kỵ = ổ khóa hầm mỏ. Thanh Long + Nguyệt Đức = 2 vị thần canh cửa. Song Kỵ (Kỵ gốc + Kỵ lưu) = khóa KÉP — càng khóa chặt, kho càng an toàn. Tràng Sinh Mộ = hầm rượu — rượu (tài sản) càng ủ lâu càng quý. ***"Giàu mà không ai biết là giàu nhất."***
>
> ĐV Điền Trạch (Dần) giáp phải Sửu = tài sản 10 năm nằm ngay kề Pháo Đài = chiến lược và thực thi SONG SONG. Mọi thứ anh xây suốt 2026 (CDMS, AI Agent, BĐS, CK) hội tụ ở đây. Thu hoạch IM LẶNG — không Facebook, không khoe, không nói cho ai biết. Mộ Khố = im lặng làm giàu.
>
> **Một câu duy nhất:** *Tháng Mộ Khố — mặc áo giáp, kiếm vàng trong sương mù, khóa kho rồi đi ngủ.*"""

OLD_T12 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn trùng khít Đại Vận (Dần-Điền) VÀ Niên Hạn (Dần). BA TẦNG TRÙNG PHÙNG tại một điểm = sự kiện 'Nhật Thực' trong Tử Vi. Cự Nhật Vượng + Triệt + Mã Đắc. Hợi (Mệnh) nhị hợp Dần = kết nối Mệnh-ĐV-NH-Nguyệt đạt mức tối đa. Gốc Thân (Sửu) giáp trái Dần = Pháo Đài ngay cạnh.
> **Kết luận:** Toàn bộ chiều dài 2026 quy tụ đổ xô vào tháng này. Triệt tại Dần vẫn còn nhưng đã nhả ~70-80% ở tuổi 34+ → Cự Nhật bắt đầu phát hào quang. Mã Đắc tại Điền = tài sản di dời, tái cơ cấu. Tháng này = BẢN THIẾT KẾ cho cả thập kỷ ĐV4 được "review tổng" trước khi bước sang 2027.
> **Hành động:** Tổng kết danh mục CK, tái cơ cấu BĐS, rà soát kiến trúc Agent. Thưởng thức thành quả trong tĩnh tại."""

NEW_T12 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — NGUYỆT HẠN T12 (DẦN — ĐIỀN TRẠCH) — ⭐⭐⭐ BA TẦNG TRÙNG PHÙNG**
>
> | Kênh | Đích | Tinh bàn đích (SOT) | Nhận định |
> |---|---|---|---|
> | **Xung chiếu** | Thân (Tử Tức) | VCD + Ân Quang + Đại Hao | 🟡 Con cái/di sản đối diện — tương lai soi ngược |
> | **Tam hợp 1** | Ngọ (Tật Ách) | VCD + Thái Tuế | ⚠️ Hỏa Cục Dần-Ngọ-Tuất lần 3 nhưng nhẹ cuối năm |
> | **Tam hợp 2** | Tuất (Huynh) | VCD + Tuần + Không H + Đà Đ | 🟡 Huynh Dark Pool — dư âm T8 |
> | **Nhị hợp** | **Hợi (GỐC MỆNH)** | Phủ Đ + Lộc Tồn + Tuần | ⭐⭐⭐ **ĐV NHỊ HỢP MỆNH = kết nối tối thượng** |
> | **Giáp trái** | **Sửu (GỐC THÂN)** | Vũ M + Tham M + Kỵ Đ | ⭐⭐ Pháo Đài KỀ SÁT bên trái |
> | **Giáp phải** | Mão (Quan Lộc) | Tướng H + Triệt + Hỏa Đ + Khôi | ⚠️ Quan Triệt kề phải — sự nghiệp chính thống vẫn bị cắt |
> | **Lục hại** | Tỵ (Thiên Di) | Tử Vi M + Sát V + Quyền | ⚠️ Ngoại giao hại Điền — đi ngoài ảnh hưởng nhà cửa |
>
> **📐 Kết luận Hình học:**
>
> **① BA TẦNG TRÙNG PHÙNG: NH = ĐV = Niên Hạn = DẦN:** Đại Vận (Dần) + Niên Hạn (Dần) + Nguyệt Hạn T12 (Dần) = **3 tầng thời gian HỘI TỤ tại 1 điểm** — "Nhật Thực" trong Tử Vi. Toàn bộ năng lượng 2026 ĐỔ DỒN vào Dần.
>
> **② Nhị hợp Dần-Hợi (ĐV-Mệnh) ĐẠT CỰC ĐẠI:** Khi 3 tầng trùng tại Dần, nhị hợp Dần-Hợi = **3 lần nhị hợp đồng thời** = kết nối Mệnh-ĐV MẠNH NHẤT CÓ THỂ. Phủ Lộc (Hợi) giao hòa Cự Nhật (Dần) x3.
>
> **③ Giáp Thân (Sửu bên trái) + Giáp Quan (Mão bên phải):** Dần kẹp giữa Pháo Đài (Sửu) và Sự nghiệp (Mão). ĐV = tài sản nằm GIỮA tiền (trái) và nghề (phải) = **vị trí chiến lược trung tâm.**
>
> ---
> **II. NGŨ HÀNH CƠ HỌC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh **KIM** vs Dần **MỘC** | Kim khắc Mộc = **CHỦ ĐỘNG CẮT** | Anh CẮT cây (tái cơ cấu tài sản) — chủ động, không bị ép |
> | Cự **THỦY** Vượng vs Dần **MỘC** | Thủy sinh Mộc = sao sinh cung | Cự NUÔI cung = tri thức/tiếng nói làm tài sản TĂNG TRƯỞNG |
> | Dương **HỎA** Vượng vs Dần **MỘC** | Mộc sinh Hỏa = **BÙNG SÁNG** | Ánh sáng RỰC RỠ — mọi thứ NHÌN THẤY RÕ |
>
> ---
> **III. ĐẠI VẬN (DẦN) × NH (DẦN) — TRÙNG KHÍT 100%**
>
> **ĐV = NH = CÙNG CUNG.** Đây là tháng DUY NHẤT trong năm mà NH trùng khít ĐV. Toàn bộ năng lượng "xây tài sản 10 năm" BẬT TOÀN TẢI trong 1 tháng. Cự Nhật Vượng phát sáng CỰC ĐẠI. Triệt nhả ~70-80% ở 34+ → **ánh sáng xuyên qua lớp Triệt mỏng còn lại.**
>
> ---
> **IV. NIÊN HẠN (DẦN) × NH (DẦN) — TRÙNG KÉP**
>
> Niên TRÙNG ĐV TRÙNG NH = **Tam Trùng Dần.** Năng lượng Cự Nhật x3. Mã Đắc x3 = di chuyển/tái cơ cấu MẠNH x3.
>
> ---
> **V. TUẦN — TRIỆT XUYÊN TẦNG**
>
> | Tầng | Cung | Tuần/Triệt? | Tác động lên T12 (Dần-Điền) |
> |---|---|---|---|
> | **Gốc Mệnh** | Hợi | **TUẦN** ☁️ | Nhị hợp Dần x3 = Tuần Mệnh bị kéo giãn tối đa. "Song Không = Không Không = CÓ" x3 |
> | **Gốc Thân** | Sửu | Không | Giáp trái — Pháo Đài THÔNG hỗ trợ tối đa |
> | **ĐV4** | **Dần** | **TRIỆT** ⚡ | ⚠️ **NH TRÙNG TRIỆT ĐV** — Triệt kích hoạt tối đa. NHƯNG 34+ → nhả 70-80% → tia sáng xuyên qua |
> | **NH T12** | **Dần** | **TRIỆT** ⚡ | NH tại cung Triệt = tháng cuối năm bị nén — áp lực chốt hạ lớn |
> | **Cung chức** | Dần (Điền) | **TRIỆT** | 100% kích hoạt + Triệt = tài sản xây trong ÁP LỰC nhưng BỀN |
> | **Giáp phải** | Mão (Quan) | **TRIỆT** ⚡ | Song Triệt Dần-Mão = đường chính thống KHÓA KÉP — xây tài sản phi truyền thống |
>
> **🔑 Kết luận:** **T12 = THÁNG TRIỆT ĐỈNH.** NH + ĐV + Niên tất cả tại Dần (Triệt). Triệt x3 = áp lực CỰC LỚN nhưng Triệt nhả dần → "tia sáng xuyên đêm". Song Không (Tuần Hợi nhị hợp Triệt Dần) x3 = CÓ x3 → **tháng tài sản BẬT TOÀN TẢI trong sương mù.**
>
> ---
> **VI. PHI TINH — Can Tân (T12)**
>
> | Phi | Sao | Vào | Hiện tượng |
> |---|---|---|---|
> | Lộc | Cự Môn | **Dần (NH=ĐV!)** | ⭐⭐⭐ **LỘC ĐÚNG TAM TRÙNG** — Cự Lộc bơm thẳng vào ĐV+NH |
> | Quyền | Thái Dương | **Dần (NH=ĐV!)** | ⭐⭐⭐ **QUYỀN ĐÚNG TAM TRÙNG** — Dương Quyền bơm thẳng |
> | Khoa | Văn Xương | Dậu (Thê) | 📝 Tri thức vào hôn nhân — đối thoại sáng suốt |
> | Kỵ | Văn Xương | Dậu (Thê) | ⚠️ Kỵ cũng vào Thê — Song Khoa-Kỵ Thê (nhẹ) |
>
> **🔥 SONG CÁT BƠM THẲNG NH=ĐV=NIÊN:** Cự Lộc + Dương Quyền PHI TRÙNG vào Dần → năng lượng tài sản CỰC ĐẠI. Triệt nén + Song Cát bơm = **áp suất tạo kim cương.** Tháng này không thoải mái nhưng TẠO RA GIÁ TRỊ CỰC CAO.
>
> ---
> **VII. TRÀNG SINH: TUYỆT 💫 (1/10) — CẮT ĐỨT RỒI TÁI SINH**
>
> Kim tại Dần = **Tuyệt** = "đứt hoàn toàn". Năng lượng Kim cũ CẮT SẠCH. NHƯNG Tuyệt = tiền đề cho Thai (T1 năm sau) → **vòng Tràng Sinh RESET.** Năm 2026 kết thúc bằng việc cắt đứt mọi thứ cũ, chuẩn bị cho vòng mới 2027.
>
> ---
> **VIII. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động | Hành động |
> |---|---|---|
> | **Y khoa** | Tam Trùng Dần = review tổng thành quả 2026 | Tổng kết số liệu, submit bài, kết đề cương NCS |
> | **AI/CDMS** | Song Cát ĐV = CDMS nhận Lộc + Quyền | ⭐ Chốt architecture, deploy stable, hand-off IT |
> | **CK** | Triệt nén + Song Cát bơm = áp suất tạo kim cương | 🟢 TÁI CƠ CẤU danh mục. Chốt lãi T9-T11, chuẩn bị port 2027 |
>
> ---
> **IX. 🗣️ DIỄN GIẢI TỰ NHIÊN**
>
> Anh Long ơi, tháng 12 là tháng "NHẬT THỰC" — khi Mặt Trời, Mặt Trăng và Trái Đất thẳng hàng. Nguyệt Hạn + Đại Vận + Niên Hạn = 3 tầng thời gian TRÙNG PHÙNG tại Dần (Điền Trạch). Toàn bộ 2026 co rút lại thành 1 tháng, tất cả năng lượng ĐỔ DỒN vào tài sản.
>
> Cảm giác tháng này: ÁP LỰC CỰC LỚN nhưng CÓ KẾT QUẢ. Triệt x3 = 3 lớp áp lực chồng lên nhau. NHƯNG Song Cát (Cự Lộc + Dương Quyền) phi TRÙNG vào Dần = năng lượng BƠM xuyên qua Triệt. Giống như mũi khoan diamond: Triệt là đá cứng, Song Cát là mũi khoan — càng áp lực, càng xuyên sâu, càng tạo ra kim cương.
>
> Pháo Đài (Sửu) giáp trái = kho tiền ngay kề bên. Mệnh (Hợi) nhị hợp x3 = bản ngã kết nối sâu nhất có thể. Tràng Sinh Tuyệt = vòng đời 2026 KẾT THÚC — cắt sạch da cũ, chuẩn bị cho Thai (T1/2027). **Tháng tổng kết, tái cơ cấu, và RESET.**
>
> Tái cơ cấu danh mục CK: chốt lãi từ T9-T11 (Tam Lộc + Mộ Khố), giữ core position, chuẩn bị port 2027. CDMS: chốt architecture, hand-off IT. NCS: submit đề cương. BĐS: ký hợp đồng cuối cùng.
>
> **Một câu duy nhất:** *Tháng Nhật Thực — 3 tầng trùng phùng, áp suất tạo kim cương, rồi RESET.*"""

content = Path(TARGET).read_text('utf-8')
count = 0
for label, old, new in [("T11", OLD_T11, NEW_T11), ("T12", OLD_T12, NEW_T12)]:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"[{label} ✅] Injected")
    else:
        print(f"[{label} ⚠️] Not found")
Path(TARGET).write_text(content, 'utf-8')
apply_hoa_ky_guardrails_to_file(TARGET)
print(f"Done: {count} month(s)")
