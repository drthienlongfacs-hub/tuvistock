import re
import sys
from pathlib import Path
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file

# Human readable summaries for each month
HUMAN_SUMMARIES = {
    1: "> **🗣️ Tóm lại:** Tháng Giêng khởi đầu chậm chạp và có phần bế tắc trong công việc chính thức (do vướng Triệt). Cảm giác như bạn có tài nhưng bị ghì lại, chưa bung sức được. Tuy nhiên, đừng nản! Trong cái khó sẽ bất ngờ xuất hiện những vị sếp hoặc chuyên gia giấu mặt (Quý nhân) ra tay giúp đỡ. **Chiến lược:** Cứ từ từ, thu mình quan sát, đừng vội đưa ra các quyết định lớn. Tiền bạc ngầm vẫn đang chảy về nên không cần hoảng.",
    
    2: "> **🗣️ Tóm lại:** Đây là tháng \"Vườn Ươm Tri Thức\" bùng nổ! Tháng này bạn sẽ tỏa sáng nhờ các mối quan hệ, bạn bè, đồng nghiệp hoặc các đối tác chuyên môn cao. Mạng lưới này không chỉ mang lại ý tưởng mà còn trực tiếp mang tới những cơ hội tài chính và quyền lực cực tốt. **Chiến lược:** Hãy bước ra ngoài, đi giao lưu, gặp gỡ network. Góp vốn kiến thức, đẩy mạnh làm việc nhóm – thành công tháng này nằm trọn trong tay các mối quan hệ của bạn.",
    
    3: "> **🗣️ Tóm lại:** Một tháng vô cùng rực rỡ và quyền lực khi bước ra ngoài xã hội. Điểm số cao chót vót (6.4). Bạn sẽ nắm thế chủ động hoàn toàn, tiếng nói có trọng lượng, đi ra ngoài đàm phán hay giao dịch đều ở thế bề trên. Tuy nhiên, quyền lực cao đi kèm áp lực lớn, như thanh gươm đang được tôi luyện trong lửa. **Chiến lược:** Đánh nhanh thắng nhanh, chốt sale, ký hợp đồng. Tự tin bước ra ngoài vì đây là sân chơi của bạn.",
    
    4: "> **🗣️ Tóm lại:** Sau tháng 3 rực rỡ, tháng này cơ thể và tinh thần bạn sẽ đòi hỏi sự nghỉ ngơi. Đừng vắt kiệt sức mình! Có những stress ngầm, mệt mỏi từ bên trong phát ra khiến bạn thấy uể oải, mất tập trung. Việc cố gắng bung sức lúc này chỉ làm phản tác dụng. **Chiến lược:** Sống chậm lại. Phanh bớt các dự án tham vọng, tập trung chăm lo giấc ngủ, sức khỏe và đời sống tinh thần. Phải nạp lại năng lượng để chuẩn bị cho giai đoạn sóng dội tới đây.",
    
    5: "> **🗣️ Tóm lại:** ⛔ **ĐÁY CỦA NĂM.** Đây là tháng nguy hiểm nhất về mặt dòng tiền và pháp lý (Điểm thấp nhất: 3.8). Tiền bạc kẹt cứng, có rủi ro liên quan đến giấy tờ, kiện tụng hoặc tiểu phẫu y tế. Cảm giác mọi thứ đều chống lại mình, nóng nảy bực dọc. **Chiến lược:** PHÒNG THỦ TUYỆT ĐỐI! Không đầu tư mới, không cho vay, không ký giấy tờ quan trọng nếu chưa đọc kỹ. Ôm tiền mặt, hạn chế tranh cãi để vượt qua tháng giông bão này.",
    
    6: "> **🗣️ Tóm lại:** Một tháng mang tính chất chững lại, có sự giằng co giữa lợi ích và sự bất ổn nhỏ. Những vấn đề liên quan đến con cái, đàn em hoặc tài sản/đất đai bắt đầu rục rịch sinh lời nhẹ nhưng mọi thứ chưa quá rõ ràng. Bạn vẫn phải xắn tay áo lên giải quyết những dọn dẹp tàn dư của tháng trước. **Chiến lược:** Tái cấu trúc lại công việc, giải quyết nốt những tồn đọng. Bắt đầu gieo hạt cho những dự án nửa cuối năm.",
    
    7: "> **🗣️ Tóm lại:** Tháng này điểm nhấn rớt trúng vào chuyện tình cảm, gia đình hoặc đối tác ruột. Bạn sẽ thấy không khí rất ngột ngạt, dễ nảy sinh cãi vã, xung đột lợi ích hoặc bất mãn do những kỳ vọng không thành. Thái Tuế nhập cung làm không khí thêm phần căng thẳng. **Chiến lược:** \"Dĩ hòa vi quý\". Đừng nổ súng trước! Hãy hạ cái tôi xuống, mềm mỏng trong ngoại giao và bao dung hơn với bạn đời/đối tác để tránh đổ vỡ không đáng có.",
    
    8: "> **🗣️ Tóm lại:** Bỏ qua những ồn ào lộ liễu, đây là tháng của những \"dòng tiền ngầm\" và cơ hội ẩn. Bề ngoài có vẻ như rơi vào khoảng không (Không Vong) và có tin buồn chán, nhưng thực chất nếu tinh ý, bạn sẽ chốt được những lợi ích bí mật cùng anh em, chiến hữu. **Chiến lược:** Làm gì cũng phải kín kẽ, đừng khoe khoang. Chọn lọc người để chia sẻ cơ hội, tập trung vào chiều sâu thay vì chiều rộng.",
    
    9: "> **🗣️ Tóm lại:** Bạn cảm nhận sự trỗi dậy của bản thân mạnh mẽ nhất vào lúc này, tham vọng lên cao nhưng... vẫn còn lấn cấn, rườm rà chưa thể dứt điểm ngay. Cảm giác như xe đang chạy mà quên nhả phanh tay. May mắn là định hướng cốt lõi đã rõ ràng, tư duy vô cùng minh mẫn. **Chiến lược:** Cứ vững vàng tiến lên, chậm mà chắc. Gỡ rối từng nút thắt một, không cần nóng vội, vì quỹ đạo đúng đã được thiết lập.",
    
    10: "> **🗣️ Tóm lại:** Trọng tâm tháng này hướng về bố mẹ, gia đình lớn hoặc các sếp lớn. Cảm xúc sẽ hơi mệt mỏi, nhiều việc phiền toái, lặt vặt liên quan đến trách nhiệm nội bộ khiến bạn đau đầu. Dù nền tảng cực tốt, nhưng những rắc rối cản đường vẫn gây mất năng lượng. **Chiến lược:** Làm tròn chữ hiếu và trách nhiệm. Sắp xếp hệ thống công việc khoa học hơn để tránh bị cuốn vào các tiểu tiết gây hao tâm tổn trí.",
    
    11: "> **🗣️ Tóm lại:** ⭐ **THÁNG CỦA LỘC NGẦM.** Vận khí bùng nổ, tiền bạc chảy vào túi ầm ầm! Đây là lúc gặt hái thành quả tài chính mạnh mẽ nhất cuối năm. Tuy nhiên, Hóa Kỵ luôn đi kèm \"Tiền nhiều sinh đố kỵ\" – sẽ có những lời ra tiếng vào, tăm tia soi mói từ xung quanh. **Chiến lược:** Cứ lẳng lặng mà kiếm tiền, ai nói gì mặc kệ! Mặc áo giáp phớt lờ thị phi, hốt mẻ lưới lớn dứt điểm trong im lặng.",
    
    12: "> **🗣️ Tóm lại:** Khép lại năm 2026, tháng này tập trung vào bất động sản, nhà cửa và tài sản tích luỹ. Dù có một chút cản trở khiến việc mua bán hay di dời không nhanh nhạy như ý (bị nén/cản), nhưng giá trị cốt lõi bạn nắm giữ lại đang sinh lời cực tốt. **Chiến lược:** Dành thời gian tận hưởng thành quả với gia đình, ổn định dinh cơ. Không cần mua bán lướt sóng, giữ chặt tài sản tốt qua năm mới."
}

