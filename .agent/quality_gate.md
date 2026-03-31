# Quality Gate — Tử Vi Đẩu Số Analysis Output

> **Version:** 2.0 | **Created:** 14/03/2026 | **Updated:** 15/03/2026
> **Áp dụng cho:** Mọi file output tại `02_luan_giai/`
> **Điều kiện PASS:** 100% mục bắt buộc ✅, ≥ 80% mục khuyến nghị

---

## A. CHÍNH TINH (Bắt buộc: 8/8 bộ)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| A1 | Trạng thái đa phái | ✅ | Bảng ≥ 2 phái (Trung Châu, Nam, Bắc) với nguồn |
| A2 | Ngũ Hành mechanism | ✅ | Bảng sao vs cung: sinh/khắc/đồng hành + hệ quả |
| A3 | Phú cổ | ✅ | ≥ 2 phú gốc + nguồn trích dẫn (URL hoặc sách) |
| A4 | So sánh vị trí | 🟡 | Vị trí hiện tại vs tối ưu/xấu nhất |
| A5 | Đặc thù lá số | ✅ | Áp dụng CỤ THỂ cho đương số, không generic |
| A6 | Expert quote | 🟡 | ≥ 1 trích dẫn chuyên gia có tên + nguồn |

**PASS:** ≥ 4 ✅ cho MỖI bộ chính tinh (8 bộ × 4 = 32 items minimum)

---

## B. PHỤ TINH (Bắt buộc: ≥ 20 sao)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| B1 | Trạng thái | ✅ | Miếu/Vượng/Đắc/Bình/Hãm — ghi rõ |
| B2 | Ngũ Hành | ✅ | Hành sao vs Hành cung + cơ chế |
| B3 | Phú cổ | ✅ | ≥ 1 phú hoặc ý nghĩa kinh điển |
| B4 | Cách cục | 🟡 | Bộ phối hợp nổi bật (nếu có) |
| B5 | Áp dụng lá số | ✅ | Cụ thể, không generic |

**PASS:** ≥ 3 ✅ cho MỖI phụ tinh + bảng tổng kết cát/hung

---

## C. CÁCH CỤC (Bắt buộc: ≥ 15 cách)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| C1 | Điều kiện hình thành | ✅ | Ghi rõ sao nào + cung nào + quan hệ gì |
| C2 | Phú cổ gốc | ✅ | Nguyên văn phú + nguồn (URL/sách) |
| C3 | Phân loại | ✅ | Cát/Trung/Hung + chấm điểm 1-10 |
| C4 | Biến thể note | 🟡 | Ghi rõ nếu là biến thể (BT), không phải chính cách |
| C5 | Bảng tổng hợp | ✅ | Bảng NET score tổng |

**PASS:** Mỗi cách cục ≥ 3 ✅ + Bảng tổng hợp có

---

## D. ĐẠI VẬN (Bắt buộc: bảng 10 ĐV + deep ĐV hiện tại)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| D1 | Bảng 10 ĐV | ✅ | Tuổi, Cung, Tinh bàn, Nhận định cho mỗi ĐV |
| D2 | Tinh bàn ĐV hiện tại | ✅ | Bảng sao + hành + trạng thái + vai trò |
| D3 | Ngũ Hành ĐV vs Mệnh | ✅ | Bảng tương tác 4+ hàng |
| D4 | Triệt Động Lực Học | ✅ | Bảng 3 giai đoạn nhả % |
| D5 | So sánh ĐV trước | ✅ | Bảng ≥ 5 tiêu chí đối chiếu |
| D6 | Tứ Hóa Lưu Niên | ✅ | Bảng 4 hóa + cung + ý nghĩa |
| D7 | Chiến lược | ✅ | Bảng 3 giai đoạn + hành động + cảnh báo |

**PASS:** ≥ 6/7 ✅ cho ĐV hiện tại

---

