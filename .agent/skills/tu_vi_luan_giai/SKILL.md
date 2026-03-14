---
name: tu-vi-luan-giai
description: Use when analyzing Tử Vi charts, luận giải cung, cách cục, đại vận, lưu niên. Data-driven methodology with 7 chiều tương tác, Tứ Hóa Phi Tinh, 3 Màng Lọc. Triggers on "luận giải", "tử vi", "tinh bàn", "cách cục", "đại vận", "lưu niên", "phân tích lá số".
---

# SKILL: TỬ VI LUẬN GIẢI CHUYÊN NGHIỆP
## Phương pháp "Data → Structure → Interpret"

---

## I. NGUYÊN TẮC CỐT LÕI

### 1. Data First, Interpret Later
- **LUÔN kiểm kê data** (sao, hành, miếu/hãm, vị trí) TRƯỚC KHI luận giải
- **KHÔNG BAO GIỜ** diễn giải khi chưa liệt kê đầy đủ sao tại cung
- Dùng Source of Truth: `.agent/source_of_truth/la_so_long_2026.md`

### 2. Cấu trúc 6 chiều PHẢI LUÔN xét
Mỗi cung luận giải PHẢI bao gồm đủ 6 chiều tương tác:

| # | Chiều | Tỷ lệ | Bắt buộc? |
|:---:|---|:---:|:---:|
| 1 | Chính cung (Tọa thủ) | 40% | ✅ |
| 2 | Xung chiếu (Đối cung) | 30% | ✅ |
| 3 | Tam hợp (Hội chiếu) | 20% | ✅ |
| 4 | Nhị hợp (Lục hợp) | 10% | ✅ |
| 5 | Giáp cung | ~5% | ✅ |
| 6 | Lục hại | biến thiên | ⚠️ (nếu có sát tinh) |

### 3. Trích dẫn bắt buộc
- Mọi cách cục phải kèm **phú cổ gốc** + **nguồn**
- Mọi định lượng (mức 1-10) phải dựa trên **miếu/hãm + cách cục**
- Ngoại lệ Sửu/Mùi (nhị hợp trùng giáp ~15%) phải ghi rõ

---

## II. QUY TRÌNH LUẬN GIẢI 1 CUNG

### Bước 1: Kiểm kê Data
```
1. Mở Source of Truth → xác nhận chính tinh + phụ tinh tại cung
2. Liệt kê dạng bảng:
   | Sao | Loại | Hành | Miếu/Hãm | Ghi chú |
3. Ghi nhận Tuần/Triệt nếu có
4. Tính Ngũ Hành tương tác: Sao vs Cung
```

### Bước 2: Liệt kê 6 chiều
```
1. Xác nhận 6 cung tương tác từ Source of Truth
2. Liệt kê chính tinh + sát tinh nổi bật tại mỗi cung
3. Bảng format:
   | Chiều | Cung | Chính tinh | Sát tinh | Cát tinh |
```

### Bước 3: Nhận diện Cách cục
```
1. Scan danh sách cách cục đã xác nhận (Source of Truth mục VI)
2. Kiểm tra điều kiện thỏa mãn
3. Tìm cách cục mới → tra cứu phú cổ + xác nhận nguồn
4. Format:
   | Cách cục | Điều kiện | Phú gốc | Nguồn | Mức |
```

### Bước 4: Luận giải
```
1. Luận từ Bản cung (40%) → Chiếu (30%) → Tam hợp (20%) → Nhị hợp (10%) → Giáp (5%)
2. Mỗi chiều: DATA trước → GIẢI sau
3. Dùng ví von hiện đại để giải thích (CEO, startup, tài chính...)
4. Ghi rõ: Tiền vận (<34t) vs Hậu vận (>34t) nếu có Tuần/Triệt
```

### Bước 5: Tổng hợp Cát/Hung
```
| Yếu tố | Cát (+) | Hung (−) | Ghi chú |
→ Định lượng rõ ràng, không mập mờ
```

---

## III. QUY TẮC CHỐNG SAI

### Danh sách lỗi thường gặp

| # | Lỗi | Cách phòng |
|---|---|---|
| 1 | Nhầm miếu/hãm | Luôn check Source of Truth |
| 2 | Nhị hợp > Chiếu | **SAI.** Chiếu 30% > Nhị hợp 10% (xem `04_ly_thuyet/ra_soat_5_chieu_tuong_tac.md`) |
| 3 | Quên Triệt/Tuần | Luôn kiểm tra cột Tuần/Triệt |
| 4 | Phú cổ không nguồn | Bắt buộc ghi nguồn, không trích phú "chế" |
| 5 | VCD không nói mượn ai | VCD PHẢI ghi rõ "mượn chính tinh cung [X]" |
| 6 | Giáp Sửu/Mùi không ghi đặc biệt | Phải note nhị hợp trùng giáp ~15% |

### Quy tắc "Sửu/Mùi Exception"
Khi luận cung Sửu, Mùi, Tý, hoặc Ngọ → kiểm tra:
- Có nhị hợp trùng giáp? (chỉ 4 cung này có)
- Nếu sao giáp đắc → ghi "kênh kép ~15%"
- Nếu Nhật Nguyệt giáp Sửu → highlight "Nhật Nguyệt Giáp Thân tối đẹp"

---

## IV. TEMPLATE OUTPUT

