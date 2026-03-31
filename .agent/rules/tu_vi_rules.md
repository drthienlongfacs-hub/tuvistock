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

## RULE R-CK6: KHÓA NGÀY ÂM-DƯƠNG + TÁCH 3 LỚP MARKET REGIME

**🔔 Trigger:** Mọi lần nối Tử Vi với chứng khoán, đặc biệt khi viết `tháng này`, `giữa tháng`, `tuần 2-3`, `đúng/sai`, `kiểm chứng`

**Áp dụng:**
- ✅ PHẢI ghi ngày tuyệt đối trước khi luận/audit. Ví dụ: `29/03/2026 = 11/2 ÂL`
- ✅ PHẢI tách ít nhất 3 lớp:
  1. `broad market` (VN-Index/VN30)
  2. `sector/basket` (nhóm bank, steel, retail...)
  3. `single-name catalyst` (SHB tăng vốn, HPG AGM...)
- ✅ Sau mỗi giai đoạn đang sống, PHẢI có `reality-check` với data thật để gắn nhãn:
  - `supported`
  - `partial`
  - `contradicted`
- ✅ Nếu broad market sai nhưng basket đúng, PHẢI nói rõ `sai ở lớp nào`
- ✅ Confidence của tháng sau PHẢI bị điều chỉnh theo outcome gần nhất
- ❌ KHÔNG dùng một điểm số/tháng để bao trùm toàn thị trường và từng mã
- ❌ KHÔNG audit "tháng 2 âm" bằng dữ liệu ngoài phạm vi tháng 2 âm mà không ghi rõ
- ❌ KHÔNG dùng từ `khớp` nếu chưa có artifact outcome audit

**RCA:** T2 âm 2026 cho thấy broad market điều chỉnh nhẹ, nhưng bank basket có catalyst vẫn outperform. Không tách lớp sẽ dẫn đến kết luận sai hoặc quá thô.

---

## RULE R-CK7: GIÁ CỔ PHIẾU PHẢI TỪ NGUỒN TRỰC TIẾP — CẤM ƯỚC TÍNH ⛔

**🔔 Trigger:** Mọi lần viết giá cổ phiếu, bảng giá, hoặc snapshot thị trường

**Áp dụng:**
- ✅ Giá PHẢI lấy từ **Vietstock EOD**, **CafeF**, **SSI**, hoặc bài **tổng kết phiên** (Baomoi, nhandan, Vibethings)
- ✅ Mọi giá PHẢI kèm **nguồn** (tên website + timestamp)
- ✅ Nếu không verify được → ghi **"N/A (chưa verify)"** thay vì đoán
- ❌ **TUYỆT ĐỐI KHÔNG** ước tính giá từ % VN-Index rồi áp lên từng mã
- ❌ **TUYỆT ĐỐI KHÔNG** dùng ký hiệu `~` cho giá (VD: ~15,200 = WRONG)
- ❌ KHÔNG dùng giá từ conversation context/memory nếu chưa cross-check

**Checklist trước khi ghi giá:**
```
□ Giá từ nguồn trực tiếp (Vietstock/CafeF/SSI)?
□ Có kèm nguồn + timestamp?
□ Không có dấu ~ (ước tính)?
□ Cross-check ≥2 nguồn cho giá quan trọng?
```

**RCA:** ERR-017 (30/03/2026) — v7.0 ước tính giá từ % VN-Index → 6/7 giá sai, 3/7 sai chiều. MWG ghi ~−1.2% (thực −2.59%), TCB ghi ~−1.1% (thực 0%).

---

## RULE R-CK8: INTRADAY CACHE ≠ GIÁ ĐÓNG CỬA — VERIFY TIMESTAMP ⛔

**🔔 Trigger:** Mọi lần lấy dữ liệu từ Vietstock/CafeF/financial pages

**Áp dụng:**
- ✅ PHẢI kiểm tra **timestamp** trên trang Vietstock trước khi dùng
- ✅ Timestamp phải **> 14:30** mới đủ tin cậy làm giá đóng cửa
- ✅ Cross-check với bài **"tổng kết phiên"** từ Baomoi/nhandan/Vibethings/ieem
- ✅ Nếu timestamp < 14:30 → ghi rõ **"intraday [HH:MM], chưa phải giá đóng cửa"**
- ❌ **KHÔNG** dùng Vietstock page snippet có timestamp buổi sáng (09:xx, 10:xx) làm giá đóng cửa
- ❌ **KHÔNG** bỏ qua việc stock có thể hồi phục chiều — VN market biên độ lớn trong ngày

