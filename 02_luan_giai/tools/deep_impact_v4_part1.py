#!/usr/bin/env python3
"""Deep Impact v4 — 20x expansion T1-T6. SOT-verified."""
import re
from pathlib import Path

# SOT Geometric Table (kiem_ke_tinh_ban_12_cung.md L258-271)
GEO = {
    "Hợi": {"house":"Mệnh","xung":"Tỵ(Di)","th1":"Mão(Quan)","th2":"Mùi(Tài)","nhi":"Dần(Điền)","hai":"Thân(Tử)","g1":"Tý(Phụ)","g2":"Tuất(Huynh)"},
    "Tý": {"house":"Phụ Mẫu","xung":"Ngọ(Ách)","th1":"Thân(Tử)","th2":"Thìn(Nô)","nhi":"Sửu(Phúc)","hai":"Mùi(Tài)","g1":"Sửu(Phúc)","g2":"Hợi(Mệnh)"},
    "Sửu": {"house":"Phúc [Thân]","xung":"Mùi(Tài)","th1":"Tỵ(Di)","th2":"Dậu(Thê)","nhi":"Tý(Phụ)","hai":"Ngọ(Ách)","g1":"Tý(Phụ)","g2":"Dần(Điền)"},
    "Dần": {"house":"Điền Trạch","xung":"Thân(Tử)","th1":"Ngọ(Ách)","th2":"Tuất(Huynh)","nhi":"Hợi(Mệnh)","hai":"Tỵ(Di)","g1":"Sửu(Phúc)","g2":"Mão(Quan)"},
    "Mão": {"house":"Quan Lộc","xung":"Dậu(Thê)","th1":"Hợi(Mệnh)","th2":"Mùi(Tài)","nhi":"Tuất(Huynh)","hai":"Thìn(Nô)","g1":"Dần(Điền)","g2":"Thìn(Nô)"},
    "Thìn": {"house":"Nô Bộc","xung":"Tuất(Huynh)","th1":"Thân(Tử)","th2":"Tý(Phụ)","nhi":"Dậu(Thê)","hai":"Mão(Quan)","g1":"Mão(Quan)","g2":"Tỵ(Di)"},
    "Tỵ": {"house":"Thiên Di","xung":"Hợi(Mệnh)","th1":"Sửu(Phúc)","th2":"Dậu(Thê)","nhi":"Thân(Tử)","hai":"Dần(Điền)","g1":"Thìn(Nô)","g2":"Ngọ(Ách)"},
    "Ngọ": {"house":"Tật Ách","xung":"Tý(Phụ)","th1":"Dần(Điền)","th2":"Tuất(Huynh)","nhi":"Mùi(Tài)","hai":"Sửu(Phúc)","g1":"Tỵ(Di)","g2":"Mùi(Tài)"},
    "Mùi": {"house":"Tài Bạch","xung":"Sửu(Phúc)","th1":"Hợi(Mệnh)","th2":"Mão(Quan)","nhi":"Ngọ(Ách)","hai":"Tý(Phụ)","g1":"Ngọ(Ách)","g2":"Thân(Tử)"},
    "Thân": {"house":"Tử Tức","xung":"Dần(Điền)","th1":"Tý(Phụ)","th2":"Thìn(Nô)","nhi":"Tỵ(Di)","hai":"Hợi(Mệnh)","g1":"Mùi(Tài)","g2":"Dậu(Thê)"},
    "Dậu": {"house":"Phu Thê","xung":"Mão(Quan)","th1":"Sửu(Phúc)","th2":"Tỵ(Di)","nhi":"Thìn(Nô)","hai":"Tuất(Huynh)","g1":"Thân(Tử)","g2":"Tuất(Huynh)"},
    "Tuất": {"house":"Huynh Đệ","xung":"Thìn(Nô)","th1":"Ngọ(Ách)","th2":"Dần(Điền)","nhi":"Mão(Quan)","hai":"Dậu(Thê)","g1":"Dậu(Thê)","g2":"Hợi(Mệnh)"},
}

# Tràng Sinh 12 cung (Kim Tứ Cục, Dương Nam, Thuận)
TRANG_SINH = {
    "Tỵ":"Trường Sinh 🌱","Ngọ":"Mộc Dục 🛁","Mùi":"Quan Đới 🎓",
    "Thân":"Lâm Quan 🏛️","Dậu":"Đế Vượng 👑","Tuất":"Suy 📉",
    "Hợi":"Bệnh 🤒","Tý":"Tử 💀","Sửu":"Mộ ⚱️",
    "Dần":"Tuyệt ❌","Mão":"Thai 🤰","Thìn":"Dưỡng 🍼"
}

