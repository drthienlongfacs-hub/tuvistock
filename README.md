# TuViStock — Workspace Navigator
> **Purpose:** Giúp Antigravity agent nhanh chóng tìm đúng file, tránh trùng lặp.
> **Updated:** 02/04/2026 | v1.0

## 📁 CẤU TRÚC THƯ MỤC

```
TuViStock/
├── .agent/                      # ⚙️ Agent system config
│   ├── rules/tu_vi_rules.md     # 📏 Rules v6.5 (R1-R12, R-CK1→8, P1-P6, QT1-13)
│   ├── skills/                  # 🧠 3 skills (ck_tuvi, giai_than, tu_vi_luan_giai)
│   ├── source_of_truth/         # 🔒 SOT: lá số gốc, cách cục, checksums
│   ├── workflows/               # 📋 4 SOPs (backup, ck-forecast, market-data, tu-vi)
│   └── quality_gate.md          # ✅ Quality gate tiêu chí
│
├── 01_data_inventory/           # 📊 Kiểm kê tinh bàn (9 lá số)
│   └── kiem_ke_tinh_ban_*.md    # ← SOT data cho từng người
│
├── 02_luan_giai/                # 📝 Luận giải chính
│   ├── core/                    # ← Luận giải 12 tháng 2026 (SOT chính)
│   ├── persons/                 # ← Luận giải theo từng người
│   ├── novel/                   # ← Tiểu thuyết Tử Vi
│   ├── tools/                   # ← Python scripts (27 files, xem NOTE)
│   ├── scripts/                 # ← Scripts phụ trợ
│   ├── topics/                  # ← Chủ đề chuyên sâu
│   └── export/                  # ← Files xuất (DOCX/PDF)
│
├── 03_cach_cuc/                 # 🏛️ Cách cục kiểm chứng (2 files)
│
├── 04_ly_thuyet/                # 📚 Lý thuyết phương pháp (12 files)
│   └── *.md                     # ← Kinh điển, GiaiThan, Hồng Phi Mộ...
│
├── 05_ck_analysis/              # 📈 Phân tích CK × Tử Vi
│   ├── analysis/                # ← Framework, QA/QC, benchmark (12 files)
│   ├── monthly_updates/         # ← Snapshots hàng ngày/tuần (8 files)
│   ├── sot/                     # ← SOT filings đã verify
│   └── tools/                   # ← market_data_pipeline.py
│
├── 05_ung_dung/                 # 🎓 Ứng dụng (không CK) — chứa Tiếng Anh Cà Rốt
│
├── GEMINI.md                    # 🤖 Agent workspace config
├── README.md                    # 📖 README gốc
├── _FEEDBACK_LOG.md             # 📝 Log phản hồi
└── _REGISTRY.md                 # 📋 Registry tổng hợp
```

## 🔑 FILE QUAN TRỌNG NHẤT (đọc trước)

| Priority | File | Mục đích |
|:---:|---|---|
| ⭐1 | `.agent/rules/tu_vi_rules.md` | TẤT CẢ rules (R, R-CK, P, QT) |
| ⭐2 | `.agent/source_of_truth/la_so_long_2026.md` | SOT lá số gốc |
| ⭐3 | `02_luan_giai/core/luan_giai_12_thang_2026.md` | Luận giải 12 tháng (SOT chính) |
| ⭐4 | `05_ck_analysis/analysis/benchmark_reference_catalog.json` | Nguồn dữ liệu CK verified |
| ⭐5 | `05_ck_analysis/analysis/QA_QC_ENTERPRISE_STANDARD.md` | QA/QC 5 cổng (E0-E5) |

## 🔍 TÌM FILE NHANH

| Cần gì | Tìm ở đâu |
|---|---|
| Giá CK real-time | Workflow `market-data-fetch.md` (dùng read_url_content) |
| Rules phân tích CK | `tu_vi_rules.md` → section R-CK1→R-CK8, QT-1→QT-13 |
| Lá số ai đó | `01_data_inventory/kiem_ke_tinh_ban_{ten}.md` |
| Luận giải tháng X | `02_luan_giai/core/luan_giai_12_thang_2026.md` |
| Dữ liệu CK snapshot | `05_ck_analysis/monthly_updates/2026_MM_snapshot_*.md` |
| Error registry | `05_ck_analysis/analysis/error_registry.md` |
| Backtest kết quả | `05_ck_analysis/analysis/backtest_t2_2026.md` |

## ⚠️ LEGACY FILES (có nhưng CẨN TRỌNG khi dùng)

| File | Status | Lý do |
|---|---|---|
| `02_luan_giai/tools/inject_*.py` (12 files) | 🟡 Legacy | Scripts injection cũ, cần migrate sang `injection_guard.py` |
| `02_luan_giai/tools/upgrade_7_chieu*.py` (2 files) | 🟡 Legacy | Đã chạy xong, giữ tham khảo |
| `05_ck_analysis/tools/market_data_pipeline.py` | ❌ Broken | RCA-043: API fail, dùng workflow thay thế |
| `05_ung_dung/` | 🟡 Unrelated | Chứa Tiếng Anh Cà Rốt, không liên quan CK/Tử Vi |

## 🚫 KHÔNG TẠO file mới tại các vị trí sau (tránh trùng):

| Nội dung | File ĐÃ CÓ | KHÔNG tạo thêm |
|---|---|---|
| Rules | `tu_vi_rules.md` | ❌ rules_v2.md, new_rules.md |
| Benchmark | `benchmark_reference_catalog.json` | ❌ benchmark_v2.json |
| QA/QC | `QA_QC_ENTERPRISE_STANDARD.md` | ❌ qaqc_v2.md |
| Lá số SOT | `la_so_long_2026.md` | ❌ Copy ở folder khác |
| Error log | `error_registry.md` | ❌ errors_new.md |

## 📋 DATA PIPELINE (QT-10→13)

**KHÔNG dùng:**
- ❌ Python API scripts (hang)
- ❌ Shell commands trên Desktop path (GDrive hang)
- ❌ vnstock library (SSL fail)

**DÙNG:**
- ✅ `read_url_content` CafeF stock page → OG tag
- ✅ Browser scraping (backup)
- ✅ Perplexity search (news + prices)
