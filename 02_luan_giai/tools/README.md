# 02_luan_giai/tools — Scripts Luận Giải

> **Navigator:** Xem `../../../README.md` cho toàn workspace

## 27 Files — Phân loại

### ✅ Active (dùng thường xuyên)
| File | Mục đích |
|---|---|
| `tuvi_engine.py` | Engine chính xử lý Tử Vi (44KB) |
| `injection_guard.py` | Idempotent injection — DÙNG THẾ CHO inject_*.py |
| `market_reality_check.py` | Kiểm tra claim CK vs thực tế |
| `market_qaqc_validator.py` | Validate QA/QC gate |
| `deep_impact_v4_part1.py` | Deep impact analysis |
| `hoa_ky_guardrails.py` | Hóa Kỵ safety check |

### 🟡 Legacy (giữ tham khảo, KHÔNG chạy trực tiếp)
| File | Thay thế bởi |
|---|---|
| `inject_deep_20x_t1.py` → `inject_deep_20x_t11t12.py` (8 files) | `injection_guard.py` |
| `inject_deep_story.py` | `injection_guard.py` |
| `inject_human_readable.py` | `injection_guard.py` |
| `inject_multi_layer.py` → `inject_multi_layer_v3_sot.py` (3 files) | `injection_guard.py` |
| `inject_sot_scores.py` | `injection_guard.py` |
| `inject_classic_theory.py` | `injection_guard.py` |
| `upgrade_7_chieu.py` + `v2.py` | Đã chạy xong |
| `upgrade_luan_giai_tables.py` | Đã chạy xong |
| `fixer_script.py` | One-time fix |
| `dedup_luan_giai.py` | Maintenance script |
| `apply_hoa_ky_guardrails.py` | Wrapper cho hoa_ky_guardrails |

## ⚠️ CẢNH BÁO (RCA-043)
- **KHÔNG chạy Python scripts trên Desktop GDrive path** — có thể treo
- Nếu cần chạy: copy script vào `/tmp/` trước