# Lưu Nguyệt Can for Bính Ngọ year 
# T1:Canh Dần, T2:Tân Mão, T3:Nhâm Thìn, T4:Quý Tỵ, T5:Giáp Ngọ, T6:Ất Mùi
# T7:Bính Thân, T8:Đinh Dậu, T9:Mậu Tuất, T10:Kỷ Hợi, T11:Canh Tý, T12:Tân Sửu
MONTH_CAN = {1:"Canh",2:"Tân",3:"Nhâm",4:"Quý",5:"Giáp",6:"Ất",7:"Bính",8:"Đinh",9:"Mậu",10:"Kỷ",11:"Canh",12:"Tân"}
TU_HOA_CAN = {
    "Canh": "Dương Lộc→Dần(Điền), Vũ Quyền→Sửu(Thân), Âm Khoa→Tý(Phụ), Đồng Kỵ→Tý(Phụ)",
    "Tân": "Cự Lộc→Dần(Điền), Dương Quyền→Dần(Điền), Xương Khoa→Dậu(Thê), Xương Kỵ→Dậu(Thê)",
    "Nhâm": "Lương Lộc→Thìn(Nô), Tử Quyền→Tỵ(Di), Phủ Khoa→Hợi(Mệnh), Vũ Kỵ→Sửu(Thân)",
    "Quý": "Phá Lộc→Dậu(Thê), Cự Quyền→Dần(Điền), Âm Khoa→Tý(Phụ), Tham Kỵ→Sửu(Thân)",
    "Giáp": "Liêm Lộc→Dậu(Thê), Phá Quyền→Dậu(Thê), Vũ Khoa→Sửu(Thân), Dương Kỵ→Dần(Điền)",
    "Ất": "Cơ Lộc→Thìn(Nô), Lương Quyền→Thìn(Nô), Tử Khoa→Tỵ(Di), Âm Kỵ→Tý(Phụ)",
    "Bính": "Đồng Lộc→Tý(Phụ), Cơ Quyền→Thìn(Nô), Xương Khoa→Dậu(Thê), Liêm Kỵ→Dậu(Thê)",
    "Đinh": "Âm Lộc→Tý(Phụ), Đồng Quyền→Tý(Phụ), Cơ Khoa→Thìn(Nô), Cự Kỵ→Dần(Điền)",
    "Mậu": "Tham Lộc→Sửu(Thân), Âm Quyền→Tý(Phụ), Hữu Khoa→Tý(Phụ), Cơ Kỵ→Thìn(Nô)",
    "Kỷ": "Vũ Lộc→Sửu(Thân), Tham Quyền→Sửu(Thân), Lương Khoa→Thìn(Nô), Xương Kỵ→Dậu(Thê)",
}

MONTH_CUNG = {1:"Mão",2:"Thìn",3:"Tỵ",4:"Ngọ",5:"Mùi",6:"Thân",7:"Dậu",8:"Tuất",9:"Hợi",10:"Tý",11:"Sửu",12:"Dần"}
MONTH_SAO = {
    1: "Tướng Hãm (Nhâm Thủy) + Triệt + Hỏa Tinh Đắc + Thiên Khôi",
    2: "Cơ Miếu (Ất Mộc) + Lương Miếu (Ất Mộc) + Hóa Lộc Vượng (Thổ)",
    3: "Tử Vi Miếu (Mậu Thổ) + Thất Sát Vượng (Canh Kim) + Hóa Quyền + Văn Khúc Đắc + Thiên Việt",
    4: "VCD (mượn Đồng Vượng Nhâm Thủy + Âm Vượng Quý Thủy từ Tý) + L.Kình Dương",
    5: "VCD (mượn Vũ Miếu Canh Kim + Tham Miếu Giáp Thủy/Mộc + Kỵ Đắc từ Sửu) + Hình Hãm (Hỏa)",
    6: "VCD (mượn Cự Vượng + Dương Vượng từ Dần) + Ân Quang + Đại Hao Đắc + L.Thiên Mã",
    7: "Liêm Hãm (Đinh Hỏa) + Phá Hãm (Nhâm Thủy) + Linh Hãm (Hỏa) + Đào Vượng + Xương Bình + L.Khoa + L.Kỵ",
    8: "VCD (mượn Cơ Lương Miếu từ Thìn) + Tuần + Không Hãm + Đà Đắc + Khốc Hãm + Tang Hãm",
    9: "Phủ Đắc (Mậu Thổ) + Lộc Tồn Đắc (Kỷ Thổ) + Hóa Khoa + Tuần + Riêu Hãm + Cô Thần",
    10: "Đồng Vượng (Nhâm Thủy) + Âm Vượng (Quý Thủy) + Bật Miếu + L.Lộc + Kiếp Hãm + Kình Hãm",
    11: "Vũ Miếu (Canh Kim) + Tham Miếu (Giáp Thủy/Mộc) + Kỵ Đắc (Phản Vi Giai) + Thanh Long + Nguyệt Đức",
    12: "Cự Vượng (Quý Thủy) + Dương Vượng (Bính Hỏa) + Triệt + Mã Đắc (Hỏa) + Tả Phù + Giải Thần",
}

