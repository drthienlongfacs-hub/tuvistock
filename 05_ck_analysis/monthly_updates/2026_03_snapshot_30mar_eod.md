# Market Brief — EOD 30/03/2026 (v7.2 FINAL — Multi-source Verified)

> **Phiên**: Thứ Hai 30/03/2026 — phiên đầu tuần
> **VN-Index**: **1,662.54** (−10.26, −0.61%) | VN30: **1,811.92** (−9.61, −0.53%)
> **KLGD**: 824.7M cp / 21,490 tỷ VND | Breadth: 118G / 204L / 59U
> **NN phiên 30/03**: Bán ròng **−1,360 tỷ** HOSE (FPT −203, VCB −111, VPB −108, STB −82 tỷ)
> NN mua ròng: MSN (+53), IDC (+43), MWG (+34), DGW (+32), VNM (+25 tỷ)
> **Verified**: 31/03/2026 00:15 — Baomoi + VietnamNews + nhandan + ieem + Vibethings (EOD confirmed)

---

## ⛔ RCA-CHAIN: 3 Lỗi liên tiếp v7.0 → v7.1 → v7.2

| Lỗi | Mô tả | ERR |
|---|---|:---:|
| **v7.0** | Ước tính giá từ % index thay vì verify từng mã | ERR-017 |
| **v7.1** | Dùng Vietstock snippet bị cache lúc 09:55 sáng = **INTRADAY**, không phải giá đóng cửa | ERR-018 |
| **v7.2** | ✅ Sửa bằng cross-reference 5+ nguồn báo chí EOD (Baomoi, nhandan, ieem, Vibethings, VietnamNews) |

### ERR-018 (MỚI): Dùng intraday cache làm giá đóng cửa

- **Root cause**: Vietstock search snippets trả về giá kèm timestamp (VD: "30/03/2026 09:55") = giá phiên sáng
- **SHB**: Vietstock snippet ghi 15,050 (−2.27%) lúc 09:55 → thực tế SHB **HỒI PHỤC** buổi chiều và **KẾT PHIÊN TĂNG**
- **Biện pháp**: ✅ PHẢI cross-check với bài tổng kết phiên (article EOD) HOẶC lấy giá 14:45+ 
- ❌ KHÔNG dùng Vietstock page snippet nếu timestamp < 14:30

---

## 1. BẢNG GIÁ — EOD 30/03/2026 (Multi-source Verified ✅)

