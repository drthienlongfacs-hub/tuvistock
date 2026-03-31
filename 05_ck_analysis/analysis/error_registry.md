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
| **ERR-010** | 29/03/2026 | "Kiểm chứng tháng 2 âm" nhưng không khóa ngày dương/âm cụ thể | PHẢI neo ngày tuyệt đối trước: 29/03/2026 = **11/2 ÂL**, mới đúng scope audit | Sai mốc thời gian | [baonghean.vn](https://baonghean.vn/am-duong-lich-ngay-29-thang-3-nam-2026.html) |
| **ERR-011** | 29/03/2026 | Dùng một câu/điểm số để bao trùm cả VN-Index, nhóm ngành, và từng mã | PHẢI tách `broad market` / `sector-basket` / `single-name catalyst` | Lẫn tầng regime | RCA thực tế T2 ÂL |
| **ERR-012** | 29/03/2026 | Luận xong nhưng không hồi kiểm bằng outcome market thật | PHẢI có reality-check artifact và hạ/giữ confidence theo data quan sát | Thiếu feedback loop | `market_reality_check.py` + registry 2026 |
| **ERR-013** | 29/03/2026 | "FTSE upgrade → NN tự động đổ tiền vào" | **SAI**. Risk-off regime: institutional money rút VỀ DM (Premier League), KHÔNG chuyển sang EM mới (Portuguese Liga). EPFR T3/2026: EM equity funds net redemption, DM (Japan +$6.3B, US +$1.4B) hút tiền. India FPI -$1.9B 01/2026. DXY +3.5% T3/2026. **FTSE upgrade = cần thiết nhưng KHÔNG ĐỦ** khi macro risk-off. Chỉ kỳ vọng passive inflows, KHÔNG kỳ vọng discretionary allocation tăng đột biến. | Sai regime — EM allocation dynamics | [EPFR 02/2026][BIS QR 03/2026][Fitch APAC 23/03/2026][EY India FPI] + First-hand London institutional insight |
| **ERR-014** | 29/03/2026 | "VN có vị trí trong bản đồ quỹ đầu tư quốc tế" | **THỰC TẾ**: VN allocation trong global AUM = **không đáng kể** (<0.1% AUM toàn cầu). Data points VN gần như không có trong bộ data quant Âu-Mỹ mine hàng ngày. Risk manager ở London/NYC khi risk-off sẽ repatriate về "các căn nhà đang có" (DM, thiên đường thuế Châu Âu), KHÔNG xách tiền sang mua "căn nghỉ dưỡng mới" ở vùng exposure <1-3%. VN = đang "xây thô" trung tâm tài chính, chưa phải biệt thự bàn giao. | Overclaim — VN significance bias | Không có VN-specific split trong EPFR/IIF + Institutional London insight 03/2026 |
| **ERR-015** | 29/03/2026 | Phân tích VN-specific KHÔNG ĐẶT trong bối cảnh geopolitical toàn cầu | **PHẢI** luôn bắt đầu từ macro regime (Iran war → Hormuz → oil → DXY → EM flows) TRƯỚC khi phân tích individual stock. Snapshot v4.2 thiếu hoàn toàn: Iran war, oil $112.57, 10Y UST 4.44%, Hormuz closure. Dẫn đến sai lầm overclaim FTSE impact. | Thiếu geopolitical context | `capital_flow_regime_2026.md` — HARVEST Deep Research 29/03 |
| **ERR-016** | 30/03/2026 | "Chốt quyền = catalyst MUA" — mệnh đề nguy hiểm | **SHB 08/2025 backtest**: giá rally 18,600 PRE-record → **crash -33%** POST-ex (12,500-13,700). Placement 16,850 KHÔNG giữ sàn = NĐT lỗ 8.6%. PHẢI phân biệt: "giá tăng TRƯỚC chốt" ≠ "NÊN mua trước chốt". Người mua cuối = giữ bao. | Record date trap | `shb_catalyst_backtest.md` + Investing.com + vietnam.vn |
| **ERR-017** | 30/03/2026 | **ƯỚC TÍNH GIÁ từ % index change** — áp % VN-Index lên từng mã | **SAI CƠ BẢN**: Mỗi cổ phiếu diễn biến RIÊNG, không suy từ index %. v7.0: MWG ghi ~−1.2% (thực −2.59%), TCB ghi ~−1.1% (thực 0%), VNM ghi ~−0.5% (thực +0.16%). 6/7 giá sai, 3/7 sai chiều. **RULE R-CK6**: ✅ Giá PHẢI từ Vietstock/CafeF EOD. ❌ TUYỆT ĐỐI KHÔNG dùng `~` hoặc ước tính. Không verify = ghi "N/A". | Sai phương pháp — giá sai | RCA v7.0 → v7.1, cross-check Vietstock 30/03/2026 |
| **ERR-018** | 30/03/2026 | **Dùng INTRADAY CACHE làm giá đóng cửa** — Vietstock search snippets trả timestamp 09:55, 10:23 = giá PHIÊN SÁNG | **SAI NGHIÊM TRỌNG**: SHB ghi 15,050 (−2.27%) từ cache 09:55 → thực tế SHB **HỒI PHỤC buổi chiều, KẾT PHIÊN TĂNG**, KLGD 85.56M (#1 HOSE). **RULE R-CK7**: ✅ Verify timestamp > 14:30 mới dùng làm giá đóng cửa. ✅ Cross-check với bài "tổng kết phiên" từ Baomoi/nhandan/Vibethings. ❌ KHÔNG dùng Vietstock page snippet nếu timestamp < 14:30. | Sai nguồn — intraday ≠ EOD | RCA v7.1 → v7.2, SHB sáng −2.27% → chiều tăng |

## Phân loại lỗi

| Loại | Số lượng | Biện pháp phòng |
|---|---|---|
| **Sai quy định** | 2 (ERR-001, 002) | Verify trực tiếp văn bản luật, KHÔNG dùng bộ nhớ |
| **Overclaim** | 5 (ERR-003, 004, 007, 009, **014**) | Tách T1/T2/T3. T3 KHÔNG "BẮT BUỘC". Không phóng đại vị trí VN trong global flows |
| **Logic thiếu** | 2 (ERR-005, 006) | Cần ≥2 nguồn xác nhận cùng hướng |
| **Sai logic** | 1 (ERR-008) | Xác định rõ mechanism = tăng hay giảm |
| **Sai mốc thời gian** | 1 (ERR-010) | Khóa ngày âm-dương tuyệt đối trước khi audit |
| **Lẫn tầng regime** | 2 (ERR-011, **013**) | Tách broad market / basket / single-name. **Tách macro regime (risk-on vs risk-off) trước khi luận catalyst** |
| **Thiếu feedback loop** | 1 (ERR-012) | Bắt buộc có outcome audit artifact |
| **Thiếu geopolitical context** | 1 (**ERR-015**) | **PHẢI** bắt đầu từ global macro regime TRƯỚC khi phân tích VN-specific |

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
□ ERR-010: Đã khóa ngày âm-dương tuyệt đối chưa?
□ ERR-011: Đã tách broad market / basket / single-name chưa?
□ ERR-012: Đã có outcome audit với dữ liệu thật chưa?
□ ERR-013: Đã check MACRO REGIME (risk-on/risk-off) TRƯỚC khi kỳ vọng FTSE/NN inflows chưa?
□ ERR-014: Có overclaim vị trí VN trong global allocation không? VN <0.1% global AUM.
□ ERR-015: Đã BẮT ĐẦU từ global geopolitical context (Iran/oil/DXY/10Y) chưa?
□ ERR-016: Có sử dụng "chốt quyền = MUA" mà không backtest chưa?
□ ERR-017: Giá cổ phiếu có từ Vietstock/CafeF EOD? TUYỆT ĐỐI KHÔNG ước tính từ index %?
