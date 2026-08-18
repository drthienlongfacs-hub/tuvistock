# 05_ck_analysis — Phân Tích CK × Tử Vi

> **Navigator:** Xem `../../README.md` cho toàn workspace

## Thư mục

| Folder | Nội dung | Files |
|---|---|:---:|
| `analysis/` | Framework, QA/QC, benchmark, error registry | 12 |
| `monthly_updates/` | Snapshots CK hàng ngày/tuần | 8 |
| `sot/` | SOT filings corporate actions đã verify | 2 |
| `tools/` | market_data_pipeline.py (❌ broken RCA-043) | 1 |

## Files quan trọng

| File | Mục đích | Status |
|---|---|---|
| `analysis/QA_QC_ENTERPRISE_STANDARD.md` | 5 cổng QA/QC (E0-E5) | ✅ Active |
| `analysis/benchmark_reference_catalog.json` | Nguồn dữ liệu verified (15 entries) | ✅ Active v1.1 |
| `analysis/error_registry.md` | 9 anti-patterns + ERR codes | ✅ Active |
| `analysis/multi_factor_calibration_v2.md` | 8-framework scoring P-6 | ✅ Active |
| `monthly_updates/2026_04_update_01apr.md` | Latest update | ✅ Active |

## Workflow lấy số liệu

**→ Dùng workflow:** `.agent/workflows/market-data-fetch.md`
**→ KHÔNG dùng:** `tools/market_data_pipeline.py` (RCA-043: API fail)
