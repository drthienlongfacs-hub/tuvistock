# RULES: TỬ VI LUẬN GIẢI — AGENT RULES

> **Áp dụng:** Mọi lần agent xử lý yêu cầu về Tử Vi trong workspace này.

---

## RULE 1: SOURCE OF TRUTH BẮT BUỘC

**🔔 Trigger:** Mọi lần luận giải, viết, hoặc trả lời về lá số Tử Vi

**Áp dụng:**
- ✅ MỞ `.agent/source_of_truth/la_so_long_2026.md` TRƯỚC KHI viết bất kỳ nội dung nào
- ✅ ĐỐI CHIẾU mọi dữ liệu (sao, hành, miếu/hãm, cách cục) với Source of Truth
- ❌ KHÔNG phỏng đoán miếu/hãm, vị trí sao, hay thông tin đương số
- ❌ KHÔNG dùng dữ liệu từ memory/conversation context — luôn đọc file

---

## RULE 2: DATA TRƯỚC — GIẢI SAU

**🔔 Trigger:** Mọi lần luận giải 1 cung hoặc 1 chủ đề Tử Vi

**Áp dụng:**
1. ✅ LIỆT KÊ đầy đủ sao tại cung (bảng) TRƯỚC
2. ✅ LIỆT KÊ 6 chiều tương tác (bảng) TRƯỚC
3. ✅ Sau khi DATA đầy đủ → mới LUẬN GIẢI
4. ❌ KHÔNG viết "Cung này tốt vì..." mà không có data kèm theo

---

## RULE 3: THANG ĐO 5 CHIỀU — TUÂN THỦ TUYỆT ĐỐI

**🔔 Trigger:** Mọi lần so sánh sức mạnh các chiều tương tác

**Áp dụng:**
```
Chính cung (40%) > Xung chiếu (30%) > Tam hợp (20%) > Nhị hợp (10%) > Giáp (~5%)
```

**Ngoại lệ duy nhất:**
- Giáp tại **Sửu/Mùi** (nhị hợp trùng giáp) → kênh kép ~15%
- Cặp Tý-Sửu, Ngọ-Mùi → nhị hợp mạnh hơn bình thường
- PHẢI ghi rõ "ngoại lệ Sửu/Mùi" khi áp dụng

**⛔ SAI phổ biến cần tránh:**
- ❌ "Nhị hợp mạnh hơn chiếu" → SAI
- ❌ "Giáp cung luôn mạnh hơn chiếu" → SAI (chỉ đúng ở Sửu/Mùi + sao đắc)

---

## RULE 4: TRÍCH DẪN PHÚ CỔ — PHẢI CÓ NGUỒN

**🔔 Trigger:** Mọi lần trích dẫn phú Tử Vi

**Áp dụng:**
- ✅ Ghi đầy đủ: Tên phú → Câu phú gốc → Nguồn → Điều kiện áp dụng
- ✅ Ghi rõ: Chính cách hay Biến thể
- ❌ KHÔNG "chế" phú mới
- ❌ KHÔNG trích phú mà không ghi nguồn

---

## RULE 5: VÔ CHÍNH DIỆU — PHẢI NÊU RÕ MƯỢN AI

**🔔 Trigger:** Khi gặp cung VCD (Vô Chính Diệu)

**Áp dụng:**
- ✅ Ghi rõ: "VCD — Mượn chính tinh cung [X] ([tên sao])"
- ✅ Luận theo sao mượn NHƯNG ghi chú giảm lực do mượn
- ❌ KHÔNG bỏ qua cung VCD, KHÔNG nói "cung trống"

---

## RULE 6: TEMPLATE LUẬN GIẢI

**🔔 Trigger:** Khi tạo file luận giải mới

**Áp dụng:**
- ✅ Đọc SKILL.md → dùng template chuẩn (6 mục: Data → 6 chiều → Cách cục → Tổng hợp)
- ✅ File đặt trong `02_luan_giai/`
- ✅ Naming convention: `luan_giai_[cung/chủ đề].md`

---

## RULE 7: CẬP NHẬT SOURCE OF TRUTH

**🔔 Trigger:** Khi phát hiện data mới hoặc sửa lỗi

**Áp dụng:**
1. ✅ Sửa Source of Truth TRƯỚC
2. ✅ Sửa các file luận giải liên quan SAU
3. ✅ Ghi errata tại cuối file bị sửa

---

## RULE 8: PHÂN LOẠI FILE

**🔔 Trigger:** Khi tạo file mới trong workspace