DEEP_T = {}
DEEP_T[1] = """
> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — BẢN ĐỒ KẾT NỐI NGUYỆT HẠN T1 (MÃO)**
>
> | Kênh | Đích | Tinh bàn đích | Sức kết nối |
> |---|---|---|---|
> | **Xung chiếu** | Dậu (Phu Thê) | Liêm Hãm + Phá Hãm + Linh Hãm + Đào V + L.Khoa + L.Kỵ | ⛔ Dậu BẮN THẲNG ↔ Mão — Thê xung Quan |
> | **Tam hợp 1** | Hợi (Mệnh) | Phủ Đắc + Lộc Tồn + Khoa + Tuần | ⭐ Mệnh HẬU THUẪN sự nghiệp |
> | **Tam hợp 2** | Mùi (Tài Bạch) | VCD + Hình Hãm + Quốc Ấn + Hồng | 🟡 Tài liên kết Quan — tiền gắn sự nghiệp |
> | **Nhị hợp** | Tuất (Huynh) | VCD + Tuần + Không Hãm + Đà Đắc + Khốc + Tang | ⚠️ Anh em rỗng — kênh yếu |
> | **Giáp trái** | Dần (Điền=ĐV4) | Cự V + Dương V + Triệt + Mã Đắc | ⭐⭐ **ĐẠI VẬN KỀ SÁT** — Giáp cung ĐV-NH cực mạnh |
> | **Giáp phải** | Thìn (Nô Bộc) | Cơ M + Lương M + Hóa Lộc V | ⭐ Brain Trust kề bên phải — nguồn cứu sinh |
> | **Lục hại** | Thìn (Nô Bộc) | (trùng giáp phải) | Mài mòn ngầm từ mạng lưới |
>
> **Kết luận Hình học:** Mão bị Dậu (Thê) bắn xung chiếu = MỌI vấn đề sự nghiệp T1 đều có bóng dáng hôn nhân/đối tác phía đối diện. NHƯNG được ĐV4 (Dần-Điền) giáp trái = toàn bộ năng lượng 10 năm "Quản trị tài sản" đổ ngay bên cạnh sự nghiệp. Và Cơ Lương Lộc (Nô) giáp phải = Brain Trust sẵn sàng hỗ trợ. **Mão bị kẹp giữa 2 lực CÁT (Dần+Thìn) mặc dù bản thân Mão hung.**
>
> ---
> **II. NGŨ HÀNH CƠ HỌC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh KIM vs Cung Mão MỘC | Kim khắc Mộc = **CHỦ ĐỘNG CẮT** | Anh CẮT BỎ quy trình cũ, tái cấu trúc. Không bị cung ép — anh ÉP cung |
> | Tướng (THỦY) vs Mão (MỘC) | Thủy sinh Mộc = **Sinh xuất** | Tướng nuôi cung → hao kiệt → "Ấn hết mực" |
> | Hỏa Đắc (HỎA) vs Mão (MỘC) | Mộc sinh Hỏa = **Hỏa cực vượng** | Hỏa kích hoạt mạnh nhất — "lửa rèn kiếm" |
> | Triệt (KIM) vs Mão (MỘC) | Kim khắc Mộc = **cắt đứt** | Sự nghiệp chính thống bị cắt ngang cấu trúc |
>
> **Chuỗi phản ứng:** Anh (Kim) → khắc cung (Mộc) → Tướng (Thủy) bị rút cạn nuôi cung → Hỏa Đắc bùng lên từ cung Mộc → Triệt (Kim) cắt thêm → **Hệ quả: sự nghiệp chính thống GÃY, nhưng LỬA PHI TRUYỀN THỐNG bùng nổ.** Y khoa không lên chức, nhưng CDMS/AI Agent bùng.
>
> ---
> **III. ĐẠI VẬN (DẦN-ĐIỀN) × NGUYỆT HẠN (MÃO-QUAN)**
>
> ĐV4 tại Dần **giáp trái** Mão = khoảng cách 1 cung = **MỐI LIÊN HỆ MẬT NHẤT có thể giữa ĐV và NH.**
>
> - ĐV Điền (tài sản) giáp Quan (sự nghiệp) = 10 năm này, sự nghiệp PHỤC VỤ tài sản, không phải ngược lại. Mỗi quyết định sự nghiệp phải hỏi: "Nó có tạo TÀI SẢN TÍCH LŨY không?"
> - Cự Nhật Vượng (ĐV) soi sáng Tướng Hãm (Mão) qua giáp = "Mặt Trời buổi sáng rọi vào kho ấn hết mực" → tri thức (Cự) + ánh sáng (Dương) THAY THẾ cho dấu ấn chính thống.
> - Triệt tại cả ĐV (Dần) lẫn NH (Mão) = **Song Triệt** — đường chính thống bị khóa kép. NHƯNG Triệt đã nhả ~70-80% ở tuổi 34 → đường phi truyền thống BẮT ĐẦU MỞ.
>
> ---
> **IV. NIÊN HẠN 2026 (DẦN) × NGUYỆT HẠN (MÃO)**
>
> Niên Hạn TRÙNG ĐV tại Dần → năng lượng Cự Nhật x2 → sức soi rọi gấp đôi. Dần giáp Mão = Niên Hạn cũng giáp NH → **BA TẦNG (ĐV + Niên + Nguyệt) kề nhau liền mạch Dần-Mão.**
>
> ---
> **V. PHI TINH KÍCH HOẠT — Can Canh (T1)**
>
> | Phi | Sao | Phi vào | Hiện tượng |
> |---|---|---|---|
> | Lộc | Thái Dương | Dần (Điền=ĐV) | ⭐ Lộc BƠM vào ĐV Điền → tài sản tăng giá trị |
> | Quyền | Vũ Khúc | Sửu (Thân=Pháo Đài) | ⭐ Pháo Đài NÂNG QUYỀN — tiền bạc cứng cáp |
> | Khoa | Thái Âm | Tý (Phụ Mẫu) | Tri thức từ cấp trên/mẹ — lời khuyên sáng suốt |
> | Kỵ | Thiên Đồng | Tý (Phụ Mẫu) | ⚠️ Song Lộc-Kỵ tại Phụ → được mẹ/sếp giúp NHƯNG kèm phiền phức |
>
> **Tương tác Phi-NH:** Không Phi Tinh nào rơi trực tiếp vào Mão (NH). Song Lộc+Kỵ đánh Phụ Mẫu (Tý) = áp lực cha mẹ/sếp. Vũ Quyền bơm Pháo Đài = tài chính được gia cố. **NH T1 chạy "khô" — không có năng lượng Phi Tinh trực tiếp.** Phải mượn sức Giáp (Dần-Thìn).
>
> ---
> **VI. TRÀNG SINH: THAI 🤰 (2/10)**
>
> Kim tại Mão = **Thai** = mầm thai nghén, chưa hình thành. Ý tưởng mới đang **ẤP Ủ**, không có kết quả T1. Đây là giai đoạn "gieo hạt trong bóng tối" — nếu gieo đúng, sẽ nở T5-T7.
>
> ---
> **VII. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động cụ thể | Hành động |
> |---|---|---|
> | **Y khoa (BVBĐ)** | Tướng Hãm + Triệt = không thăng chức, không được giao quyền mới. Hỏa Đắc = khi ca mổ khó, anh tỏa sáng → quý nhân (Khôi) ghi nhận | Mổ robot, giải quyết case khó. KHÔNG đòi thăng chức |
> | **AI/CDMS** | ĐV Điền giáp Quan = xây hạ tầng CDMS là LÀM ĐÚNG đường ĐV4. Triệt cắt "deploy chính thức" → hệ thống chạy ngầm, chưa official | Xây module, test UAT. KHÔNG ép deadline deploy chính thức |
> | **CK/Đầu tư** | CK T1 = Thai (chưa hình thành). Triệt NÉN. Lưu Lộc→ĐV Điền | ❌ HOLD CHẶT. KHÔNG mua/bán. Giá SHB bị nén = đúng chu kỳ |
>
> **KẾT LUẬN TỔNG:** Tháng 1 = "Thai nghén trong bão" — bề mặt lung lay (Triệt+Tướng Hãm), bên trong đang ấp ủ (Thai). ĐV Điền giáp trái, Brain Trust giáp phải = 2 trụ cột đỡ lấy tháng yếu. **Chiến lược tối ưu: Xây ngầm, gieo hạt, không đòi hỏi kết quả tháng này.**
"""

