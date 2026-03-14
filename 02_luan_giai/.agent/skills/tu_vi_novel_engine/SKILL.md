---
name: Tử Vi Novel Engine
description: Quy trình chuẩn viết tiểu thuyết dựa trên dữ liệu Tử Vi — từ kiến trúc cốt truyện đến kiểm duyệt đầu ra. Đã kiểm chứng thực tế qua dự án "Thanh Kiếm Ra Khỏi Vỏ" (03/2026).
---

# TỬ VI NOVEL ENGINE — SKILL MASTER

> **Phiên bản:** 1.0 | **Ngày tạo:** 2026-03-13
> **Dự án gốc:** "THE SWORD LEAVES THE SHEATH" — Biên niên ký Long 2026
> **Trạng thái:** Đã kiểm chứng qua 12 chương, 48 cảnh, 13 ảnh bìa

---

## 1. MỤC ĐÍCH

Skill này chuẩn hóa toàn bộ quy trình tạo tiểu thuyết văn học dựa trên dữ liệu Tử Vi, bao gồm:
- Kiến trúc cốt truyện (Story Architecture)
- Bộ máy nhân vật (Character Engine)
- Vòng lặp viết lặp đi lặp lại (Self-Evolving Writing Loop)
- Kiểm duyệt đa tầng (Multi-Layer QA)
- Bảo mật và phục hồi file (Asset Protection)

## 2. TRIGGER

Kích hoạt khi user yêu cầu:
- "viết tiểu thuyết từ Tử Vi", "novel from destiny data"
- "tạo sách vận mệnh", "personal destiny novel"
- "Master Writer Mode", "Self-Evolving Book Engine"

## 3. PIPELINE TỔNG QUAN (7 PHASE)

```
Phase 1: DATA INTAKE → Phase 2: STORY ARCHITECTURE → Phase 3: CHARACTER ENGINE
→ Phase 4: ITERATIVE WRITING LOOP (×12 chapters) → Phase 5: VISUAL GENERATION
→ Phase 6: QA GATE (3 tầng) → Phase 7: COMPILATION & PROTECTION
```

---

## 4. PHASE 1 — DATA INTAKE (Nạp Dữ Liệu Gốc)

### 4.1 Source of Truth (SSoT)
| # | File | Vai trò | Bắt buộc |
|---|---|---|:---:|
| 1 | `luan_giai_toan_dien_*.md` | Luận giải Tử Vi toàn diện (Gold SSoT) | ✅ |
| 2 | `tinh_ban_12_cung.md` | Tinh bàn 12 cung chi tiết | ✅ |
| 3 | `cach_cuc_chinh_thong.md` | Cách cục chính thống | ⬜ |
| 4 | `goc_re_an_sao_menh.md` | Góc rễ an sao | ⬜ |
| 5 | `ra_soat_5_chieu_tuong_tac.md` | Rà soát 5 chiều tương tác | ⬜ |

### 4.2 Trích xuất bắt buộc trước khi viết
Từ SSoT, BẮT BUỘC extract và lưu vào bộ nhớ:
1. **Năm Can Chi:** Ví dụ `Bính Ngọ` (2026). KHÔNG nhầm với năm sinh.
2. **Năm sinh Can Chi:** Ví dụ `Nhâm Thân` (1992).
3. **Nạp Âm mệnh:** Ví dụ `Kiếm Phong Kim` + `Thiên Hà Thủy`.
4. **12 tháng Can Chi:** Tính chính xác theo CAN NĂM (xem bảng 4.3).
5. **Tuần Triệt:** Vị trí chính xác (Tuần Tuất-Hợi, Triệt Dần-Mão).
6. **Tứ Hóa:** Lương Lộc → Tử Quyền → Khoa → Vũ Kỵ.
7. **Cung trọng yếu:** Mệnh, Thân, Quan, Tài, Điền, Phu Thê.

### 4.3 Bảng Can Chi 12 Tháng (Năm Bính)
> **Công thức tính Can tháng:** Năm Bính → tháng Giêng (Dần) = **Canh Dần**
> **Nguồn:** Lịch Vạn Niên chuẩn, đối chiếu Perplexity MCP

| Tháng ÂL | Chi tháng | Can tháng | Can Chi đầy đủ |
|:---:|:---:|:---:|---|
| 1 | Dần | Canh | **Canh Dần** |
| 2 | Mão | Tân | **Tân Mão** |
| 3 | Thìn | Nhâm | **Nhâm Thìn** |
| 4 | Tỵ | Quý | **Quý Tỵ** |
| 5 | Ngọ | Giáp | **Giáp Ngọ** |
| 6 | Mùi | Ất | **Ất Mùi** |
| 7 | Thân | Bính | **Bính Thân** |
| 8 | Dậu | Đinh | **Đinh Dậu** |
| 9 | Tuất | Mậu | **Mậu Tuất** |
| 10 | Hợi | Kỷ | **Kỷ Hợi** |
| 11 | Tý | Canh | **Canh Tý** |
| 12 | Sửu | Tân | **Tân Sửu** |