| Loại nội dung | Thư mục | Naming |
|---|---|---|
| Kiểm kê data thô | `01_data_inventory/` | `kiem_ke_[chủ đề].md` |
| Luận giải/phân tích | `02_luan_giai/` | `luan_giai_[chủ đề].md` |
| Cách cục kiểm chứng | `03_cach_cuc/` | `cach_cuc_[chủ đề].md` |
| Lý thuyết/phương pháp | `04_ly_thuyet/` | `[chủ đề].md` |

---

## RULE 9: KHUNG PHÂN TÍCH 7 TRỤC — SINGLE SOURCE OF TRUTH TOÀN DIỆN

**🔔 Trigger:** Mọi lần luận giải Tử Vi — đặc biệt khi phân tích tổng thể lá số, dự báo Đại Vận, hoặc tư vấn hướng đi

**Nền tảng:** Mọi vấn đề phải được đặt vào trung tâm ma trận 2 trục:

### Trục Con Người — Chủ Quan (4 Nhân)

| # | Trục | Nội dung | Ánh xạ Tử Vi | Căn cứ khoa học |
|:---:|---|---|---|---|
| 1 | **Nhân sinh** | Triết lý sống, mục đích đời người | Mệnh + Phúc Đức + Đại Vận | Tâm lý học, triết học thực hành |
| 2 | **Nhân tính** | Bản ngã, tâm lý, xu hướng hành vi | Chính tinh + Tứ Hóa + Miếu/Hãm | Tâm lý học, sinh học tiến hóa |
| 3 | **Nhân tướng** | "Tâm sinh tướng" — thần thái, body language | Cung Mệnh (VCD/chính tinh) + Tật Ách | Nội tiết tố, thói quen, tâm lý biểu cảm |
| 4 | **Nhân quả** | Nguyên nhân → Hệ quả dây chuyền | Tứ Hóa chuỗi (Lộc→Quyền→Khoa→Kỵ) | Systems thinking, logic thực tiễn |

### Trục Vũ Trụ/Môi Trường — Khách Quan (3 Thiên-Địa-Duyên)

| # | Trục | Nội dung | Ánh xạ Tử Vi | Căn cứ khoa học |
|:---:|---|---|---|---|
| 5 | **Bối cảnh Thiên-Địa** | Thời đại (Thiên thời) + Không gian (Địa lợi) | Lưu Niên + Đại Vận (Thiên) / Thiên Di + Ngũ Hành cung (Địa) | Xã hội học, địa chính trị, lịch sử |
| 6 | **Nhân Duyên** | Điều kiện xúc tác, tính ngẫu nhiên, biến số | Tuần Không + Triệt Không + Sát tinh | Xác suất thống kê, Chaos theory, Black Swan |
| 7 | **Quy luật Tự nhiên** | Quy luật vật lý vô cảm, không phụ thuộc ý chí | Ngũ Hành Tương Sinh Tương Khắc | Vật lý, sinh học tiến hóa, logic toán học |

**Áp dụng:**
1. ✅ Khi luận giải 1 cung/1 vấn đề → PHẢI xét ít nhất **cả 2 trục** (Chủ quan + Khách quan)
2. ✅ Khi dự báo → PHẢI đặt trong **Bối cảnh Thiên-Địa** (thời đại, môi trường cụ thể)
3. ✅ Khi nói "cung này tốt/xấu" → PHẢI kèm **Nhân Duyên** (điều kiện để tốt/xấu xảy ra)
4. ✅ Khi phân tích Ngũ Hành sao vs cung → đó chính là trục **Quy luật Tự nhiên** (ghi rõ sinh/khắc)
5. ❌ KHÔNG áp dụng Nhân quả cứng nhắc: "Sao A tại cung B → luôn ra kết quả C" (thiếu Nhân Duyên)
6. ❌ KHÔNG mê tín: Mọi luận giải phải có logic Ngũ Hành HOẶC căn cứ phú cổ có nguồn

**Ví dụ áp dụng — Cung Tài Bạch (Ngọ):**
- **Nhân tính:** VCD → linh hoạt tài chính, không cố định
- **Nhân quả:** Nhật Nguyệt Tịnh Minh (nhân) → dòng tiền lớn từ danh tiếng (quả)
- **Nhân Duyên:** Triệt + Địa Không (duyên xấu) → cắt dòng tiền gốc, tiền khó giữ
- **Quy luật Tự nhiên:** Triệt (Kim) tại Ngọ (Hỏa) → Hỏa khắc Kim → Triệt yếu ~20%
- **Bối cảnh Thiên:** Triệt nhả sau 30 tuổi → phải đợi Thiên thời

