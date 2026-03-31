import re
from pathlib import Path
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file

# ============================================================
# SOT-VERIFIED DATA (from kiem_ke_tinh_ban_12_cung.md + luan_giai_toan_dien_long_2026.md)
# ============================================================
# Đại Vận 4 = Dần (Điền Trạch), Cự Nhật Vượng + Triệt, 34-43 tuổi (SOT line 736, 2636)
# Mệnh = Hợi, Thiên Phủ Đắc + Lộc Tồn + Hóa Khoa + Tuần
# Thân = Sửu (Phúc Đức), Vũ Tham Miếu + Hóa Kỵ Đắc  
# Niên Hạn 2026 = Dần (trùng Điền Trạch, Cự Dương Vượng)
# Kim Tứ Cục, Dương Nam, Thuận Lý → ĐV đi thuận từ 4 tuổi

# Cung vị mapping (SOT): 12 cung theo thứ tự
# Hợi=Mệnh, Tý=Phụ Mẫu, Sửu=Phúc Đức[Thân], Dần=Điền Trạch, Mão=Quan Lộc, 
# Thìn=Nô Bộc, Tỵ=Thiên Di, Ngọ=Tật Ách, Mùi=Tài Bạch,
# Dậu=Phu Thê, Thân=Tử Tức, Tuất=Huynh Đệ

MONTHLY_SOT = {
    1: {"cung": "Mão", "house": "Quan Lộc", "sao": "Tướng Hãm + Triệt + Hỏa Đắc + Khôi"},
    2: {"cung": "Thìn", "house": "Nô Bộc", "sao": "Cơ Miếu + Lương Miếu + Hóa Lộc Vượng"},
    3: {"cung": "Tỵ", "house": "Thiên Di", "sao": "Tử Vi Miếu + Thất Sát Vượng + Hóa Quyền"},
    4: {"cung": "Ngọ", "house": "Tật Ách", "sao": "VCD (mượn Đồng Âm Vượng từ Tý)"},
    5: {"cung": "Mùi", "house": "Tài Bạch", "sao": "VCD (mượn Vũ Tham Kỵ Miếu từ Sửu) + Hình Hãm"},
    6: {"cung": "Thân", "house": "Tử Tức", "sao": "VCD + Ân Quang + Đại Hao"},
    7: {"cung": "Dậu", "house": "Phu Thê", "sao": "Liêm Hãm + Phá Hãm + Linh Hãm + Đào Vượng"},
    8: {"cung": "Tuất", "house": "Huynh Đệ", "sao": "VCD + Tuần + Địa Không Hãm + Đà La Đắc"},
    9: {"cung": "Hợi", "house": "Mệnh", "sao": "Thiên Phủ Đắc + Lộc Tồn Đắc + Hóa Khoa + Tuần"},
    10: {"cung": "Tý", "house": "Phụ Mẫu", "sao": "Đồng Vượng + Âm Vượng + Kiếp Hãm + Kình Hãm"},
    11: {"cung": "Sửu", "house": "Phúc Đức [Thân]", "sao": "Vũ Khúc Miếu + Tham Lang Miếu + Hóa Kỵ Đắc"},
    12: {"cung": "Dần", "house": "Điền Trạch", "sao": "Cự Môn Vượng + Thái Dương Vượng + Triệt + Mã Đắc"}
}

# Deep impact analyses rewritten with CORRECT data
IMPACT_V3 = {
    1: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Mão) là cung Quan Lộc gốc, có Triệt đóng. Mão tam hợp Hợi (Mệnh) — kênh 20% liên kết nguyệt hạn thẳng về Mệnh. Đại Vận hiện tại (Dần-Điền) kề sát bên trái Mão, tạo cấu trúc **Giáp cung ĐV-NH** cực kỳ mạnh.