DEEP_T[2] = """
> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — NGUYỆT HẠN T2 (THÌN — NÔ BỘC)**
>
> | Kênh | Đích | Tinh bàn | Nhận định |
> |---|---|---|---|
> | **Xung chiếu** | Tuất (Huynh) | VCD+Tuần+Không Hãm+Đà Đắc+Khốc+Tang | ⚠️ Đối cung rỗng — anh em không phản hồi |
> | **Tam hợp 1** | Thân (Tử Tức) | VCD+Ân Quang+Đại Hao | 🟡 Con cái gắn mạng lưới nhẹ |
> | **Tam hợp 2** | Tý (Phụ Mẫu) | Đồng V+Âm V+Bật M+Kiếp H+Kình H | ⭐⚠️ Phụ Mẫu mạnh nhưng hung kèm |
> | **Nhị hợp** | Dậu (Phu Thê) | Liêm Phá Hãm+Linh+Đào+L.Khoa+L.Kỵ | ⚠️ Thê liên hệ ngầm với Nô |
> | **Giáp trái** | Mão (Quan=Triệt) | Tướng H+Hỏa Đ+Khôi | 💼 Quan kề bên — sự nghiệp theo dõi mạng lưới |
> | **Giáp phải** | Tỵ (Di) | Tử Sát Quyền+Khúc Đ+Việt | ⭐ Quyền lực bên ngoài kề cạnh |
> | **Lục hại** | Mão (Quan) | (trùng giáp trái) | Mài mòn ngầm Quan↔Nô |
>
> **Kết luận Hình học:** Thìn (Nô) được giáp bởi Mão (Quan-sự nghiệp) và Tỵ (Di-ngoại giao) = **Mạng lưới nằm GIỮA sự nghiệp và thế giới bên ngoài** — đúng vai trò cầu nối. Gốc Thân (Sửu-Pháo Đài) giáp trái Dần (ĐV), giáp phải Tý, cách Thìn 3 cung → Pháo Đài liên kết gián tiếp qua tam hợp Thân-Tý-Thìn = **THỦY CỤC kích hoạt** — dòng chảy Thủy nuôi mạng lưới.
>
> ---
> **II. NGŨ HÀNH CƠ HỌC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh KIM vs Thìn THỔ | Thổ sinh Kim = **được nuôi** | Nô Bộc = nơi nuôi dưỡng bản mệnh — mạng lưới BƠM năng lượng |
> | Cơ+Lương (MỘC) vs Thìn (THỔ) | Mộc khắc Thổ = **sao khắc cung** | Cơ Lương phải gồng sức → mạng lưới CHẤT LƯỢNG nhưng vất vả |
> | Hóa Lộc (THỔ) vs Thìn (THỔ) | Thổ=Thổ = **đồng hành** | Lộc CỰC VƯỢNG tại đây — tiền từ bạn bè RẤT BỀN |
>
> ---
> **III. ĐẠI VẬN (DẦN) × NH (THÌN)**
>
> ĐV Dần cách Thìn **2 cung** (Dần→Mão→Thìn). Không giáp, không tam hợp, không nhị hợp. **ĐV tác động GIÁN TIẾP qua Mão (cầu nối).** Chuỗi: Dần(ĐV) giáp Mão giáp Thìn(NH) = **liên hoàn 3 cung liền** Dần-Mão-Thìn, nhưng sức truyền giảm qua mỗi cung. ĐV tập trung xây tài sản (Dần), NH tập trung bung mạng lưới (Thìn) = **mạng lưới PHỤC VỤ tài sản** — nhờ bạn bè/cộng sự để xây nền tảng. 
>
> ---
> **IV. PHI TINH — Can Tân (T2)**
>
> | Phi | Sao | Vào | Hiện tượng |
> |---|---|---|---|
> | Lộc | Cự Môn | Dần (Điền=ĐV) | ⭐⭐ **Song Lộc ĐV:** Gốc Dương Lộc + Lưu Cự Lộc → BĐS/tài sản được bơm Lộc cả tháng |
> | Quyền | Thái Dương | Dần (Điền=ĐV) | ⭐⭐ **Song Quyền ĐV:** Cự Lộc + Dương Quyền đồng phi Dần → ĐV BÙNG NỔ |
> | Khoa | Văn Xương | Dậu (Thê) | 📝 Tri thức hóa giải hôn nhân — lời nói nhẹ nhàng cứu vãn |
> | Kỵ | Văn Xương | Dậu (Thê) | ⚠️ **Song Kỵ Thê** (Xương Kỵ + L.Kỵ Liêm) → thị phi hôn nhân kép |
>
>  **Tương tác Phi-NH:** Song Lộc+Quyền đổ hết vào ĐV (Dần), KHÔNG vào NH (Thìn). Mạng lưới T2 chạy "tự nhiên" bằng nội lực Cơ Lương Lộc gốc — không cần Phi Tinh kích hoạt. BĐS/tài sản được bơm MẠNH NHẤT theo Phi Tinh. **Chiến lược: Dùng mạng lưới để xây tài sản (ĐV), không phải ngược lại.**
>
> ---
> **V. TRÀNG SINH: DƯỠNG 🍼 (3/10)**
>
> Kim tại Thìn = **Dưỡng** = đang được nuôi nấng, bú sữa. Mạng lưới ĐÃ TỒN TẠI nhưng đang ở giai đoạn "bé sơ sinh" — cần chăm sóc, không được ép chạy. Đúng Cơ Lương Miếu = hệ thống tri thức nuôi dưỡng tĩnh lặng.
>
> ---
> **VI. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động | Hành động |
> |---|---|---|
> | **Y khoa** | Nô=đồng nghiệp. Song Cát ĐV→Điền = tài sản hệ thống tăng giá trị | Trao đổi chuyên môn, review case, build protocol |
> | **AI/CDMS** | Song Lộc+Quyền vào ĐV=hạ tầng. Cơ Lương=chuyên gia | Mời reviewer CDMS, deploy UAT, build partnership |
> | **CK** | CK=5/10 trung tính. Song Cát đánh ĐV, không đánh Tài | 🔶 Trung tính. Giám sát SHB tăng vốn |
>
> **KẾT LUẬN:** T2 = "Vườn ươm nhân lực" — mạng lưới Brain Trust (Cơ Lương Lộc) là nguồn lực chính. Tất cả Phi Tinh cát đổ vào ĐV Điền = tài sản được bơm mạnh. Dùng mạng lưới xây tài sản, không ngược lại.
"""

