#!/usr/bin/env python3
"""Audit lunar-month market claims against observed market data."""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "05_ck_analysis" / "analysis" / "market_reality_registry_2026.json"
REPORT_PATH = ROOT / "05_ck_analysis" / "analysis" / "market_reality_check_2026.md"


def load_registry(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def pct_change(start: float, end: float) -> float:
    if start == 0:
        return 0.0
    return ((end - start) / start) * 100.0


def classify_claim(claim: dict, metrics: dict) -> tuple[str, str]:
    observed = metrics[claim["metric"]]
    expected = claim["expected"]
    support_min = claim["support_range"][0]
    support_max = claim["support_range"][1]
    partial_min = claim["partial_range"][0]
    partial_max = claim["partial_range"][1]

    if expected == "neutral_sideways":
        abs_value = abs(observed)
        if support_min <= abs_value <= support_max:
            return "supported", f"abs(return)={abs_value:.2f}% nam trong vung sideway ho tro."
        if partial_min <= abs_value <= partial_max:
            return "partial", f"abs(return)={abs_value:.2f}% vuot sideway chat, nhung chua den muc pha vo luan de."
        return "contradicted", f"abs(return)={abs_value:.2f}% qua lon de goi la sideway."

    if expected == "selective_outperformance":
        if support_min <= observed <= support_max:
            return "supported", f"outperformance={observed:.2f}% xac nhan thi truong phan hoa theo catalyst."
        if partial_min <= observed <= partial_max:
            return "partial", f"outperformance={observed:.2f}% co dau hieu phan hoa nhung chua that manh."
        return "contradicted", f"outperformance={observed:.2f}% khong xac nhan duoc lua chon co catalyst."

    if expected == "hold_watch":
        if support_min <= observed <= support_max:
            return "supported", f"basket_return={observed:.2f}% chua tao missed move lon; giu/watch van chap nhan duoc."
        if partial_min <= observed <= partial_max:
            return "partial", f"basket_return={observed:.2f}% duong nhe; kha nang qua bao thu ton tai."
        return "contradicted", f"basket_return={observed:.2f}% qua manh; 'khong mua them' da bo lo co hoi ro."

    raise ValueError(f"unsupported expected value: {expected}")


def build_metrics(audit: dict) -> dict:
    broad = audit["broad_market"]
    basket = audit["basket"]
    broad_return = pct_change(broad["start"]["value"], broad["end"]["value"])

    basket_returns = {}
    for item in basket["components"]:
        basket_returns[item["ticker"]] = pct_change(item["start_value"], item["end_value"])

    basket_avg = sum(basket_returns.values()) / len(basket_returns)
    return {
        "broad_return_pct": broad_return,
        "basket_avg_return_pct": basket_avg,
        "basket_vs_broad_pct": basket_avg - broad_return,
        "basket_returns": basket_returns,
    }


def render_report(data: dict) -> str:
    audit = data["audits"][0]
    metrics = build_metrics(audit)

    claim_rows = []
    for claim in audit["claims"]:
        status, note = classify_claim(claim, metrics)
        claim_rows.append((claim, status, note))

    broad = audit["broad_market"]
    basket = audit["basket"]
    anchor = data["calendar_anchor"]
    basket_parts = ", ".join(
        f"{ticker} {ret:+.2f}%"
        for ticker, ret in metrics["basket_returns"].items()
    )

    lines = []
    lines.append("# Market Reality Check 2026")
    lines.append("")
    lines.append(f"- As of: `{data['as_of']}`")
    lines.append(
        f"- Calendar anchor: `{anchor['gregorian_date']}` = `{anchor['lunar_date']}` ({anchor['note']})"
    )
    lines.append(f"- Anchor source: {anchor['source_url']}")
    if anchor.get("benchmark_ref"):
        lines.append(f"- Anchor benchmark_ref: `{anchor['benchmark_ref']}`")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append(f"- Audit id: `{audit['id']}`")
    lines.append(f"- Prediction source: `{audit['prediction_source']['label']}`")
    lines.append(f"- File: `{audit['prediction_source']['path']}`")
    lines.append("")
    lines.append("## Observed Metrics")
    lines.append("")
    lines.append(
        f"- Broad market: VN-Index `{broad['start']['date']}` {broad['start']['value']:.2f} -> "
        f"`{broad['end']['date']}` {broad['end']['value']:.2f} = `{metrics['broad_return_pct']:+.2f}%`"
    )
    if broad["start"].get("benchmark_ref") or broad["end"].get("benchmark_ref"):
        lines.append(
            f"- Broad market benchmark_ref: start=`{broad['start'].get('benchmark_ref', '-')}` / "
            f"end=`{broad['end'].get('benchmark_ref', '-')}`"
        )
    lines.append(
        f"- Bank/catalyst basket ({basket['window']}): average return = `{metrics['basket_avg_return_pct']:+.2f}%`"
    )
    if basket.get("benchmark_ref"):
        lines.append(f"- Basket benchmark_ref: `{basket['benchmark_ref']}`")
    lines.append(f"- Basket detail: {basket_parts}")
    lines.append(f"- Basket vs broad market = `{metrics['basket_vs_broad_pct']:+.2f}%`")
    lines.append("")
    lines.append("## Claim Audit")
    lines.append("")
    for claim, status, note in claim_rows:
        lines.append(f"- `{claim['claim_id']}`: `{status}`")
        lines.append(f"  Prediction: {claim['text']}")
        lines.append(f"  Metric: `{claim['metric']}` = `{metrics[claim['metric']]:+.2f}%`")
        lines.append(f"  Note: {note}")
    lines.append("")
    lines.append("## RCA")
    lines.append("")
    lines.append("- Loi goc khong nam o viec T2 'sai 100%'. Loi goc la he thong dang tron `broad market`, `basket/sector`, va `single-name catalyst` vao mot lop dien giai.")
    lines.append("- Du lieu thuc te hien tai cho thay broad market giam nhe, trong khi basket bank-catalyst van outperform. Vi vay tu 'sideway' la qua tho, con logic 'chon loc, khong broad bull' thi gan hon su that.")
    lines.append("- Score thang 8/10 cho Nhan-Khi/Nho-Boc de bi nguoi doc hieu lan sang CK. Tu nay phai tach rieng market regime layer khoi social/networking layer.")
    lines.append("")
    lines.append("## Derived Rules")
    lines.append("")
    lines.append("- Khoa ngay am-duong bang ngay duong cu the truoc khi danh gia dung/sai.")
    lines.append("- Tach it nhat 3 lop: `broad market`, `sector/basket`, `single-name catalyst`.")
    lines.append("- Sau moi giai doan dang song, phai co report outcome va ha/giu confidence theo du lieu that.")
    lines.append("")
    lines.append("## Sources")
    lines.append("")
    lines.append(f"- {anchor['source_url']}")
    lines.append(f"- {broad['start']['source_url']}")
    lines.append(f"- Local snapshot: `{broad['end']['source_ref']}`")
    lines.append(f"- Local basket start: `{basket['start_ref']}`")
    lines.append(f"- Local basket end: `{basket['end_ref']}`")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit lunar-month stock claims against observed data")
    parser.add_argument("--registry", default=str(REGISTRY_PATH), help="Reality-check registry JSON")
    parser.add_argument("--output", default=str(REPORT_PATH), help="Markdown report path")
    args = parser.parse_args()

    registry = load_registry(Path(args.registry))
    report = render_report(registry)
    Path(args.output).write_text(report, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