### Template Luận Giải 1 Cung
```markdown
# LUẬN GIẢI CUNG [TÊN CUNG] — [CHI] ([HÀNH])

## 1. DATA KIỂM KÊ
[Bảng sao tại cung]

## 2. 6 CHIỀU TƯƠNG TÁC
### 2.1 Bản cung (40%)
[DATA → GIẢI]

### 2.2 Xung chiếu (30%)
[DATA → GIẢI]

### 2.3 Tam hợp (20%)
[DATA → GIẢI]

### 2.4 Nhị hợp (10%)
[DATA → GIẢI]

### 2.5 Giáp cung (~5%)
[DATA → GIẢI]

### 2.6 Lục hại
[DATA → GIẢI]

## 3. CÁCH CỤC NHẬN DIỆN
[Bảng cách cục + phú + nguồn + mức]

## 4. TỔNG HỢP CÁT/HUNG
[Bảng điểm + kết luận]
```

---

## V. CÁC VÍ DỤ THAM KHẢO

| File | Nội dung | Dùng làm mẫu cho |
|---|---|---|
| `02_luan_giai/luan_giai_menh_than.md` | Luận giải mẫu Mệnh + Thân (6 chiều) | Luận giải cung |
| `02_luan_giai/goc_re_an_sao_menh.md` | Truy nguyên gốc rễ từng sao | Phân tích sao chi tiết |
| `02_luan_giai/tinh_ban_12_cung.md` | Macro: 4 vòng tam hợp | Phân tích tổng thể |
| `03_cach_cuc/cach_cuc_chinh_thong.md` | 12 cách cục đã kiểm chứng | Nhận diện cách cục |
| `04_ly_thuyet/ra_soat_5_chieu_tuong_tac.md` | Thang đo 5 chiều | Lý thuyết nền |
| `02_luan_giai/giap_cung_suu_mui_dac_biet.md` | Ngoại lệ Sửu/Mùi | Xử lý edge case |

---

## VI. NGUỒN TƯ LIỆU TIN CẬY

| # | Nguồn | Loại | Tin cậy |
|---|---|---|:---:|
| 1 | kabala.vn | Website Tử Vi chuyên sâu | ⭐⭐⭐ |
| 2 | lyso.vn | Website Lý Số | ⭐⭐⭐ |
| 3 | tuvi.vn | Website Tử Vi | ⭐⭐⭐ |
| 4 | tuviglobal.com | Website Tử Vi | ⭐⭐ |
| 5 | huyenhocvietnam.vn | Huyền Học | ⭐⭐ |
| 6 | aituvi.com | AI Tử Vi | ⭐⭐ |
| 7 | Sách Trình Minh Đức | Sách in | ⭐⭐⭐⭐ |
| 8 | cohoc.vn | Cổ Học | ⭐⭐ |
| 9 | free.fr (Tử Vi Phú) | Archive phú cổ | ⭐⭐⭐ |

---

## VII. KHUNG PHÂN TÍCH 7 TRỤC — MA TRẬN SSoT TOÀN DIỆN

> **Nguyên tắc:** Mọi luận giải Tử Vi phải đặt vấn đề vào trung tâm ma trận 2 trục: **Con Người (Chủ quan)** × **Vũ Trụ/Môi Trường (Khách quan)**. Sự va đập giữa 2 trục tạo ra câu trả lời có tính thực tiễn cao nhất.

### Trục Con Người — Chủ Quan (4 Nhân)

```
┌─────────────────────────────────────────────────────────────────────┐
│  NHÂN SINH          NHÂN TÍNH          NHÂN TƯỚNG       NHÂN QUẢ  │
│  (Triết lý sống)    (Bản ngã)          (Tâm sinh tướng) (Nhân→Quả)│
│  ↕                  ↕                  ↕                ↕         │
│  Mệnh + Phúc Đức   Chính tinh + Hóa   Mệnh + Tật Ách   Tứ Hóa   │
│  + Đại Vận          + Miếu/Hãm         VCD/body          chuỗi    │
│                                                                     │
│  Căn cứ: Tâm lý    Căn cứ: Tâm lý     Căn cứ: Nội      Căn cứ:  │
│  học, triết học     học, sinh học       tiết tố, tâm lý   Systems  │
│  thực hành          tiến hóa           biểu cảm          thinking │
└─────────────────────────────────────────────────────────────────────┘
```

### Trục Vũ Trụ/Môi Trường — Khách Quan (3 Thiên-Địa-Duyên)

```
┌─────────────────────────────────────────────────────────────────────┐
│  BỐI CẢNH THIÊN-ĐỊA     NHÂN DUYÊN            QUY LUẬT TỰ NHIÊN  │
│  (Thiên thời + Địa lợi)  (Điều kiện xúc tác)   (Khoa học vạn vật) │
│  ↕                       ↕                      ↕                  │
│  Lưu Niên/Đại Vận        Tuần/Triệt/Sát tinh   Ngũ Hành           │
│  + Thiên Di + Hành cung   (Biến số, xác suất)   Sinh Khắc          │
│                                                                     │
│  Căn cứ: Xã hội học,     Căn cứ: Xác suất,     Căn cứ: Vật lý,   │
│  địa chính trị,          Chaos theory,          sinh học tiến hóa, │
│  lịch sử                 Black Swan events      logic toán học      │
└─────────────────────────────────────────────────────────────────────┘
```

