#!/usr/bin/env python3
"""Inject 20x Deep Impact for T5-T6. SOT-verified."""
from pathlib import Path
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file

TARGET = '/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md'

OLD_T5 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Mùi-Tài Bạch) xung chiếu trực diện Gốc Thân (Sửu-Vũ Tham Kỵ). Trục Sửu-Mùi là trục TÀI-PHÚC — mũi khoan Kỵ (Sửu) xuyên thẳng vào VCD Hình Hãm (Mùi). ĐV Điền (Dần) giáp phải Mão (Quan-Triệt) = đòn bẩy ĐV không vươn tới Mùi, phải qua 3 cung trung gian → ĐV KHÔNG che chắn được trục Tài.
> **Kết luận:** Đây KHÔNG phải tháng xui ngẫu nhiên — mà là kích nổ có toán học của trục Sửu-Mùi gốc: Kỵ "khóa kho" PHẢN chuyển thành "khóa thanh khoản" khi NH rơi đúng Mùi. ĐV Điền (Dần) cách xa Mùi (5 cung) → KHÔNG CAN THIỆP ĐƯỢC. Gốc Mệnh Phủ (Hợi) tam hợp Mùi = tuyến phòng thủ duy nhất, nhưng Phủ bị Tuần → chỉ cản 50%.
> **Hành động:** Phòng thủ thanh khoản TUYỆT ĐỐI. Ôm tiền mặt. Không ký văn bản pháp lý."""

NEW_T5 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — NGUYỆT HẠN T5 (MÙI — TÀI BẠCH)**
>
> | Kênh | Đích | Tinh bàn đích (SOT) | Nhận định |
> |---|---|---|---|
> | **Xung chiếu** | **Sửu (GỐC THÂN!)** | Vũ M + Tham M + Kỵ Đ + Thanh Long + Nguyệt Đức | ⛔⭐ **TRỤC THÂN-TÀI kích hoạt** — Pháo Đài xung chiếu trực tiếp |
> | **Tam hợp 1** | **Hợi (GỐC MỆNH)** | Phủ Đ + Lộc Tồn + Khoa + Tuần | ⭐ Mệnh hậu thuẫn tài chính |
> | **Tam hợp 2** | Mão (Quan Lộc) | Tướng H + Triệt + Hỏa Đ + Khôi | ⚠️ Quan Triệt gắn Tài — sự nghiệp chính thống KHÔNG mang tiền |
> | **Nhị hợp** | Ngọ (Tật Ách) | VCD + Thái Tuế + L.Kình | ⚠️ Sức khỏe gắn tiền bạc |
> | **Giáp trái** | Ngọ (Tật Ách) | (trùng nhị hợp) | Ách kề Tài — chi phí y tế |
> | **Giáp phải** | Thân (Tử Tức) | VCD + Ân Quang + Đại Hao | 🟡 Con cái kề Tài — chi tiêu cho con |
> | **Lục hại** | Tý (Phụ Mẫu) | Đồng V + Âm V + Kiếp H + Kình H | ⚠️ Phụ Mẫu hại Tài — cha mẹ/sếp gây phiền phức tài chính |
>
> **📐 Kết luận Hình học:**
>
> **① Trục Xung Sửu-Mùi (Thân↔Tài) kích hoạt:** Đây là trận chiến TÀI CHÍNH trung tâm. Vũ Tham Kỵ (Sửu/Pháo Đài) bắn xung chiếu thẳng vào VCD Hình Hãm (Mùi/Tài) = "Kỵ khóa kho" chuyển thành "Kỵ khóa thanh khoản" — tiền CÓ nhưng KHÔNG LẤY RA ĐƯỢC.
>
> **② ĐV cách xa 5 cung (Dần→...→Mùi):** Không giáp, không tam hợp, không nhị hợp, không xung = **ĐV HOÀN TOÀN KHÔNG CAN THIỆP trục Tài.** Tháng này anh đơn độc trên mặt trận tiền bạc.
>
> **③ Phòng thủ duy nhất = tam hợp Mệnh (Hợi-Mão-Mùi):** Phủ Đắc Lộc (Hợi) tam hợp Mùi = tuyến cứu sinh. NHƯNG Phủ bị Tuần → chỉ cản 50%. Mão (Quan) cũng trong tam hợp nhưng bị Triệt → thêm 1 mắt xích yếu.
>
> ---
> **II. NGŨ HÀNH CƠ HỌC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh **KIM** vs Mùi **THỔ** | Thổ sinh Kim = **ĐƯỢC NUÔI** | Cung Tài nuôi bản mệnh — TIỀN CÓ, nhưng bị Hình cản trở |
> | VCD mượn Vũ Tham **KIM/MỘC** (Sửu) | Kim đồng hành, Mộc bị Kim khắc | Tiền từ nguồn ĐỐI DIỆN — phụ thuộc vào Pháo Đài |
> | Hình **HỎA** Hãm vs Mùi **THỔ** | Hỏa sinh Thổ nhưng Hãm | Áp lực pháp lý/quan tài nhẹ → tiền kèm phiền |
>
> ---
> **III. ĐẠI VẬN (DẦN) × NH (MÙI) — KHÔNG KẾT NỐI**
>
> ĐV Dần cách Mùi 5 cung. Không có kênh trực tiếp nào. **ĐV "bỏ rơi" NH T5** — anh phải tự xử lý trục tài chính mà không có năng lượng 10 năm hậu thuẫn. Đây là tháng CÔ ĐỘC NHẤT về cơ cấu.
>
> ---
> **IV. NIÊN HẠN (DẦN) × NH (MÙI) — KHÔNG KẾT NỐI**
>
> Niên trùng ĐV, cũng cách 5 cung. Tương tự — không can thiệp.
>
> ---
> **V. TUẦN — TRIỆT XUYÊN TẦNG**
>
> | Tầng | Cung | Tuần/Triệt? | Tác động lên T5 (Mùi-Tài) |
> |---|---|---|---|
> | **Gốc Mệnh** | Hợi | **TUẦN** ☁️ | Tam hợp Mùi NHƯNG Tuần che → phòng thủ chỉ 50% |
> | **Gốc Thân** | Sửu | Không | Pháo Đài thông suốt BẮN xung Mùi = toàn lực đánh trục Tài |
> | **ĐV4** | Dần | **TRIỆT** ⚡ | Xa 5 cung + Triệt = hoàn toàn vô hiệu |
> | **NH T5** | **Mùi** | **KHÔNG** ✅ | Mùi sạch — tài chính HIỆN RÕ, không bị che |
> | **Cung chức** | Mùi (Tài) | **KHÔNG** | NH trùng cung chức = 100% kích hoạt trục Tài |
> | **Mão (Quan) trong tam hợp** | Mão | **TRIỆT** ⚡ | Mắt xích yếu trong tam hợp phòng thủ Hợi-Mão-Mùi |
>
> **🔑 Kết luận:** Mùi sạch + Sửu thông = trục Tài TRẦN TRỤI — không che, không đỡ. Tài chính T5 "naked" — tốt xấu đều hiện rõ. Phòng thủ tam hợp (Hợi-Mão-Mùi) bị suy yếu vì Hợi Tuần + Mão Triệt = 2/3 mắt xích phòng thủ bị phong.
>
> ---
> **VI. PHI TINH — Can Giáp (T5)**
>
> | Phi | Sao | Vào | Hiện tượng |
> |---|---|---|---|
> | Lộc | Liêm Trinh | Dậu (Thê) | 🟢 Vợ/chồng MANG LỘC tài chính — phao cứu sinh |
> | Quyền | Phá Quân | Dậu (Thê) | 🟢 **Song Cát Thê** — vợ/chồng nắm quyền quyết định tài chính đúng |
> | Khoa | Vũ Khúc | Sửu (Thân) | ⭐ Trí tuệ bảo vệ Pháo Đài — lá chắn tài chính |
> | Kỵ | Thái Dương | Dần (ĐV) | ⚠️ Kỵ đánh ĐV Điền → BĐS/tài sản gặp xáo trộn nhẹ |
>
> **🔥 Điểm sáng Phi Tinh T5:** Song Cát (Lộc+Quyền) đổ vào Phu Thê (Dậu) = **VỢ/CHỒNG là nguồn cứu sinh T5.** Đây là tháng vợ/chồng mang tiền về, đưa quyết định tài chính đúng, hoặc giới thiệu cơ hội đầu tư.
>
> ---
> **VII. TRÀNG SINH: QUAN ĐỚI 🎓 (7/10) — ĐƯỢC CÔNG NHẬN**
>
> Kim tại Mùi = **Quan Đới** = "đội mũ, mặc áo công chức". Bắt đầu được xã hội CÔNG NHẬN. Vị trí tăng. Tuy NH Tài khó khăn, nhưng GIÁ TRỊ bản thân đang TĂNG — thành quả tích lũy từ T1-T4 bắt đầu hiện.
>
> ---
> **VIII. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động | Hành động |
> |---|---|---|
> | **Y khoa** | Ách (Ngọ) nhị hợp Tài (Mùi) = sức khỏe gắn tiền | Thu phí tư vấn, nhận ca mổ ngoài giờ chọn lọc |
> | **AI/CDMS** | ĐV không can thiệp = CDMS tạm dừng sprint | Bảo trì, fix bug, KHÔNG feature mới |
> | **CK** | Trục Tài naked + Song Cát Thê | ✅ Nghe vợ/chồng + khóa thanh khoản. MSCI T6 DL sắp tới — ĐỪNG bán trước |
>
> ---
> **IX. 🗣️ DIỄN GIẢI TỰ NHIÊN**
>
> Anh Long ơi, tháng 5 là tháng "đếm tiền giữa bão". Mùi (Tài Bạch) VCD = kho tiền trống, phải mượn từ Sửu (Pháo Đài) đối diện. Hình ảnh trực quan: anh đứng ở kho trống (Mùi), nhìn qua bên kia thấy két sắt Vũ Tham Kỵ (Sửu) đầy ắp — nhưng giữa 2 bên là con sông xung chiếu. Tiền CÓ nhưng phải qua cầu mới lấy được, mà cầu lại rung lắc (Kỵ).
>
> Điều đặc biệt nhất tháng này: Đại Vận (Dần) cách Mùi tận 5 cung, KHÔNG CÓ KÊNH nào kết nối — ĐV "bỏ rơi" tháng này. Anh tự xử. NHƯNG Phi Tinh Can Giáp đổ Song Cát (Liêm Lộc + Phá Quyền) vào Dậu (Phu Thê) = **vợ/chồng là phao cứu sinh.** Nếu vợ đưa ra ý kiến tài chính, NGHE. Nếu vợ giới thiệu cơ hội, XEM XÉT. Đây là tháng Dậu (Thê) thay thế ĐV làm trụ cột.
>
> Tràng Sinh Quan Đới = bắt đầu được công nhận. Dù tiền khó khăn, giá trị bản thân TĂNG — người ta bắt đầu nhìn anh khác. MSCI review T6 DL sắp tới — hold chặt SHB/TCB.
>
> **Một câu duy nhất:** *Tháng nghe vợ — kho trống nhưng cầu vẫn có.*"""

