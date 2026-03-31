import re
import sys
from pathlib import Path
from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file

MONTHLY_DATA = {
    1: {"cung": "Mão", "house": "Quan Lộc", "sao": "Tướng Hãm + Triệt"},
    2: {"cung": "Thìn", "house": "Nô Bộc", "sao": "Cơ Lương Miếu + Lộc Vượng"},
    3: {"cung": "Tỵ", "house": "Thiên Di", "sao": "Tử Sát Vượng"},
    4: {"cung": "Ngọ", "house": "Tật Ách", "sao": "VCD (mượn Đồng Âm)"},
    5: {"cung": "Mùi", "house": "Tài Bạch", "sao": "VCD + Hình Hãm"},
    6: {"cung": "Thân", "house": "Tử Tức", "sao": "VCD + Đại Hao"},
    7: {"cung": "Dậu", "house": "Phu Thê", "sao": "Liêm Phá Hãm"},
    8: {"cung": "Tuất", "house": "Huynh Đệ", "sao": "VCD + Không + Đà Đắc"},
    9: {"cung": "Hợi", "house": "Mệnh", "sao": "Thiên Phủ Đắc + Tuần"},
    10: {"cung": "Tý", "house": "Phụ Mẫu", "sao": "Đồng Âm Vượng + Kiếp Kình Hãm"},
    11: {"cung": "Sửu", "house": "Phúc / Thân", "sao": "Vũ Tham Miếu + Hóa Kỵ"},
    12: {"cung": "Dần", "house": "Điền Trạch", "sao": "Cự Dương Vượng + Triệt"}
}

def generate_table(month):
    data = MONTHLY_DATA[month]
    cung = data["cung"]
    house = data["house"]
    sao = data["sao"]
    
    table = [
        "##### 🌐 QUY CHIẾU ĐA TẦNG (Nguyệt Hạn ⊂ Niên Hạn ⊂ Đại Vận ⊂ Gốc)",
        "| Cấp Độ | Cung Vị | Tình Trạng / Tinh Bàn | Mức Chi Phối |",
        "|---|---|---|---|",
        "| **Gốc (Mệnh/Thân)** | Hợi (Phủ) / Sửu (Vũ Tham) | Tích lũy nền tảng vững chắc, quyền bính ngầm | ⭐⭐⭐ Hệ quy chiếu tối hậu |",
        f"| **Gốc ({house})** | {cung} | {sao} | ⭐⭐⭐ Năng lượng cội nguồn |",
        "| **Đại Vận (33-42)** | Mão (Quan Lộc) | Tướng Hãm + Triệt (Đập đi xây lại hệ thống) | ⭐⭐⭐ Định hình thập kỷ |",
        "| **Niên Hạn 2026** | Dần (Điền Trạch) | Cự Dương Vượng (Sáng sủa, thâu tóm tài sản) | ⭐⭐ Chủ đề của năm |",
        f"| **Nguyệt Hạn T{month}** | {cung} ({house}) | Chịu tác động đồng thời từ 4 lớp trên | ⭐ Biến động ngắn hạn |",
        ""
    ]
    return table

def inject_multi_layer(file_path):
    print(f"Injecting Multi-Layer matrices into {file_path}...")
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

        if line.startswith('##### HỆ QUY CHIẾU KINH ĐIỂN'):
            # Double check we haven't already injected it recently
            if len(out_lines) > 0 and 'QUY CHIẾU ĐA TẦNG' not in '\n'.join(out_lines[-15:]):
                table_lines = generate_table(current_month)
                out_lines.extend(table_lines)
                
        out_lines.append(line)
        i += 1
        
    Path(file_path).write_text('\n'.join(out_lines), encoding='utf-8')
    apply_hoa_ky_guardrails_to_file(file_path)
    print(f"Done injecting Multi-Layer into {file_path}")

inject_multi_layer('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md')
inject_multi_layer('/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md')