### Ánh xạ Tam Tài → 7 Trục

| Tam Tài | Trục 7 SSoT | Ý nghĩa |
|:---:|---|---|
| **Thiên** (Trời) | Bối cảnh Thiên (Thời gian, xu hướng vĩ mô) + Quy luật Tự nhiên | Quy luật khách quan chi phối vạn vật |
| **Địa** (Đất) | Bối cảnh Địa (Không gian, văn hóa, thị trường) + Nhân Duyên | Môi trường + điều kiện xúc tác |
| **Nhân** (Người) | Nhân sinh + Nhân tính + Nhân tướng + Nhân quả | Chủ thể con người với ý chí và hành vi |

### Quy trình 7 Trục khi Luận Giải

```
Bước 1: NHÂN TÍNH → Đọc chính tinh, Tứ Hóa, miếu/hãm (Con người LÀ GÌ?)
Bước 2: NHÂN DUYÊN → Xét Tuần/Triệt/Sát (Điều kiện CÓ hay KHÔNG?)
Bước 3: QUY LUẬT TỰ NHIÊN → Ngũ Hành sao vs cung (Vật lý NÓI GÌ?)
Bước 4: BỐI CẢNH THIÊN-ĐỊA → Đại Vận, Lưu Niên, Thiên Di (THỜI ĐÚng không? NƠI ĐÚNG không?)
Bước 5: NHÂN QUẢ → Tứ Hóa chuỗi (Hành vi A → Kết quả B trong điều kiện C)
Bước 6: NHÂN SINH → Tổng hợp ý nghĩa cuộc đời (Triết lý gì rút ra?)
Bước 7: NHÂN TƯỚNG → Body language, thần thái phản ánh (Biểu hiện bên ngoài?)
```

---

## VIII. PHÂN TÍCH HUNG/SÁT TINH — PHƯƠNG PHÁP

### 8.1 Phân loại

| Nhóm | Sao | Tính chất |
|---|---|---|
| **Lục Sát** (6 sát tinh chính) | Kình Dương, Đà La, Hỏa Tinh, Linh Tinh, Địa Không, Địa Kiếp | Sát phạt mạnh, phá hoại hoặc kích phát |
| **Hung tinh phụ** | Thiên Hình, Tang Môn, Bạch Hổ, Đại Hao, Tiểu Hao, Quả Tú | Gây trở ngại, đau đớn, cô độc |
| **Hóa Kỵ** | Tứ Hóa Kỵ | Ám ảnh, thị phi, trục trặc — nhưng có thể phản vi giai |
| **Tuần Không** | Tuần Không (2 cung) | Che mờ, trì hoãn, BẢO VỆ ngầm |
| **Triệt Không** | Triệt Không (2 cung) | Cắt đứt gốc rễ, phải TỰ LẬP |

### 8.2 Quy Tắc Ngũ Hành — Sát Tinh vs Cung

```
CÙNG HÀNH    → TĂNG LỰC    (VD: Kình Kim ở Dậu Kim = cực mạnh)
BỊ CUNG KHẮC → GIẢM LỰC    (VD: Triệt Kim ở Ngọ Hỏa = yếu hơn)
SINH cho CUNG → HUNG nhưng NUÔI CUNG (VD: Hình Hỏa ở Tuất Thổ = đau để lớn)
BỊ CUNG TIẾT → HUNG nhưng BỊ HÚT CẠN (VD: Tướng Thủy ở Mão Mộc = tiều tụy)
```

### 8.3 Checklist Phân Tích Hung/Sát (Áp dụng mỗi cung)

```markdown
☐ Liệt kê MỌI sát/hung tinh tại cung
☐ Ghi Hành của sao + Hành của cung
☐ Xác định tương tác: Sinh? Khắc? Đồng hành? Tiết khí?
☐ Đánh giá: Sát tinh TĂNG hay GIẢM lực tại cung?
☐ Kiểm tra Tuần/Triệt: Hành Tuần/Triệt vs Hành cung
☐ So sánh với cung xung chiếu: Hung/Sát có cộng hưởng?
☐ So sánh trong tam hợp: Cung nào hung nhất, cung nào sạch?
☐ Ghi nhận nếu cung SẠCH sát (ý nghĩa bảo vệ/an toàn)
```

---

## IX. TUẦN KHÔNG & TRIỆT KHÔNG — QUY TẮC CỨng

> ⛔ **QUY TẮC TUYỆT ĐỐI:** Tuần/Triệt KHÔNG PHẢI SAO. Chúng là **khoảng trống cấu trúc** (structural void).

### 9.1 Tuần/Triệt KHÔNG CHIẾU

```
⛔ Tuần/Triệt KHÔNG:           ✅ Tuần/Triệt CHỈ:
  ❌ Xung chiếu (đối cung)        ✅ Án ngữ tại 2 cung cố định
  ❌ Tam hợp                      ✅ Ảnh hưởng SAO tại cung đó
  ❌ Nhị hợp (lục hợp)            ✅ Sao bị ảnh hưởng → chiếu đi
  ❌ Giáp cung                       với LỰC GIẢM/CẮT
  ❌ Lan tỏa, phóng chiếu         ✅ Tác động GÁN TIẾP qua sao
```

