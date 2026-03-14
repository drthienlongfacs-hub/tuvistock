---
name: Tử Vi Luận Giải Chuyên Sâu
description: Pipeline 7 phase tạo luận giải Tử Vi toàn diện từ ảnh lá số — chuẩn v5.0. Tích hợp triết lý Liễu Phàm Tứ Huấn (Mệnh do ta lập). Kết hợp skill viết chuyên nghiệp cho văn phong hàn lâm nhưng con người.
---

# TỬ VI LUẬN GIẢI CHUYÊN SÂU — SKILL v3.0

> **Phiên bản:** 3.0 | **Ngày tạo:** 2026-03-13 | **Cập nhật:** Tích hợp Liễu Phàm Tứ Huấn
> **Gold Standard:** `luan_giai_toan_dien_long_2026.md` + phản biện Liễu Phàm
> **Bảng tra:** `reference_tables.md` (cùng thư mục skill)

> ⚠️ **NGUYÊN TẮC CỐT LÕI (Liễu Phàm Tứ Huấn):**
> 1. **Lá số = XU HƯỚNG, không phải bản án.** *"Mệnh do ta lập, phúc do ta cầu."*
> 2. **Đức lớn phá mệnh xấu.** *"Thiện dày thì họa tiêu."*
> 3. **Cách cục = khuynh hướng, KHÔNG PHẢI hằng số.** Phụ thuộc Đại Vận + môi trường + đạo đức + hành vi.
> 4. **3 lớp vận mệnh:** Thiên mệnh (lá số) → Phong thủy (môi trường) → Nhân đức (hành vi).

---

## 1. TRIGGER

- "luận giải Tử Vi", "phân tích lá số", "xem lá số"
- "tạo bản luận giải", "Tử Vi toàn diện"
- "analyze birth chart", "destiny analysis"

## 2. INPUT BẮT BUỘC

| # | Input | Nguồn | Bắt buộc |
|---|---|---|:---:|
| 1 | Ảnh lá số (hoặc tinh bàn văn bản) | User cung cấp | ✅ |
| 2 | Năm sinh (Can Chi + Dương Lịch) | User / extract từ lá số | ✅ |
| 3 | Giới tính | User | ✅ |
| 4 | Giờ sinh (Chi) | User / extract | ✅ |
| 5 | Năm cần luận (Lưu Niên) | User | ⬜ (tùy chọn) |

## 3. PIPELINE 7 PHASE

```
PHASE 1: DATA INTAKE (Ảnh → SSoT)
    ↓
PHASE 2: FOUNDATION (Mệnh-Thân, Cục, Nạp Âm, Cách Cục)
    ↓
PHASE 3: DEEP ANALYSIS (12 Cung × 5 Chiều)
    ↓
PHASE 4: TEMPORAL (Đại Vận + Lưu Niên + Phi Tinh 12 tháng)
    ↓
PHASE 5: MULTI-DIMENSIONAL (7 Trục)
    ↓
PHASE 6: SYNTHESIS (Cẩm Nang Hành Động)
    ↓
PHASE 7: QA GATE + EXPORT
```

---

## 4. PHASE 1 — DATA INTAKE

### 4.1 Từ ảnh lá số → Structured SSoT

**Bước 1:** Extract từ ảnh hoặc dữ liệu user cung cấp:
- 12 cung vị (Tý → Hợi) + Cung Chức (Mệnh, Phụ Mẫu...)
- Tất cả sao trong mỗi cung + trạng thái (M/V/Đ/B/H)
- Tuần/Triệt vị trí
- Tứ Hóa (theo Can năm sinh, tra `reference_tables.md` mục 2)
- Cục + Nạp Âm (tra `reference_tables.md` mục 9)
- Tràng Sinh khởi điểm (tra `reference_tables.md` mục 4.2)

**Bước 2:** Xây dựng SSoT Table (bảng nguồn sự thật):

```markdown
| Cung | Chi | Cung Chức | Chính Tinh | Phụ Tinh | Sát Tinh | Tràng Sinh |
|---|---|---|---|---|---|---|
| Hợi | Âm Thủy | Mệnh | Thiên Phủ(Đ) | Lộc Tồn(Đ), Khoa | Riêu(H), Cô | Bệnh 🤒 |
| ... | ... | ... | ... | ... | ... | ... |
```

