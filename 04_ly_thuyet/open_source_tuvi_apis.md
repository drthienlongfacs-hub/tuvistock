# 💻 Mã Nguồn Mở, Thuật Toán & API Tử Vi Đẩu Số
> **Cập nhật (HARVEST)**: 2026-03-28 | Nguồn: Perplexity Deep Research

Trong kỷ nguyên số, tử vi đẩu số không còn gói gọn trong các bảng tra cứu thủ công mà đã được mô hình hóa thành các thư viện phần mềm phức tạp, đảm bảo độ chính xác tuyệt đối về thuật toán thiên văn.

## 1. Hệ Sinh Thái Mã Nguồn Mở (Open Source)

### 🐍 Python: `lasotuvi` (tác giả: doanguyen)
- **Đặc điểm**: Thư viện API Backend chuyên dụng và mạnh mẽ nhất cho Python. Tách biệt hoàn toàn tầng logic an sao với giao diện người dùng.
- **Tích hợp**: Có thể dùng chung với `lasotuvi-django` để tạo Frontend.
- **GitHub**: [doanguyen/lasotuvi](https://github.com/doanguyen/lasotuvi)
- **Xử lý thuật toán**:
  - Giao hoán Lịch Âm ↔ Dương.
  - Phân định Giờ Địa Chi (1 canh = 2 giờ đồng hồ hiện đại, ví dụ canh Tý = 23h-01h).
  - An vị chính tinh theo Cục và Ngày sinh.
  - An Tứ Hóa (Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ).

### 🟨 JavaScript/TypeScript: `iztro` (tác giả: SylarLong)
- **GitHub**: [SylarLong/iztro](https://github.com/SylarLong/iztro) | **NPM**: `npm i iztro`
- **Đặc điểm**: Thư viện Front-end/Node.js hoàn thiện, documentation đa ngôn ngữ (CN/EN/TW).
- **Tính năng ưu việt**:
  - Lập tinh bàn bằng cả Lịch Dương (`bySolar()`) và Lịch Âm (`byLunar()`) có hỗ trợ **tháng nhuận** (`isLeapMonth` flag).
  - Gọi được Tứ Trụ (Bát Tự) dựa theo Thiên Can, Địa Chi.
  - Tìm sao lưu (Flowing stars) cho Đại Vận 10 năm và Lưu Niên hàng năm.
  - Hỗ trợ phương thức kiểm tra cung đối xung, tam phương tứ chính.
  - Phân phối qua NPM hoặc CDN.

### 📱 Flutter/Dart: `dart_iztro` (tác giả: EdwinXiang)
- **Đặc điểm**: Cross-platform plugin cho Android, iOS, Windows, macOS, Web.
- **Toán học Thiên Văn**: Tích hợp thuật toán **True Solar Time** (Giờ Mặt Trời Thật) để bù trừ độ lệch múi giờ dựa theo kinh độ/vĩ độ chính xác tại nơi sinh.

### ☕ Java: `tuvi-dauso-tanbien` (tác giả: minhthytran)
- **GitHub**: [minhthytran/tuvi-dauso-tanbien](https://github.com/minhthytran/tuvi-dauso-tanbien)
- **Đặc điểm**: Viết dựa trên sách "Tử Vi Đẩu Số Tân Biên" của **Thái Thứ Lang** (bút danh Vân Đằng). Ứng dụng dòng lệnh chạy đa nền tảng qua JVM.

## 2. APIs và Nền Tảng Dịch Vụ
- **Tu Vi Global WordPress Plugin**: Cắm trực tiếp tính năng lập lá số vào các website WordPress.
- **mingming3.com**: Lập lá số online truyền thống theo tứ trụ.
- **AItuvi**: Áp dụng AI Model phân tích cụ thể các cung, mang đậm tính dự báo dựa trên logic hệ chuyên gia.

## 3. Requirements (Điều Kiện Tiên Quyết) Cho Một Hệ Thống Lập Lá Số
1. **True Solar Time**: Phải tính được giờ mặt trời thực tế, vì quỹ đạo Trái Đất là hình elip khiến độ dài các ngày không bằng nhau trong năm.
2. **Leap Months (Tháng Nhuận)**: Lịch Âm có tháng nhuận để đuổi kịp Lịch Dương. Các thuật toán phải có cờ bàng (`isLeapMonth: boolean`) để dịch chuyển cung Mệnh.
3. **Phase Dynamics (Đại Vận/Lưu Niên)**: Khung 10 năm và 1 năm biến đổi, mang theo vòng Lộc Tồn, Thái Tuế và các sao Lưu.
