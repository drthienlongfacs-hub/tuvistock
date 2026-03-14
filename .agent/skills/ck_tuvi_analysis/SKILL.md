---
name: CK-TuVi Analysis
description: Phân tích chứng khoán (CK/CW) kết hợp Tử Vi — Framework 3 tầng, 9 anti-patterns, checklist thẩm định. Trigger on "chứng khoán", "CK", "CW", "VN30", "FTSE", "forced catalyst", "cổ phiếu", "chứng quyền".
---

# CK-TuVi Analysis Skill

## Mục đích
Phân tích cổ phiếu và chứng quyền VN30 kết hợp lá số Tử Vi, đảm bảo kết quả **data-driven**, **đã thẩm định**, không overclaim.

## RCA
Skill này sinh ra từ phiên 14/03/2026 khi phát hiện **9 lỗi phân tích nghiêm trọng** (overclaim, sai logic, sai quy định). Mọi phân tích CK PHẢI tuân theo framework dưới đây.

---

## FRAMEWORK 3 TẦNG (v4 — đã thẩm định 2 vòng)

### Tầng 1 — QUY ĐỊNH CỨNG (⭐⭐⭐ Tin cậy cao nhất)
- **Nguồn**: NQ HĐQT, filing HOSE/HNX/UBCKNN, Circular, Luật CK, website DN
- **Ví dụ**: VN30 rebalance dates, Circular 08 hiệu lực, SHB NQ tăng vốn
- **Cách dùng**: CƠ SỞ QUYẾT ĐỊNH CHÍNH. Kiểm chứng được 100%
- **Xếp loại output**: "Đã xác thực" hoặc "Đã công bố"

### Tầng 2 — CẦU CƠ HỌC (⭐⭐ Có thật nhưng giới hạn)
- **Nguồn**: ETF prospectus, CW issuance data, foreign ownership data
- **Ví dụ**: FTSE passive inflows (nếu upgrade), CW hedge (~10% free float), room ngoại
- **Cách dùng**: Có thật nhưng THƯỜNG KHÔNG ĐỦ MẠNH một mình quyết xu hướng >vài tuần
- **Xếp loại output**: "Có thật, quy mô hạn chế" hoặc "Tiềm năng"

### Tầng 3 — NARRATIVE (⭐ Đọc tâm lý, KHÔNG đặt lệnh)
- **Nguồn**: Báo cáo analyst, target price CTCK, phỏng vấn CEO, MXH, room chat
- **Ví dụ**: TCB "15% deal" (VPS report), analyst clusters
- **Cách dùng**: Đọc timing, KHÔNG quyết direction. Phải xếp SAU filing chính thức
- **Xếp loại output**: "Luận điểm phân tích" hoặc "Giả thuyết"

---

## 9 ANTI-PATTERNS (BẮT BUỘC CHECK TRƯỚC MỌI OUTPUT)

| # | Lỗi | Đúng | Check |
|---|---|---|---|
| ❌1 | "AGM công bố trước 10 ngày" | Luật DN: ≥**21 ngày**. 10 ngày = lập DS CĐ | Quy định pháp lý → verify Luật DN |
| ❌2 | "Insider >2,000$ → 24h báo" | Đăng ký TRƯỚC + 3 ngày GD SAU | Verify Thông tư 96/2020 |
| ❌3 | ">3 CTCK nâng target = deal" | Heuristic, KHÔNG phải rule | Không khẳng định từ heuristic |
| ❌4 | "CEO trên Bloomberg = deal gần xong" | Heuristic, không chứng minh được | Chờ filing, không chờ phỏng vấn |
| ❌5 | "Volume cao = mua thật" | FPT phản ví dụ: volume cao + ngoại BÁN ròng | Volume ≠ direction |
| ❌6 | "VN30F basis dương = smart money long" | Basis = kỳ vọng ngắn hạn, cần xác nhận thêm | Không dùng basis đơn lẻ |
| ❌7 | "Giá phát hành = floor đảm bảo" | DN có ĐỘNG CƠ nhưng ≠ SÀN ĐẢM BẢO | "Động cơ" ≠ "đảm bảo" |
| ❌8 | "M7 margin = ép tăng" | M7 = forced SELLING = ép GIẢM | **SAI LOGIC** — margin call = bán |
| ❌9 | "SHB 92/100 đã xác thực" | Score = ước tính, vượt data | Ghi rõ "ước tính" vs "xác thực" |

---

## CHECKLIST THẨM ĐỊNH — TRƯỚC MỌI OUTPUT CK

```
□ 1. Mọi con số/mốc có source link?
□ 2. Mọi mệnh đề xếp loại 4 cột? (Đúng / Đúng một phần / Chưa xác thực / Sai)
□ 3. T3 narrative có dùng "BẮT BUỘC/CHẮC CHẮN" không? → Nếu có = SỬA
□ 4. Score/điểm ghi "ước tính" hay "xác thực"?
□ 5. Check 9 anti-patterns?
□ 6. Tách rõ T1 vs T2 vs T3?
□ 7. Giao thoa lá số ghi "conditional" nếu catalyst chưa confirm?
□ 8. Version + ngày + đính chính rõ?
□ 9. Backup → 05_ck_analysis/?
```

---

## QUY TẮC TRÍCH DẪN

| Loại | Format | Ví dụ |
|---|---|---|
| Filing DN | `[shb.com](URL)` | NQ tăng vốn SHB |
| Luật/Circular | `Luật CK 2019 Điều X, Khoản Y` | Verify trực tiếp văn bản |
| Perplexity search | `[nguồn](URL) via Perplexity YYYY-MM-DD` | Ghi ngày search |
| Analyst report | `[CTCK](URL) — luận điểm phân tích` | Ghi rõ = T3, không T1 |

---

## GIAO THOA VỚI TỬ VI

1. Đọc SOT tinh bàn (01_data_inventory/) → xác định cung Tài Bạch, ĐV, NH
2. Map nguyệt hạn (tháng AL) với mốc T1 (filing dates) và T2 (FTSE, rebalance)
3. Giao thoa CHỈ đánh "⭐⭐⭐" khi T1 confirmed + NH tốt
4. Giao thoa T2/T3 + NH → đánh "⭐⭐ conditional" hoặc "⭐ giả thuyết"

---

## FILES LIÊN QUAN

| File | Mục đích |
|---|---|
| `05_ck_analysis/sot/` | Source of Truth filings đã verify |
| `05_ck_analysis/analysis/forced_catalyst_v4.md` | Framework v4 chính |
| `05_ck_analysis/analysis/error_registry.md` | 9 lỗi + anti-patterns |
| `.agent/workflows/ck-tuvi-forecast.md` | SOP 7 bước |
| `.agent/rules/tu_vi_rules.md` | Rules R-CK1→R-CK5 |
| `02_luan_giai/luan_giai_toan_dien_long_2026.md` → B.7 | Bản thẩm định pháp y |
