---
description: Quy trình phân tích CK/CW kết hợp Tử Vi — 7 bước chuẩn hóa, thẩm định 4 cột, tách 3 tầng. Trigger khi cần dự báo CK, đánh giá forced catalyst, hoặc giao thoa lá số × macro.
---

# Workflow: CK-TuVi Forecast

## Điều kiện tiên quyết
- Đã có tinh bàn trong `01_data_inventory/`
- Đã có luận giải trong `02_luan_giai/`
- Kết nối internet (cho Perplexity research)

## 7 Bước

### Bước 1: Xác minh lá số
// turbo
```
Đọc SOT tinh bàn → xác định:
- Cung Tài Bạch: sao nào, vượng/hãm
- Đại Vận hiện tại: cung nào (KHÔNG được giả định)
- Tiểu Hạn: cung nào
- Lưu Niên: Lưu Lộc Tồn, Lưu Thiên Mã, Tuần/Triệt
- Nguyệt Hạn cho từng tháng AL
```

### Bước 2: Research macro (Perplexity)
```
Search verified events:
- Capital raise plans (T1: filing DN)
- FTSE/MSCI timeline (T1: regulatory)
- ETF rebalancing dates (T2: cầu cơ học)
- Analyst reports (T3: narrative — ghi rõ T3)
```

### Bước 3: Xác minh forced catalysts
```
CHỈ xét T1 + T2:
- T1: NQ HĐQT, UBCKNN filing, Circular
- T2: ETF weight changes, CW hedge, foreign room
- T3: Ghi nhận NHƯNG KHÔNG dùng để quyết direction
```

### Bước 4: Giao thoa lá số × macro
```
Map nguyệt hạn (tháng AL) với:
- Mốc T1 đã xác thực (filing dates)
- Mốc T2 tiềm năng (FTSE, rebalance)
Output: bảng 12 tháng × catalyst × nguyệt hạn
```

### Bước 5: Thẩm định 4 cột
```
MỖI mệnh đề → xếp loại:
| Đúng | Đúng một phần | Chưa xác thực | Sai |

CHECK 9 anti-patterns:
□ AGM 21 ngày (không 10)
□ Insider 3 ngày GD (không 24h)
□ Heuristic ≠ rule (❌3,4)
□ Volume ≠ direction (❌5)
□ Basis ≠ proof (❌6)
□ Floor ≠ đảm bảo (❌7)
□ M7 = ép GIẢM (❌8)
□ Score = ước tính (❌9)
□ T3 không "BẮT BUỘC" (rule R-CK2)
```

### Bước 6: Output
```
Ghi file với:
- Version number (v1, v2, v3...)
- Ngày thẩm định
- Đính chính rõ nếu sửa từ version trước
- Bảng 4 cột cho mọi mệnh đề
- Source links cho mọi con số/mốc
```

### Bước 7: Backup
```
1. Copy output → 05_ck_analysis/monthly_updates/YYYY_MM_xxx.md
2. Update 05_ck_analysis/README.md index
3. Drive sync tự động (folder đã trên GDrive)
4. Push GitHub nếu milestone lớn: branch ck-analysis-2026
```

## Quality Gate — PASS/FAIL
- FAIL nếu: bất kỳ mệnh đề T3 nào dùng "BẮT BUỘC/CHẮC CHẮN"
- FAIL nếu: score không ghi "ước tính" vs "xác thực"
- FAIL nếu: bất kỳ anti-pattern nào trong 9 lỗi bị vi phạm
- FAIL nếu: không có source link cho con số/mốc
- PASS: tất cả điều kiện trên đều OK → ghi "✅ QG-CK PASS [ngày]"