> ⚠️ **RCA-NOVEL-001:** Nhầm "Nhâm Thìn" (tháng 3 ÂL) thành "năm" hoặc gán sai cho tháng 4. Đã xảy ra tại Chương 4, 9, 12 trong phiên bản v1.0.

---

## 5. PHASE 2 — STORY ARCHITECTURE

### 5.1 Cấu trúc bắt buộc
- **3-Act Structure:** Act I (Lò Rèn), Act II (Dòng Chảy), Act III (Kiếm Ra Khỏi Vỏ)
- **12 Chapters:** Mỗi tháng = 1 chương
- **48 Scenes:** 4 cảnh/chương (tối thiểu 3, tối đa 5)
- **Target:** 4,000–5,500 từ/chương → 50,000–70,000 từ toàn bộ

### 5.2 Hệ thống Chống Lặp (Anti-Repetition System)
Các motif lặp lại (bất động sản, cám dỗ tiền bạc) PHẢI thay đổi cơ chế tâm lý khước từ:
| Lần | Tháng | Cơ chế khước từ |
|---|---|---|
| 1 | Tháng 1 | Bản năng + Hóa Kỵ cảnh giác |
| 2 | Tháng 6 | Phản xạ tự động (Autopilot) |
| 3 | Tháng 7 | Phớt lờ hoàn toàn (Chặn Zalo) |
| 4 | Tháng 11 | Phân tích dữ liệu vĩ mô (Cự Nhật) |

### 5.3 Framework Vận Mệnh
| Lực lượng Tử Vi | Biểu hiện trong truyện | Cách xử lý |
|---|---|---|
| Triệt Không | Rào cản sự nghiệp chính thống | Re-route năng lượng (đi ngầm) |
| Tuần Không | Phong ấn 34 năm tiềm năng | Chịu áp lực cho đến khi vỡ |
| Song Kỵ | Xung đột hôn nhân/tình cảm | Hạ Ego, dùng Hóa Khoa |
| Hóa Lộc Nô Bộc | Mạng lưới tri thức mang lộc | Cho đi vô tư, nhận về bất ngờ |
| Hóa Kỵ Phản Vi Giai | Bí mật, giấu kín thành công | Tuyệt đối ẩn danh |

---

## 6. PHASE 4 — ITERATIVE WRITING LOOP

### Quy trình mỗi chương:
```
1. PLAN: Tóm tắt chương trước → duy trì tính liền mạch → kiểm tra Anti-Repetition
2. WRITE: Văn phong văn học mở rộng, Paulo Coelho/Murakami, độc thoại nội tâm sâu
3. VERIFY: Chạy QA Gate 3 tầng (xem Phase 6)
4. NEXT: Chuyển chương tiếp theo
```

### Quy tắc văn phong:
- **Ngôn ngữ:** Tiếng Việt văn học, KHÔNG dùng tiếng lóng
- **Giọng kể:** Ngôi thứ 3, hướng nội, có điểm nhìn hạn chế (Limited POV)
- **Dialogue:** Tự nhiên, không giải thích quá mức, phải bộc lộ tính cách
- **Hành động:** Cinematic — mô tả vật lý, giác quan, không trừu tượng hóa quá mức
- **Triết học:** Tích hợp tự nhiên qua suy nghĩ nhân vật, KHÔNG thuyết giáo

---

## 7. PHASE 6 — QA GATE (3 TẦNG KIỂM DUYỆT)

### Tầng 1: Logic & Data (Tử Vi Accuracy)
| # | Kiểm tra | Phương pháp |
|---|---|---|
| 1 | Can Chi năm, tháng đúng | Đối chiếu bảng 4.3 |
| 2 | Thuật ngữ Tử Vi chính xác | Đối chiếu SSoT `luan_giai_toan_dien_*.md` |
| 3 | Cung vị, sao, trạng thái đúng | grep + manual cross-check vs SSoT |
| 4 | Tiểu sử nhân vật nhất quán | So với Character Engine (Phase 2) |
| 5 | Luật "Không mua BĐS 2026" | Verify tất cả 4 lần từ chối |