> **Kết luận:** Triệt tại Mão (Quan) là cấu trúc CỐ ĐỊNH 10 năm ĐV4 — sự nghiệp chính thống bị cắt ngang KHÔNG phải do vận xấu nhất thời, mà do *thiết kế* của Đại Vận Điền Trạch: 10 năm này yêu cầu anh dồn sức xây TÀI SẢN (Dần), không phải leo thang chức vụ (Mão). Gốc Mệnh Phủ Đắc (Hợi) tam hợp Mão = vẫn hậu thuẫn ngầm, nhưng Phủ bị Tuần phong nên lộc chỉ rỉ chảy, không xối.
> **Hành động:** Không cướp đường sự nghiệp chính thống. Cứ xây hạ tầng (CDMS, AI Agent, BĐS) — Đại Vận Điền hỗ trợ tối đa cho tài sản tích lũy.""",

    2: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Thìn-Nô Bộc) kề bên phải Đại Vận (Dần-Điền). Cơ Lương Miếu + Hóa Lộc tại Nô = Brain Trust engine. Thìn nhị hợp Dậu (Phu Thê) = mạng lưới liên hệ mật với đối tác/vợ chồng. Gốc Thân (Sửu-Vũ Tham Kỵ) giáp trái cung Nô (Thìn) = Pháo Đài tài chính kề ngay mạng lưới.
> **Kết luận:** ĐV4 Điền (Dần) + NH Nô (Thìn) = chiến lược "Dùng mạng lưới xây tài sản" vận hành tối ưu. Lộc Vượng tại Nô được Gốc Thân (Vũ Tham) giáp bên trái hút thẳng vào Pháo Đài. Gốc Mệnh (Phủ Hợi) tam hợp Mão (kề trái Thìn) = liên hoàn hỗ trợ.
> **Hành động:** Bung mạng lưới chuyên gia. Mời cộng sự review CDMS, đi giao lưu y khoa, nhờ partner check deal CK.""",

    3: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Tỵ-Thiên Di) xung chiếu trực diện Gốc Mệnh (Hợi-Phủ). Tử Sát Quyền (Tỵ) đối mặt Phủ Lộc Khoa (Hợi) = Đế Vương ra trận giao chiến KHO VÀNG. ĐV Điền (Dần) tam hợp Ngọ+Tuất, không trực tiếp can thiệp Tỵ — NH tháng này hoạt động khá ĐỘC LẬP so với ĐV.
> **Kết luận:** Gốc Mệnh Phủ Đắc đủ lực phòng thủ khi Tử Sát đánh thẳng. Vì ĐV đang Điền (xây tài sản) nên sức chiến tại Thiên Di lấy năng lượng từ Niên Hạn (Dần-Cự Nhật) nhị hợp Hợi (Mệnh) = Mặt Trời Dần soi đường cho Phủ Hợi kháng cự. Quyền lực ngoại giao cực đỉnh, nhưng gốc nội lực (Phủ Tuần) đang kiệt → áp lực dội ngược.
> **Hành động:** Chốt sale, ký hợp đồng, báo cáo Ban Giám Đốc — tận dụng Tử Quyền. Nhưng NGAY SAU ĐÓ phải rút về nạp lực.""",

    4: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Ngọ-Tật Ách) nằm trong tam hợp Dần-Ngọ-Tuất. ĐV Điền (Dần) = gốc tam hợp → NH T4 bị ĐV chi phối TRỰC TIẾP qua tam hợp. VCD tại Ngọ mượn Đồng Âm Vượng (Tý) = bệnh mượn, stress ẩn từ bên ngoài. Gốc Thân (Sửu) kề trái Tý (Phụ Mẫu nơi Kiếp Kình đóng) = bệnh tật cũ gõ cửa.
> **Kết luận:** Tam hợp Dần(ĐV)-Ngọ(NH)-Tuất(Huynh) tạo Hỏa cục thiêu đốt trực tiếp bản mệnh Kim. Đây là hệ quả cơ học của cấu trúc ĐV4 gặp NH Ách: Toàn bộ năng lượng xây tài sản (Dần) đốt cháy sinh lực (Ngọ) và mạng lưới anh em (Tuất). Gốc Mệnh (Phủ Hợi) nhị hợp Dần (ĐV) nhưng Phủ Tuần yếu → bơm cứu sinh chậm.
> **Hành động:** DỪNG mọi dự án mới. Kiểm tra sức khỏe. Không lướt sóng CK. Ngủ đủ giấc.""",

    5: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Mùi-Tài Bạch) xung chiếu trực diện Gốc Thân (Sửu-Vũ Tham Kỵ). Trục Sửu-Mùi là trục TÀI-PHÚC — mũi khoan Kỵ (Sửu) xuyên thẳng vào VCD Hình Hãm (Mùi). ĐV Điền (Dần) giáp phải Mão (Quan-Triệt) = đòn bẩy ĐV không vươn tới Mùi, phải qua 3 cung trung gian → ĐV KHÔNG che chắn được trục Tài.