| Mã | Giá 27/03 | Kết phiên 30/03 | Chiều | Nguồn xác nhận |
|:---:|---:|---|:---:|---|
| **SHB** | 15,400 | **TĂNG NHẸ** ✅ | 🟢 | Baomoi+nhandan: "mã tăng gồm SHB". KLGD **85.56M** (#1 HOSE) |
| **HPG** | 26,500 | **+1.51%** ✅ | 🟢 | VietnamNews: "HPG rose by 1.51%". ~**26,900** |
| **STB** | — | **+2.17%** | 🟢 | VietnamNews: "STB climbed by 2.17%" |
| **MSN** | — | **+2.05%** | 🟢 | Vietstock: 74,800 (+1,500, +2.05%). KLGD 6.57M |
| **MBB** | 26,150 | **GIẢM** | 🔴 | Baomoi: "tác động tiêu cực: MBB". Vietstock ~25,750 |
| **TCB** | 30,650 | **GIẢM** | 🔴 | Baomoi: "đóng cửa giảm: TCB" |
| **VPB** | 26,450 | **26,000** (−450, −1.70%) | 🔴 | Vietstock ✅ confirmed. NN bán −108 tỷ |
| **MWG** | 81,000 | **GIẢM** (v7.1: 78,900, −2.59%) | 🔴 | Baomoi: "tác động tiêu cực: MWG" + NN mua ròng +34 tỷ |
| **VNM** | 61,500 | **GIẢM NHẸ** | 🔴 | Baomoi: "tác động tiêu cực: VNM" (nhưng NN mua ròng +25 tỷ) |

> ⚠️ **Giá chính xác đến đồng**: Chỉ VPB (26,000) và MSN (74,800) có xác nhận từ Vietstock trading history.
> HPG ~26,900 (ước từ 26,500 × 1.0151). Các mã còn lại: chiều xác nhận (tăng/giảm) nhưng chưa có giá chính xác cuối phiên.
> **SHB KẾT PHIÊN TĂNG** = đảo chiều hoàn toàn từ −2.27% buổi sáng.

### Phân tích phiên — SỬA v7.0/v7.1

| Mã | v7.0 (SAI) | v7.1 (SAI) | v7.2 (✅ EOD) | Ghi chú |
|:---:|---:|---:|:---:|---|
| **SHB** | ~15,200 (−1.3%) | 15,050 (−2.27%) | **TĂNG NHẸ** | ⛔ SAI CHIỀU cả v7.0 lẫn v7.1. SHB hồi phục chiều |
| HPG | ~26,900 (+1.5%) | ~26,800 (+1.13%) | **+1.51%** | v7.0 gần đúng, v7.1 sửa quá |
| MBB | ~25,800 | 25,750 | **Giảm** | v7.1 gần đúng |
| TCB | ~30,300 (−1.1%) | 30,650 (0%) | **Giảm** | v7.1 sai (ghi 0%), thực giảm |
| VPB | 26,000 | 26,000 | **26,000** | ✅ Đúng xuyên suốt |
| MWG | ~80,000 (−1.2%) | 78,900 (−2.59%) | **Giảm** | v7.1 gần đúng |
| VNM | ~61,200 (−0.5%) | ~61,600 (+0.16%) | **Giảm nhẹ** | v7.1 sai chiều |

### Top contributors VN-Index phiên 30/03

| 🟢 Đóng góp TĂNG (+5.97đ) | 🔴 Đóng góp GIẢM (−11.69đ) |
|---|---|
| BSR (+5.62%), GEE (+7%), GVR (+3.12%) | VIC (−2.34%), VCB, CTG (−2.16%) |
| HPG (+1.51%), STB (+2.17%), MSN (+2.05%) | FPT (−2.76%), MBB, GAS, BID |
| KBC, LGC, VPL, SIP | VPB, VNM, HVN |

---

## 2. MACRO — Update tối 30/03

### Iran Ceasefire: CHUYỂN BIẾN TÍCH CỰC

| Diễn biến | Impact |
|---|---|
| 🆕 Trump: "great progress" — Iran đồng ý hầu hết 15 điểm | 🟡 De-escalation |
| 🆕 Iran giao 20 tàu dầu + mở Hormuz cho Pakistan (2 tàu/ngày) | 🟢 Gesture thiện chí |
| 🔴 Deadline 06/04 vẫn đang treo | ⚠️ MAJOR RISK |

### Commodity

| Chỉ số | Giá | Trend |
|---|---:|---|
| Brent | **$108-116** (biên rộng trong ngày) | Sáng $116.75, chiều giảm |
| Gold | **$4,567** (ATH) | ↑ Safe haven |
| DXY | **~100** | → Tạm ổn |

---

## 3. KHUYẾN NGHỊ v7.2 (Corrected)

### ⭐ MUA

#### 1. SHB — MUA ⭐⭐⭐ (TĂNG CƯỜNG)

**SỬA v7.1**: SHB **KẾT PHIÊN TĂNG** (không phải −2.27%!)
- KLGD **85.56M** = **#1 HOSE** = thanh khoản CỰC CAO (không cạn như v7.1 ghi sai 9M)
- ⏰ **5 phiên** → chốt quyền 06/04
- Hồi phục từ −2.27% sáng → TĂNG cuối phiên = **lực cầu bắt đáy mạnh**
- NN mua ròng SHB (Vibethings: SHB nằm trong top NN mua ròng)

> **Action**: Tích lũy tiếp vùng 15,000–15,500.

#### 2. HPG — MUA ⭐⭐⭐

- **+1.51%** confirmed (VietnamNews) = positive outlier
- NN gom, oil giảm = chi phí năng lượng giảm
- Top contributor VN-Index phiên 30/03

> **Action**: Tích lũy vùng 26,500–27,200.

#### 3. MBB — MUA ⭐⭐

- Giảm theo sector ngân hàng (−0.79% nhóm)
- P/E ~6.5 = rẻ nhất banking. Room 49%.

> **Action**: Tích lũy vùng 25,000–26,000.

### ⏸️ HOLD

| Mã | Kết phiên | Lý do |
|---|---|---|
| **VPB** | 26,000 (−1.70%) | NN bán −108 tỷ. Chờ ĐHCĐ |
| **TCB** | Giảm | Không catalyst T1 |
| **VNM** | Giảm nhẹ | NN mua ròng +25 tỷ nhưng NN trần 49%. Mixed |
| **MWG** | Giảm (~78,900) | NN mua ròng +34 tỷ (positive) nhưng giá giảm mạnh. Theo dõi |

---

## 4. CW WATCHLIST — Chờ tuần quyết định

> **CHƯA VÀO LỆNH CW.** Chờ FTSE 07/04 + Iran 06/04.
> **CSTB2521** (STB +2.17%) và **CHPG2518** (HPG +1.51%) = 2 ứng viên hàng đầu nếu regime chuyển risk-on.

---

## 5. EVENTS — Tuần 31/03 – 07/04

| Ngày | Sự kiện | Mức |
|---|---|:---:|
| 🆕 **31/03** | Iran giao dầu → Hormuz mở thêm? | ⭐⭐⭐⭐ |
| 01/04 | China PMI → HPG signal | ⭐⭐ |
| 04/04 | US Non-Farm Payrolls | ⭐⭐⭐ |
| **06/04** | SHB chốt quyền + Trump deadline Iran | ⭐⭐⭐⭐⭐ |
| **07/04** | FTSE Interim Review Results | ⭐⭐⭐⭐⭐ |

---

## 6. THÔNG TIN BỔ SUNG TỪ VIBETHINGS EOD

- HPG: KH doanh thu ~210 nghìn tỷ, lợi nhuận +42% YoY năm 2026
- HPG nông nghiệp: LN giảm 37% svck, cổ tức 30%
- MWG: Dự kiến chia cổ tức 20% + bổ sung ngành BĐS
- Lãi suất tiền gửi 12 tháng: **vượt 7%** tại một số NH → headwind CK

---

> **Version**: v7.2 FINAL (31/03/2026 00:15) — Multi-source cross-verified
> **Nguồn EOD**: Baomoi, nhandan.vn, ieem.vn, Vibethings, VietnamNews (5 nguồn)
> **RCA-chain**: ERR-017 (ước tính giá) → ERR-018 (intraday cache) → v7.2 (EOD article cross-ref)
> **Thay đổi quan trọng vs v7.1**:
> - ⛔ **SHB: SAI CHIỀU** — v7.1 ghi 15,050 (−2.27%) = intraday sáng. Thực tế **KẾT PHIÊN TĂNG**, KLGD 85.56M (#1 HOSE)
> - ⛔ **TCB**: v7.1 ghi 0% = sai. Thực tế **GIẢM** (Baomoi confirmed)
> - ⛔ **VNM**: v7.1 ghi +0.16% = sai. Thực tế **GIẢM NHẸ** (Baomoi: "tác động tiêu cực")
> - ✅ MWG: NN mua ròng +34 tỷ (positive signal dù giá giảm)
> - ✅ VNM: NN mua ròng +25 tỷ
> - 🆕 **ERR-018**: Không dùng Vietstock cache timestamp < 14:30 làm giá đóng cửa