**Sai thường gặp:**
- ❌ "Tuần chiếu từ Tỵ sang Hợi" → SAI (Tuần không chiếu)
- ❌ "ĐV tại Sửu tam hợp Tỵ nên nhận Tuần" → SAI (Tuần không tam hợp)
- ✅ "ĐV tại Sửu tam hợp Tỵ → nhận Tử Vi/Thất Sát bị Tuần che mờ → lực chiếu giảm" → ĐÚNG

### 9.2 Tuần Không — Hằng Số Cấu Trúc (KHÔNG ĐỔI)

**Gốc toán học:**
```
10 Thiên Can ghép 12 Địa Chi → 2 Chi THỪA (Tuần Không)
10 ≠ 12 → VĨNH VIỄN → Tuần = HẰNG SỐ
```

| Câu hỏi | Trả lời | Lý do |
|---|---|---|
| Tuần nhạt theo tuổi? | ❌ KHÔNG | Khoảng trống không "lấp đầy" được |
| Tuần mạnh lên? | ❌ KHÔNG | Sự vắng mặt không tích lũy thêm |
| Cái gì thay đổi? | Đại Vận | ĐV rời cung Tuần → ít đối mặt trực tiếp |

### 9.3 So Sánh Tuần vs Triệt

| | Tuần Không | Triệt Không |
|---|---|---|
| Gốc | 10 Can < 12 Chi → 2 Chi thừa | Nạp Âm giao thoa → 2 Chi bị cắt |
| Bản chất | Thiên KHÔNG ĐẾN (vắng mặt) | Thiên CẮT ĐỨT (chủ động) |
| Chiếu? | ❌ KHÔNG | ❌ KHÔNG |
| Thay đổi? | ❌ Hằng số | ⚠️ Có thể nhả dần (~30t) |
| Tính chất | Che mờ + bảo vệ ngầm | Cắt gốc + buộc tự lập |

---

## X. TỨ HÓA PHI TINH — CHUỖI NHÂN QUẢ

> **Nguyên tắc:** Tứ Hóa = 4 biến số thời gian xoắn vào tinh bàn. Phân tích CHUỖI (chain), không phân tích rời lẻ.

### 10.1 Bảng Tứ Hóa Theo Can

```
Can Giáp: Liêm(Lộc) Phá(Quyền) Vũ(Khoa)  Dương(Kỵ)
Can Ất:   Cơ(Lộc)  Lương(Quyền) Tử(Khoa)  Âm(Kỵ)
Can Bính: Đồng(Lộc) Cơ(Quyền)  Xương(Khoa) Liêm(Kỵ)
Can Đinh: Âm(Lộc)  Đồng(Quyền) Cơ(Khoa)  Cự(Kỵ)
Can Mậu:  Tham(Lộc) Âm(Quyền)  Bật(Khoa)  Cơ(Kỵ)
Can Kỷ:   Vũ(Lộc)  Tham(Quyền) Lương(Khoa) Khúc(Kỵ)
Can Canh:  Dương(Lộc) Vũ(Quyền) Phủ(Khoa)  Đồng(Kỵ)
Can Tân:  Cự(Lộc)  Dương(Quyền) Xương(Khoa/Kỵ) [tranh luận]
Can Nhâm: Lương(Lộc) Tử(Quyền)  Xương/Tả(Khoa) Vũ(Kỵ)
Can Quý:  Phá(Lộc) Cự(Quyền)  Âm(Khoa)  Tham(Kỵ)
```

> ⚠️ Lưu ý: Có tranh luận giữa các trường phái. Ghi rõ trường phái sử dụng.

### 10.2 Phân Tích Chuỗi Nhân Quả

```
Bước 1: Xác định VỊ TRÍ 4 Hóa → cung nào, sao nào
Bước 2: VẼ CHUỖI theo chiều:
         Lộc (NHÂN gốc) → Quyền (ĐIỀU KIỆN) → Khoa (TRÍ TUỆ) → Kỵ (HỆ QUẢ PHỤ)
Bước 3: Xác định VÒNG THUẬN (tăng cường) và VÒNG NGHỊCH (cân bằng)
Bước 4: Tìm BỘ NGẮT MẠCH (sao/cung nào cắt vòng nghịch)
```

### 10.3 Tam Hóa Liên Châu — Cách Cục Đặc Biệt

```
Điều kiện: Lộc-Quyền-Khoa nằm liên tiếp 3 cung kề nhau
Ý nghĩa:  "Bánh đà phú quý" — vòng lặp tự gia tốc
Cảnh báo:  Nếu Kỵ đồng cung 1 trong 3 → bánh đà bị phanh gián tiếp
Phú cổ:   "Tam Hóa liên châu phúc tất trùng lai"
```

### 10.4 Phi Hóa Kỵ (Phi Tinh Nâng Cao)

```
Dùng cho: Lưu Niên / Đại Vận phi tinh
Quy trình:
  1. Lấy Can của cung Tiểu Hạn (hoặc Đại Vận)
  2. Tra bảng Tứ Hóa theo Can đó
  3. Chiếu các Hóa lên 12 cung → tìm điểm Lộc đổ và Kỵ đánh
  4. Diễn giải: "Lộc rót vào đâu = nguồn lợi; Kỵ đánh vào đâu = rủi ro"
```

> **Ví dụ (Long 2026):** Tiểu Hạn Mùi mang Can Kỷ → Vũ(Lộc)+Tham(Quyền) đổ vào Sửu (Thân), Khúc(Kỵ) đánh Di → "Phần thịt giấu kín, xương xẩu đẩy ra ngoài"