**Bước 3:** Xác minh SSoT
- Cross-check Tứ Hóa vs `reference_tables.md` mục 2
- Verify Tuần/Triệt tính toán (Can Chi → 2 chi cuối của bộ Can)
- Verify Tràng Sinh vs Cục (mục 4.2)

> ⛔ **KHÔNG ĐƯỢC viết bất kỳ phân tích nào trước khi SSoT hoàn tất và verify.**

---

## 5. PHASE 2 — FOUNDATION ANALYSIS

### Output cần tạo (theo thứ tự):

**5.1 Tổng Quan Mệnh-Thân:**
- Mệnh ở đâu, chính tinh gì, trạng thái
- Thân ở đâu, chính tinh gì, liên hệ Mệnh-Thân
- Tuổi chuyển giao Mệnh → Thân
- Nạp Âm mệnh + ý nghĩa ví von (xem `writing_style_guide.md`)

**5.2 Phân Tích 6 Chiều Cung Mệnh:**
```
1. Bản cung (40%) → tinh bàn + Ngũ Hành interaction
2. Đối cung chiếu (30%) → sao chiếu + lực
3. Tam hợp (20%) → 2 cung tam hợp + Ngũ Hành Cục
4. Nhị hợp (10%) → kênh ẩn
5. Giáp cung (~5%) → 2 cung kế
6. Lục Hại → xung khắc ngầm
```

**5.3 Bốn Tam Hợp Vòng Macro:**
```
Mệnh-Tài-Quan (Trục Sự Nghiệp)
Huynh-Nô-Thê (Trục Quan Hệ)
Tử-Điền-Phúc (Trục Tài Sản)
Phụ-Ách-Di (Trục Xã Hội)
```

**5.4 Tràng Sinh 12 Cung:**
- Map Tràng Sinh → 12 cung chức
- Highlight cung Đế Vượng, Tràng Sinh, Mộ (điểm mạnh)
- Highlight cung Tuyệt, Suy, Bệnh (điểm yếu)

**5.5 Cách Cục:**
- Identify TẤT CẢ cách cục trong lá số
- Verify bằng phú cổ (`reference_tables.md` mục 6)
- Đánh giá mức ảnh hưởng (cát/hung) — nhưng GHI RÕ: đây là **khuynh hướng**, không phải hằng số
- ⚠️ **KHÔNG chấm điểm tuyệt đối kiểu toán học.** Ghi kèm điều kiện kích hoạt (Đại Vận nào, hành vi nào)

---

## 6. PHASE 3 — DEEP ANALYSIS (12 CUNG × 5 CHIỀU)

### Template mỗi cung:

```markdown
#### [ICON] CUNG [N]: [TÊN CUNG] — [Chi] ([Âm/Dương] [Hành]) — [HEADLINE VÍ VON]

> **Phương pháp:** 5 chiều tương tác (40-30-20-10-5%)

##### N.1 BẢN CUNG (40%) — [Tinh bàn tóm tắt]

**Tinh bàn đầy đủ:** [liệt kê tất cả sao + trạng thái]

| Sao/Yếu tố | Hành | Trạng thái | Ngũ Hành vs Cung |
|---|:---:|:---:|---|

**Luận bản cung:** [Phân tích narrative]
**Tràng Sinh:** [Giai đoạn + ý nghĩa]

##### N.2 XUNG CHIẾU (30%) — [Đối cung]
##### N.3 TAM HỢP (20%) — [2 cung tam hợp]
##### N.4 NHỊ HỢP (10%) — [Cung nhị hợp]
##### N.5 GIÁP CUNG (~5%) — [2 cung giáp]
##### N.6 LỤC HẠI — [Cung lục hại]

##### 🔑 TỔNG KẾT [TÊN CUNG]

| Chiều | Hung/Cát | Lượng hóa | Cơ chế |
|---|:---:|:---:|---|
| BẢN CUNG (40%) | | | |
| CHIẾU (30%) | | | |
| TAM HỢP (20%) | | | |
| NHỊ HỢP (10%) | | | |
| GIÁP (~5%) | | | |
| **NET** | | | |

**N đặc điểm [tên cung] [Tên người]:**
1. ...

> **[Expert]:** *"[Trích dẫn]"*
```