---

## RULE 10: PHÂN TÍCH HUNG/SÁT TINH — BẮT BUỘC

**🔔 Trigger:** Mọi lần luận giải đầy đủ 1 cung hoặc tổng thể lá số

**Áp dụng:**
1. ✅ PHẢI liệt kê **mọi sát tinh** (Kình, Đà, Hỏa, Linh, Không, Kiếp) + **hung tinh** (Hình, Kỵ, Tang, Hao...) tại cung
2. ✅ PHẢI ghi **Ngũ Hành sao vs Ngũ Hành cung** + tương tác (sinh/khắc/đồng hành/tiết khí)
3. ✅ PHẢI đánh giá: Sát tinh **tăng lực** hay **giảm lực** tại cung đó (dựa vào Ngũ Hành)
4. ✅ PHẢI xét Tuần/Triệt tại cung đó: Hành Tuần/Triệt vs Hành cung → bảo vệ hay cắt đứt?
5. ✅ Khi luận tổng thể → PHẢI so sánh hung/sát **liên cung**: xung chiếu, tam hợp, trục Tuần vs Triệt
6. ❌ KHÔNG bỏ qua cung "sạch sát" — vẫn phải ghi nhận "Sạch" và giải thích ý nghĩa
7. ❌ KHÔNG nói "cung bị Triệt = xấu" mà không phân tích Ngũ Hành Triệt vs Cung

**Quy tắc Ngũ Hành Sát tinh:**
```
Sát tinh CÙNG HÀNH cung → TĂNG LỰC (VD: Kình Kim tại Dậu Kim = cực mạnh)
Sát tinh bị cung KHẮC → GIẢM LỰC (VD: Triệt Kim tại Ngọ Hỏa = yếu hơn)
Sát tinh SINH cho cung → Hung nhưng NUÔI cung (VD: Hình Hỏa tại Tuất Thổ = đau để trưởng thành)
Sát tinh bị cung TIẾT KHÍ → Hung nhưng bị hút cạn (VD: Tướng Thủy tại Mão Mộc = tiều tụy)
```

---

## RULE 11: TUẦN/TRIỆT — ÁN NGỮ, KHÔNG CHIẾU ⛔

**🔔 Trigger:** Mọi lần phân tích Tuần Không hoặc Triệt Không

**Nguyên tắc cốt lõi:** Tuần Không và Triệt Không **KHÔNG PHẢI SAO.** Chúng là **khoảng trống cấu trúc** (structural void). Do đó:

**⛔ TUYỆT ĐỐI KHÔNG:**
1. ❌ Tuần/Triệt **KHÔNG CHIẾU** (không xung chiếu qua đối cung)
2. ❌ Tuần/Triệt **KHÔNG TAM HỢP** (không hội với cung tam hợp)
3. ❌ Tuần/Triệt **KHÔNG NHỊ HỢP** (không lục hợp)
4. ❌ Tuần/Triệt **KHÔNG GIÁP** (không giáp cung kề cạnh)
5. ❌ KHÔNG viết: "Tuần chiếu từ Tỵ sang Hợi" → **SAI**
6. ❌ KHÔNG viết: "Triệt tam hợp với Dần" → **SAI**

**✅ CƠ CHẾ ĐÚNG:**
1. ✅ Tuần/Triệt **ÁN NGỮ** (occupy) tại 2 cung cố định → ảnh hưởng **CHỈ CÁC SAO** đang đứng tại cung đó
2. ✅ Sao bị Tuần che mờ → khi sao đó chiếu/tam hợp đi nơi khác → chiếu với **LỰC GIẢM**
3. ✅ Sao bị Triệt cắt → khi sao đó chiếu/tam hợp đi nơi khác → chiếu với **LỰC CẮT**
4. ✅ **Tuần/Triệt ảnh hưởng GÁN TIẾP** thông qua sao bị ảnh hưởng, KHÔNG trực tiếp

**Ví dụ đúng — Lá số Cà Rốt:**
```
Tuần tại Thìn (Di): Cơ Lương Miếu bị Tuần che mờ
→ Cơ Lương chiếu về Mệnh (Tuất) với LỰC GIẢM
→ KHÔNG PHẢI "Tuần chiếu về Mệnh" — Tuần KHÔNG chiếu!

Triệt tại Ngọ (Tài): VCD bị Triệt cắt
→ Nhật Nguyệt Tịnh Minh bị giảm hiệu lực TẠI CUNG
→ KHÔNG PHẢI "Triệt lan sang Dần (tam hợp)"
```

