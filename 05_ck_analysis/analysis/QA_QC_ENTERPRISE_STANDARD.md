# QA/QC Enterprise Standard — CK x Tử Vi

> **Version**: v1.0  
> **Ngày**: 29/03/2026  
> **Phạm vi**: `05_ck_analysis/`, `02_luan_giai/` khi chạm đến CK, market audit, hoặc forecasting

## Mục tiêu

Biến workflow hiện tại từ `thẩm định thủ công` sang `QA/QC có gate, có benchmark, có reject condition`.

## Nguyên tắc gốc

1. `Evidence before narrative`
   Narrative chỉ được phép đứng sau benchmark data.
2. `Scope before conclusion`
   Phải khóa ngày âm-dương và cửa sổ quan sát trước khi đánh giá đúng/sai.
3. `Regime separation`
   Không trộn `broad market`, `sector/basket`, `single-name catalyst`.
4. `Primary-source priority`
   Giá, corporate action, policy phải dùng benchmark tier B1 trước.
5. `Fail-loud`
   Thiếu benchmark, sai scope, hoặc dùng source yếu làm chuẩn thì validator phải báo fail/warn rõ.

## Benchmark tiers

Tham chiếu máy đọc được nằm ở [benchmark_reference_catalog.json](/Users/mac/Desktop/TuViStock/05_ck_analysis/analysis/benchmark_reference_catalog.json#L1).

- `B1_primary_operational`
  Nguồn chuẩn để khóa ngày, giá, broad market, corporate action, policy.
- `B2_secondary_context`
  Nguồn bối cảnh/hỗ trợ; không đủ một mình để kết luận giá hay catalyst binding.
- `B3_prohibited_for_binding_claim`
  Không được dùng để chốt claim binding.
  Ví dụ: chatbot output, memory, analyst rumor, terminal chưa verify chéo.

## Gate levels

### QG-CK-E0 — Structure Gate

Pass khi:
- report có `version/date`
- có scope rõ
- có source path hoặc source URL
- không có file deprecated làm SOT

### QG-CK-E1 — Benchmark Gate

Pass khi:
- calendar anchor dùng benchmark B1
- broad market dùng benchmark B1
- single-name price dùng benchmark B1
- corporate action binding dùng filing/VSD/exchange-equivalent

### QG-CK-E2 — Logic Gate

Pass khi:
- tách đủ 3 lớp `broad market / basket / single-name`
- không lấy một điểm số/tháng bao trùm toàn bộ CK
- phân biệt `data observed`, `estimate`, `conditional`

### QG-CK-E3 — Outcome Gate

Pass khi:
- có outcome audit artifact
- claim được gắn `supported / partial / contradicted`
- confidence hoặc rule được cập nhật nếu outcome lệch

### QG-CK-E4 — Enterprise Release Gate

Chỉ PASS khi:
- E0, E1, E2, E3 đều pass
- không dùng source deprecated
- không có contradiction giữa benchmark mới và SOT nội bộ mà chưa giải thích

## Reject conditions

Reject ngay nếu có một trong các lỗi sau:

- dùng ngày âm lịch tương đối mà không có ngày dương cụ thể
- dùng giá CK VN từ Perplexity/chatbot làm benchmark
- dùng analyst note để gắn `binding catalyst`
- broad market và basket mâu thuẫn nhưng report không tách lớp
- file deprecated vẫn được dùng như SOT

## QA deliverables bắt buộc

Mỗi audit/forecast mức enterprise nên có:

1. `registry` máy đọc được
2. `report` markdown cho người đọc
3. `validator output`
4. `error log / feedback log`
5. `rule update` nếu phát hiện lỗi hệ thống

## Lệnh chuẩn

```bash
python3 /Users/mac/Desktop/TuViStock/02_luan_giai/tools/market_reality_check.py
python3 /Users/mac/Desktop/TuViStock/02_luan_giai/tools/market_qaqc_validator.py
```

## Cách dùng để đối sánh

- Nếu cần audit tháng đang sống: khóa ngày trước, rồi chạy `market_reality_check.py`
- Nếu cần publish/report: chạy tiếp `market_qaqc_validator.py`
- Nếu validator fail: sửa benchmark/scope/source trước, không được nhảy sang narrative
