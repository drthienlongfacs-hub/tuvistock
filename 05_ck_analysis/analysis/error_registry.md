# Error Registry — Anti-Pattern CK Analysis

> **Tạo**: 14/03/2026
> **RCA**: Phiên thẩm định pháp y phát hiện 9 lỗi trong framework v2

## Mục đích
Tài liệu hóa MỌI lỗi phân tích đã phát hiện để tránh lặp lại. Trước mỗi output CK, PHẢI check danh sách này.

## Registry

| ID | Ngày | Mệnh đề SAI | Đúng là gì | Loại lỗi | Nguồn verify |
|---|---|---|---|---|---|
| **ERR-001** | 14/03/2026 | "AGM công bố trước 10 ngày" | Luật DN: ≥ **21 ngày** trước họp. 10 ngày = lập danh sách CĐ | Sai quy định | [luatvietnam](https://english.luatvietnam.vn/legal-news/annual-shareholder-meeting-requirements-in-vietnam-legal-guide-2025-4729-101344-article.html) |
| **ERR-002** | 14/03/2026 | "Insider >2,000$ → 24h báo" | Đăng ký TRƯỚC giao dịch + báo **3 ngày GD SAU**. 24h = sự kiện DN công bố khẩn | Sai quy định | [russinvecchi](https://www.russinvecchi.com.vn/publication/insider-trading-rules-in-vietnam/) |
| **ERR-003** | 14/03/2026 | ">3 CTCK nâng target = deal đàm phán" | Heuristic, KHÔNG phải rule. TCB 15% = luận điểm VPS, không xác nhận DN | Overclaim | [vps.com](https://vps.com.vn/en/post/vps--tcb---company-update-report) |
| **ERR-004** | 14/03/2026 | "CEO trên Bloomberg = deal gần xong" | Heuristic, không chứng minh được | Overclaim | Suy luận, không data |
| **ERR-005** | 14/03/2026 | "Volume cao = mua thật" | FPT phản ví dụ: volume cao + ngoại BÁN ròng mạnh | Logic thiếu | Phản ví dụ thực tế |
| **ERR-006** | 14/03/2026 | "VN30F basis dương = smart money long" | Basis = kỳ vọng ngắn hạn phái sinh, không đủ kết luận nếu thiếu xác nhận spot | Logic thiếu | — |
| **ERR-007** | 14/03/2026 | "Giá phát hành = floor đảm bảo" | DN có **ĐỘNG CƠ** nhưng ≠ **SÀN ĐẢM BẢO** trên thị trường | Overclaim | [shb.com](https://www.shb.com.vn/announcement-on-the-resolution-on-approval-of-rights-issue-of-shares-documents/) |
| **ERR-008** | 14/03/2026 | "M7 margin call = cơ chế buộc TĂNG" | M7 = forced **SELLING** = ép GIẢM. **HOÀN TOÀN SAI LOGIC** | Sai logic | [vndirect](https://www.vndirect.com.vn/cmsupload/beta/Format-bao-cao-daily-ENG-FINAL-2026.pdf) |
| **ERR-009** | 14/03/2026 | "SHB 92/100, TCB 82/100 đã xác thực" | Score = **ước tính**, vượt mức data cho phép. Phải ghi "ước tính" | Overclaim | Thẩm định 2 vòng |

## Phân loại lỗi

| Loại | Số lượng | Biện pháp phòng |
|---|---|---|
| **Sai quy định** | 2 (ERR-001, 002) | Verify trực tiếp văn bản luật, KHÔNG dùng bộ nhớ |
| **Overclaim** | 4 (ERR-003, 004, 007, 009) | Tách T1/T2/T3. T3 KHÔNG "BẮT BUỘC" |
| **Logic thiếu** | 2 (ERR-005, 006) | Cần ≥2 nguồn xác nhận cùng hướng |
| **Sai logic** | 1 (ERR-008) | Xác định rõ mechanism = tăng hay giảm |

## Cách sử dụng
Trước MỌI output CK, chạy checklist:
```
□ ERR-001: AGM = 21 ngày?
□ ERR-002: Insider = đăng ký trước + 3 ngày sau?
□ ERR-003: Có ghi rõ heuristic không?
□ ERR-004: Có dựa vào phỏng vấn thay filing không?
□ ERR-005: Volume có được đối chiếu direction không?
□ ERR-006: Basis có đi kèm spot xác nhận không?
□ ERR-007: Có ghi "dynamic cơ" thay "đảm bảo" không?
□ ERR-008: Margin = ép giảm, KHÔNG ép tăng?
□ ERR-009: Score ghi "ước tính" hay "xác thực"?
```
