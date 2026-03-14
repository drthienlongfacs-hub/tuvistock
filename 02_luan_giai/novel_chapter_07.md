# CHƯƠNG 7: DÒNG CHẢY XUYÊN BỜ
*(Tháng 7 – Kiến Trúc Tàng Hình)*

### Cảnh 25: Phân Quyền Sáng Tạo

Tháng Bảy âm lịch, tháng mà người đời thường kiêng kỵ những khởi đầu mới (tháng Cô Hồn), lại chính là điểm bùng nổ của một công trình ngầm. Làn nước mát lạnh từ Đà Lạt đã tưới dịu tâm trí Long, mang lại một góc nhìn hoàn toàn mới về cách vận hành dự án CDMS.

"Từ bỏ sự kiểm soát tuyệt đối," Long lầm bầm, tay thoăn thoắt gõ lệnh trên Terminal. Màn hình đen nền chữ xanh lá cây chạy dọc những dòng mã hóa báo tín hiệu deploy (triển khai) lên một máy chủ đám mây độc lập.

Sự sụp đổ của hệ thống hồi tháng Tư đã dạy anh bài học đắt giá về kiến trúc tập trung. Nếu cố nhét mọi thứ vào một cửa ngõ chính thức của bệnh viện, Triệt Lộ sẽ luôn chực chờ bóp nghẹt đường băng thông, hoặc Bác sĩ Minh sẽ lại dùng các rào cản hành chính để đóng sập nó. 

Chiến thuật mới của Long là "Guerilla Deployment" (Triển khai Du kích). 

Thay vì xây dựng một hệ thống cồng kềnh đòi hỏi sự phê duyệt từ cấp cao nhất, anh chẻ nhỏ CDMS thành những vi dịch vụ (microservices). Mỗi vi dịch vụ chỉ phục vụ một chức năng sắc bén duy nhất: một cái để y tá check lỗi phát thuốc, một cái để nội trú tự động trích xuất bệnh án. Các module này hoạt động độc lập trên trình duyệt, không cần cài đặt rườm rà. Chúng ẩn mình dưới dạng những tiện ích nhỏ gọn mà nhân viên y tế tự truyền tay nhau. 

Nó như nước. Không có hình dạng cố định, nhưng đủ sức len lỏi qua mọi rào cản đá tảng.

Quỳnh ngồi trên sofa, chiếc iPad trên đùi, đang test các chức năng bằng tài khoản user bình thường. 
"Anh Long, cái luồng nhập liệu bệnh án phân tuyến này chạy mượt lắm, nhưng nếu chọn sai mục bảo hiểm thì nó không có nút Back (Quay lại) nhanh. Phải bấm ba lần. Vậy là hỏng trải nghiệm," cô nói, mắt không rời màn hình.

Long mỉm cười. QA (Quality Assurance) của anh đang làm việc rất hiệu quả. Sự có mặt của Quỳnh trong dự án đã xóa tan hoàn toàn cái rào cản "Song Kỵ" ngột ngạt. Cô không cần hiểu code, cô hiểu con người.

"Sửa ngay đây. Thêm nút Back toàn cục ở thanh điều hướng trên cùng," Long gõ phím lạch cạch. 

### Cảnh 26: Bức Tường Lửa API

Tuy nhiên, nước không thể chảy nếu gặp một con đập chặn kín. 

Giai đoạn cuối cùng của tháng Bảy, Long đụng phải một bức tường kỹ thuật kiên cố: Tích hợp dữ liệu thời gian thực từ API lỗi thời của hệ thống HIS (Hospital Information System) trung tâm. Hệ thống HIS cũ kỹ được xây dựng từ mười năm trước bằng một nền tảng đóng kín, việc móc nối dữ liệu bị mã hóa theo một kiểu quy ước nội bộ không có tài liệu hướng dẫn.

Hàng đêm ròng rã, Long dùng mọi công cụ phân tích gói tin (packet sniffer) để dịch ngược giao thức của bọn họ. Vô vọng. Mỗi lần gửi request, server trung tâm đều trả về mã lỗi 403 Forbidden. Cảm giác như đang đứng trước một cánh cổng sắt khổng lồ mà không có chìa khóa.

Ngửa mặt lên trần nhà lúc ba giờ sáng, Long vuốt mặt mệt mỏi. "Cần một người hiểu ruột gan cái HIS này. Hoặc cần phép màu." 

Anh đã nghĩ đến việc dùng tiền để "mua" tài liệu API từ một nhân viên IT trong phòng công nghệ thông tin bệnh viện. Một kỹ năng quen thuộc của thế giới ngầm. Nhưng lương tâm và sự cảnh giác kỷ luật đã cản anh lại. Nếu để lộ danh tính người dùng tool trích xuất dữ liệu, dự án du kích sẽ bị dập tắt ngay lập tức. 