> **Kết luận:** Đây KHÔNG phải tháng xui ngẫu nhiên — mà là kích nổ có toán học của trục Sửu-Mùi gốc: Kỵ "khóa kho" PHẢN chuyển thành "khóa thanh khoản" khi NH rơi đúng Mùi. ĐV Điền (Dần) cách xa Mùi (5 cung) → KHÔNG CAN THIỆP ĐƯỢC. Gốc Mệnh Phủ (Hợi) tam hợp Mùi = tuyến phòng thủ duy nhất, nhưng Phủ bị Tuần → chỉ cản 50%.
> **Hành động:** Phòng thủ thanh khoản TUYỆT ĐỐI. Ôm tiền mặt. Không ký văn bản pháp lý.""",

    6: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Thân-Tử Tức) tam hợp Tý (Phụ Mẫu) + Thìn (Nô). VCD mượn chiếu Dần (Cự Nhật) = ĐV Điền. ĐV Điền chiếu thẳng vào NH Thân qua đối cung = ĐV CHI PHỐI MẠNH tháng này. Gốc Mệnh (Phủ Hợi) không có kênh trực tiếp đến Thân → Nguyệt hạn chạy theo ĐV, không theo Mệnh.
> **Kết luận:** Năng lượng Đại Hao (Thân) + chiếu từ Cự Nhật ĐV → chi tiêu tái cơ cấu phục vụ chiến lược tài sản dài hạn. Khác hẳn tháng 5 (mất mát do xung chiếu): tháng 6 là CHI TIỀN CÓ CHỦ ĐÍCH để xây nền tảng ĐV.
> **Hành động:** Đầu tư hạ tầng (server, công cụ AI, sửa nhà). Dọn dẹp hệ thống.""",

    7: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Dậu-Phu Thê) xung chiếu Mão (Quan Lộc-Triệt), nơi kề cạnh ĐV (Dần). Bộ Liêm Phá Hãm (Dậu) bắn thẳng vào Quan Lộc-Triệt = đòn giáng kép vào sự nghiệp. Gốc Thân (Sửu) tam hợp Tỵ+Dậu (Kim cục) = Thân kích hoạt mạnh tháng này → cái tôi bùng nổ. Dậu = ĐẾ VƯỢNG (Tràng Sinh) = năng lượng Kim cực đại.
> **Kết luận:** Đế Vượng + Liêm Phá Hãm = CHÁY BÙNG. Sự bất ổn Thê tháng này gián tiếp qua xung chiếu phá vỡ khu vực Quan-ĐV (Mão-Dần), làm rung lắc cả nền tảng tài sản đang xây. Gốc Mệnh (Phủ Hợi) nhị hợp Dần (ĐV) vẫn giữ = bền, nhưng cuộc chiến tình cảm ở Dậu sẽ thiêu đốt sinh lực.
> **Hành động:** Không đưa ra tối hậu thư trong mọi mối quan hệ. Minh bạch hóa kế hoạch kinh doanh cho đối tác yên tâm.""",

    8: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Tuất-Huynh Đệ) nằm trong tam hợp Dần(ĐV)-Ngọ-Tuất = Hỏa cục. ĐV (Dần) trực tiếp cộng hưởng NH qua tam hợp. Tuất VCD+Tuần+Không = mặt ngoài tối tăm. Nhưng tam hợp Dần (Cự Nhật Vượng ĐV) soi rọi ánh sáng ngầm xuyên tam hợp. Gốc Thân (Sửu) nhị hợp chặt Tý, cách Tuất 2 cung = vẫn gián tiếp bơm.
> **Kết luận:** Niên Hạn 2026 (Dần) + ĐV4 (Dần) = TRÙNG KHÍT → năng lượng Cự Nhật rót toàn lực qua tam hợp vào Tuất. Dù Tuất rỗng bề ngoài, kênh ngầm cực mạnh. Dark Pool kích hoạt chính xác = tháng gom hàng CK bị ruồng bỏ.
> **Hành động:** Hoạt động ngầm, kín kẽ. Gom mã chứng khoán chiến lược khi F0 bi quan. Chỉ chia sẻ với 1-2 cộng sự lõi.""",

    9: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn trùng khít Gốc Mệnh (Hợi-Phủ Lộc Khoa Tuần). Năng lượng hồi quy 100% về nguồn. Hợi nhị hợp Dần (ĐV Điền + Niên Hạn) = kết nối Mệnh-ĐV mạnh nhất năm. Gốc Thân (Sửu) tam hợp Tỵ+Dậu = trục Kim cục hoạt động song song, không can thiệp trực tiếp.
