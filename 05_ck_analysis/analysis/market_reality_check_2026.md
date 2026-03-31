# Market Reality Check 2026

- As of: `2026-03-29`
- Calendar anchor: `2026-03-29` = `11/2/Binh Ngo` (tuan 2 thang 2 am lich)
- Anchor source: https://baonghean.vn/am-duong-lich-ngay-29-thang-3-nam-2026.html
- Anchor benchmark_ref: `CAL-01`

## Scope

- Audit id: `t2_lunar_midmonth_2026`
- Prediction source: `T2 am lich trong luan_giai_12_thang_2026`
- File: `/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md`

## Observed Metrics

- Broad market: VN-Index `2026-03-19` 1699.13 -> `2026-03-27` 1672.80 = `-1.55%`
- Broad market benchmark_ref: start=`MKT-01` / end=`MKT-02`
- Bank/catalyst basket (2026-03-13 -> 2026-03-27): average return = `+2.07%`
- Basket benchmark_ref: `MKT-02`
- Basket detail: SHB +3.01%, MBB +0.00%, TCB +2.17%, VPB +3.12%
- Basket vs broad market = `+3.62%`

## Claim Audit

- `t2_broad_market_sideway`: `partial`
  Prediction: CK/Macro T2: 5/10 - trung tinh. CK sideway, focus networking.
  Metric: `broad_return_pct` = `-1.55%`
  Note: abs(return)=1.55% vuot sideway chat, nhung chua den muc pha vo luan de.
- `t2_selective_not_broad`: `supported`
  Prediction: Song Cat nham BDS/ha tang va mang luoi, khong phai broad bull market cho CK.
  Metric: `basket_vs_broad_pct` = `+3.62%`
  Note: outperformance=3.62% xac nhan thi truong phan hoa theo catalyst.
- `t2_hold_shb_watch`: `supported`
  Prediction: Giam sat SHB tang von. Chua mua them.
  Metric: `basket_avg_return_pct` = `+2.07%`
  Note: basket_return=2.07% chua tao missed move lon; giu/watch van chap nhan duoc.

## RCA

- Loi goc khong nam o viec T2 'sai 100%'. Loi goc la he thong dang tron `broad market`, `basket/sector`, va `single-name catalyst` vao mot lop dien giai.
- Du lieu thuc te hien tai cho thay broad market giam nhe, trong khi basket bank-catalyst van outperform. Vi vay tu 'sideway' la qua tho, con logic 'chon loc, khong broad bull' thi gan hon su that.
- Score thang 8/10 cho Nhan-Khi/Nho-Boc de bi nguoi doc hieu lan sang CK. Tu nay phai tach rieng market regime layer khoi social/networking layer.

## Derived Rules

- Khoa ngay am-duong bang ngay duong cu the truoc khi danh gia dung/sai.
- Tach it nhat 3 lop: `broad market`, `sector/basket`, `single-name catalyst`.
- Sau moi giai doan dang song, phai co report outcome va ha/giu confidence theo du lieu that.

## Sources

- https://baonghean.vn/am-duong-lich-ngay-29-thang-3-nam-2026.html
- https://www.vndirect.com.vn/la-ban-thi-truong-19-03-2026-vn-index-giam-0-9-sau-khi-fed-va-ecb-dong-loat-giu-nguyen-lai-suat/
- Local snapshot: `/Users/mac/Desktop/TuViStock/05_ck_analysis/monthly_updates/2026_03_snapshot_28mar.md`
- Local basket start: `/Users/mac/Desktop/TuViStock/05_ck_analysis/monthly_updates/2026_03_snapshot_13mar.md`
- Local basket end: `/Users/mac/Desktop/TuViStock/05_ck_analysis/monthly_updates/2026_03_snapshot_28mar.md`