def inject_human_readable(file_path):
    print(f"Injecting human readable texts into {file_path}...")
    content = Path(file_path).read_text(encoding='utf-8')
    lines = content.split('\n')
    out_lines = []
    
    i = 0
    current_month = 1
    
    while i < len(lines):
        line = lines[i]
        
        m = re.search(r'THÁNG (\d+) ÂM LỊCH', line, re.IGNORECASE)
        if not m:
            m = re.search(r'THÁNG (\d+)', line, re.IGNORECASE)
        if m and line.startswith('### '):
            current_month = int(m.group(1))
            
        # We look for "##### HỆ QUY CHIẾU KINH ĐIỂN" and inject our text right before it
        if line.startswith('##### HỆ QUY CHIẾU KINH ĐIỂN'):
            # Only inject if not already injected
            # We can check the previous lines
            if len(out_lines) > 0 and 'TỔNG LUẬN NHANH' not in '\n'.join(out_lines[-10:]):
                summary_text = HUMAN_SUMMARIES.get(current_month, "")
                if summary_text:
                    out_lines.append("##### 🗣️ TỔNG LUẬN NHANH (Human-Readable)")
                    out_lines.append(summary_text)
                    out_lines.append("")
                
        out_lines.append(line)
        i += 1
        
    Path(file_path).write_text('\n'.join(out_lines), encoding='utf-8')
    apply_hoa_ky_guardrails_to_file(file_path)
    print(f"Done injecting into {file_path}")

inject_human_readable('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md')
inject_human_readable('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md')
