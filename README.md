# 📚 Luận Giải Tử Vi Đẩu Số — BS Long 2026

> **Version:** 5.0 | **Updated:** 14/03/2026
> **Đương số:** Lê Trọng Thiên Long | **Nhâm Thân 1992** | Dương Nam | Kim Tứ Cục

---

## 📁 CẤU TRÚC THƯ MỤC (Tự chứa — Self-contained)

```
Luan giai tu vi by BS Long/
├── .agent/                          ← 🔧 HỆ THỐNG SOP/SKILL/RULE
│   ├── quality_gate.md              ← QG 35+ items, 6 categories (A-F)
│   ├── rules/
│   │   └── tu_vi_rules.md           ← Quy tắc chống sai (11KB)
│   ├── skills/
│   │   └── tu_vi_luan_giai/
│   │       ├── SKILL.md             ← SKILL v5.0 (737 dòng, 20 sections)
│   │       └── SKILL.docx           ← Bản DOCX (backup)
│   ├── source_of_truth/
│   │   ├── la_so_long_2026.md       ← SOT tinh bàn 12 cung
│   │   └── la_so_long_2026.docx     ← SOT bản DOCX
│   └── workflows/
│       └── tu-vi-analysis.md        ← SOP 7 bước end-to-end
│
├── 01_data_inventory/               ← 📊 DỮ LIỆU GỐC (9 tinh bàn)
│   ├── kiem_ke_tinh_ban_12_cung.md  ← Long: master 12 cung
│   ├── kiem_ke_tinh_ban_an.md       ← An
│   ├── kiem_ke_tinh_ban_ba.md       ← Bà
│   ├── kiem_ke_tinh_ban_ca_rot.md   ← Cà Rốt
│   ├── kiem_ke_tinh_ban_hy.md       ← Hy
│   ├── kiem_ke_tinh_ban_kim.md      ← Kim
│   ├── kiem_ke_tinh_ban_luong_2026.md ← Lương
│   ├── kiem_ke_tinh_ban_thai_2026.md  ← Thái
│   └── kiem_ke_tinh_ban_uyen_anh.md   ← Uyên Anh
│
├── 02_luan_giai/                    ← 📝 OUTPUT CHÍNH (65 files)
│   └── luan_giai_toan_dien_long_2026.md ← Master: ~2600 dòng, 10+ PHẦN
│
├── 03_cach_cuc/                     ← 🎯 CÁCH CỤC CHÍNH THỐNG
│   └── cach_cuc_chinh_thong.md      ← 19 cách đã kiểm chứng
│
├── 04_ly_thuyet/                    ← 📚 LÝ THUYẾT NỀN
│   ├── ra_soat_5_chieu_tuong_tac.md ← Thang đo 5 chiều (14KB)
│   └── menh_dep_nhat_7_truc.md      ← Ma trận 7 trục SSoT
│
└── README.md                        ← File này
```

> **✅ Self-contained:** Folder này chứa ĐẦY ĐỦ mọi thứ cần cho luận giải Tử Vi — không cần tham chiếu folder khác.

## 🛡️ HỆ THỐNG SOP/SKILL/WORKFLOW

| Thành phần | Vị trí | Mô tả |
|---|---|---|
| **SKILL.md v5.0** | `CDMS_Project/.agent/skills/tu_vi_luan_giai/SKILL.md` | 20 sections, 700+ dòng — phương pháp luận giải |
| **Workflow** | `.agent/workflows/tu-vi-analysis.md` | SOP 7 bước end-to-end |
| **Quality Gate** | `.agent/quality_gate.md` | 35+ checkpoints, 6 categories |
| **SOT Tinh bàn** | `.agent/source_of_truth/la_so_long_2026.md` | Ground truth 12 cung |

## 📊 ASSET REGISTRY — Output Files

| File | Dòng | Nội dung | Version |
|---|:---:|---|---|
| `luan_giai_toan_dien_long_2026.md` | ~2600 | 10+ PHẦN toàn diện | v5.0 |

### Các PHẦN trong output chính:

| PHẦN | Nội dung | Dòng ~approx |
|:---:|---|:---:|
| I | Nền tảng Mệnh — Cốt cách | 55 |
| I-BIS | Chính Tinh Deep Analysis (8 bộ, đa phái) | 330 |
| I-TER | Phụ Tinh Deep Analysis (5 nhóm, 27 sao) | 108 |
| II | 6 Chiều Tương Tác — Mệnh Thiên Phủ Hợi | 300 |
| III | Tràng Sinh 12 Cung | 100 |
| IV | Cách Cục (19 cách, NET +61) | 160 |
| V | 4 Cung Trọng Yếu | 200 |
| V-B | Nội Hàm 12 Cung | 50 |
| VI | Hung/Sát + Tuần-Triệt 12 Cung | 400 |
| VII | Tứ Hóa Chuỗi (Can Nhâm) | 50 |
| VIII | Đại Vận Blueprint + Deep ĐV4 | 160 |
| VIII-A | Tuần Triệt Động Lực Học | 100 |
| VIII-B | Lưu Niên 2026 Bính Ngọ | 300 |
| IX | 7 Trục Đa Chiều | 100 |
| X | Cẩm Nang Hành Động | 50 |

## 🔄 BACKUP STRATEGY

| Tầng | Vị trí | Phương thức |
|---|---|---|
| **Local** | Mac Mini / MBP | File system trực tiếp |
| **Cloud** | Google Drive | GDrive auto-sync (thư mục Downloads) |
| **VCS** | GitHub (nếu có) | `git commit` manual |
| **CDMS** | Document Library | Metadata seeding (nếu cần) |

## 📝 VERSION HISTORY

| Version | Ngày | Thay đổi |
|---|---|---|
| 1.0 | 25/02/2026 | Initial: Mệnh + Thân analysis |
| 2.0 | 27/02/2026 | SKILL v4.0: 16 sections |
| 3.0 | 13/03/2026 | DeepDive: Phu Thê, Tài, Ách, Tràng Sinh |
| 4.0 | 13/03/2026 | Lưu Niên 12 tháng, 7 Trục |
| **5.0** | **14/03/2026** | **Chính tinh đa phái + Phụ tinh 27 sao + Cách cục 19 + ĐV4 deep + SOP system** |