### Thứ tự phân tích 12 cung:
1. Mệnh → 2. Phục/Thân → 3. Thiên Di → 4. Nô Bộc → 5. Quan Lộc
   → 6. Điền Trạch → 7. Phụ Mẫu → 8. Tật Ách → 9. Tài Bạch
   → 10. Tử Tức → 11. Phu Thê → 12. Huynh Đệ

> **Lý do:** Mệnh-Thân-Di trước (trục chính) → Quan-Tài-Điền (trục sự nghiệp) → Phụ-Ách (sức khỏe/gia đình) → Tử-Thê-Huynh (quan hệ thân mật).

---

## 7. PHASE 4 — TEMPORAL ANALYSIS

### 7.1 Đại Vận Blueprint (10 thập kỷ)
- Bảng 10 Đại Vận: tuổi, cung, tinh bàn, nhận định
- Tuần-Triệt dynamics xuyên Đại Vận
- Nguyên lý "Tuần-Triệt Tháo Gỡ" (nếu áp dụng)

### 7.2 Lưu Niên Cụ Thể (nếu user yêu cầu)
**Nền tảng năm:**
- Bát Tự năm (Can + Chi + Nạp Âm + tương tác Mệnh)
- Kinh Dịch quẻ chủ đạo (Perplexity verify)
- Tứ Hóa Lưu Niên (tra `reference_tables.md` mục 2)
- Lưu Tinh năm

**Tiểu Hạn năm:**
- Xác định Tiểu Hạn cung

**12 Tháng Phi Tinh Lưu Nguyệt:**

Template mỗi tháng:
```markdown
##### [ICON] THÁNG [N] ÂM LỊCH ([CAN CHI]) — Cung [TÊN] — **[Điểm]/10**

| Hạng mục | Chi tiết |
|---|---|
| **Lưu Nguyệt cung** | [Chi + tinh bàn bản mệnh] |
| **Can tháng** | [Can] → TH: [4 Hóa] |
| **Phi Tinh chính** | [4 phi tinh + cung đổ vào + ý nghĩa] |
| **Ngũ Hành tháng** | [Can vs Chi tháng] |

**Luận mở rộng:** [Narrative analysis]

> **Kinh nghiệm:** [Actionable advice]
```

---

## 8. PHASE 5 — MULTI-DIMENSIONAL (8 TRỤC)

| # | Trục | Nội dung | Nguồn |
|---|---|---|---|
| 1 | **Nhân Sinh** | Triết lý sống tổng hợp từ Mệnh-Thân-Đại Vận | Stoicism, Lão Tử, Frankl |
| 2 | **Nhân Tính** | Big Five Personality mapping | Costa & McCrae 1992 |
| 3 | **Nhân Tướng** | Tâm Sinh Tướng — ngoại hình dự đoán | Truyền thống + tâm lý |
| 4 | **Nhân Quả** | Tứ Hóa chuỗi + Systems Thinking | Senge, Meadows |
| 5 | **Bối Cảnh** | Thiên thời (xu hướng thời đại) + Địa lợi | Sociological |
| 6 | **Nhân Duyên** | Xác suất + Chống Giòn | Nassim Taleb |
| 7 | **Quy Luật** | Ngũ Hành = bảo toàn năng lượng | Darwin, Physics |
| 8 | **⭐ Nhân Đức** | **Đức-Tâm-Hành vi quyết định biến số** | **Liễu Phàm Tứ Huấn** |

> ⚠️ **TRỤC 8 (NHÂN ĐỨC) LÀ BẮT BUỘC** — theo nguyên lý *"Mệnh do ta lập, phúc do ta cầu."*
> Template Trục 8:
> - Phúc Đức so với Mệnh: Phúc > Mệnh = "càng tích đức, vận càng mở"
> - 3 lớp biến số: Thiên mệnh (lá số) → Phong thủy (môi trường) → Nhân đức (hành vi)
> - Khuyến nghị tu tâm cụ thể (giúp người, giữ tín, không tham)
> - ⛔ KHÔNG viết kiểu "định mệnh tuyệt đối" — LUÔN ghi rõ: "đây là xu hướng, có thể thay đổi bằng đức và hành vi"

---

## 9. PHASE 6 — SYNTHESIS

Tạo bảng **Cẩm Nang Hành Động**:

```markdown
| Vấn đề | Tinh bàn | Hành động cụ thể |
|---|---|---|
| Sự Nghiệp | [cung Quan] | [advice] |
| Dòng Tiền | [cung Tài + Phúc] | [advice] |
| Hôn Nhân | [cung Thê] | [advice] |
| Sức Khỏe | [cung Ách] | [advice] |
| Mạng Lưới | [cung Nô] | [advice] |
| [Năm cụ thể] | [Lưu Niên] | [advice] |
```

---

## 10. PHASE 7 — QA GATE

### 3 Tầng Kiểm Duyệt

**Tầng 1: Data Accuracy**
- [ ] SSoT table verified vs ảnh lá số gốc
- [ ] Can Chi tháng/năm đúng (`reference_tables.md` mục 1)
- [ ] Tứ Hóa đúng (`reference_tables.md` mục 2)
- [ ] Tràng Sinh đúng (`reference_tables.md` mục 4)
- [ ] Tuần/Triệt vị trí đúng
- [ ] Phú cổ trích đúng nguồn

**Tầng 2: Analysis Consistency**
- [ ] 12 cung đều có bảng lượng hóa NET
- [ ] Tổng cát/hung nhất quán (không mâu thuẫn giữa cung)
- [ ] Đại Vận logic (không nhảy cóc, tuổi liên tục)
- [ ] Lưu Niên Can tháng đúng

**Tầng 3: Writing Quality**
- [ ] Mỗi cung có ví von headline
- [ ] Mỗi cung có expert quote
- [ ] Ngũ Hành interaction giải thích rõ ràng
- [ ] Văn phong nhất quán (xem `writing_style_guide.md`)
- [ ] Không AI-speak, không emoji quá mức

**Tầng 4: Tone Balance & Nhân Đức (Liễu Phàm)**
- [ ] KHÔNG dùng "hung nặng nhất" — thay bằng "khuynh hướng cần lưu ý nhất"
- [ ] KHÔNG viết kiểu "định mệnh tuyệt đối" — luôn kèm "có thể thay đổi bằng..."
- [ ] Cách cục score GHI RÕ "khuynh hướng" và điều kiện kích hoạt
- [ ] Trục 8 (Nhân Đức) PHẢI CÓ trong Phần IX
- [ ] Phần X (Cẩm Nang) PHẢI có mục "Tu tâm tích đức"
- [ ] Tổng thể: hung ≤ 40% dung lượng, cát + hướng dẫn ≥ 60%

---

## 11. OUTPUT SPECS

### File structure đầu ra:

```
luan_giai_toan_dien_[TÊN]_[NĂM].md
├── PHẦN I: Nền Tảng Mệnh (~130 dòng)
├── PHẦN II: 6 Chiều Tương Tác Mệnh (~110 dòng)
├── PHẦN III: 4 Tam Hợp + Tràng Sinh (~100 dòng)
├── PHẦN IV: 12 Cách Cục (~80 dòng)
├── PHẦN V: 4 Cung Trọng Yếu + Nội Hàm (~130 dòng)
├── PHẦN VI: 12 Cung Chi Tiết (~640 dòng)
├── PHẦN VII: Tứ Hóa Chuỗi (~30 dòng)
├── PHẦN VIII: Đại Vận + Lưu Niên (~460 dòng)
├── PHẦN IX: 7 Trục Đa Chiều (~140 dòng)
└── PHẦN X: Cẩm Nang Hành Động (~50 dòng)
```

**Target:** 1500-2000 dòng | ~150-180KB

---

## 12. DEPENDENCY FILES

| File | Vị trí | Vai trò |
|---|---|---|
| `reference_tables.md` | Cùng skill folder | Bảng tra Can Chi, Tứ Hóa, etc. |
| `writing_style_guide.md` | Cùng skill folder | Hướng dẫn văn phong |
| `ra_soat_5_chieu_tuong_tac.md` | `02_luan_giai/` | Framework 5 chiều gốc |
| `menh_dep_nhat_7_truc.md` | `02_luan_giai/` | Framework 7 trục gốc |
| `cach_cuc_chinh_thong.md` | `02_luan_giai/` | Database cách cục |
| Perplexity MCP | External | Cross-verify thuật ngữ, phú cổ |
