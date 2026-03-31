#!/usr/bin/env python3
"""Enterprise QA/QC validator for market reality-check artifacts."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "05_ck_analysis" / "analysis" / "benchmark_reference_catalog.json"
REGISTRY_PATH = ROOT / "05_ck_analysis" / "analysis" / "market_reality_registry_2026.json"
REPORT_PATH = ROOT / "05_ck_analysis" / "analysis" / "market_reality_check_2026.md"
OUTPUT_PATH = ROOT / "05_ck_analysis" / "analysis" / "market_qaqc_validator_report.md"
DEPRECATED_PATH = ROOT / "05_ck_analysis" / "analysis" / "backtest_t2_2026.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_domain(url: str) -> str:
    return urlparse(url).netloc.replace("www.", "")


def contains_required_sections(report_text: str) -> list[str]:
    required = [
        "# Market Reality Check 2026",
        "## Scope",
        "## Observed Metrics",
        "## Claim Audit",
        "## RCA",
        "## Derived Rules",
        "## Sources",
    ]
    return [section for section in required if section not in report_text]


def build_catalog_index(catalog: dict) -> dict:
    return {item["domain"]: item for item in catalog.get("benchmarks", [])}


def build_catalog_id_index(catalog: dict) -> dict:
    return {item["benchmark_id"]: item for item in catalog.get("benchmarks", [])}


def validate(registry: dict, report_text: str, catalog: dict) -> dict:
    findings = []
    warnings = []
    passes = []

    catalog_index = build_catalog_index(catalog)
    catalog_id_index = build_catalog_id_index(catalog)
    audit = registry["audits"][0]
    anchor_domain = extract_domain(registry["calendar_anchor"]["source_url"])
    broad_domain = extract_domain(audit["broad_market"]["start"]["source_url"])
    anchor_benchmark = registry["calendar_anchor"].get("benchmark_ref")
    broad_start_benchmark = audit["broad_market"]["start"].get("benchmark_ref")
    broad_end_benchmark = audit["broad_market"]["end"].get("benchmark_ref")
    basket_benchmark = audit["basket"].get("benchmark_ref")

    if registry.get("schema_version") != "1.0":
        findings.append("Registry schema_version khong hop le.")
    else:
        passes.append("Registry schema_version = 1.0")

    if anchor_domain not in catalog_index:
        findings.append(f"Calendar anchor domain `{anchor_domain}` khong co trong benchmark catalog.")
    elif catalog_index[anchor_domain]["tier"] != "B1_primary_operational":
        findings.append(f"Calendar anchor domain `{anchor_domain}` khong dat B1.")
    else:
        passes.append(f"Calendar anchor dung benchmark B1: `{anchor_domain}`")

    if anchor_benchmark not in catalog_id_index:
        findings.append(f"Calendar benchmark_ref `{anchor_benchmark}` khong hop le.")
    else:
        passes.append(f"Calendar benchmark_ref hop le: `{anchor_benchmark}`")

    if broad_domain not in catalog_index:
        findings.append(f"Broad market domain `{broad_domain}` khong co trong benchmark catalog.")
    elif catalog_index[broad_domain]["tier"] != "B1_primary_operational":
        findings.append(f"Broad market domain `{broad_domain}` khong dat B1.")
    else:
        passes.append(f"Broad market dung benchmark B1: `{broad_domain}`")

    for benchmark_name, benchmark_value in [
        ("broad_start", broad_start_benchmark),
        ("broad_end", broad_end_benchmark),
        ("basket", basket_benchmark),
    ]:
        if benchmark_value not in catalog_id_index:
            findings.append(f"{benchmark_name} benchmark_ref `{benchmark_value}` khong hop le.")
        else:
            passes.append(f"{benchmark_name} benchmark_ref hop le: `{benchmark_value}`")

    basket = audit.get("basket", {})
    start_ref = Path(basket.get("start_ref", ""))
    end_ref = Path(basket.get("end_ref", ""))
    if not start_ref.exists() or not end_ref.exists():
        findings.append("Basket snapshot refs khong ton tai tren disk.")
    else:
        passes.append("Basket snapshot refs ton tai.")

    if len(basket.get("components", [])) < 3:
        findings.append("Basket co qua it components de so sanh regime.")
    else:
        passes.append("Basket co du so component de doi chieu.")

    missing_sections = contains_required_sections(report_text)
    if missing_sections:
        findings.append(f"Report thieu sections: {', '.join(missing_sections)}")
    else:
        passes.append("Report co du sections bat buoc.")

    if "`supported`" not in report_text and "`partial`" not in report_text and "`contradicted`" not in report_text:
        findings.append("Report khong co claim status labels.")
    else:
        passes.append("Report co claim status labels.")

    if "broad market" not in report_text or "single-name catalyst" not in report_text:
        warnings.append("Report/rule chua the hien ro day du 3 lop regime separation.")
    else:
        passes.append("Report co regime separation language.")

    deprecated_text = DEPRECATED_PATH.read_text(encoding="utf-8") if DEPRECATED_PATH.exists() else ""
    if "[DEPRECATED]" not in deprecated_text:
        findings.append("Deprecated backtest file chua duoc danh dau fail-loud.")
    else:
        passes.append("Deprecated backtest file da duoc danh dau fail-loud.")

    status = "PASS" if not findings else "FAIL"
    return {
        "status": status,
        "findings": findings,
        "warnings": warnings,
        "passes": passes,
    }


def render_report(result: dict) -> str:
    lines = []
    lines.append("# Market QAQC Validator")
    lines.append("")
    lines.append(f"- Status: `{result['status']}`")
    lines.append("")
    lines.append("## Passes")
    lines.append("")
    if result["passes"]:
        for item in result["passes"]:
            lines.append(f"- {item}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Findings")
    lines.append("")
    if result["findings"]:
        for item in result["findings"]:
            lines.append(f"- {item}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Warnings")
    lines.append("")
    if result["warnings"]:
        for item in result["warnings"]:
            lines.append(f"- {item}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Release Gate")
    lines.append("")
    if result["status"] == "PASS":
        lines.append("- QG-CK-E4 PASS: artifact dat muc enterprise co ban cho reality-check.")
    else:
        lines.append("- QG-CK-E4 FAIL: sua findings truoc khi coi artifact la enterprise-ready.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate CK QA/QC artifacts against enterprise gates")
    parser.add_argument("--catalog", default=str(CATALOG_PATH))
    parser.add_argument("--registry", default=str(REGISTRY_PATH))
    parser.add_argument("--report", default=str(REPORT_PATH))
    parser.add_argument("--output", default=str(OUTPUT_PATH))
    args = parser.parse_args()

    catalog = load_json(Path(args.catalog))
    registry = load_json(Path(args.registry))
    report_text = Path(args.report).read_text(encoding="utf-8")
    result = validate(registry, report_text, catalog)
    output_text = render_report(result)
    Path(args.output).write_text(output_text, encoding="utf-8")
    print(args.output)
    if result["status"] != "PASS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