---

## XI. QUY TRÌNH LUẬN GIẢI ĐẠI VẬN

> **Nguyên tắc:** Đại Vận = 10 năm. Mỗi Đại Vận cần phân tích riêng biệt bằng phương pháp 5 chiều + Tuần Triệt Động Lực Học.

### 11.1 Xác Định Đại Vận

```
Bước 1: Xác định Ngũ Cục → Tuổi khởi Đại Vận
         Thủy Nhị Cục: 2t | Mộc Tam Cục: 3t | Kim Tứ Cục: 4t
         Thổ Ngũ Cục: 5t | Hỏa Lục Cục: 6t
Bước 2: Xác định CHIỀU ĐI (Thuận/Nghịch)
         Dương Nam / Âm Nữ → Thuận (chiều kim đồng hồ)
         Âm Nam / Dương Nữ → Nghịch (ngược kim đồng hồ)
Bước 3: Liệt kê Đại Vận → Cung → Tuổi → Tinh bàn bản cung
```

### 11.2 Phân Tích 5 Chiều Đại Vận

| Chiều | Tỷ trọng | Nội dung phân tích |
|:---:|:---:|---|
| Tọa thủ (40%) | **40%** | Chính tinh + phụ tinh + Tuần/Triệt tại cung Đại Vận |
| Xung chiếu (30%) | **30%** | Cung đối diện: Hỗ trợ hay phá hoại? |
| Tam hợp (20%) | **20%** | Tam hợp cục: Hỏa/Kim/Thủy/Mộc/Thổ cục nào? |
| Nhị hợp (10%) | **10%** | Ám lực truyền ngầm |
| Giáp (~5%) | **~5%** | Gọng kìm khắc nghiệt hay bảo vệ? |

### 11.3 Tuần Triệt Động Lực Học (Mốc 30 Tuổi)

```
⚠️ QUY TẮC QUAN TRỌNG:
   TRIỆT: Sát phạt MẠNH NHẤT ở Tiền Vận (< 30t)
           Sau 30t → Triệt NHẢ DẦN, giảm sức cắt
   TUẦN:   Hằng số vĩnh viễn — KHÔNG đổi theo tuổi
           Nhưng khi ĐV rời cung Tuần → ít đối mặt trực tiếp

HIỆN TƯỢNG ĐẶC BIỆT — "Tuần Triệt Tháo Gỡ":
   Khi Mệnh ôm Tuần đi vào Vận ôm Triệt (hoặc ngược lại)
   → Hai Không Vong đâm sầm nhau → Tự triệt tiêu lẫn nhau
   → Phá phong ấn → Bạo phát
   (Lê Quang Lăng — Tử Vi Nam Phái)
```

### 11.4 Template Bảng Đại Vận

```markdown
| Đại Vận | Tuổi | Cung | Tinh bàn | Nhận định |
|:---:|---|---|---|---|
| **1** | x-y | Cung A | Sao (M/H) + Sát | Cát/Hung + lý do |
```

---

## XII. QUY TRÌNH LUẬN GIẢI LƯU NIÊN — PHƯƠNG PHÁP 3 MÀNG LỌC

> **Nguyên tắc:** Mỗi năm cần xét qua 3 tầng lọc. Không bỏ qua tầng nào.

### 12.1 Thông Tin Nền Bắt Buộc

```
☐ Ngũ Hành năm (Nạp Âm Can Chi → Sinh/Khắc Mệnh?)
☐ Tiểu Hạn cư cung nào?
☐ Lưu Thái Tuế đóng cung nào?
☐ Tứ Hóa Lưu Niên (theo Can năm) → 4 Hóa rơi vào đâu?
```

### 12.2 Ba Màng Lọc

#### Màng lọc 1: Bản Cung & Ngũ Hành
```
✅ Xác định cung Tiểu Hạn: Hành cung SINH hay KHẮC Mệnh?
✅ Liệt kê bản cung: Chính tinh + phụ tinh + sát tinh
✅ Đánh giá môi trường: Đắc Địa Lợi (cung sinh Mệnh) hay Khắc Phạt?
```

#### Màng lọc 2: Trọng Số 5 Chiều
```
✅ Tọa thủ (40%): Bản cung cường hay nhược?
✅ Xung chiếu (30%): Đối cung hỗ trợ hay phá hoại?
   → Nếu bản cung VCD: Xung chiếu chiếm 80% sức mạnh bản cung
✅ Tam hợp (20%): Tam hợp cục có hung/sát tinh gì?
✅ Nhị hợp (10%): Ám lực truyền ngầm
✅ Giáp (~5%): Gọng kìm
```

#### Màng lọc 3: Lưu Niên Tứ Hóa & Phi Tinh
```
✅ 4 Hóa Lưu Niên rơi vào cung nào? (Đặc biệt L.Kỵ!)
✅ Trùng Kỵ? (L.Kỵ + Kỵ bản mệnh = Song Kỵ → ĐẠI HUNG)
✅ Phi Hóa Kỵ: Can Tiểu Hạn → phi ra 4 Hóa phụ
✅ Lưu Kình Dương, Lưu Lộc Tồn, Lưu Thiên Mã?
```

### 12.3 Ma Trận 12 Cung (Đánh Giá Toàn Cảnh Năm)

