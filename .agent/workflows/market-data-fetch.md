---
description: Lấy số liệu CK real-time bằng read_url_content — thay thế browser scraping và API. RCA-043 proven.
---

# Market Data Fetch — SOP Chuẩn (RCA-043)

> **Trigger:** Khi cần cập nhật số liệu cổ phiếu
> **Proven:** 02/04/2026 — 7 mã trong <5 giây, 0 hang, ~100 token
> **Thay thế:** Browser scraping (~50 calls), API scripts (hang/fail)

## Bước 1: Fetch giá real-time bằng `read_url_content`

// turbo-all

Gọi `read_url_content` cho mỗi mã trong watchlist:

```
URL pattern: https://cafef.vn/du-lieu/hose/{symbol}-{company}.chn
```

Watchlist mặc định:
1. `cafef.vn/du-lieu/hose/shb-ngan-hang-thuong-mai-co-phan-sai-gon-ha-noi.chn`
2. `cafef.vn/du-lieu/hose/mbb-ngan-hang-thuong-mai-co-phan-quan-doi.chn`
3. `cafef.vn/du-lieu/hose/vpb-ngan-hang-thuong-mai-co-phan-viet-nam-thinh-vuong.chn`
4. `cafef.vn/du-lieu/hose/hpg-cong-ty-co-phan-tap-doan-hoa-phat.chn`
5. `cafef.vn/du-lieu/hose/stb-ngan-hang-thuong-mai-co-phan-sai-gon-thuong-tin.chn`
6. `cafef.vn/du-lieu/hose/vhm-cong-ty-co-phan-vinhomes.chn`
7. `cafef.vn/du-lieu/hose/vic-tap-doan-vingroup-cong-ty-co-phan.chn`

**Gọi TẤT CẢ SONG SONG** (parallel tool calls).

## Bước 2: Parse OG Description

Dữ liệu nằm trong `OG Description` tag:

```
Giá cổ phiếu ( chiều  02/04/2026): 14.850 VNĐ. Khối lượng 46.899.800. Vốn hóa tt: 68.216,5 tỷ VNĐ
```

Parse ra: **Giá | Volume | Vốn hóa | Timestamp**

## Bước 3: Validate (Gate E5)

- [ ] E5.1: Source = cafef.vn (B1) ✅
- [ ] E5.2: Method = read_url_content ✅
- [ ] E5.3: Date = ngày giao dịch hiện tại ±1? → check OG tag date
- [ ] E5.5: Ghi timestamp vào output

## Bước 4: Format tổng hợp

```markdown
| Mã  | Giá     | Volume     | Vốn hóa   | Timestamp |
|-----|---------|------------|-----------|-----------|
| SHB | 14,850  | 46,899,800 | 68,217 tỷ | chiều 02/04 |
```

## Bước 5: So sánh với phiên trước (nếu cần OHLCV chi tiết)

Nếu cần Open/High/Low/Close đầy đủ → dùng Browser scraping CafeF lịch sử giao dịch (backup method).

## Quy tắc bắt buộc

| # | Quy tắc | Tham chiếu |
|---|---------|-----------|
| 1 | KHÔNG dùng API VN stock (CafeF/TCBS/SSI/VND) | QT-10 |
| 2 | Ưu tiên read_url_content > Browser > Perplexity | QT-11 |
| 3 | Timeout ≤5s, fallback nếu fail | QT-12 |
| 4 | Validate date, reject nếu stale >1 ngày | QT-13 |