---

## RULE 12: TUẦN KHÔNG — HẰNG SỐ CẤU TRÚC

**🔔 Trigger:** Mọi lần đánh giá Tuần theo thời gian (Đại Vận, Lưu Niên)

**Gốc rễ toán học:**
```
10 Thiên Can < 12 Địa Chi → 2 Chi THỪA (không được ghép Can)
→ 2 Chi thừa = Tuần Không
→ Số 10 KHÔNG BAO GIỜ thành 12 → Tuần là HẰNG SỐ
```

**Áp dụng:**
1. ✅ Tuần **KHÔNG NHẠT** theo tuổi (khác Triệt — Triệt có thể nhả dần sau 30t)
2. ✅ Tuần **KHÔNG MẠNH LÊN** theo tuổi
3. ✅ Tuần **KHÔNG ĐỔI** — là khoảng trống vĩnh viễn
4. ✅ Cái thay đổi là **GÓC NHÌN**: Đại Vận rời cung Tuần → ít đối mặt trực tiếp. Đại Vận vào cung Tuần → đối mặt 100%
5. ❌ KHÔNG viết: "Tuần nhạt sau 25 tuổi" → **SAI**
6. ❌ KHÔNG viết: "Tuần mạnh lên theo thời gian" → **SAI**

**So sánh Tuần vs Triệt:**

| | Tuần Không | Triệt Không |
|---|---|---|
| Bản chất | Thiên KHÔNG ĐẾN (vắng mặt) | Thiên CẮT ĐỨT (chủ động phá) |
| Chiếu? | ❌ KHÔNG | ❌ KHÔNG |
| Thay đổi? | ❌ Hằng số vĩnh viễn | ⚠️ Có thể nhả dần (~30t) |
| Tính chất | Che mờ + bảo vệ ngầm | Cắt gốc + buộc tự lập |

---

## RULE R-CK1: MỌI MỆNH ĐỀ CK PHẢI CÓ SOURCE LINK

**🔔 Trigger:** Mọi lần viết phân tích CK/CW/FTSE/VN30

**Áp dụng:**
- ✅ Mọi con số, mốc thời gian, tỷ lệ PHẢI kèm source link
- ✅ Mọi mệnh đề PHẢI xếp loại 4 cột: Đúng / Đúng một phần / Chưa xác thực / Sai
- ❌ KHÔNG viết số liệu từ bộ nhớ — PHẢI verify qua Perplexity hoặc source chính thức
- ❌ KHÔNG trộn T1 (filing) với T3 (narrative) trong cùng câu

**RCA:** ERR-001, ERR-002 — sai quy định vì dùng bộ nhớ thay verify

---

## RULE R-CK2: KHÔNG DÙNG "BẮT BUỘC/CHẮC CHẮN" CHO T3

**🔔 Trigger:** Mọi lần viết về narrative, analyst estimate, phỏng vấn CEO

**Áp dụng:**
- ✅ T3 (narrative) chỉ được dùng: "khả năng", "tiềm năng", "luận điểm phân tích", "giả thuyết"
- ✅ T1 (filing) mới được dùng: "đã xác nhận", "đã công bố"
- ❌ KHÔNG dùng "BẮT BUỘC", "CHẮC CHẮN", "SẼ XẢY RA" cho bất kỳ info T3 nào
- ❌ KHÔNG ghi "⭐⭐⭐" cho mệnh đề T3

**RCA:** ERR-003, ERR-004, ERR-009 — overclaim từ analyst report

---

## RULE R-CK3: ĐẠI VẬN PHẢI KIỂM TRA TRƯỚC KHI LUẬN

**🔔 Trigger:** Mọi lần kết nối Tử Vi với CK

**Áp dụng:**
- ✅ Đọc SOT để xác nhận ĐV hiện tại ở cung NÀO
- ✅ Xác nhận ĐV = Điền Trạch (tài sản) hay Quan Lộc (sự nghiệp) hay cung khác
- ❌ KHÔNG giả định ĐV tại cung nào — PHẢI ĐỌC FILE

**RCA:** Lỗi ĐV4 ban đầu (ghi Quan Lộc thay Điền Trạch) đã gây sai chain analysis

---

## RULE R-CK4: M7 MARGIN = ÉP GIẢM, KHÔNG ÉP TĂNG