> **Kết luận:** "Tuần Triệt đương đầu": Mệnh có Tuần (phòng thủ), ĐV Dần có Triệt (phá vỡ). Nhị hợp Hợi-Dần kết nối 2 lực đối nghịch → xung đột nội tại. Triệt (ĐV) đòi phá Tuần (Mệnh) để giải phóng Phủ Lộc bị phong ấn. Tháng 9 = Ground Zero của cuộc tái cấu trúc bản ngã 10 năm.
> **Hành động:** Nhẫn nại tuyệt đối. Mọi rườm rà hành chính (viện, dự án) là hệ quả cào xé Tuần. Đừng cưỡng lại.""",

    10: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn (Tý-Phụ Mẫu) giáp trái Gốc Mệnh (Hợi). Đồng Âm Vượng + Kiếp Kình Hãm = áp lực mạnh từ bề trên dội thẳng vào Mệnh qua kênh giáp 5%. ĐV Điền (Dần) nhị hợp Hợi (Mệnh) NHƯNG Tý cách Dần 2 cung → ĐV không can thiệp được Phụ Mẫu. Gốc Thân (Sửu) kề phải Tý = giáp Thân-Phụ = áp lực cha mẹ chọc thẳng vào Pháo Đài tài chính.
> **Kết luận:** Bộ Kiếp+Kình Hãm tại Phụ Mẫu là cấu trúc CỐ ĐỊNH = mối quan hệ với cấp trên/phụ huynh luôn mang dao kéo. Khi NH rơi đúng Tý, vết thương này kích hoạt tối đa. Nhưng Đồng Âm Vượng là nền tảng cực mạnh = có ĐAU nhưng không CHẾT.
> **Hành động:** Giải quyết việc gia đình cha mẹ trước. Không khởi động project mới. Tạo vùng đệm hậu phương.""",

    11: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn trùng khít Gốc Thân (Sửu-Vũ Tham Kỵ Miếu). Năng lượng tài chính hồi quy 100% về nguồn Pháo Đài. Sửu tam hợp Tỵ(Di-Tử Quyền)+Dậu(Thê-Đế Vượng) = toàn bộ Kim cục KÍCH HOẠT. Sửu giáp trái ĐV Điền (Dần) = Pháo Đài kề ngay Đại Vận xây tài sản. Nhật Nguyệt Giáp Sửu trực tiếp (Dương V Dần + Âm V Tý) = cách cục CÁT CỰC ĐẠI.
> **Kết luận:** Vũ Tham Miếu + Kỵ Đắc Phản Vi Giai + NH trùng Thân + Kim cục kích hoạt + Nhật Nguyệt Giáp = ĐỈNH CAO TÀI CHÍNH NĂM. Tuy nhiên, Kỵ đi kèm thị phi (Hóa Kỵ ôm Thân = bản thân gánh chịu tiếng nói đố kỵ). Gốc Mệnh (Phủ Hợi) nhị hợp Dần (ĐV) đang dõi theo, nhưng không kiểm soát trực tiếp Sửu → anh ở thế solo.
> **Hành động:** Thu hoạch tài chính trong tĩnh lặng. 'Mặc áo giáp, kiếm tiền trong sương mù.' Tuyệt đối không khoe khoang.""",

    12: """> ➯ **PHÂN TÍCH TÁC ĐỘNG & KẾT LUẬN QUY CHIẾU:**
