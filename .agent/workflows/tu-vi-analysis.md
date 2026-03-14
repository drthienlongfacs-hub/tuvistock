---
description: Quy trình luận giải Tử Vi Đẩu Số end-to-end — 7 bước chuẩn hóa từ data đến output đạt quality gate
---
// turbo-all

# /tu-vi-analysis — SOP Luận Giải Tử Vi Đẩu Số

> **Version:** 1.0 | **Created:** 14/03/2026
> **Skill:** `/Users/mac/Desktop/Downloads/CDMS_Project/.agent/skills/tu_vi_luan_giai/SKILL.md`
> **Quality Gate:** `/Users/mac/Desktop/Downloads/Luan giai tu vi by BS Long/.agent/quality_gate.md`

---

## BƯỚC 1: DATA INVENTORY (Kiểm kê dữ liệu)

1. Mở Source of Truth: `.agent/source_of_truth/la_so_[ten]_[nam].md`
2. Xác nhận: Ngày sinh, Giờ sinh, Ngũ Cục, Can Chi, Giới tính
3. Liệt kê 12 cung: Chính tinh + Phụ tinh + Sát tinh + Tuần/Triệt
4. Format bảng:
   ```
   | Cung | Chi | Hành | Chính Tinh (Trạng thái) | Phụ Tinh | Sát Tinh | Tuần/Triệt |
   ```
5. **Checkpoint:** Bảng 12 cung đầy đủ ≥ 90% sao → PASS

---

## BƯỚC 2: CHÍNH TINH ANALYSIS (Phân tích đa phái)

1. Đọc SKILL.md Section II (Quy trình luận giải 1 cung)
2. Với MỖI bộ chính tinh (8 bộ):
   - Bảng trạng thái đa phái (3 dòng: Trung Châu/Nam/Bắc)
   - Bảng Ngũ Hành (2-3 cơ chế sao vs cung)
   - Bảng Phú cổ (2-3 phú + nguồn + giải nghĩa)
   - So sánh vị trí (vị trí hiện tại vs vị trí tối ưu/xấu nhất)
   - Đặc thù lá số (áp dụng cụ thể)
   - Expert quote (1 trích dẫn có nguồn)
3. **Perplexity verification:** Ít nhất 2 queries/bộ chính tinh, kèm citations
4. **Checkpoint:** 8/8 bộ chính tinh đều có ≥ 5/6 tiêu chí → PASS

---

## BƯỚC 3: PHỤ TINH ANALYSIS (5 nhóm)

1. Chia 5 nhóm (theo PHẦN I-TER template):
   - Nhóm 1: Tứ Hóa (4 sao)
   - Nhóm 2: Lục Sát (6 sao)
   - Nhóm 3: Lục Cát Phụ (6 sao)
   - Nhóm 4: Lộc/Mã/Đào Hoa (4 sao)
   - Nhóm 5: Hình/Riêu/Cô + Tiểu Tinh (5+ sao)
2. Mỗi sao cần:
   - Trạng thái (Miếu/Vượng/Đắc/Bình/Hãm)
   - Ngũ Hành mechanism (sao vs cung)
   - Phú cổ (≥1 phú + nguồn)
   - Cách cục liên quan (nếu có)
   - Áp dụng lá số cụ thể
3. Kết thúc bằng bảng tổng kết: # cát vs # hung + tỷ lệ %
4. **Checkpoint:** ≥ 20 phụ tinh, mỗi sao ≥ 4/5 tiêu chí → PASS

---

## BƯỚC 4: CÁCH CỤC AUDIT (Registry 19+)

1. Scan tất cả cách cục chính thống có thể hình thành:
   - Đối chiếu: lichngaytot.com, tuvivietnam.vn, lyso.vn
   - Kiểm tra từng cách: điều kiện, thỏa mãn?, phú gốc, nguồn
2. Phân loại: Cát / Trung / Hung
3. Chấm điểm mỗi cách (1-10)
4. Bảng tổng hợp: # cách cục, NET score
5. **Checkpoint:** ≥ 15 cách cục, mỗi cách có phú + nguồn → PASS

---

## BƯỚC 5: ĐẠI VẬN DEEP DIVE

1. Bảng tổng quan 10 đại vận (tuổi, cung, tinh bàn, nhận định)
2. Deep dive ĐẠI VẬN HIỆN TẠI (6 subsections):
   a. Tinh bàn ĐV (bảng sao + trạng thái + vai trò)
   b. Ngũ Hành ĐV vs Bản Mệnh (bảng 4 tương tác)
   c. Triệt Không Động Lực Học (bảng 3 giai đoạn)
   d. So sánh ĐV trước ↔ ĐV hiện tại (bảng 7 tiêu chí)
   e. Tứ Hóa Lưu Niên trong ĐV (bảng 4 hóa)
   f. Chiến lược (bảng 3 giai đoạn + hành động + cảnh báo)
3. **Checkpoint:** ĐV hiện tại có đủ 6 subsections → PASS

---

## BƯỚC 6: QUALITY GATE VERIFICATION

1. Chạy quality gate checklist (xem file `.agent/quality_gate.md`)
2. Mọi mục PHẢI PASS
3. Nếu FAIL → quay lại bước tương ứng, sửa, re-verify
4. **Output:** Stamp `✅ QG PASS [ngày] [version]` cuối file

---

## BƯỚC 7: FILE EXPORT + BACKUP

1. File output chính: `02_luan_giai/luan_giai_toan_dien_[ten]_[nam].md`
2. Backup checklist:
   - [ ] File tại local: `Luan giai tu vi by BS Long/`
   - [ ] Google Drive: auto-sync (GDrive folder)
   - [ ] Git commit: `git add . && git commit -m "TVDS: [ten] v[x.y] — [mô tả]"`
3. Notify user kèm:
   - Số dòng output
   - Quality gate result
   - Danh sách files modified

---

## TRIGGERS
- Khi user yêu cầu "luận giải tử vi", "phân tích lá số", "tu vi analysis"
- Khi user gõ `/tu-vi-analysis`