### Cảnh 27: Hạt Giống Hóa Lộc Nảy Mầm

Sáng thứ Năm. Điện thoại Long rung lên một thông báo tin nhắn Telegram. Người gửi: *Hiếu - ĐH Bách Khoa (Student GS Hoàng)*.

Long nhíu mày. Tháng Hai, anh đã thức trắng vài đêm để thiết kế xong kiến trúc tầng dữ liệu AI cho dự án của Giáo sư Hoàng, sau đó bàn giao lại cho cậu sinh viên tên Hiếu này để cậu ta làm luận văn bảo vệ. Anh đã giúp đỡ hoàn toàn vô tư, không đòi hỏi trả công hay đứng tên. Giúp vì đam mê học thuật thuần túy (Thiên Cơ Hóa Lộc).

Tin nhắn hiển thị: 
*"Dạ chào anh Long. Luận văn của em tháng trước bảo vệ xuất sắc, thầy Hoàng gửi lời cảm ơn anh rất nhiều. Nghe thầy nói anh dạo này đang nghiên cứu tích hợp dữ liệu hệ thống bệnh viện. Hồi xưa em đi thực tập ở công ty X (công ty viết cái HIS bệnh viện anh), em có còn giữ một bộ tài liệu cấu trúc mã hóa token API nội bộ của họ. Không biết anh có cần không, em gửi anh tham khảo ạ."*

Tim Long đập mạnh một nhịp. Kèm theo tin nhắn là một file PDF định dạng tài liệu kỹ thuật giải mã chính xác bức tường 403 Forbidden mà anh đang bế tắc phá cửa suốt hai tuần qua.

Khoảnh khắc đó, Long thực sự nổi da gà. Tử Vi không phải là mê tín. Nó là xác suất của năng lượng. Hóa Lộc ở cung Nô Bộc (Bạn bè/Đồng nghiệp/Đàn em) không có nghĩa là tiền từ trên trời rơi xuống. Nó có nghĩa là khi bạn cho đi trí tuệ một cách hào sảng, không mưu cầu, vũ trụ sẽ trả lại cho bạn một mảnh ghép vô giá vào đúng thời điểm bạn cạn kiệt hy vọng nhất. 

"Em cứu mạng anh rồi, Hiếu," Long nhắn lại nhanh chóng. 

Chỉ với bộ tài liệu đó, hai đêm sau, CDMS của Long đã chính thức chọc thủng được lớp bảo mật của HIS cũ, rút dữ liệu sạch sẽ, im lặng và mượt mà như một bóng ma. Hệ thống đã có luồng huyết mạch thực thụ.

### Cảnh 28: Sự Khước Từ Tĩnh Lặng

Cuối tháng Bảy. CDMS giờ đây đã có gần bốn mươi tài khoản y tá ngầm sử dụng hàng ngày để giảm bớt gánh nặng nhập liệu và đối chiếu thuốc. 

Giờ nghỉ trưa, trong lúc đang ngồi phòng trực ăn hộp cơm tấm, điện thoại Long sáng màn hình. Một tin nhắn Zalo từ đầu số lạ, nhưng văn phong thì rất quen quen.

*"Anh Long khỏe không. Em là nhân viên cũ của anh Hưng. Bên em đang đánh sóng một dự án đất nền vùng ven, pháp lý cực chuẩn, cam kết ra hàng sau 6 tháng lãi tối thiểu 25%. Chỉ một lô suất ngoại giao duy nhất giá rẻ..."*

Vẫn là điệp khúc bất động sản. Sự cám dỗ luôn tìm cơ hội quay lại khi người ta bắt đầu có những thành tựu nhỏ và cảm giác chủ quan. 

Nhưng, nếu như sự khước từ ở Đà Lạt hồi tháng Sáu là một quyết định dựa trên sự tĩnh tâm sau khủng hoảng, thì hôm nay, sự khước từ này hoàn toàn nằm ở chế độ "Lái tự động" (Autopilot). 

Anh không buồn đọc hết dòng chữ "lãi tối thiểu 25%". Anh không có phản ứng hóa học nào trong não tiết ra dopamine của lòng tham. Tâm trí anh hiện tại chỉ tràn ngập những biểu đồ kiến trúc hệ thống và chiến lược mở rộng lượng người dùng (scaling base). 

Ngón tay anh chạm vào góc phải màn hình. *Chặn người dùng này.* 

Long tiếp tục xúc muỗng cơm, mắt dán vào màn hình laptop theo dõi những dòng log dữ liệu truyền tải trơn tru. Lão tử nói đúng: Khi người ta có một mục tiêu đạo sống đủ lớn, những thứ phù phiếm xung quanh tự khắc trở thành hạt bụi.

Dòng chảy đã xuyên bờ. Bây giờ, hệ thống sẽ tự vươn ra biển.

*(Hết Chương 7)*
