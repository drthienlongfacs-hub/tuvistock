# TuViStock Workspace — GEMINI.md

> **Workspace**: TuViStock — Phân tích CK × Tử Vi
> **GitHub**: [drthienlongfacs-hub/tuvistock](https://github.com/drthienlongfacs-hub/tuvistock)
> **Tách riêng**: KHÔNG liên quan CDMS_Project
> **Updated**: 02/04/2026 — RCA-043 data pipeline, QT-1→13, README system

## ⭐ BƯỚC ĐẦU TIÊN MỖI SESSION

1. **ĐỌC `README.md`** (workspace root) → biết file nào ở đâu, tránh tạo trùng
2. **ĐỌC `tu_vi_rules.md`** → biết rules hiện hành (R, R-CK, P, QT)
3. **Dùng `read_url_content`** khi cần số liệu CK (KHÔNG dùng API/shell)

## Mục đích

Workspace độc lập chuyên về phân tích chứng khoán (CK/CW) kết hợp Tử Vi Đẩu Số.

## Cấu trúc (xem `README.md` root cho chi tiết đầy đủ)

```
TuViStock/
├── README.md                    # ⭐ WORKSPACE NAVIGATOR — đọc đầu tiên
├── .agent/
│   ├── README.md                # Agent config guide
│   ├── rules/tu_vi_rules.md     # ⭐ Rules v6.5 (R, R-CK, P, QT)
│   ├── skills/ (3)              # ck_tuvi, giai_than, tu_vi_luan_giai
│   ├── workflows/ (4)           # backup, ck-forecast, market-data-fetch, tu-vi
│   ├── source_of_truth/ (4)     # 🔒 SOT gốc — KHÔNG copy
│   └── quality_gate.md
├── 01_data_inventory/ (9)       # Kiểm kê tinh bàn 9 lá số
├── 02_luan_giai/
│   ├── core/                    # ⭐ Luận giải 12 tháng 2026 (SOT chính)
│   ├── tools/
│   │   ├── README.md            # Phân loại 27 scripts Active vs Legacy
│   │   ├── tuvi_engine.py       # ✅ Active: Engine chính
│   │   ├── injection_guard.py   # ✅ Active: Thay thế inject_*.py
│   │   └── inject_*.py          # 🟡 Legacy: 12 files giữ archive
│   └── persons|novel|topics|export
├── 03_cach_cuc/ (2)
├── 04_ly_thuyet/ (12)           # Kinh điển, GiaiThan, methodology
├── 05_ck_analysis/
│   ├── README.md                # CK analysis guide
│   ├── analysis/ (12)           # QA/QC, benchmark, errors, multi-factor
│   ├── monthly_updates/ (8)     # Daily/weekly snapshots
│   └── sot/ (2)                 # Corporate action filings
└── 05_ung_dung/ (2)             # Ứng dụng khác (Tiếng Anh Cà Rốt)
```

## Quy tắc quan trọng

### 1. Data Pipeline (RCA-043, 02/04/2026)
- ✅ Dùng `read_url_content` CafeF stock page → OG tag
- ❌ KHÔNG dùng API (CafeF/TCBS/SSI/VND — tất cả fail)
- ❌ KHÔNG chạy shell commands trên Desktop GDrive path
- **Workflow:** `.agent/workflows/market-data-fetch.md`

### 2. Framework 3 Tầng CK
- T1 Quy định cứng ⭐⭐⭐ → Cơ sở quyết định
- T2 Cầu cơ học ⭐⭐ → Có thật nhưng giới hạn
- T3 Narrative ⭐ → Đọc tâm lý, KHÔNG đặt lệnh
- **Skill:** `.agent/skills/ck_tuvi_analysis/SKILL.md`

### 3. Rules tổng hợp (v6.5)
- **R1→R12**: 12 base rules Tử Vi
- **R-CK1→R-CK8**: 8 rules CK (source link, score ghi ước tính, giá trực tiếp)
- **P1→P6**: 6 patterns (Tử Phá, Tràng Sinh, Tứ Mộ, Multi-factor 8 khung)
- **QT-1→QT-13**: 13 quy tắc vận động thị trường (Wyckoff, MM, data pipeline)
- **File:** `.agent/rules/tu_vi_rules.md`

### 4. QA/QC Enterprise (5 gates)
- E0: Schema | E1: Benchmark tier | E2: Regime separation
- E3: Report sections | E4: QG compliance | **E5: Data pipeline integrity**
- **File:** `05_ck_analysis/analysis/QA_QC_ENTERPRISE_STANDARD.md`

### 5. KHÔNG tạo trùng (xem README.md root → "KHÔNG TẠO")
- 1 file rules duy nhất: `tu_vi_rules.md`
- 1 file benchmark: `benchmark_reference_catalog.json`
- 1 file QA/QC: `QA_QC_ENTERPRISE_STANDARD.md`
- 1 file SOT lá số: `la_so_long_2026.md`

### 6. Git (GDrive constraint)
- Git commands CÓ THỂ TREO trên Desktop GDrive path
- User push thủ công từ Terminal khi cần
- Agent KHÔNG chạy `git` trên path này

## Backup
- **Local**: Folder này trên Desktop (GDrive synced)
- **GitHub**: `drthienlongfacs-hub/tuvistock` (main branch)
- **Drive**: Original data tại `~/Desktop/Downloads/Luan giai tu vi by BS Long/`
