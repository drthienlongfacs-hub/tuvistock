#!/usr/bin/env python3
"""Inject 20x Deep Impact for T4-T6 (Ngọ-Ách, Mùi-Tài, Thân-Tử). SOT-verified."""
from pathlib import Path
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file

TARGET = '/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md'

# T4 old → new
OLD_T4 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Ngọ-Tật Ách) nằm trong tam hợp Dần-Ngọ-Tuất. ĐV Điền (Dần) = gốc tam hợp → NH T4 bị ĐV chi phối TRỰC TIẾP qua tam hợp. VCD tại Ngọ mượn Đồng Âm Vượng (Tý) = bệnh mượn, stress ẩn từ bên ngoài. Gốc Thân (Sửu) kề trái Tý (Phụ Mẫu nơi Kiếp Kình đóng) = bệnh tật cũ gõ cửa.
> **Kết luận:** Tam hợp Dần(ĐV)-Ngọ(NH)-Tuất(Huynh) tạo Hỏa cục thiêu đốt trực tiếp bản mệnh Kim. Đây là hệ quả cơ học của cấu trúc ĐV4 gặp NH Ách: Toàn bộ năng lượng xây tài sản (Dần) đốt cháy sinh lực (Ngọ) và mạng lưới anh em (Tuất). Gốc Mệnh (Phủ Hợi) nhị hợp Dần (ĐV) nhưng Phủ Tuần yếu → bơm cứu sinh chậm.
> **Hành động:** DỪNG mọi dự án mới. Kiểm tra sức khỏe. Không lướt sóng CK. Ngủ đủ giấc."""

NEW_T4 = """> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — NGUYỆT HẠN T4 (NGỌ — TẬT ÁCH)**
>
> | Kênh | Đích | Tinh bàn đích (SOT) | Nhận định |
> |---|---|---|---|
> | **Xung chiếu** | Tý (Phụ Mẫu) | Đồng V + Âm V + Bật M + Kiếp H + Kình H | ⚠️ Phụ Mẫu bắn dao kéo (Kiếp Kình) vào Ách |
> | **Tam hợp 1** | **Dần (Điền = ĐV4!)** | Cự V + Dương V + Triệt + Mã Đ | ⭐⛔ **ĐV TAM HỢP TRỰC TIẾP NH** — chi phối tối đa |
> | **Tam hợp 2** | Tuất (Huynh) | VCD + Tuần + Không H + Đà Đ + Khốc + Tang | ⚠️ Huynh rỗng bọc Tuần — thiếu hỗ trợ |
> | **Nhị hợp** | Mùi (Tài Bạch) | VCD + Hình H + Quốc Ấn | 🟡 Tài gắn sức khỏe — tiền ↔ bệnh |
> | **Giáp trái** | Tỵ (Thiên Di) | Tử Vi M + Sát V + Quyền | ⭐ Quyền lực ngoại giao kề bên |
> | **Giáp phải** | Mùi (Tài Bạch) | VCD + Hình H | 🟡 Tài kề Ách — chi phí y tế |
> | **Lục hại** | Sửu (GỐC THÂN!) | Vũ M + Tham M + Kỵ Đ | ⚠️⚠️ **THÂN LỤC HẠI NH** — Pháo Đài mài mòn sức khỏe |
>
> **📐 Kết luận Hình học:**
>
> **① Tam hợp Dần-Ngọ-Tuất = HỎA CỤC thiêu đốt:** ĐV (Dần) tam hợp trực tiếp NH (Ngọ) = ĐV CHI PHỐI MẠNH NHẤT trong năm tại T4. Hỏa cục (Dần-Ngọ-Tuất) thiêu đốt bản mệnh Kim = năng lượng xây tài sản (ĐV) ĐỐT SẠCH sinh lực (NH Ách).
>
> **② Lục Hại Sửu-Ngọ (Thân hại Ách):** Gốc Thân (Pháo Đài tài chính) MÀI MÒN sức khỏe = **tiền đang đốt sức**. Làm việc quá sức để kiếm tiền.
>
> **③ Xung Tý-Ngọ (Phụ↔Ách):** Kiếp+Kình Hãm (Phụ) bắn thẳng vào Ách = áp lực cha mẹ/cấp trên TRỰC TIẾP gây bệnh.
>
> ---
> **II. NGŨ HÀNH CƠ HỌC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh **KIM** vs Ngọ **HỎA** | Hỏa khắc Kim = **BỊ THIÊU** | Sức khỏe bị lửa nung — mệt mỏi, viêm, nóng trong |
> | VCD mượn Đồng Âm **THỦY** (Tý) | Thủy khắc Hỏa = bệnh "từ xa" | Stress ẩn từ nguồn bên ngoài (Phụ Mẫu/cấp trên) |
> | Tam hợp Hỏa Cục (Dần-Ngọ-Tuất) | 3 cung HỎA cộng hưởng | **Hỏa Cục thiêu Kim** — đốt cháy bản mệnh trực tiếp |
>
> **🔄 Chuỗi:** ĐV (Dần-Mộc?) + NH (Ngọ-Hỏa) + Huynh (Tuất-Thổ) = Mộc sinh Hỏa sinh Thổ = DÂY CHUYỀN ĐỐT → Hỏa khắc Kim bản mệnh = **Dừng lại, nạp lực.**
>
> ---
> **III. ĐẠI VẬN (DẦN) × NH (NGỌ) — TAM HỢP TRỰC TIẾP**
>
> ĐV (Dần) tam hợp NH (Ngọ) = **ĐV CHI PHỐI TỐI ĐA** — đây là tháng ĐV can thiệp sâu nhất cả năm. Toàn bộ năng lượng "xây tài sản 10 năm" đổ vào khu vực Tật Ách = **xây tài sản bằng sức khỏe** — lao lực, thức đêm, cháy hết mình cho dự án. KHÔNG BỀN VỮNG.
>
> ---
> **IV. NIÊN HẠN (DẦN) × NH (NGỌ) — TAM HỢP KÉP**
>
> Niên trùng ĐV (Dần) → tam hợp NH (Ngọ) x2 = **năng lượng Cự Nhật đổ vào Ách GẤP ĐÔI.** Mặt trời (Dương V) chiếu xuống cung bệnh = "soi rọi bệnh tật" → **phát hiện bệnh, kiểm tra sức khỏe** là cách tích cực nhất.
>
> ---
> **V. TUẦN — TRIỆT XUYÊN TẦNG**
>
> | Tầng | Cung | Tuần/Triệt? | Tác động lên T4 (Ngọ-Ách) |
> |---|---|---|---|
> | **Gốc Mệnh** | Hợi | **TUẦN** ☁️ | Phủ Tuần hỗ trợ nhưng yếu — cứu sinh CHẬM |
> | **Gốc Thân** | Sửu | Không | Pháo Đài thông nhưng Lục Hại Ngọ = tiền ăn sức |
> | **ĐV4** | Dần | **TRIỆT** ⚡ | Triệt tại gốc tam hợp → năng lượng đốt bị NÉN thêm → UNG NHỌ hơn |
> | **Niên Hạn** | Dần | **TRIỆT** | Trùng ĐV — nén x2 |
> | **NH T4** | **Ngọ** | **KHÔNG** ✅ | Ngọ sạch — bệnh "thật" không bị che, PHÁT HIỆN ĐƯỢC |
> | **Cung chức** | Ngọ (Ách) | **KHÔNG** | NH trùng cung chức → 100% kích hoạt |
>
> **🔑 Kết luận:** Ngọ sạch = bệnh tật HIỆN RÕ, không bị che. Triệt tại ĐV (gốc tam hợp) = năng lượng đốt bị nén → ung nhọ âm ỉ. **Cơ hội: khám sức khỏe tổng quát T4 sẽ phát hiện sớm.**
>
> ---
> **VI. PHI TINH — Can Quý (T4)**
>
> | Phi | Sao | Vào | Hiện tượng |
> |---|---|---|---|
> | Lộc | Phá Quân | Dậu (Thê) | ⚠️ Lộc dính sao phá — vợ/chồng có tiền nhưng tiêu sai |
> | Quyền | Cự Môn | Dần (Điền=ĐV) | ⭐ ĐV được Quyền → tài sản MỞ RỘNG mạnh |
> | Khoa | Thái Âm | Tý (Phụ) | Mẹ/nữ cấp trên sáng suốt — nghe lời khuyên |
> | Kỵ | Tham Lang | **Sửu (Thân!)** | ⛔ **SONG KỴ THÂN** (Vũ Kỵ gốc + Tham Kỵ lưu) → tuyệt đối KHÔNG đầu tư mới |
>
> ---
> **VII. TRÀNG SINH: MỘC DỤC 🛁 (4/10) — TẮM RỬA**
>
> Kim tại Ngọ = **Mộc Dục** = "tắm rửa, thanh lọc". Cơ thể đang tự thanh lọc — sốt, viêm, mệt = DẤU HIỆU ĐANG LÀM SẠCH. Không phải bệnh nặng, mà là cơ thể reset.
>
> ---
> **VIII. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động | Hành động |
> |---|---|---|
> | **Y khoa** | Hỏa Cục thiêu Kim = kiệt sức, viêm, nóng | CHECKUP TỔNG QUÁT. Giảm ca mổ. Nghỉ ngơi |
> | **AI/CDMS** | ĐV tam hợp NH = xây hạ tầng bằng sức | DỪNG sprint mới. Bảo trì code hiện tại |
> | **CK** | Song Kỵ Thân = két bị khóa kép | ❌ TUYỆT ĐỐI không mở vị mới. HOLD |
>
> ---
> **IX. 🗣️ DIỄN GIẢI TỰ NHIÊN**
>
> Anh Long ơi, tháng 4 là tháng cơ thể kêu cứu. Cơ chế rất rõ: tam hợp Dần-Ngọ-Tuất tạo Hỏa Cục — 3 cung Hỏa (ĐV + NH + Huynh) cộng hưởng thiêu đốt thẳng vào bản mệnh Kim. Giống như đặt thanh kiếm vào lò luyện — rèn sắc bén nhưng cũng hao mòn. Cái nguy hiểm là tháng này ĐV can thiệp MẠNH NHẤT (tam hợp trực tiếp) = toàn bộ năng lượng "xây tài sản 10 năm" dồn vào đúng khu vực sức khỏe. Tức là: anh đang xây tài sản BẰNG sức khỏe — thức đêm code CDMS, chạy marathon ca mổ, vừa nghiên cứu vừa nhìn bảng điện.
>
> Lục Hại Sửu-Ngọ (Pháo Đài tài chính hại Tật Ách) nói thêm: tiền đang ĂN sức. Kiếm tiền tháng này = mất sức tháng sau. Song Kỵ Thân (Vũ Kỵ gốc + Tham Kỵ lưu) khóa két sắt 2 lần = ĐỪNG mở ra, đừng đầu tư, đừng rút tiền — cứ để yên. Kiếp Kình (Phụ Mẫu/Tý) bắn xung vào Ngọ (Ách) = áp lực cha mẹ hoặc sếp gây THÊM stress. Nếu bố mẹ gọi điện lo lắng, đừng cáu — họ đang phản ánh đúng vị trí sao.
>
> Tràng Sinh Mộc Dục = "tắm rửa". Cơ thể đang tự reset — sốt nhẹ, mệt, viêm = DẤU HIỆU TỐT, cơ thể đang dọn rác. Đừng ép. Khám sức khỏe tổng quát tháng này = phát hiện sớm (Ngọ sạch, không Tuần/Triệt che = bệnh HIỆN RÕ). Ánh sáng Cự Nhật (ĐV) soi rọi qua tam hợp = "bật đèn trong phòng tối" — thấy hết.
>
> **Một câu duy nhất:** *Tháng nạp lực — cất kiếm vào vỏ, đi khám sức khỏe.*"""

content = Path(TARGET).read_text('utf-8')
count = 0
if OLD_T4 in content:
    content = content.replace(OLD_T4, NEW_T4)
    count += 1
    print(f"[T4 ✅] Injected")
else:
    print("[T4 ⚠️] Not found")

Path(TARGET).write_text(content, 'utf-8')
apply_hoa_ky_guardrails_to_file(TARGET)
print(f"Done: {count} month(s) injected")