```markdown
| # | Cung Vị | Hệ Thống Lưu Niên Giáng Xuống | TV-10 | Hành Động |
|---|---|---|:---:|---|
| 1-12 | Mỗi cung | Phi tinh + Lưu tinh + sát tinh lưu niên | x/10 | Hướng dẫn |
```

> **Template này đã áp dụng thành công cho:** Long, Uyên Anh, An, Bà — tất cả đều dùng 3 Màng Lọc + Ma Trận 12 Cung.

---

## XIII. VÔ CHÍNH DIỆU — QUY TẮC ĐẶC BIỆT

> **Nguyên tắc:** Cung VCD (Vô Chính Diệu) = cung không có 14 chính tinh tọa thủ. PHẢI xử lý đặc biệt.

### 13.1 Quy Tắc Mượn Sao

```
VCD tại cung A → Mượn chính tinh từ cung ĐỐI DIỆN (xung chiếu)
⚠️ Luôn ghi rõ: "VCD — Mượn [tên sao] từ cung [X]"
```

### 13.2 Quy Tắc 80% Xung Chiếu

```
Cung VCD:  Tọa thủ (40%) → GẦN NHƯ TRỐNG
           Xung chiếu (30%) → CHIẾM 80% SỨC MẠNH BẢN CUNG

Công thức: Sức mạnh thực tế VCD ≈ 0.8 × Sức mạnh Xung chiếu
```

> **Lê Quang Lăng:** *"Cung VCD mượn 80% lực xung chiếu. Nếu xung chiếu đẹp → VCD đẹp. Nếu xung chiếu xấu → VCD xấu."*

### 13.3 Ý Nghĩa Tâm Lý VCD

```
VCD tại Mệnh   → Người linh hoạt, thích ứng, "tấm gương phản chiếu"
VCD tại Tài     → Tiền bạc trồi sụt, phụ thuộc xung chiếu
VCD tại Quan    → Sự nghiệp đứt đoạn, tự do hơn là hệ thống
VCD tại Thiên Di → Ra ngoài trống trải, cần chiếu về mạnh
```

### 13.4 VCD + Tuần/Triệt

```
VCD + Triệt = Trống + Cắt → Cực hung (không nền, không gốc)
VCD + Tuần  = Trống + Che  → Che cái trống → nghịch lý "bảo vệ sự trống rỗng"
```

---

## XIV. PHÂN TÍCH MỆNH — THÂN

> **Nguyên tắc:** Mệnh = Tiền Vận (< 34t). Thân = Hậu Vận (> 34t). Vị trí Thân CƯ cung nào quyết định trọng tâm hậu vận.

### 14.1 Các Trường Hợp Thân Cư

| Thân cư | Ý nghĩa Hậu Vận |
|---|---|
| **Mệnh** (Đồng Cung) | Nhất quán trọn kiếp. Nghĩ sao làm vậy. Kiên cường nhưng bảo thủ |
| **Phu Thê** | Gia đạo chi phối. Hôn nhân = trọng tâm sau 34t |
| **Quan Lộc** | Sự nghiệp chi phối. Đau đáu chức vụ, chuyên môn |
| **Phúc Đức** | Tích lũy ngầm. Hậu vận về với gốc rễ tổ tiên |
| **Tài Bạch** | Tiền bạc chi phối. Kiếm tiền là mục đích |
| **Thiên Di** | Ra ngoài. Hậu vận gắn với xã giao, xuất ngoại |

### 14.2 Mệnh-Thân Không Đồng Cung

```
Phân tích 2 pha:
  TIỀN VẬN (< 34t): Luận theo cung MỆNH → 5 chiều tương tác
  HẬU VẬN (> 34t): Luận theo cung THÂN → 5 chiều tương tác
  
⚠️ Chú ý: Chủ Mệnh ≠ Chủ Thân
   Chủ Mệnh: Sao chủ cung Mệnh → tính cách gốc
   Chủ Thân: Sao chủ cung Thân cư → xu hướng hậu vận
```

### 14.3 Định Lượng Mệnh-Thân

```
☐ Đánh giá ĐỘ VỮNG Mệnh (Baseline Resilience): x/10
☐ Đánh giá ĐỘ VỮNG Thân (Baseline Resilience): x/10
☐ So sánh: Mệnh mạnh + Thân yếu → "Tiền vận rực rỡ, hậu vận suy"
            Mệnh yếu + Thân mạnh → "Tiền bần hậu phú"
            Cả hai mạnh → "Rồng phượng trọn kiếp"
```

---

## XV. TƯƠNG TÁC ĐA LÁ SỐ — PHÂN TÍCH QUAN HỆ

> **Nguyên tắc:** Khi phân tích quan hệ giữa 2+ người, PHẢI đối chiếu tinh bàn MỖI NGƯỜI, tìm điểm CỘNG HƯỞNG và XUNG ĐỘT.

### 15.1 Phân Tích Cặp Đôi (Hôn Nhân / Đối Tác)

```
Bước 1: Xác định cung Thê/Phu của TỪNG NGƯỜI
Bước 2: So sánh chính tinh Thê/Phu:
         - Cùng hành → Tương hòa
         - Sinh nhau → Bổ trợ
         - Khắc nhau → Xung đột
Bước 3: Kiểm tra Sát tinh tại cung Thê/Phu MỖI NGƯỜI
Bước 4: Xét Tứ Hóa: Hóa Kỵ ở cung Thê/Phu → Song Kỵ?
Bước 5: Tổng hợp "Bản đồ tương tác tình cảm"
```

