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
| `monthly_updates/2026_03_initial.md` | v1 | 14/03/2026 | Báo cáo phân tích đầu tiên |

## Quy tắc
1. Mọi file phải có version + ngày
2. Không xóa file cũ — rename thành `_archived_YYYYMMDD`
3. SOT files phải có checksums
4. Drive sync tự động qua Google Drive