### Tầng 2: Narrative Consistency
| # | Kiểm tra | Phương pháp |
|---|---|---|
| 1 | Liên tục thời gian (timeline) | Mỗi chương = 1 tháng, kiểm tra nhảy cóc |
| 2 | Arc nhân vật tiến triển | Long: Ego → Humility → Mastery |
| 3 | Anti-Repetition | 4 cơ chế từ chối BĐS KHÁC nhau |
| 4 | Tension Curve | Act I↑ Act II~↗ Act III↑↓→ |
| 5 | Không mâu thuẫn giữa chương | Kiểm tra cross-reference |

### Tầng 3: Writing Style & Polish
| # | Kiểm tra | Phương pháp |
|---|---|---|
| 1 | Văn phong nhất quán | Ngôi 3, limited POV, không thay đổi |
| 2 | Từ ngữ chuyên nghiệp | Không lóng, không emoji, không AI-speak |
| 3 | Dialogue tự nhiên | Không giải thích quá mức |
| 4 | Mật độ triết học cân bằng | Không quá 2 đoạn triết/cảnh |
| 5 | Tiếng Việt chuẩn mực | Chính tả, ngữ pháp, dấu thanh |

### Hành động sau QA:
- **PASS tất cả 3 tầng:** Chuyển Phase 7
- **FAIL bất kỳ tầng nào:** Fix → re-verify → chỉ PASS mới đi tiếp

---

## 8. PHASE 7 — COMPILATION & ASSET PROTECTION

### 8.1 Cấu trúc file đầu ra
```
02_luan_giai/
├── novel_chapter_01.md ... novel_chapter_12.md  (12 chapters)
├── compile_novel_full.py                        (compilation script)
├── THE_SWORD_LEAVES_THE_SHEATH_FULL_2026.docx   (final DOCX)
├── luan_giai_toan_dien_long_2026.md              (SSoT - gold)
└── .agent/skills/tu_vi_novel_engine/SKILL.md     (THIS FILE)

brain/<conversation-id>/
├── chapter_*_cover_*.png                         (12 chapter covers)
├── the_sword_leaves_the_sheath_cover_*.png       (main book cover)
├── implementation_plan.md                        (story architecture)
├── task.md                                       (progress tracker)
└── novel_qa_report.md                            (audit report)
```

### 8.2 Quy trình Backup
1. **Trước mỗi phiên viết:** Verify SSoT file integrity
2. **Sau mỗi chương:** Commit chapter file + verify word count
3. **Sau Phase 6:** Backup toàn bộ folder qua Git hoặc Time Machine
4. **Final:** Compile DOCX + verify image embedding

### 8.3 Recovery Protocol
Nếu mất file hoặc lỗi:
1. Kiểm tra `.md` chapter files (nguồn chính)
2. Kiểm tra `brain/` folder cho ảnh bìa
3. Re-run `compile_novel_full.py` để tái tạo DOCX
4. Nếu mất SSoT: recover từ `.docx` -> convert lại `.md`

---

## 9. BÀI HỌC RCA (Root Cause Analysis)

### RCA-NOVEL-001: Nhầm Can Chi tháng/năm
- **Triệu chứng:** "Nhâm Thìn" (Can Chi tháng 3) bị dùng như tên NĂM tại Ch.4, Ch.9, Ch.12
- **Nguyên nhân gốc:** Không có bảng tra Can Chi tháng cố định trong prompt
- **Khắc phục:** Bổ sung bảng 4.3 vào skill, BẮT BUỘC tra cứu trước khi viết
- **Phòng ngừa:** QA Tầng 1 kiểm tra tất cả Can Chi references

### RCA-NOVEL-002: Trùng lặp cơ chế từ chối BĐS
- **Nguyên nhân:** Không có Anti-Repetition Matrix
- **Khắc phục:** Bảng 5.2 chỉ định cơ chế tâm lý khác cho mỗi lần

### RCA-NOVEL-003: Mật độ triết học không đều
- **Khắc phục:** Quy tắc max 2 đoạn triết/cảnh, tích hợp qua nội tâm

---

## 10. CHECKLIST TRƯỚC KHI XUẤT BẢN

- [ ] SSoT file đã verify integrity (shasum nếu có)
- [ ] Tất cả 12 chapters đã PASS QA Gate 3 tầng
- [ ] Can Chi tháng/năm đã đối chiếu bảng 4.3
- [ ] Anti-Repetition Matrix đã verify 4 cơ chế khác nhau
- [ ] 13 ảnh bìa (1 main + 12 chapter) đã tạo và verify
- [ ] Python compile script đã chạy thành công
- [ ] DOCX output đã verify: text + images embedded
- [ ] Backup folder đã thực hiện
- [ ] QA Report đã tạo và lưu tại `brain/novel_qa_report.md`
