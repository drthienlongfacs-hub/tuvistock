---
description: Tạo bản luận giải Tử Vi toàn diện từ ảnh lá số — 7 phase, QA gate, chuẩn v4.5
---

# /generate-luan-giai — Workflow Tạo Luận Giải Tử Vi Toàn Diện

> **Skill:** `.agent/skills/tu_vi_luan_giai/SKILL.md`
> **Bảng tra:** `.agent/skills/tu_vi_luan_giai/reference_tables.md`
> **Văn phong:** `.agent/skills/tu_vi_luan_giai/writing_style_guide.md`

---

## PRE-FLIGHT

// turbo
1. Đọc SKILL.md để nắm pipeline 7 phase
// turbo
2. Đọc reference_tables.md để có bảng tra sẵn
// turbo
3. Đọc writing_style_guide.md để biết chuẩn văn phong

---

## PHASE 1: DATA INTAKE

4. User cung cấp ảnh lá số (hoặc tinh bàn văn bản)
5. Extract từ ảnh: 12 cung, tất cả sao, trạng thái, Tuần/Triệt
6. Xác định: Năm sinh Can Chi, Cục, Nạp Âm, Tứ Hóa
7. Build SSoT Table (12 cung × sao × trạng thái)
8. **VERIFY SSoT:** Cross-check Tứ Hóa, Tuần/Triệt, Tràng Sinh vs reference_tables.md
9. **CHECKPOINT:** Trình user duyệt SSoT Table trước khi tiếp

---

## PHASE 2: FOUNDATION

10. Viết PHẦN I: Nền Tảng Mệnh (Ngũ Hành, Âm Dương, Mệnh-Thân)
11. Viết PHẦN II: 6 Chiều Tương Tác Mệnh (40-30-20-10-5%)
12. Viết PHẦN III: 4 Tam Hợp + Tràng Sinh 12 giai đoạn
13. Viết PHẦN IV: 12 Cách Cục (verify phú cổ từ reference_tables.md)
14. Viết PHẦN V: 4 Cung Trọng Yếu + Bảng Nội Hàm 12 cung
15. **QA Mini:** Verify Can Chi, Tứ Hóa, Tràng Sinh trong nội dung vừa viết

---

## PHASE 3: DEEP ANALYSIS

16. Viết PHẦN VI: 12 Cung × 5 Chiều — theo thứ tự:
    - Mệnh → Phúc/Thân → Thiên Di → Nô Bộc → Quan Lộc
    - → Điền Trạch → Phụ Mẫu → Tật Ách → Tài Bạch
    - → Tử Tức → Phu Thê → Huynh Đệ

> Mỗi cung PHẢI tuân thủ template từ SKILL.md Phase 3:
> - Headline ví von + 5 chiều chi tiết + bảng NET + expert quote

17. Viết PHẦN VII: Tứ Hóa Chuỗi Nhân Quả
18. **QA Mini:** Verify tổng cát/hung nhất quán, không mâu thuẫn giữa cung

---

## PHASE 4: TEMPORAL (Tùy chọn — nếu user yêu cầu năm cụ thể)

19. Viết PHẦN VIII-A: Đại Vận Blueprint (10 thập kỷ)
20. Viết PHẦN VIII-B: Tuần-Triệt Dynamics xuyên Đại Vận
21. Viết PHẦN VIII-C: Lưu Niên cụ thể:
    - Bát Tự năm + Kinh Dịch quẻ (Perplexity verify)
    - Tứ Hóa Lưu Niên + Lưu Tinh
    - Tiểu Hạn
    - 12 Tháng Phi Tinh Lưu Nguyệt (template từ SKILL.md)
22. **QA Mini:** Verify Can Chi tháng vs reference_tables.md mục 1

---

## PHASE 5: MULTI-DIMENSIONAL

23. Viết PHẦN IX: 7 Trục (Nhân Sinh, Nhân Tính, Nhân Tướng, Nhân Quả, Bối Cảnh, Nhân Duyên, Quy Luật)
24. Sử dụng Perplexity MCP để verify khoa học (Big Five, Taleb, Darwin)

---

## PHASE 6: SYNTHESIS

25. Viết PHẦN X: Cẩm Nang Hành Động (bảng thực tiễn)
26. Viết Kết luận (1 đoạn ví von kết thúc, phải xúc động)
27. Viết Nguồn Tư Liệu Tham Khảo (bảng đầy đủ)

---

## PHASE 7: QA GATE + EXPORT

28. Chạy QA Gate 3 tầng (SKILL.md Section 10):
    - Tầng 1: Data Accuracy (Can Chi, Tứ Hóa, Tràng Sinh, Phú cổ)
    - Tầng 2: Analysis Consistency (12 cung NET, Đại Vận logic)
    - Tầng 3: Writing Quality (ví von, quote, Ngũ Hành, văn phong)
29. Fix mọi lỗi phát hiện
30. Tạo QA Report
31. **CHECKPOINT:** Trình user duyệt bản hoàn chỉnh
32. Backup file output

---

## RECOVERY

Nếu mất file hoặc conversation bị cắt:
1. Tìm file `.md` đã lưu trong cùng folder
2. SSoT Table là nguồn khôi phục quan trọng nhất
3. Re-run từ Phase bị gián đoạn, KHÔNG cần bắt đầu lại từ đầu
4. reference_tables.md luôn tồn tại trong skill folder → sử dụng lại