# T6 old → new
OLD_T6 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Thân-Tử Tức) tam hợp Tý (Phụ Mẫu) + Thìn (Nô). VCD mượn chiếu Dần (Cự Nhật) = ĐV Điền. ĐV Điền chiếu thẳng vào NH Thân qua đối cung = ĐV CHI PHỐI MẠNH tháng này. Gốc Mệnh (Phủ Hợi) không có kênh trực tiếp đến Thân → Nguyệt hạn chạy theo ĐV, không theo Mệnh.
> **Kết luận:** Năng lượng Đại Hao (Thân) + chiếu từ Cự Nhật ĐV → chi tiêu tái cơ cấu phục vụ chiến lược tài sản dài hạn. Khác hẳn tháng 5 (mất mát do xung chiếu): tháng 6 là CHI TIỀN CÓ CHỦ ĐÍCH để xây nền tảng ĐV.
> **Hành động:** Đầu tư hạ tầng (server, công cụ AI, sửa nhà). Dọn dẹp hệ thống."""

NEW_T6 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — NGUYỆT HẠN T6 (THÂN — TỬ TỨC)**
>
> | Kênh | Đích | Tinh bàn đích (SOT) | Nhận định |
> |---|---|---|---|
> | **Xung chiếu** | **Dần (Điền = ĐV4!)** | Cự V + Dương V + Triệt + Mã Đ | ⭐⛔ **ĐV XUNG CHIẾU TRỰC TIẾP NH** — chi phối tối đa |
> | **Tam hợp 1** | Tý (Phụ Mẫu) | Đồng V + Âm V + Bật M + Kiếp H + Kình H | ⭐⚠️ Phụ Mẫu mạnh nhưng mang dao kéo |
> | **Tam hợp 2** | Thìn (Nô Bộc) | Cơ M + Lương M + Hóa Lộc V | ⭐ Brain Trust hỗ trợ qua tam hợp |
> | **Nhị hợp** | Tỵ (Thiên Di) | Tử Vi M + Sát V + Quyền | ⭐ Ngoại giao liên hệ ngầm con cái |
> | **Giáp trái** | Mùi (Tài Bạch) | VCD + Hình H | 🟡 Tài kề Tử — chi phí cho con |
> | **Giáp phải** | Dậu (Phu Thê) | Liêm Phá H + Linh H + Đào V | ⚠️ Thê kề Tử — vợ/chồng gắn con cái |
> | **Lục hại** | **Hợi (GỐC MỆNH!)** | Phủ Đ + Lộc Tồn + Tuần | ⚠️⚠️ **MỆNH LỤC HẠI NH** — bản mệnh mài mòn ngầm |
>
> **📐 Kết luận Hình học:**
>
> **① ĐV xung chiếu trực tiếp:** Dần (ĐV) ↔ Thân (NH) = xung chiếu = ĐV ĐỔ TOÀN LỰC vào tháng này. Cự Nhật V chiếu thẳng từ Điền sang Tử = "Mặt trời rọi nhà con cái" → chi tiêu tái cơ cấu CÓ CHỦ ĐÍCH.
>
> **② Lục Hại Hợi-Thân (Mệnh hại Tử):** Mệnh (Hợi) hại NH (Thân) = bản mệnh MÀI MÒN NGẦM khi lo cho con cái/dự án nhỏ. **Cho đi quá nhiều năng lượng bản thân.**
>
> **③ Thủy Cục tam hợp (Thân-Tý-Thìn):** Brain Trust (Thìn) + Phụ Mẫu (Tý) hội vào Tử (Thân) = mạng lưới + cha mẹ cùng hỗ trợ chuyện con cái/di sản.
>
> ---
> **II. NGŨ HÀNH CƠ HỌC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh **KIM** vs Thân **KIM** | Kim = Kim = **đồng hành** | Cung Tử đồng hành bản mệnh — thoải mái, tự nhiên |
> | VCD mượn Cự Nhật **THỦY/HỎA** (Dần) | Thủy sinh Kim, Hỏa khắc Kim | Năng lượng hỗn hợp — vừa được nuôi vừa bị áp lực |
> | Đại Hao **KIM** tại Thân **KIM** | Kim x Kim = hao tốn CÙNG CHẤT | Tiêu tiền ĐÚNG HẠNG MỤC — chi cho hạ tầng, không phí phạm |
>
> ---
> **III. ĐẠI VẬN (DẦN) × NH (THÂN) — XUNG CHIẾU TRỰC TIẾP**
>
> ĐV (Dần) xung chiếu NH (Thân) = **can thiệp MẠNH NHẤT** (cùng với T4 tam hợp). Khác T4 (đốt sức): T6 là ĐV Điền (tài sản) CHIẾU vào Tử (di sản, con cái) = **xây di sản dài hạn.** Chi tiêu tháng này = ĐẦU TƯ cho tương lai 10 năm. Mua server, sửa nhà, đóng học phí = ĐÚNG đường ĐV.
>
> ---
> **IV. NIÊN HẠN (DẦN) × NH (THÂN) — XUNG KÉP**
>
> Niên trùng ĐV → xung x2 = năng lượng Cự Nhật chiếu gấp đôi vào Thân. Mã Đắc (Dần) chiếu Thân = di chuyển NHANH, thay đổi MÔI TRƯỜNG sống.
>
> ---
> **V. TUẦN — TRIỆT XUYÊN TẦNG**
>
> | Tầng | Cung | Tuần/Triệt? | Tác động lên T6 (Thân-Tử) |
> |---|---|---|---|
> | **Gốc Mệnh** | Hợi | **TUẦN** ☁️ | Lục Hại Hợi-Thân = Tuần Mệnh "rì rì" mài nhẹ NH — cho mà mệt |
> | **Gốc Thân** | Sửu | Không | Pháo Đài thông — tài chính hậu thuẫn chi tiêu |
> | **ĐV4** | Dần | **TRIỆT** ⚡ | Xung chiếu NH nhưng Triệt nén → chi tiêu bị GIỚI HẠN — không xài hoang được |
> | **NH T6** | **Thân** | **KHÔNG** ✅ | Thân sạch — tự do hoạt động |
> | **Cung chức** | Thân (Tử) | **KHÔNG** | 100% kích hoạt |
>
> **🔑 Kết luận:** ĐV xung chiếu nhưng Triệt nén = chi tiêu CÓ GIỚI HẠN TỰ NHIÊN — Triệt đóng vai "kiểm toán" tự động, ngăn xài quá tay. Mệnh Tuần Lục Hại = cho đi nhiều nhưng bản thân mệt.
>
> ---
> **VI. PHI TINH — Can Ất (T6)**
>
> | Phi | Sao | Vào | Hiện tượng |
> |---|---|---|---|
> | Lộc | Thiên Cơ | Thìn (Nô) | ⭐ Brain Trust sinh Lộc — cộng sự mang cơ hội |
> | Quyền | Thiên Lương | Thìn (Nô) | ⭐ **Song Cát Nô** — mạng lưới CỰC MẠNH tháng này |
> | Khoa | Tử Vi | Tỵ (Di) | 📝 Danh tiếng ngoại giao — được nhìn nhận |
> | Kỵ | Thái Âm | Tý (Phụ) | ⚠️ Mẹ/nữ cấp trên lo lắng quá mức |
>
> ---
> **VII. TRÀNG SINH: LÂM QUAN 🏛️ (8/10) — VÀO CỬA QUAN**
>
> Kim tại Thân = **Lâm Quan** = "bước vào cổng triều đình". Đây là vị trí CỰC MẠNH — năng lượng Kim đạt gần đỉnh. Mọi hành động đều CÓ TRỌNG LƯỢNG.
>
> ---
> **VIII. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động | Hành động |
> |---|---|---|
> | **Y khoa** | Lâm Quan = vào cổng triều đình, uy tín tăng | Nhận case lớn, trình bày trước hội đồng |
> | **AI/CDMS** | ĐV chiếu = đầu tư hạ tầng CDMS dài hạn | Mua server, deploy staging, sửa kiến trúc |
> | **CK** | Song Cát Nô = tip từ mạng lưới | 🟢 Nghe Brain Trust. MSCI T6 DL — xem xét mua nhẹ bluechip |
>
> ---
> **IX. 🗣️ DIỄN GIẢI TỰ NHIÊN**
>
> Anh Long ơi, tháng 6 là tháng "xây móng nhà lần hai". Sau T4 (đốt sức) và T5 (kho trống), T6 xuất hiện với cơ chế hoàn toàn khác: ĐV Điền trạch (Dần) XUNG CHIẾU THẲNG vào NH Tử Tức (Thân). Xung chiếu thường là đối đầu, nhưng ở đây nó là ĐỐI THOẠI — Đại Vận "nói chuyện" trực tiếp với tháng hiện tại, bảo: "Chi tiền, nhưng chi cho TÀI SẢN."
>
> Đại Hao Đắc tại Thân = chi tiêu LỚN — nhưng Đắc = chi ĐÚNG. Mua server cho CDMS, sửa sang nhà cửa, đóng tiền học cho con = tất cả đều ĐÚNG đường ĐV Điền. Triệt tại ĐV ngăn xài hoang — giống như có ông kế toán tự động kiểm soát ngân sách, không cho vượt quota.
>
> Brain Trust (Thìn) được bơm Song Cát (Cơ Lộc + Lương Quyền) = mạng lưới mạnh nhất tháng này. Cộng sự đưa cơ hội, bạn bè giới thiệu deal. Tràng Sinh Lâm Quan = gần đỉnh năng lượng — mọi quyết định đều có trọng lượng, đừng quyết bừa.
>
> NHƯNG coi chừng: Lục Hại Mệnh-NH (Hợi hại Thân) = cho đi quá nhiều, bản thân kiệt. Âm Kỵ đánh Tý (mẹ) = mẹ lo lắng gọi điện liên tục. Giải: nhận cuộc gọi, trấn an, nhưng KHÔNG để ảnh hưởng quyết định tài chính.
>
> **Một câu duy nhất:** *Tháng xây móng — chi tiền cho tài sản, không cho cảm xúc.*"""

content = Path(TARGET).read_text('utf-8')
count = 0
for label, old, new in [("T5", OLD_T5, NEW_T5), ("T6", OLD_T6, NEW_T6)]:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"[{label} ✅] Injected")
    else:
        print(f"[{label} ⚠️] Not found")

Path(TARGET).write_text(content, 'utf-8')
apply_hoa_ky_guardrails_to_file(TARGET)
print(f"Done: {count} month(s) injected")
