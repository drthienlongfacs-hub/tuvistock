# 05_ck_analysis — Phân Tích CK × Tử Vi

> **Tạo**: 14/03/2026
> **Mục đích**: Lưu trữ có hệ thống toàn bộ phân tích chứng khoán kết hợp Tử Vi
> **Tách riêng**: KHÔNG chung với CDMS_Project

## Cấu trúc thư mục

```
05_ck_analysis/
├── README.md                 ← (file này)
├── sot/                      ← Source of Truth — filings đã verify
│   ├── shb_filings_2026.md
│   ├── vtse_regulations_2026.md
│   └── CHECKSUMS.sha256
├── analysis/                 ← Bài phân tích đã thẩm định
│   ├── forced_catalyst_v4.md
│   └── error_registry.md
└── monthly_updates/          ← Cập nhật hàng tháng
    └── 2026_03_initial.md
```

## Index — Files hiện có

| File | Version | Ngày | Mô tả |
|---|---|---|---|
| `sot/shb_filings_2026.md` | v1 | 14/03/2026 | NQ tăng vốn SHB, rights issue, ESOP |
| `sot/vtse_regulations_2026.md` | v1 | 14/03/2026 | Circular 08, FTSE timeline, KRX |
| `analysis/forced_catalyst_v4.md` | v4 | 14/03/2026 | Framework 3 tầng đã thẩm định |
| `analysis/error_registry.md` | v1 | 14/03/2026 | 9 lỗi đã phát hiện |
| `analysis/QA_QC_ENTERPRISE_STANDARD.md` | **v1** | **29/03/2026** | **Chuẩn QA/QC enterprise + gate levels + reject conditions** |
| `analysis/benchmark_reference_catalog.json` | **v1** | **29/03/2026** | **Catalog benchmark machine-readable cho benchmark tiers** |
| `analysis/market_reality_registry_2026.json` | **v1** | **29/03/2026** | **Registry outcome audit máy đọc được** |
| `analysis/market_reality_check_2026.md` | **v1** | **29/03/2026** | **Reality-check T2 âm: broad market vs basket vs catalyst** |
| `analysis/market_qaqc_validator_report.md` | **v1** | **29/03/2026** | **Báo cáo validator QA/QC enterprise** |
| `monthly_updates/2026_03_initial.md` | v1 | 14/03/2026 | Báo cáo phân tích đầu tiên |
| `monthly_updates/2026_03_snapshot_13mar.md` | v1 | 13/03/2026 | Snapshot thị trường giữa tháng |
| `monthly_updates/2026_03_snapshot_27mar.md` | v3 | 27/03/2026 | Snapshot multi-channel verified (Vietstock browser) |
| `monthly_updates/2026_03_snapshot_28mar.md` | **v4** | **28/03/2026** | **Full system: browser prices + 3-Tier + 9 Anti-patterns + events calendar** |

## Quy tắc
1. Mọi file phải có version + ngày
2. Không xóa file cũ — rename thành `_archived_YYYYMMDD`
3. SOT files phải có checksums
4. Drive sync tự động qua Google Drive
5. Reality-check enterprise phải pass `market_qaqc_validator.py` trước khi coi là artifact chuẩn đối sánh
