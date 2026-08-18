# .agent — Agent System Config

> **Navigator:** Xem `../README.md` cho toàn workspace

## Thư mục

| Folder | Nội dung | Status |
|---|---|---|
| `rules/tu_vi_rules.md` | ⭐ Rules v6.5 — TẤT CẢ rules ở đây | ✅ Active |
| `rules/tu_vi_rules.md` chứa: | R1-R12 (base), R-CK1→8 (CK), P1-P6 (patterns), QT1-13 (market) | |
| `skills/` | 3 skills: ck_tuvi, giai_than, tu_vi_luan_giai | ✅ Active |
| `source_of_truth/` | 4 files: lá số gốc (md+docx), cách cục, checksums | 🔒 Read-Only |
| `workflows/` | 4 SOPs: backup, ck-forecast, market-data, tu-vi | ✅ Active |
| `quality_gate.md` | Quality gate tiêu chí | ✅ Active |

## Quy tắc

- **KHÔNG tạo file rules mới** — thêm vào `tu_vi_rules.md` duy nhất
- **KHÔNG copy SOT** — luôn đọc từ `source_of_truth/`
- **Workflows** là SOP chuẩn — agent tự động dùng khi trigger đúng