## E. TRÍCH DẪN & NGUỒN (Bắt buộc)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| E1 | Perplexity verified | ✅ | Ghi rõ ngày + số trích dẫn |
| E2 | URLs kiểm chứng | ✅ | ≥ 5 nguồn web khác nhau |
| E3 | Sách tham khảo | 🟡 | ≥ 1 sách/tác giả trích dẫn |
| E4 | Không phú "chế" | ✅ | Mọi phú đều có nguồn, không tự sáng tác |
| E5 | Multi-school noted | ✅ | Ghi khi có tranh luận giữa các phái |

**PASS:** ≥ 4/5

---

## F. CẤU TRÚC & TRÌNH BÀY (Bắt buộc)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| F1 | Markdown hợp lệ | ✅ | Bảng, heading, blockquote đúng cú pháp |
| F2 | Phân phần rõ ràng | ✅ | PHẦN I → PHẦN X, không trộn lẫn |
| F3 | Không duplicate | ✅ | Không có section trùng lặp — **verify bằng `injection_guard.verify_no_duplicates()`** (RCA-040) |
| F4 | Emoji nhất quán | 🟡 | Sử dụng emoji có hệ thống (⭐⚠️⛔🟡) |
| F5 | Dung lượng hợp lý | ✅ | ≥ 1500 dòng cho bài toàn diện |

**PASS:** ≥ 4/5

---

## VERIFICATION STAMP

```
✅ QG PASS [DD/MM/YYYY] v[x.y]
Chính tinh: [x]/8 bộ PASS
Phụ tinh: [x] sao analyzed
Cách cục: [x] cách ([NET])
Đại vận: [x]/7 ĐV hiện tại PASS
Trích dẫn: [x] nguồn verified
Nguyệt Hạn: [x]/12 tháng ≥15 dòng
Feedback: [x] corrections applied
Mệnh Foundation: [x]/12 tháng có ③
Dung lượng: [x] dòng
```

---

## G. NGUYỆT HẠN (Bắt buộc cho file có Nguyệt Hạn)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| G1 | ≥15 dòng/tháng | ✅ | Mỗi tháng ít nhất 15 dòng phân tích |
| G2 | 3-Layer có đủ | ✅ | L1(Tinh bàn) + L2(Mệnh Foundation) + L3(Giải Thần) |
| G3 | Tứ Hóa tháng | ✅ | Bảng 4 hóa + cung + ý nghĩa |
| G4 | Giải Thần Pattern | ✅ | Blockquote > **Pattern T[x]:** cho mỗi tháng |
| G5 | CK/CW recommendation | ✅ | 1 dòng CK/CW cho mỗi tháng |

**PASS:** ≥ 4/5 cho MỖI tháng

---

## H. FEEDBACK CORRECTION (Bắt buộc)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| H1 | `_FEEDBACK_LOG.md` cập nhật | ✅ | Mọi correction từ đương số đều ghi log |
| H2 | Tag `[FEEDBACK]` trong file | ✅ | File được sửa có tag + ngày |
| H3 | Skill updated | 🟡 | Pattern lặp → cập nhật vào SKILL.md |

**PASS:** ≥ 2/3

---

## I. MỆNH FOUNDATION (Bắt buộc cho Nguyệt Hạn)

| # | Tiêu chí | Ký hiệu | Mô tả |
|:---:|---|:---:|---|
| I1 | ③ header có mặt | ✅ | Mỗi tháng có `**③ Mệnh Foundation →**` |
| I2 | ≥4 sao Mệnh analyzed | ✅ | Phủ/Lộc/Khoa/Riêu/Cô Thần — ít nhất 4 |
| I3 | Riêu direction đúng | ✅ | PHÁT RA, không NHẬN VÀO (R13) |
| I4 | Cô Thần context-dependent | ✅ | Ghi rõ tốt/xấu tùy tháng |

**PASS:** ≥ 3/4
