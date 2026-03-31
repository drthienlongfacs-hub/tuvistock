#!/usr/bin/env python3
"""Shared guardrails for Hoa Ky interpretation and post-generation fixes."""

from pathlib import Path


MECHANICAL_REPLACEMENTS = [
    (
        "⭐⚠️ **SONG KỴ THÂN** — Kỵ kép KHÓA Pháo Đài = tiền không chảy ra",
        "⭐⚠️ **Vũ Kỵ TRÙNG THÂN** — xu hướng siết chi và giữ tiền mạnh hơn; đây là tín hiệu tăng kiểm soát dòng tiền, không tự động đồng nghĩa mất tiền hay bất động hoàn toàn",
    ),
    (
        "Song Kỵ Thân = tiền bị khóa = KHÔNG rút ra, PHẢI HOLD",
        "Vũ Kỵ trùng Thân = dòng tiền cần kỷ luật hơn, hạn chế phản xạ mua bán nóng; quyết định hold hay giảm vị thế vẫn phải nhìn thêm cấu trúc tài sản và bối cảnh thực tế",
    ),
    (
        "Vũ Kỵ phi vào Sửu = tưởng hung nhưng Sửu có Khóa 3 Lớp (Vũ Tham Kỵ Đắc). Kỵ chồng Kỵ tại Tứ Mộ = **lãi kép ẩn** (khóa chặt hơn = tiền KHÔNG CHẢY RA).",
        "Vũ Kỵ phi vào Sửu làm rõ chủ đề phòng thủ tài chính của gốc Thân: ưu tiên khóa thất thoát, rà soát nhịp rút tiền và bớt hành động bốc đồng. `Phản Vi Giai` ở đây nên đọc như năng lực giữ khung, không phải công thức tự động suy ra `lãi kép ẩn`.",
    ),
    (
        "| **Vũ Kỵ** | Sửu (Thân) | Tài chính | ⚠️ Kỵ đánh Thân nhưng **Phản Vi Giai** = Kỵ chồng Kỵ = lãi kép ẩn, giữ chặt hơn |",
        "| **Vũ Kỵ** | Sửu (Thân) | Tài chính | ⚠️ Kỵ nhấn mạnh nhu cầu siết quản trị tiền và giảm bốc đồng; `Phản Vi Giai` chỉ cho phép đọc theo hướng giữ khung tốt hơn, không được suy diễn thành lợi nhuận tự sinh |",
    ),
    (
        "| **Tham Kỵ** | **Sửu (Thân!)** | Bản thân | ⛔ **SONG KỴ THÂN** (Vũ Kỵ gốc + Tham Kỵ lưu) → tuyệt đối KHÔNG đầu tư mới |",
        "| **Tham Kỵ** | **Sửu (Thân!)** | Bản thân | ⚠️ Kỵ lặp tại trục Thân làm tăng tham muốn nhưng nghẽn hành động; ưu tiên giảm mở vị thế mới và rà lại thanh khoản, không cộng cơ học thành `cấm tuyệt đối` cho mọi tình huống |",
    ),
    (
        "| **Tham Kỵ** | **Sửu (Thân)** | Bản thân | ⛔ **SONG KỴ THÂN**: Vũ Kỵ gốc + Tham Kỵ phi tinh = 2 Kỵ đập vào Pháo Đài. Tham = tham lam, Kỵ = nghẽn → **TUYỆT ĐỐI không đầu tư mới** |",
        "| **Tham Kỵ** | **Sửu (Thân)** | Bản thân | ⚠️ Kỵ lặp tại trục Thân làm tăng tham muốn nhưng nghẽn hành động; ưu tiên giảm mở vị thế mới và rà lại thanh khoản, không cộng cơ học thành `cấm tuyệt đối` cho mọi tình huống |",
    ),
    (
        "| **CK** | Song Kỵ Thân = két bị khóa kép | ❌ TUYỆT ĐỐI không mở vị mới. HOLD |",
        "| **CK** | Kỵ lặp tại Thân = tâm lý và thanh khoản bị siết | ⚠️ Hạn chế vị thế mới, giữ kỷ luật rủi ro; không biến Kỵ thành mệnh lệnh cơ học cho mọi quyết định |",
    ),
    (
        "> | Kỵ | Tham Lang | **Sửu (Thân!)** | 🔐 **SONG KỴ THÂN ĐẮC** (Vũ Kỵ gốc + Tham Kỵ lưu) = Mộ Khố KHÓA KÉP. Kỵ Đắc Phản Vi Giai + Sửu Tứ Mộ + Thanh Long + Nguyệt Đức → **tích trữ chiến lược**, không phải bế tắc. NHƯNG T4 = Ách + Hỏa Cục thiêu → không mở kho, chỉ giữ chặt |",
        "> | Kỵ | Tham Lang | **Sửu (Thân!)** | ⚠️ Kỵ lặp tại Thân cho thấy xu hướng co cụm và siết dòng tiền mạnh hơn thường lệ. `Phản Vi Giai` + Tứ Mộ + cát tinh phụ cho phép đọc theo hướng giữ khung và chống thất thoát, nhưng vẫn phải nhường chỗ cho bài toán sức khỏe và thanh khoản thực tế; không nên biến nó thành mệnh lệnh `không mở kho bằng mọi giá` |",
    ),
    (
        "| **Tham Kỵ** | **Sửu (Thân)** | Bản thân | 🔐 **SONG KỴ THÂN ĐẮC** = MỘ KHỐ khóa kép. Vũ Kỵ gốc + Tham Kỵ lưu = 2 ổ khóa trên két vàng. Kỵ Đắc Phản Vi Giai (càng khóa càng giá trị) + Sửu=Tứ Mộ (chôn giữ) + Thanh Long Nguyệt Đức bảo hộ. **Giữ chặt vị thế, KHÔNG RÚT, không mở — đặc biệt khi Ách đang bị Hỏa thiêu** |",
        "| **Tham Kỵ** | **Sửu (Thân)** | Bản thân | ⚠️ Kỵ lặp tại trục Thân làm phản xạ thủ thế và nhu cầu kiểm soát tiền rất mạnh. `Phản Vi Giai` tại Tứ Mộ cho phép ưu tiên giữ kỷ luật vốn và chặn thất thoát, nhưng vẫn phải xét nhu cầu thanh khoản, sức khỏe và dữ liệu thị trường; không nên tuyệt đối hóa thành `không rút, không mở` trong mọi bối cảnh |",
    ),
    (
        "| **Liêm Kỵ ×2** | **Dậu (Thê)** | Vợ/chồng | ⛔ **TAM KỴ LIÊM**: Kỵ bản mệnh (Sửu TH) + Kỵ LN + Kỵ tháng = cãi nhau dữ dội |",
        "| **Liêm Kỵ ×2** | **Dậu (Thê)** | Vợ/chồng | ⚠️ Liêm Kỵ lưu niên + Liêm Kỵ tháng làm chủ đề quan hệ nổi rõ tại cung Thê; Vũ Kỵ gốc ở Sửu chỉ là nền tâm lý kiểm soát, không được cộng thô thành `tam kỵ đồng cung` hay mặc định cãi vã dữ dội |",
    ),
    (
        "| **Xương Khoa ×2** | **Dậu (Thê)** | Vợ/chồng | ✅ **ĐỐI TRỌNG**: ai nói ĐÚNG sẽ THẮNG. Khoa chế Kỵ |",
        "| **Xương Khoa ×2** | **Dậu (Thê)** | Vợ/chồng | ✅ Khoa làm sáng vấn đề, đặt lại ngôn ngữ và cho phép đối thoại có cấu trúc; đây không phải trò thắng-thua và cũng không triệt tiêu Kỵ hoàn toàn |",
    ),
    (
        "**Tuần 3 — ĐỈNH ĐIỂM:** 3 tầng Kỵ chồng lên: (1) Vũ Kỵ gốc tam hợp, (2) Liêm Kỵ LN, (3) Liêm Kỵ tháng TRÙNG. Liêm = miệng độc, Phá = phá hỏng, Linh = bùng nổ. **Cãi vã lớn, có thể đập phá, nói lời tổn thương sâu.** Đồng thời sự nghiệp rung lắc (Mão chiếu) → vòng xoáy tiêu cực.",
        "**Tuần 3 — ĐỈNH ĐIỂM:** Đây là lúc chủ đề Kỵ trên trục Thê - Thân lộ rõ nhất: Liêm Kỵ lưu niên + Liêm Kỵ tháng làm lời nói dễ sắc và suy diễn, còn Vũ Kỵ gốc khiến phản xạ phòng thủ tăng. Biểu hiện thực tế nên đọc là dễ truy vấn, cố chứng minh mình đúng, nói quá lời hoặc lạnh mặt kéo dài; mức độ nặng nhẹ còn phụ thuộc nền quan hệ và khả năng dừng đúng lúc.",
    ),
    (
        "**Giải pháp duy nhất: NÓI CHUYỆN bằng logic, không bằng cảm xúc.**",
        "**Giải pháp chính:** dùng Khoa để gọi đúng vấn đề, nói chậm, đổi bối cảnh trao đổi và có khoảng dừng; lý trí là một đối trọng quan trọng, nhưng không phải giải pháp duy nhất.",
    ),
    (
        "Sự giao thoa của Vũ Tham thiết lập một cỗ máy in xèng khổng lồ, đặc biệt năng lượng từ can Nhâm bản mệnh làm bùng nổ Hóa Kỵ ôm Thân, giật đứt mọi rào cản tài chính.",
        "Sự giao thoa của Vũ Tham làm nổi bật năng lực gom nguồn lực và giữ tài sản. Hóa Kỵ ôm Thân ở đây nên đọc như áp lực quản trị, giữ kín và siết thất thoát, không phải công thức `phá mọi rào cản tài chính`.",
    ),
    (
        "Dòng tiền vào ồ ạt tỷ lệ thuận tuyệt đối với sự săm soi, đố kỵ, báo cáo thọc gậy bánh xe từ đám đồng nghiệp/đối thủ ganh ghét.",
        "Nếu dòng tiền hoặc thành quả tăng, đi kèm có thể là cảm giác bị săm soi nhiều hơn; nhưng mức độ thực tế còn tùy môi trường và cách anh vận hành sự kín kẽ, không nên suy diễn thành quan hệ tuyệt đối một-một.",
    ),
    (
        "Về tiền: Song Kỵ đánh vào Pháo Đài Sửu (Vũ Tham Kỵ bản gốc + thêm Vũ Kỵ lưu nguyệt = Kỵ chồng Kỵ). Nghe đáng sợ nhưng thực ra tốt: Kỵ tại Tứ Mộ = Phản Vi Giai, khóa chặt kho = tiền KHÔNG CHẢY RA ngoài ý muốn. Giống như cái két sắt bị khóa 2 lần — mất chìa khóa cũng tốt, vì không ai mở được kể cả bản thân. **Kết luận CK: HOLD CHẶT, không mua không bán, đợi MSCI review T6 DL.**",
        "Về tiền: Vũ Kỵ lưu nguyệt quay về đúng trục Thân làm chủ đề phòng thủ tài chính nổi lên rất mạnh. `Phản Vi Giai` tại Tứ Mộ cho phép đọc theo hướng giữ khung, chống thất thoát và giảm phản xạ bốc đồng; nó không tự động biến mọi quyết định `hold` thành đúng hay suy ra lợi nhuận ẩn. Kết luận thực tế hơn là: giảm giao dịch theo cảm hứng, bám kế hoạch vốn và chỉ giữ vị thế khi thesis nền còn đúng.",
    ),
    (
        "**Giữa tháng (tuần 3):** **ĐIỂM NGUY HIỂM:** Song Kỵ đập vào Pháo Đài Sửu. Tham Kỵ = lòng tham bị nghẽn, muốn kiếm tiền mà BẾ TẮC. Vũ Kỵ gốc + Tham Kỵ phi tinh = kế hoạch tài chính bị TRỤC TRẶC. **CK T4:** Lesson 2025: T4 DL (tháng 4 dương) luôn là tháng crash (thuế quan Trump T4/2025). Song Kỵ cá nhân + macro xấu = ⛔ **TUYỆT ĐỐI không mua CW, không trading**. Nhưng Kỵ Đắc Phản Vi Giai gốc = tiền KHÔNG MẤT — chỉ bị GHÌM, không chảy.",
        "**Giữa tháng (tuần 3):** Đây là điểm nhạy nhất của trục Thân - Tài: Tham Kỵ làm ham muốn kiếm tiền tăng nhưng quyết định dễ nghẽn hoặc quá tay, còn Vũ Kỵ gốc đẩy phản xạ phòng thủ lên cao. Nếu macro bên ngoài cùng xấu thì nên thu hẹp trading ngắn hạn và tránh các vị thế đòn bẩy; tuy vậy vẫn phải kiểm theo dữ liệu thị trường thực, không dùng `Song Kỵ` như lệnh cấm tuyệt đối. `Phản Vi Giai` chỉ nói rằng tiền có xu hướng bị ghìm/giữ lại tốt hơn, chứ không bảo đảm miễn nhiễm rủi ro.",
    ),
    (
        "Lục Hại Sửu-Ngọ (Pháo Đài tài chính hại Tật Ách) nói thêm: tiền đang ĂN sức. Kiếm tiền tháng này = mất sức tháng sau. Song Kỵ Thân (Vũ Kỵ gốc + Tham Kỵ lưu) khóa két sắt 2 lần = ĐỪNG mở ra, đừng đầu tư, đừng rút tiền — cứ để yên.",
        "Lục Hại Sửu-Ngọ cho thấy bài toán tiền và sức khỏe đang kéo ngược nhau. Kỵ lặp tại Thân làm phản xạ thủ thế rất mạnh, vì vậy tháng này nên hạn chế quyết định tài chính cảm tính và tránh ép bản thân vừa giữ sức vừa săn lợi nhuận. Điều cần nhấn là giảm bốc đồng và ưu tiên thanh khoản an toàn, không phải `đóng băng mọi dòng tiền` một cách máy móc.",
    ),
]