### 15.2 Phân Tích Tam Giác Quan Hệ

```
Khi có 3 lá số tương tác:
  ☐ Vẽ MA TRẬN: Ai tác động ai? Qua cung nào?
  ☐ Tìm "Nút đồng bệnh" (chung Kỵ/Hung → đồng cảm bệnh lý)
  ☐ Tìm "Nút xung khắc" (nghịch Hành/Kỵ chiếu chéo)
```

> **Ví dụ thực:** An (Mệnh Phủ Mùi) — Uyên Anh (Mệnh Cơ Hợi) — Bà (Mệnh Phá Tý): Ba người đều có cung Thê/Phu hung nặng (Vũ Phá Kỵ / Nhật Nguyệt Hãm / Vũ Kỵ Cô Quả) → "Nút đồng bệnh hôn nhân" kéo họ lại gần nhau.

### 15.3 Phân Tích Gia Đình (Phụ Mẫu ↔ Con Cái)

```
Bước 1: Lá số Cha/Mẹ → cung Tử Tức → Chính tinh + Sát tinh
Bước 2: Lá số Con → cung Phụ Mẫu → Chính tinh + Sát tinh  
Bước 3: Đối chiếu: Phụ Mẫu (con) vs Tử (cha/mẹ) khớp không?
Bước 4: Tìm "Bệ phóng" (Phụ Mẫu sạch sát → cha mẹ là bệ phóng)
         hoặc "Gánh nặng" (Phụ Mẫu hung → cha mẹ là thử thách)
```

---

## XVI. GLOSSARY — THUẬT NGỮ CHUẨN

| Thuật ngữ | Viết tắt | Nghĩa |
|---|:---:|---|
| Vô Chính Diệu | VCD | Cung không có 14 chính tinh |
| Miếu | M | Sao đắc trường sinh tại cung |
| Vượng | V | Sao vượng khí tại cung |
| Đắc | Đ | Sao đắc địa (tốt) |
| Hãm | H | Sao thất thế (xấu) |
| Bình | B | Sao bình thường |
| Đại Vận | ĐV | Chu kỳ 10 năm |
| Lưu Niên | LN | Chu kỳ 1 năm |
| Tiểu Hạn | TH | Cung đại diện cho 1 năm |
| Tam Phương Tứ Chính | TPTC | Bản cung + Xung chiếu + 2 Tam hợp |
| Phi Tinh | — | Hệ thống Hóa bay theo Can |
| Song Kỵ | — | 2 Hóa Kỵ đồng cung (cực hung) |
| Phản Vi Giai | — | Hung biến thành cát khi đắc địa |
| Thiên La | — | Cung Tuất (lưới trời) |
| Địa Võng | — | Cung Thìn (lưới đất) |

---

## XVII. PHỤ TINH DEEP ANALYSIS — SOP 5 NHÓM

> **Bổ sung từ phiên luận giải Long (14/03/2026)**. Khung phân tích phụ tinh đã kiểm chứng qua 50+ trích dẫn Perplexity.

### 17.1 Phân nhóm phụ tinh (5 nhóm)

| Nhóm | Sao | Ưu tiên |
|:---:|---|:---:|
| 1 | **Tứ Hóa** (Lộc/Quyền/Khoa/Kỵ) | 🔴 Cao nhất |
| 2 | **Lục Sát** (Kình/Đà/Hỏa/Linh/Không/Kiếp) | 🔴 Cao |
| 3 | **Lục Cát Phụ** (Xương/Khúc/Khôi/Việt/Tả/Hữu) | 🟡 Trung |
| 4 | **Lộc Tồn + Mã + Đào Hoa hệ** | 🟡 Trung |
| 5 | **Hình/Riêu/Cô + Tiểu Tinh** | 🟢 Bổ sung |

### 17.2 Mỗi phụ tinh cần

```
☐ Trạng thái (Miếu/Vượng/Đắc/Bình/Hãm) — tranh luận đa phái nếu có
☐ Ngũ Hành mechanism (hành sao vs hành cung: sinh/khắc/đồng hành)
☐ Phú cổ (≥1 phú + nguồn)
☐ Cách cục liên quan (bộ phối hợp)
☐ Áp dụng lá số cụ thể
```

### 17.3 Nguồn đáng tin cho phụ tinh

| Nguồn | URL | Chuyên mục |
|---|---|---|
| phoenix164.blogspot.com | Lục Sát | Trạng thái chi tiết |
| tuvi.vn | Phụ tinh | Tả Hữu, Kình Đà |
| horos.vn | Lục cát tinh | Tổng quan |
| tuvivietnam.vn | Tả Hữu toàn thư | Deep analysis |
| lyso.vn | Phú giải | Phú cổ + giải thích |

---

## XVIII. QUALITY GATE — CHECKLIST VÀ VỊ TRÍ

> **File:** `/Users/mac/Desktop/Downloads/Luan giai tu vi by BS Long/.agent/quality_gate.md`

### 18.1 Tóm tắt 6 hạng mục