**Quy trình verify giá chính xác:**
```
1. Lấy giá từ Vietstock → CHECK timestamp
2. Nếu timestamp < 14:30 → CẢNH BÁO "intraday"
3. Search bài "tổng kết phiên" hoặc "kết phiên" ngày đó → cross-check
4. Nếu 2 nguồn đồng ý → ✅ dùng
5. Nếu 2 nguồn conflict → ghi cả 2 + flag "⚠️ cần verify thêm"
```

**RCA:** ERR-018 (30/03/2026) — SHB ghi 15,050 (−2.27%) từ Vietstock cache lúc 09:55 → thực tế SHB **HỒI PHỤC buổi chiều, KẾT PHIÊN TĂNG**, KLGD 85.56M (#1 HOSE). Sai lệch nghiêm trọng.

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

## RULE R16: ANTI-BIAS WARNING — CẢNH BÁO THIÊN KIẾN ⚠️

**🔔 Trigger:** Mọi lần luận giải cung hoặc viết dự báo

**Áp dụng:**
- ✅ Mỗi luận giải PHẢI có **confidence level**: `[Cao]` / `[Trung bình]` / `[Thấp]`
- ✅ Khi mô tả quá generic → FLAG `[Barnum Warning]` (mô tả đúng 80% dân số)
- ✅ Khi kết luận tuyệt đối → FLAG `[Absolute Claim]` → phải thêm điều kiện
- ❌ KHÔNG viết "chắc chắn sẽ..." cho bất kỳ dự báo nào (Chaos Theory)
- ❌ KHÔNG gán mọi sự kiện xấu vào Kỵ mà không evidence cụ thể (Retrofitting)

**Anti-patterns nhận thức:**
| Bias | Dấu hiệu | Cách phòng |
|------|-----------|-----------|
| Barnum Effect | Mô tả mơ hồ, ai cũng thấy đúng | Thêm chi tiết cụ thể ≥ 2 điểm |
| Confirmation Bias | Chỉ nhớ lần đúng, quên lần sai | Ghi cả ĐÚNG và SAI vào log |
| Retrofitting | Diễn giải lại sau khi biết kết quả | Viết dự đoán TRƯỚC khi xảy ra |

**Căn cứ:** Nghiên cứu Carlson (1985), Dean & Kelly (1997-2003). Harvest Round 4 — master_menh_ly_harvest.md Phần C.

---

## RULE R17: CROSS-SYSTEM REFERENCE — ĐỐI CHIẾU ĐA HỆ THỐNG

**🔔 Trigger:** Khi luận giải cấp NĂM hoặc Đại Hạn

**Áp dụng:**
- ✅ KHI có dữ liệu Bát Tự → BỔ SUNG cross-ref Dụng Thần với Hóa Lộc TVĐS
- ✅ Thập Thần BT phải CONSISTENT với chính tinh TVĐS (theo bảng mapping bat_tu_kinh_dien.md §V)
- ✅ Nếu BT và TVĐS cho kết luận KHÁC NHAU → ghi rõ cả 2 + phân tích vì sao
- ❌ KHÔNG đồng nhất các hệ thống (mỗi hệ có epistemological claim riêng)
- ❌ KHÔNG map 1:1 cứng nhắc — chỉ 4/12 cung có chức năng tương đồng cao

**Bảng mapping nhanh (từ bat_tu_kinh_dien.md):**
| Bát Tự | TVĐS | Tương đồng |
|--------|------|:----------:|
| Thất Sát | Thất Sát | ⭐⭐⭐ |
| Chính Quan | Tử Vi/Thiên Phủ | ⭐⭐ |
| Thương Quan | Phá Quân | ⭐⭐ |
| Thực Thần | Thiên Đồng | ⭐⭐ |
| Dụng Thần | Hóa Lộc | ⭐⭐ |
| Kỵ Thần | Hóa Kỵ | ⭐⭐ |

**Căn cứ:** Harvest Round 4 — bat_tu_kinh_dien.md, master_menh_ly_harvest.md Phần D.

---

## RULE R18: ARCHETYPE ≠ EVENT — NGUYÊN TẮC CHAOS THEORY

**🔔 Trigger:** Mọi lần dự báo sự kiện cụ thể

**Áp dụng:**
- ✅ TVĐS dự đoán **xu hướng** (attractor), KHÔNG dự đoán **sự kiện cụ thể** (trajectory)
- ✅ Viết: "Xu hướng tháng X: năng lượng [A] → có thể biểu hiện qua [B1, B2, B3]"
- ✅ Luôn cho ≥ 2 khả năng biểu hiện cho mỗi xu hướng
- ❌ KHÔNG viết: "Tháng X sẽ xảy ra Y" (tuyên bố sự kiện)
- ❌ KHÔNG dùng TVĐS để bói toán cặn — TVĐS = bản đồ khí quyển nội tâm

**Nguyên lý:** Hệ xác định (deterministic) nhưng nhạy cảm ban đầu (sensitive dependence) → xu hướng lớn đúng, chi tiết nhỏ phân kỳ.

**Căn cứ:** Chaos Theory (Lorenz), Harvest Round 4 — master_menh_ly_harvest.md Phần D §VI.

---

## RULE R19: HÓA KỴ PHẢI ĐỌC THEO NGỮ CẢNH, KHÔNG CỘNG CƠ HỌC

**🔔 Trigger:** Mọi lần luận Hóa Kỵ, Song Kỵ, Kỵ lặp, hoặc Kỵ đi cùng Khoa/Lộc/Quyền

**Áp dụng:**
- ✅ PHẢI xét `Kỵ ở đâu`: bản cung, tam hợp, xung chiếu, nhị hợp, giáp, hay chỉ là dư âm gốc
- ✅ PHẢI xét `Kỵ đi với ai`: Khoa soi sáng, Lộc/Quyền tăng tài nguyên, sát tinh làm ma sát nặng hơn
- ✅ PHẢI xét `vai trò cung`: Kỵ ở Thân/Tài khác Kỵ ở Thê/Phụ/Điền; không dùng một mẫu kết luận cho mọi cung
- ✅ PHẢI phân biệt `nghẽn / giữ / lộ vấn đề / thị phi / thanh khoản chậm` với `đại hung`
- ✅ Khi Kỵ lặp khác cung/chức năng, chỉ được nói là `chủ đề lặp`, không được cộng thô thành "tam kỵ đồng cung"
- ❌ KHÔNG viết kiểu `có Kỵ => cấm tuyệt đối`, `Kỵ chồng Kỵ => auto tốt`, hoặc `Khoa chế Kỵ = thắng-thua`
- ❌ KHÔNG biến Hóa Kỵ thành mệnh lệnh đầu tư/hôn nhân nếu chưa cross-check hình học cung và đối trọng sao

**Checklist tối thiểu:**
1. Kỵ đánh đúng cung nào, trực tiếp hay gián tiếp?
2. Cung đó mạnh/yếu, có Tuần/Triệt, đắc/hãm, hay `Phản Vi Giai` không?
3. Có Khoa/Lộc/Quyền hoặc sao trung gian làm dịu/đổi nghĩa không?
4. Kết luận cuối cùng là `nghẽn`, `siết`, `soi sáng mâu thuẫn`, hay `hung thật`?

---

## RULE BT-1: ĐẠI HẠN TVĐS ↔ ĐẠI VẬN BÁT TỰ — CROSS-CHECK

**🔔 Trigger:** Khi luận Đại Hạn TVĐS

**Áp dụng:**
- ✅ Nếu có dữ liệu BT → cross-check Đại Vận BT cùng giai đoạn 10 năm
- ✅ Ghi rõ: "TVĐS: ĐH tại [cung] | BT: ĐV hành [X]"
- ✅ Nếu 2 hệ thống ĐỀU thuận → confidence tăng → `[Cao]`
- ✅ Nếu 2 hệ thống NGƯỢC → flag và phân tích thêm → `[Thấp]`

---

## RULE BT-2: DỤNG THẦN ↔ HÓA LỘC — MẬT ĐỘ KIỂM TRA

**🔔 Trigger:** Khi xác định Hóa Lộc trong TVĐS

**Áp dụng:**
- ✅ Dụng Thần BT phải CÙNG HÀNH với cung/sao mang Hóa Lộc TVĐS
- ✅ Nếu khác hành → **FLAG**: "⚠️ BT-TVĐS divergence — cần xét kỹ"
- ❌ KHÔNG tự động bác bỏ TVĐS hoặc BT — chỉ flag để awareness

---

## RULE BT-3: THÔNG QUAN — TÌM CẦU NỐI KHI KỴ MẠNH

**🔔 Trigger:** Khi phát hiện Hóa Kỵ mạnh trong cung quan trọng

**Áp dụng:**
- ✅ Tìm sao/hành có chức năng "Thông Quan" (cầu nối) theo Trích Thiên Tùy
- ✅ Thông Quan = hành THỨ BA hòa giải 2 hành XUNG (VD: Mộc nối Kim-Thủy)
- ✅ Ghi: "Thông Quan: [sao X] tại [cung Y] có thể hòa giải Kỵ tại [cung Z]"
- ❌ Thông Quan KHÔNG triệt tiêu Kỵ — chỉ GIẢM NHẸ

---

## RULE BT-4: ĐIỀU HẦU × KHÍ SẮC — THÁNG SINH MAPPING

**🔔 Trigger:** Khi luận Nguyệt Hạn hoặc phân tích theo tháng

**Áp dụng:**
- ✅ Check Điều Hầu Dụng Thần (Cùng Thông Bảo Giám) cho tháng đó
- ✅ Cross-ref với Khí Sắc Hồng Phi Mô (hong_phi_mo_tuong_dien.md)
- ✅ Ghi: "Điều Hầu tháng [X]: [Hàn/Noãn/Táo/Thấp] → cần [hành bổ]"
- ✅ Map từ bảng tra bat_tu_kinh_dien.md §III

---

## RULE BT-5: THẬP THẦN ↔ CHÍNH TINH — CONSISTENCY CHECK

**🔔 Trigger:** Khi đánh giá tính cách/bản thể trong luận giải

**Áp dụng:**
- ✅ Khi TVĐS nói "Thất Sát mạnh" → BT cũng phải thấy Thất Sát hoặc Thiên Ấn vượng
- ✅ Bảng mapping: bat_tu_kinh_dien.md §IV (Thập Thần ↔ 14 Chính Tinh)
- ✅ Inconsistency → "⚠️ BT-TVĐS character divergence"

---

## RULE BT-6: NẠP ÂM — BỔ SUNG TẦNG GIA TỘC/TỔ TIÊN

**🔔 Trigger:** Khi luận giải cung Phụ Mẫu hoặc Phúc Đức

**Áp dụng:**
- ✅ Tra Nạp Âm năm sinh (Tam Mệnh Thông Hội) → bổ sung insight "gốc gia tộc"
- ✅ Ghi: "Nạp Âm: [tên], ý nghĩa: [mô tả ngắn]"
- ✅ Nạp Âm bổ sung cho TVĐS (TVĐS thiếu tầng ancestral)
- ❌ KHÔNG dùng Nạp Âm thay thế chính tinh — chỉ BỔ SUNG

---

## RULE R-INJ1: IDEMPOTENT INJECTION — CHỐNG TRÙNG LẶP (RCA-040)

**🔔 Trigger:** Khi chạy bất kỳ injection script nào vào file luận giải (inject_*.py, upgrade_*.py)

**Bối cảnh RCA-040 (29/03/2026):** Injection scripts append-only → 4× duplication per month, file 6501→2628 dòng sau dedup. 81% nội dung bị trùng.

**Áp dụng:**
1. ✅ **TRƯỚC KHI INJECT:** Check fingerprint nội dung — nếu block đã tồn tại → SKIP, không append
2. ✅ **Mỗi block phải có unique anchor:** VD `<!-- DEEP_DIVE_T1_v1 -->` để detect duplicate
3. ✅ **Mỗi injection script PHẢI import `injection_guard.py`** và gọi `is_already_injected(content, anchor)` trước khi chèn
4. ✅ **Sau inject:** Chạy `dedup_luan_giai.py` để verify 0 duplicate blocks
5. ❌ **KHÔNG BAO GIỜ** dùng pattern append-only (tìm section → chèn cuối) mà không check existing
6. ❌ **KHÔNG chạy inject script >1 lần** trên cùng file mà không verify dedup trước

**Code pattern BẮT BUỘC:**
```python
from injection_guard import is_already_injected

anchor = f"<!-- DEEP_DIVE_T{month}_v1 -->"
if is_already_injected(content, anchor):
    print(f"⏭️ T{month}: already injected, skipping")
    continue
# ... inject content with anchor ...
```

**Lý do:** RCA-040 (29/03/2026) — 3,873 dòng trùng lặp xóa bỏ. Script `dedup_luan_giai.py` là safety net.

---

## RULE R-BT1: BACKTEST CALIBRATION — 6 NGUYÊN TẮC TỪ THỰC TẾ (Backtest T2/2026)

**🔔 Trigger:** Mọi lần scoring Nguyệt Hạn, dự đoán CK, hoặc đánh giá cung

**Bối cảnh:** Reality-check T2 ÂL 2026 cho thấy broad market yếu nhưng basket có catalyst vẫn outperform. Xem `05_ck_analysis/analysis/market_reality_check_2026.md`.

**6 nguyên tắc BẮT BUỘC:**

### P-1: TÁCH RÕ SCORE CK vs SCORE ĐỜI SỐNG
- ❌ Score 8/10 cho tháng = reader hiểu CK cũng 8/10 → SAI
- ✅ Mỗi tháng PHẢI có 2 score: **Score Đời sống** (9-chiều gốc) + **Score CK** (Tài/Di/Phi/Macro)

### P-2: HÓA LỘC ≠ GIÁ TĂNG
- ❌ "Hóa Lộc Vượng" → chart xanh
- ✅ Hóa Lộc = **dòng chảy nguồn lực** (thông tin, cơ hội, giới thiệu), KHÔNG phải P&L

### P-3: SONG KỴ MAP SANG SELLING PRESSURE
- ❌ Song Kỵ chỉ luận hôn nhân
- ✅ Song Kỵ nếu chiếu trục Tài-Quan → **có thể = institutional/foreign selling**. Cross-check foreign flow

### P-4: TỨ MỘ (Thìn/Tuất/Sửu/Mùi) + TRÀNG SINH YẾU → CK SIDEWAY/GIẢM
- Tứ Mộ = "chôn cất/tàng trữ". Khi NH vào Tứ Mộ + Tràng Sinh ≤4 → CK likely không tăng

### P-5: FOREIGN FLOW = "VÉ THỰC TẾ" VERIFY PHI TINH
- Phi Tinh = NỘI LỰC. Ngoại lực phải check foreign net buy/sell để verify

### ⭐ P-6: SCORING ĐA KHUNG 8 NHÂN TỐ — KHÔNG PHIẾN DIỆN (Quan trọng nhất!)
- **QUY LUẬT:** `Final_Score = Σ(weight_i × score_i)` cho 8 khung:
- ① 9-Chiều Engine (25%) — NPL score
- ② Mệnh Foundation Phanh↔Ga (20%) — Phủ/Tham/Kỵ phản ứng với cung NH?
- ③ Tứ Hóa Phi Tinh (15%) — Phi Tinh có đánh vào NH không?
- ④ Tuần-Triệt (10%) — NH có bị phong tỏa?
- ⑤ Hình Học Thiên Bàn (10%) — Tam hợp/xung/giáp mạnh hay yếu?
- ⑥ Tràng Sinh (5%) — Governor nhẹ, KHÔNG override toàn bộ
- ⑦ Cách Cục kích hoạt (10%) — Có catalyst cách cục nào?
- ⑧ Macro/CK (5%) — Chỉ cho score CK
- **KHÔNG BAO GIỜ** dùng 1 khung đơn lẻ quyết score (Bản Cung đẹp ≠ tháng đẹp)
- **Chứng cứ:** T2 Bản Cung 9/10 nhưng Multi-factor = 4.5 → khớp thực tế ~4/10 ✅
- **Chi tiết:** `05_ck_analysis/analysis/multi_factor_calibration_v2.md`

---

*Created: 25/02/2026 | Updated: 31/03/2026 | Version: 6.4 — R-CK7 (giá phải từ nguồn trực tiếp, ERR-017), R-CK8 (intraday cache ≠ EOD, ERR-018).*
