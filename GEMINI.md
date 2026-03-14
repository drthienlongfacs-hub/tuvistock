# TuViStock Workspace — GEMINI.md

> **Workspace**: TuViStock — Phân tích CK × Tử Vi
> **GitHub**: [drthienlongfacs-hub/tuvistock](https://github.com/drthienlongfacs-hub/tuvistock)
> **Tách riêng**: KHÔNG liên quan CDMS_Project

## Mục đích
Workspace độc lập chuyên về phân tích chứng khoán (CK/CW) kết hợp Tử Vi Đẩu Số.
Bao gồm: tinh bàn inventory, luận giải toàn diện, lý thuyết phương pháp, và hệ thống phân tích CK.

## Cấu trúc

```
TuViStock/
├── .agent/                     # Agent system (skills, rules, workflows, SOT)
│   ├── skills/
│   │   ├── ck_tuvi_analysis/   # ⭐ CK Analysis × Tử Vi skill
│   │   └── tu_vi_luan_giai/    # Tử Vi luận giải skill
│   ├── rules/tu_vi_rules.md    # Rules v4.0 (12 base + 5 CK rules)
│   ├── workflows/
│   │   ├── ck-tuvi-forecast.md # ⭐ SOP 7 bước phân tích CK
│   │   └── tu-vi-analysis.md   # Workflow luận giải Tử Vi
│   ├── source_of_truth/        # SOT tinh bàn gốc
│   └── quality_gate.md         # Quality gate chung
├── 01_data_inventory/          # Kiểm kê tinh bàn (9 lá số)
├── 02_luan_giai/               # Luận giải toàn diện + NOVEL
├── 03_cach_cuc/                # Cách cục kiểm chứng
├── 04_ly_thuyet/               # Lý thuyết phương pháp
├── 05_ck_analysis/             # ⭐ Phân tích CK × Tử Vi
│   ├── sot/                    # Source of Truth filings đã verify
│   ├── analysis/               # Framework v4, error registry
│   └── monthly_updates/        # Cập nhật hàng tháng
└── GEMINI.md                   # (file này)
```

## Quy tắc quan trọng

1. **Framework 3 Tầng CK** (xem `.agent/skills/ck_tuvi_analysis/SKILL.md`):
   - T1 Quy định cứng ⭐⭐⭐ → Cơ sở quyết định
   - T2 Cầu cơ học ⭐⭐ → Có thật nhưng giới hạn
   - T3 Narrative ⭐ → Đọc tâm lý, KHÔNG đặt lệnh

2. **9 Anti-patterns** (xem `05_ck_analysis/analysis/error_registry.md`):
   - ERR-008: Margin call = ép GIẢM, không ép TĂNG
   - ERR-009: Score = ước tính, không xác thực

3. **Rules R-CK1→R-CK5** (xem `.agent/rules/tu_vi_rules.md`):
   - R-CK1: Source link bắt buộc
   - R-CK2: Không "BẮT BUỘC" cho T3
   - R-CK3: ĐV phải check trước khi luận
   - R-CK4: M7 = ép giảm
   - R-CK5: Score ghi "ước tính" vs "xác thực"

4. **Git workflow**: Commit + push sau mỗi milestone lớn

## Backup
- **Local**: Folder này trên Desktop
- **GitHub**: `drthienlongfacs-hub/tuvistock` (main branch)
- **Drive**: Original data tại `~/Desktop/Downloads/Luan giai tu vi by BS Long/` (auto-sync)