| Hạng | Bắt buộc | Mô tả |
|:---:|:---:|---|
| A | 8 bộ chính tinh × 4 tiêu chí | Đa phái, Ngũ Hành, phú, áp dụng |
| B | ≥ 20 phụ tinh × 3 tiêu chí | Trạng thái, Ngũ Hành, áp dụng |
| C | ≥ 15 cách cục × 3 tiêu chí | Điều kiện, phú, phân loại |
| D | ĐV hiện tại × 6 subsections | Tinh bàn, NH, Triệt, so sánh, TH LN, chiến lược |
| E | Trích dẫn ≥ 5 nguồn | Perplexity verified + URLs |
| F | Cấu trúc ≥ 1500 dòng | Markdown hợp lệ, không duplicate |

### 18.2 Verification Stamp Template

```
✅ QG PASS [DD/MM/YYYY] v[x.y]
Chính tinh: [x]/8 bộ | Phụ tinh: [x] sao | Cách cục: [x] ([NET])
Đại vận: [x]/7 | Trích dẫn: [x] nguồn | Dung lượng: [x] dòng
```

---

## XIX. CÁCH CỤC REGISTRY — 19 CÁCH CỤC ĐÃ KIỂM CHỨNG

> **Cập nhật:** 14/03/2026. Danh sách tối thiểu cần kiểm tra cho mỗi lá số.

### 19.1 Cát Cách (13)

| # | Cách cục | Điều kiện ngắn | Chính/Biến thể |
|:---:|---|---|:---:|
| 1 | Phủ Lộc Đồng Cung | Phủ + Lộc Tồn Đắc đồng cung | Chính |
| 2 | Tam Kỳ Gia Hội | Lộc+Quyền+Khoa tam phương | Chính/BT |
| 3 | Lộc Mã Giao Trì | Lộc Tồn + Thiên Mã đồng/nhị hợp | Chính |
| 4 | Nhật Nguyệt Giáp Thân | Dương+Âm Vượng giáp cung Thân | Chính |
| 5 | Vũ Tham Đồng Hành | Vũ+Tham Miếu tại Tứ Mộ | Chính |
| 6 | Tham Linh Tịnh Thủ | Tham+Linh đồng/tam hợp | Chính/BT |
| 7 | Kỵ Phản Vi Giai | Kỵ Đắc tại Tứ Mộ Điền Tài | Chính |
| 8 | Cự Nhật Đồng Cung | Cự+Dương Vượng đồng cung | Chính |
| 9 | Tử Phủ Triều Viên | Tử Vi + Phủ xung chiếu | Chính |
| 10 | Nhật Nguyệt Tịnh Minh | Dương+Âm đều Vượng | Chính |
| 11 | Thất Sát Triều Đẩu | Sát + Tử Vi đồng cung | BT |
| 12 | Phủ Tướng Triều Viên | Phủ + Tướng tam hợp | Chính/BT |
| 13 | Lộc Hợp Uyên Ương | Hóa Lộc nhị hợp/Tứ Mộ với Kỵ Đắc | Chính |

### 19.2 Trung (1)

| 14 | Cơ Nguyệt Đồng Lương | 4 sao phân tán tam phương | BT |

### 19.3 Hung Cách (5)

| 15 | Lộc Tồn Kình Đà Giáp | Lộc thủ Mệnh, K-Đ giáp | Chính |
| 16 | Giáp Không Kiếp | Mệnh bị Không+Kiếp giáp | Chính |
| 17 | Liêm Phá cư Dậu | Liêm+Phá Hãm tại Dậu | Chính |
| 18 | Vũ Khúc Kiếp Không | Vũ Khúc nhị hợp Kiếp/Không | BT |
| 19 | Hình Sát Phùng Không | Hình+Sát tinh+Không đồng tam phương | Chính |

---

## XX. ĐẠI VẬN DEEP DIVE — TEMPLATE 6 SUBSECTIONS

> Template chuẩn cho phân tích ĐV hiện tại. Đã áp dụng thành công: Long ĐV4 (Dần, 34-43t).

```markdown
### PHÂN TÍCH CHUYÊN SÂU ĐẠI VẬN [X] ([tuổi], [năm]) — "[Biệt danh]"

#### 1. TINH BÀN ĐẠI VẬN
| Sao | Hành | Trạng thái | Vai trò |

#### 2. NGŨ HÀNH ĐẠI VẬN vs BẢN MỆNH
| Yếu tố | Hành | Tương tác | Hệ quả |

#### 3. TRIỆT KHÔNG ĐỘNG LỰC HỌC
| Giai đoạn | Triệt nhả | Biểu hiện |

#### 4. SO SÁNH VỚI ĐẠI VẬN TRƯỚC
| Tiêu chí | ĐV trước | ĐV hiện tại |

#### 5. TỨ HÓA LƯU NIÊN [Can] TRONG ĐV
| Hóa LN | Phi vào | Cung | Ý nghĩa |

#### 6. CHIẾN LƯỢC ĐẠI VẬN
| Giai đoạn | Hành động ưu tiên | Cảnh báo |
```

---

*Created: 25/02/2026 | Updated: 14/03/2026 | Version: 5.0*
*v5.0 — Bổ sung Section XVII (Phụ Tinh SOP), XVIII (Quality Gate), XIX (Cách Cục Registry 19), XX (Đại Vận Deep Template)*
*Workflow: `/tu-vi-analysis` | Quality Gate: `.agent/quality_gate.md`*