**🔔 Trigger:** Mọi lần phân tích forced catalyst / cơ chế ép giá

**Áp dụng:**
- ✅ Margin call = forced SELLING = ép GIẢM giá
- ✅ Phải phân rõ: mechanism ép TĂNG hay ép GIẢM
- ❌ KHÔNG xếp margin call vào nhóm "cơ chế buộc tăng"
- ❌ KHÔNG trộn cơ chế tăng và giảm trong cùng bảng scoring

**RCA:** ERR-008 — sai logic hoàn toàn

---

## RULE R-CK5: SCORE PHẢI GHI "ƯỚC TÍNH" VS "XÁC THỰC"

**🔔 Trigger:** Mọi lần chấm điểm, xếp hạng cổ phiếu

**Áp dụng:**
- ✅ Nếu dùng điểm số → ghi rõ "[ước tính]" bên cạnh
- ✅ Ưu tiên xếp loại text (Bộ catalyst rõ nhất / Tiềm năng / Thiếu bằng chứng) thay điểm số
- ❌ KHÔNG ghi điểm dạng "92/100" như kết quả đã xác thực
- ❌ KHÔNG so sánh score giữa các mã như đã chốt xong

**RCA:** ERR-009 — SHB 92, TCB 82 overclaim

---

## RULE R13: RIÊU TẠI MỆNH = PHÁT RA, KHÔNG NHẬN VÀO ⚠️

**🔔 Trigger:** Mọi lần luận Thiên Riêu tại cung Mệnh hoặc An Thân

**Áp dụng:**
- ✅ Riêu tại Mệnh = **PHÁT RA** năng lượng đào hoa → NGƯỜI KHÁC nghi BẢN THỂ
- ✅ Bản thể KHÔNG nghi ngờ — bản thể TỎA sức hút tự nhiên
- ✅ Combo Riêu + Cô Thần + Tham = "quyến rũ + bận + im lặng" → "chắc có bồ"
- ❌ KHÔNG viết "Riêu = đương số đa nghi/ghen tuông"
- ❌ KHÔNG viết "Riêu = bản thể ham sắc dục" (trừ khi có evidence khác)

**RCA:** FC-001 — Real-life feedback đương số (15/03/2026): vợ nghi chồng, KHÔNG phải chồng nghi vợ.

**Giải Thần:** PHÁ Cô Thần ở nhà = chia sẻ lịch, minh bạch, NÓI nhiều hơn.

---

## RULE R14: REAL-LIFE FEEDBACK = SỬA NGAY + GHI LOG

**🔔 Trigger:** Khi đương số cung cấp thông tin thực tế mâu thuẫn với luận giải

**Áp dụng:**
1. ✅ GHI VÀO `_FEEDBACK_LOG.md` (FC-xxx)
2. ✅ SỬA file liên quan NGAY + tag `[FEEDBACK YYYYMMDD]`
3. ✅ Cập nhật Skill nếu là pattern lặp lại
4. ✅ **Real-life feedback > lý thuyết sách vở** (priority)
- ❌ KHÔNG giữ nguyên luận giải cũ khi đã có feedback mâu thuẫn
- ❌ KHÔNG cần Perplexity verify — feedback thực tế = highest authority

**Priority chain:** Real-life feedback > SOT JSON > Perplexity verified > Phú cổ > Agent memory

---

## RULE R15: NGUYỆT HẠN 3-LAYER BẮT BUỘC

**🔔 Trigger:** Mọi lần viết phân tích Nguyệt Hạn (tháng)

**Áp dụng:** Mỗi tháng PHẢI có 3 lớp:

| Lớp | Nội dung bắt buộc | Minimum |
|---|---|---|
| **L1: Tinh bàn** | Chính tinh + phụ tinh trạng thái + Tràng Sinh + Ngũ Hành | Bảng sao |
| **L2: Mệnh Foundation ③** | Phủ/Lộc/Khoa/Riêu/Cô Thần phản ứng gì | Bảng hoặc bullet 4+ items |
| **L3: Giải Thần Pattern** | Tứ Hóa + blockquote pattern + CK/CW | Blockquote + 1 dòng CK |

**Minimum lines/tháng:** ≥ 15 dòng (T1-T5 hiện ~40-60, T6-T12 hiện ~25-35)

---

*Created: 25/02/2026 | Updated: 15/03/2026 | Version: 5.0 — Bổ sung R13 (Riêu direction), R14 (Feedback protocol), R15 (Nguyệt Hạn 3-layer)*