> **Hình học:** Nguyệt Hạn trùng khít Đại Vận (Dần-Điền) VÀ Niên Hạn (Dần). BA TẦNG TRÙNG PHÙNG tại một điểm = sự kiện 'Nhật Thực' trong Tử Vi. Cự Nhật Vượng + Triệt + Mã Đắc. Hợi (Mệnh) nhị hợp Dần = kết nối Mệnh-ĐV-NH-Nguyệt đạt mức tối đa. Gốc Thân (Sửu) giáp trái Dần = Pháo Đài ngay cạnh.
> **Kết luận:** Toàn bộ chiều dài 2026 quy tụ đổ xô vào tháng này. Triệt tại Dần vẫn còn nhưng đã nhả ~70-80% ở tuổi 34+ → Cự Nhật bắt đầu phát hào quang. Mã Đắc tại Điền = tài sản di dời, tái cơ cấu. Tháng này = BẢN THIẾT KẾ cho cả thập kỷ ĐV4 được "review tổng" trước khi bước sang 2027.
> **Hành động:** Tổng kết danh mục CK, tái cơ cấu BĐS, rà soát kiến trúc Agent. Thưởng thức thành quả trong tĩnh tại."""
}

def generate_corrected_block(month):
    data = MONTHLY_SOT[month]
    cung = data["cung"]
    house = data["house"]
    sao = data["sao"]
    analysis = IMPACT_V3[month]
    
    block = [
        "##### 🌐 QUY CHIẾU ĐA TẦNG (Nguyệt Hạn ⊂ Niên Hạn ⊂ Đại Vận ⊂ Gốc) — SOT Verified ✅",
        "",
        "| Cấp Độ | Cung Vị | Tinh Bàn (SOT) | Mức Chi Phối |",
        "|---|---|---|---|",
        "| **Gốc Mệnh** | Hợi | Thiên Phủ Đắc + Lộc Tồn Đắc + Hóa Khoa + Tuần | ⭐⭐⭐ Hệ quy chiếu tối hậu |",
        "| **Gốc Thân (Phúc Đức)** | Sửu | Vũ Khúc Miếu + Tham Lang Miếu + Hóa Kỵ Đắc (Phản Vi Giai) | ⭐⭐⭐ Pháo Đài tài chính |",
        f"| **Gốc Chức Năng ({house})** | {cung} | {sao} | ⭐⭐⭐ Cung gốc theo chủ đề tháng |",
        "| **Đại Vận 4 (34-43t)** | Dần (Điền Trạch) | Cự Môn Vượng + Thái Dương Vượng + Triệt + Mã Đắc | ⭐⭐⭐ Thập kỷ quản trị tài sản |",
        "| **Niên Hạn 2026 (Bính Ngọ)** | Dần (Điền Trạch) | Trùng ĐV4 → Năng lượng Cự Nhật x2 | ⭐⭐ Chủ đề của năm |",
        f"| **Nguyệt Hạn T{month}** | {cung} ({house}) | Chịu tác động đồng thời từ 5 lớp trên | ⭐ Biến động ngắn hạn |",
        "",
        analysis,
        ""
    ]
    return block

def inject_corrected(file_path):
    print(f"[v3 SOT-VERIFIED] Rewriting Multi-Layer in {file_path}...")
    content = Path(file_path).read_text(encoding='utf-8')
    lines = content.split('\n')
    out_lines = []
    
    i = 0
    current_month = 1
    skip_mode = False
    
    while i < len(lines):
        line = lines[i]
        
        m = re.search(r'THÁNG (\d+) ÂM LỊCH', line, re.IGNORECASE)
        if not m:
            m = re.search(r'THÁNG (\d+)', line, re.IGNORECASE)
        if m and line.startswith('### '):
            current_month = int(m.group(1))

        if skip_mode:
            if line.startswith('##### HỆ QUY CHIẾU KINH ĐIỂN'):
                skip_mode = False
                block = generate_corrected_block(current_month)
                out_lines.extend(block)
                out_lines.append(line)
            i += 1
            continue

        if line.startswith('##### 🌐 QUY CHIẾU ĐA TẦNG'):
            skip_mode = True
            i += 1
            continue
            
        out_lines.append(line)
        i += 1
        
    Path(file_path).write_text('\n'.join(out_lines), encoding='utf-8')
    apply_hoa_ky_guardrails_to_file(file_path)
    print(f"[v3 SOT-VERIFIED] Complete: {file_path}")

inject_corrected('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md')
inject_corrected('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md')