def score_tu_hoa_context(hoa_luu_list):
    """Context-aware Tứ Hóa scoring to avoid binary 'has Ky => minus two' logic."""
    if not hoa_luu_list:
        return 5.0, "Không có Lưu Tứ Hóa / Lưu Tinh mạnh"

    text = ", ".join(hoa_luu_list)
    score = 5.0
    ky_count = text.count("Kỵ")

    if "Lộc" in text:
        score += 1.0
    if "Quyền" in text:
        score += 0.75
    if "Khoa" in text:
        score += 0.75

    if ky_count == 1:
        score -= 0.75
    elif ky_count >= 2:
        score -= 1.25

    if "Khoa" in text and "Kỵ" in text:
        score += 0.5
    if "Đắc" in text or "Phản Vi Giai" in text:
        score += 0.5
    if any(bad in text for bad in ["L.Đà La", "L.Bạch Hổ", "L.Kình", "L.Kinh Dương"]):
        score -= 0.75

    score = max(1.0, min(10.0, score))

    if "Kỵ" in text and "Khoa" in text:
        note = "Kỵ có đối trọng Khoa; phải đọc theo ngữ cảnh cung và mức lặp"
    elif ky_count >= 2:
        note = "Kỵ lặp làm tăng ma sát, nhưng không được cộng cơ học nếu khác cung/chức năng"
    elif "Kỵ" in text:
        note = "Kỵ hiện diện như điểm nghẽn/rà soát, cần xét vị trí và sao đi kèm"
    else:
        note = "Tứ Hóa thiên về cát tính hoặc trung tính"

    return round(score, 1), f"{text} | Note: {note}"


def apply_hoa_ky_guardrails_text(content):
    updated = content
    for old, new in MECHANICAL_REPLACEMENTS:
        updated = updated.replace(old, new)
    return updated


def apply_hoa_ky_guardrails_to_file(file_path):
    path = Path(file_path)
    original = path.read_text(encoding="utf-8")
    updated = apply_hoa_ky_guardrails_text(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False