DEEP_T[3] = """
> ➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**
>
> ---
> **I. HÌNH HỌC THIÊN BÀN — NGUYỆT HẠN T3 (TỴ — THIÊN DI)**
>
> | Kênh | Đích | Tinh bàn | Nhận định |
> |---|---|---|---|
> | **Xung chiếu** | **Hợi (GỐC MỆNH)** | Phủ Đắc+Lộc Tồn+Khoa+Tuần+Riêu H+Cô Thần | ⛔⭐ **TRỤC XUNG MỆNH-DI kích hoạt** — đối đầu trực diện Mệnh |
> | **Tam hợp 1** | Sửu (GỐC THÂN) | Vũ M+Tham M+Kỵ Đắc+Thanh Long+Nguyệt Đức | ⭐⭐ **PHÁO ĐÀI tam hợp Di** — hậu phương tài chính VỮ NG |
> | **Tam hợp 2** | Dậu (Phu Thê) | Liêm Phá Hãm+Linh+Đào+L.Khoa+L.Kỵ | ⚠️ Thê cũng trong KIM CỤC — vợ/chồng liên quan hoạt động ngoại giao |
> | **Nhị hợp** | Thân (Tử Tức) | VCD+Ân Quang+Đại Hao | 🟡 Con cái liên hệ ngầm |
> | **Giáp trái** | Thìn (Nô Bộc) | Cơ Lương Miếu+Lộc V | ⭐ Brain Trust hỗ trợ ngoại giao |
> | **Giáp phải** | Ngọ (Tật Ách) | VCD+Thái Tuế+L.Kình | ⚠️ Sức khỏe kề bên — hoạt động ngoại giao tiêu hao sinh lực |
> | **Lục hại** | Dần (Điền=ĐV4) | Cự V+Dương V+Triệt+Mã Đ | ⚠️ **ĐV Lục Hại NH** — Điền hại Di = tài sản ở nhà "cản" di chuyển |
>
> **Kết luận Hình học cực kỳ quan trọng:**
> 1. **Trục Xung Mệnh-Di (Hợi-Tỵ) kích hoạt** = Trận chiến TRUNG TÂM năm. Phủ Lộc Khoa (Mệnh) đối đầu Tử Sát Quyền (Di). Đây là thiết kế GỐC của lá số: ra ngoài = gặp kẻ mạnh.
> 2. **Tam hợp Tỵ-Sửu-Dậu = KIM CỤC kích hoạt** = Cỗ máy chiến đấu Hậu Vận bật công tắc. Vũ Tham Kỵ (Sửu-Pháo Đài) →  Tử Sát Quyền (Tỵ-Di) → Liêm Phá (Dậu-Thê) = **Toàn bộ trục KIM CHIẾN ĐẤU hoạt động tháng này.** 
> 3. **Lục Hại Dần-Tỵ** = ĐV4 (Điền) HẠI Di = mâu thuẫn ngầm: muốn xây tài sản (Dần) nhưng phải ra ngoài chiến đấu (Tỵ). **Không thể vừa ở nhà vừa ra trận** — phải chọn.
>
> ---
> **II. NGŨ HÀNH CƠ HỌC**
>
> | Tương tác | Cơ chế | Hệ quả |
> |---|---|---|
> | Bản Mệnh KIM vs Tỵ HỎA | Hỏa khắc Kim = **BỊ ÉP** | Ra ngoài = bị lửa nung — áp lực, thử thách. NHƯNG Kim được rèn = SẮC BÉN hơn |
> | Tử Vi (THỔ) tại Tỵ (HỎA) | Hỏa sinh Thổ = **Đế Tinh cực vượng** | Vua (Tử Vi) được lửa nuôi = uy quyền TỐI ĐA |
> | Thất Sát (KIM) tại Tỵ (HỎA) | Hỏa khắc Kim = **Kiếm bị nung** | Sát bị rèn = sắc bén nhưng hao tổn. "Thanh kiếm qua lò luyện" |
> | Hóa Quyền (MỘC) tại Tỵ (HỎA) | Mộc sinh Hỏa = **Quyền bùng nổ** | Quyền lực TĂNG BẠO LIỆT nhờ cung Hỏa nuôi |
>
> **Chuỗi phản ứng:** Tỵ (Hỏa) → nuôi Tử Vi (Thổ) → Đế Vương cực đỉnh → Sát (Kim) bị rèn sắc bén → Quyền (Mộc) bùng → Toàn bộ CHIẾU THẲNG vào Mệnh (Hợi-Thủy) → Mệnh Thủy DẬP LỬA = **xử lý bằng mềm mỏng, quy trình, trí tuệ (Khoa).**
>
> ---
> **III. ĐẠI VẬN (DẦN-ĐIỀN) × NH (TỴ-DI)**
>
> ĐV Dần và NH Tỵ có quan hệ **LỤC HẠI** (Dần-Tỵ) = mâu thuẫn cấu trúc:
> - ĐV yêu cầu **Ở NHÀ xây tài sản** (Điền)
> - NH đưa anh **RA NGOÀI chiến đấu** (Di)
> - Hại = 2 lực KÉO NGƯỢC nhau → stress nội tại
>
> **Cách hóa giải:** Hoạt động ngoại giao T3 phải PHỤC VỤ tài sản (ĐV). VD: hội nghị y khoa → ký hợp đồng CDMS = ra ngoài (Di) để mang tài sản về (Điền). Nếu ra ngoài "cho vui" mà không mang gì về → lãng phí NH cát + vi phạm ĐV.
>
> ---
> **IV. NIÊN HẠN (DẦN) × NH (TỴ)**
>
> Niên Hạn (Dần) cũng Lục Hại NH (Tỵ) = **Song Hại** (ĐV + Niên cùng Hại NH). Sức kéo ngược x2. NHƯNG: Niên (Dần-Cự Nhật V) nhị hợp Hợi (Mệnh) = **Năng lượng Niên Hạn chảy về Mệnh** → khi Tỵ bắn xung chiếu Hợi, Hợi được Niên (Dần) nhị hợp bơm thêm = **PHÒNG THỦ TĂNG CƯỜNG.** Mệnh Phủ Đắc + Lộc + Khoa + nhị hợp Cự Nhật = đủ sức hứng Tử Sát Quyền từ Tỵ.
>
> ---
> **V. PHI TINH — Can Nhâm (T3) — TRÙNG CAN BẢN MỆNH!**
>
> ⚡ **Đặc biệt:** Can T3 = Nhâm = TRÙNG can năm sinh Nhâm Thân → **Tứ Hóa Lưu Nguyệt TRÙNG Tứ Hóa Bản Mệnh:**
>
> | Phi | Sao | Vào | Trùng bản mệnh? | Hiện tượng |
> |---|---|---|---|---|
> | Lộc | Thiên Lương | Thìn (Nô) | ✅ TRÙNG khít! | ⭐⭐ **SONG LỘC NÔ** — Brain Trust sinh Lộc GẤP ĐÔI |
> | Quyền | Tử Vi | Tỵ (Di=NH!) | ✅ TRÙNG khít! | ⭐⭐ **SONG QUYỀN DI** — Tử Vi Song Quyền tại NH = ĐẾ VƯƠNG TOÀN LỰC |
> | Khoa | Thiên Phủ | Hợi (Mệnh) | ✅ TRÙNG khít! | ⭐⭐ **SONG KHOA MỆNH** — Trí tuệ + danh tiếng GẤP ĐÔI bảo vệ |
> | Kỵ | Vũ Khúc | Sửu (Thân) | ✅ TRÙNG khít! | ⭐⚠️ **SONG KỴ THÂN** — Kỵ kép khóa Pháo Đài = tiền bị giữ chặt |
>
> **Kết luận Phi Tinh T3:** CAN NHÂM TRÙNG BẢN MỆNH = **tháng anh hoạt động đúng tần số gốc nhất cả năm.** Tử Sát Quyền tại Di + Song Quyền (bản+lưu) = **UY QUYỀN CỰC ĐẠI khi ra ngoài.** Song Lộc Nô = mạng lưới bơm Lộc kép. Song Khoa Mệnh = trí tuệ + danh bảo vệ kép. NHƯNG Song Kỵ Thân = tiền bị khóa → **uy quyền không chuyển thành tiền ngay được.**
>
> ---
> **VI. TRÀNG SINH: TRƯỜNG SINH 🌱 (8/10)**
>
> Kim tại Tỵ = **Trường Sinh** = KHỞI NGUỒN. Mọi thứ BẮT ĐẦU ở đây. Di = "ra ngoài là được SINH" — phú: *"Trường Sinh tại Di = đi xa là sống."* Tháng 3 = tháng **SINH SẢN, KHỞI ĐẦU** — khởi động dự án mới, kết nối mới, chiến dịch mới.
>
> ---
> **VII. ÁP DỤNG THỰC TẾ 3 LĨNH VỰC**
>
> | Lĩnh vực | Tác động chi tiết | Hành động cụ thể |
> |---|---|---|
> | **Y khoa** | Song Quyền Di = uy quyền chuyên môn CỰC CAO khi ra ngoài. Hội nghị, thuyết trình = trận đánh mà anh THẮNG | Đăng ký báo cáo hội nghị. Soi case hiếm. Thể hiện chuyên môn phẫu thuật robot |
> | **AI/CDMS** | Song Khoa Mệnh = hệ thống trí tuệ được bảo vệ kép. Song Lộc Nô = đối tác review | Ký hợp đồng CDMS. Demo cho BV. Mời reviewer chuyên gia |
> | **CK** | 6.5/10 🟢. MSCI review T6 DL gần. Tử Quyền tại Di = CƠ HỘI BÊN NGOÀI. Song Kỵ Thân = tiền bị khóa → KHÔNG rút ra, phải HOLD | ✅ Kỳ vọng MSCI. HOLD SHB. KHÔNG mua thêm T3 (đợi T5) |
>
> **KẾT LUẬN:** T3 = **THÁNG CỰC ĐỈNH NGOẠI GIAO** (Trường Sinh + Tử Sát Song Quyền + Can Nhâm trùng bản mệnh). ĐV Lục Hại NH = ra ngoài phải MANG GÌ VỀ (tài sản). Song Kỵ Thân = tiền bị khóa → quyền lực chưa đổi thành tiền. Chiến lược: **Ra trận + Ký kết + Rút về.**
"""

# Save part 1 for now
SCRIPT_PATH = Path(__file__).parent
print("Part 1 (T1-T3) loaded. Run inject_all() after Part 2 is ready.")
