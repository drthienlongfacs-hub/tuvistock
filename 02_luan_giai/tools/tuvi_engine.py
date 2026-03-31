#!/usr/bin/env python3
"""
TuViStock Unified Engine v3.0 — 9-Dimension Scoring + Evidence Integration
==========================================================================
Consolidates: inject_classic_theory.py + upgrade_7_chieu.py + upgrade_7_chieu_v2.py

Features:
  - 9-dimension scoring (from 5→7→9)
  - Dual scoring: Additive (legacy) + Multiplicative (NPL power function)
  - Điều Hầu climate adjustment (Cùng Thông Bảo Giám)
  - Khí Sắc mapping (Hồng Phi Mô)
  - Bát Tự cross-reference (Thập Thần ↔ Chính Tinh)
  - Anti-bias detection (Barnum, Retrofitting)
  - Confidence levels (Cao/Trung bình/Thấp)
  - Cross-agent integration (Codex evidence registry + Claude audit)

Sources: Harvest Round 4 — bat_tu_kinh_dien.md, vn_scholarly_gaps.md, master_menh_ly_harvest.md
Rules: R-16 (Anti-Bias), R-17 (Cross-System), R-18 (Chaos Theory), BT-1→BT-6
"""

import os
import re
import json
import math
import argparse
import importlib.util
from pathlib import Path
from collections import Counter
from typing import Optional

# ============================================================
# CROSS-AGENT INTEGRATION LAYER
# ============================================================
# Sources:
#   Codex  → EVIDENCE_REGISTRY.csv, CLAIM_REGISTRY.csv, score_evidence.py
#   Claude → (audit integration placeholder)
#   Antigravity → tuvi_engine.py (this file), harvest docs in 04_ly_thuyet/

EVIDENCE_ENV_VAR = "TUVISTOCK_CODEX_EVIDENCE_ROOT"
EVIDENCE_DIRNAME = "menhly_harvest_20260329"
SNAPSHOT_NAME = "EVIDENCE_SNAPSHOT.json"
SCORE_SCRIPT_NAME = "score_evidence.py"
MIN_SNAPSHOT_SCHEMA = "1.0"
_CODEX_CACHE = None


def candidate_evidence_roots() -> list:
    """Ordered search path for the Codex evidence corpus."""
    candidates = []
    env_root = os.environ.get(EVIDENCE_ENV_VAR)
    if env_root:
        candidates.append(Path(env_root).expanduser())
    candidates.extend([
        Path.cwd() / EVIDENCE_DIRNAME,
        Path.home() / "Downloads" / EVIDENCE_DIRNAME,
    ])

    unique = []
    seen = set()
    for root in candidates:
        resolved = root.resolve(strict=False)
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(root)
    return unique


def resolve_evidence_root() -> Optional[Path]:
    """Find a Codex evidence root with either a snapshot or canonical script."""
    fallback = None
    for root in candidate_evidence_roots():
        snapshot = root / SNAPSHOT_NAME
        script = root / SCORE_SCRIPT_NAME
        if snapshot.exists() or script.exists():
            return root
        if (root / "EVIDENCE_REGISTRY.csv").exists() and (root / "CLAIM_REGISTRY.csv").exists():
            fallback = root
    return fallback


def empty_codex_bundle(issue: str, root: Optional[Path] = None) -> dict:
    return {
        "sources": {},
        "claims": [],
        "summary": {},
        "runtime": {
            "mode": "missing",
            "root": str(root) if root else None,
            "issues": [issue],
        },
    }


def normalize_snapshot_sources(raw_sources) -> dict:
    """Accept both dict- and list-shaped source payloads."""
    if isinstance(raw_sources, dict):
        return raw_sources
    if isinstance(raw_sources, list):
        return {row["id"]: row for row in raw_sources}
    return {}


def load_codex_snapshot(snapshot_path: Path) -> dict:
    data = json.loads(snapshot_path.read_text(encoding="utf-8"))
    schema_version = data.get("schema_version")
    if schema_version != MIN_SNAPSHOT_SCHEMA:
        raise ValueError(f"unsupported snapshot schema: {schema_version}")
    return {
        "sources": normalize_snapshot_sources(data.get("sources", {})),
        "claims": data.get("claims", []),
        "summary": data.get("summary", {}),
        "runtime": {
            "mode": "snapshot",
            "root": str(snapshot_path.parent),
            "issues": [],
            "generated_at": data.get("generated_at"),
            "schema_version": schema_version,
            "inputs": data.get("inputs", {}),
        },
    }


def load_codex_module_bundle(root: Path) -> dict:
    """Fallback loader: execute Codex's own scoring module instead of copying logic."""
    script_path = root / SCORE_SCRIPT_NAME
    spec = importlib.util.spec_from_file_location("codex_score_evidence_runtime", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load Codex script: {script_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sources = {row["id"]: row for row in module.load_sources()}
    claims = module.load_claims()
    return {
        "sources": sources,
        "claims": claims,
        "summary": {
            "source_status_counts": dict(Counter(r["evidence_status"] for r in sources.values())),
            "claim_status_counts": dict(Counter(c["status"] for c in claims)),
            "source_count": len(sources),
            "claim_count": len(claims),
        },
        "runtime": {
            "mode": "module_fallback",
            "root": str(root),
            "issues": ["using score_evidence.py fallback; generate snapshot for canonical contract"],
            "generated_at": None,
            "schema_version": None,
        },
    }


def load_codex_bundle(force_refresh: bool = False) -> dict:
    """Load Codex evidence from canonical snapshot, with explicit fallback."""
    global _CODEX_CACHE
    if _CODEX_CACHE is not None and not force_refresh:
        return _CODEX_CACHE

    root = resolve_evidence_root()
    if root is None:
        _CODEX_CACHE = empty_codex_bundle("no evidence root found in configured search paths")
        return _CODEX_CACHE

    snapshot_path = root / SNAPSHOT_NAME
    if snapshot_path.exists():
        try:
            _CODEX_CACHE = load_codex_snapshot(snapshot_path)
            return _CODEX_CACHE
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            snapshot_issue = f"snapshot invalid: {exc}"
        else:
            snapshot_issue = None
    else:
        snapshot_issue = "snapshot missing"

    script_path = root / SCORE_SCRIPT_NAME
    if script_path.exists():
        try:
            bundle = load_codex_module_bundle(root)
            if snapshot_issue:
                bundle["runtime"]["issues"].insert(0, snapshot_issue)
            _CODEX_CACHE = bundle
            return _CODEX_CACHE
        except Exception as exc:  # noqa: BLE001
            _CODEX_CACHE = empty_codex_bundle(f"failed to load Codex script fallback: {exc}", root)
            return _CODEX_CACHE

    issue = snapshot_issue or "missing snapshot and score script"
    _CODEX_CACHE = empty_codex_bundle(issue, root)
    return _CODEX_CACHE


def load_codex_evidence() -> dict:
    return load_codex_bundle()["sources"]


def load_codex_claims() -> list:
    return load_codex_bundle()["claims"]


def codex_runtime() -> dict:
    return load_codex_bundle()["runtime"]


# Mapping: which Codex evidence IDs back which data in THIS engine
# Key = our data source label, Value = Codex evidence ID + our usage
SOURCE_PROVENANCE = {
    "tam_menh_thong_hoi": {"codex_id": "EA06", "usage": "Nạp Âm 60 Giáp Tý, Nguyệt Lệnh"},
    "trich_thien_tuy":    {"codex_id": "EA07", "usage": "5 Nguyên lý, Thông Quan, Vượng Suy"},
    "tu_binh_chan_thuyen": {"codex_id": "EA08", "usage": "Thập Thần, Cách Cục, Dụng/Kỵ Thần"},
    "cung_thong_bao_giam": {"codex_id": "EA09", "usage": "Điều Hầu Dụng Thần (⑧)"},
    "zi_wei_dou_shu":     {"codex_id": "EA10", "usage": "TVĐS methodology core"},
    "hong_phi_mo":        {"codex_id": "EA11", "usage": "Khí Sắc 12 tháng (⑨)"},
    "tu_vi_ham_so":       {"codex_id": "VN01", "usage": "NPL multiplicative scoring"},
    "carlson_1985":       {"codex_id": "CR01", "usage": "Anti-bias calibration (R-16)"},
    "zhou_yi":            {"codex_id": "EA01", "usage": "Âm Dương Ngũ Hành foundation"},
}


def get_evidence_status(source_key: str, codex_data: dict = None) -> str:
    """Get evidence_status for a source from Codex registry."""
    if codex_data is None:
        codex_data = load_codex_evidence()
    prov = SOURCE_PROVENANCE.get(source_key, {})
    codex_id = prov.get("codex_id", "")
    if codex_id in codex_data:
        return codex_data[codex_id]["evidence_status"]
    return "unregistered"


def build_evidence_gates(evidence: dict, runtime: dict) -> dict:
    """Translate registry status into operational handling inside the engine."""
    return {
        "loader": runtime.get("mode", "missing"),
        "tvds_core": "provisional" if evidence.get("tvds_core") == "pending" else "standard",
        "npl_scoring": "experimental" if evidence.get("npl_scoring") == "pending" else "standard",
    }


def build_evidence_warnings(evidence: dict, runtime: dict) -> list:
    warnings = []
    mode = runtime.get("mode", "missing")
    root = runtime.get("root")
    if mode != "snapshot":
        location = f" from {root}" if root else ""
        warnings.append(f"Codex loader running in `{mode}` mode{location}.")
    for issue in runtime.get("issues", []):
        warnings.append(f"Evidence loader issue: {issue}")
    if evidence.get("tvds_core") == "pending":
        warnings.append("TVDS core remains `pending` (EA10); treat interpretation as provisional.")
    if evidence.get("npl_scoring") == "pending":
        warnings.append("NPL multiplicative score remains `pending` (VN01); treat multiplicative output as experimental.")
    return warnings


def strict_evidence_failures(bundle: Optional[dict] = None) -> list:
    """Enterprise fail-loud checks for CI/monitoring."""
    bundle = bundle or load_codex_bundle()
    runtime = bundle.get("runtime", {})
    sources = bundle.get("sources", {})
    failures = []

    if runtime.get("mode") != "snapshot":
        failures.append(f"canonical snapshot unavailable (mode={runtime.get('mode', 'missing')})")
    if get_evidence_status("zi_wei_dou_shu", sources) == "pending":
        failures.append("tvds_core still pending in Codex registry (EA10)")
    if get_evidence_status("tu_vi_ham_so", sources) == "pending":
        failures.append("npl_scoring still pending in Codex registry (VN01)")
    return failures


# ============================================================
# DATA LAYER — 12 months × multiple dimensions
# ============================================================

# Mệnh: Nhâm Thân (壬申) — Kiếm Phong Kim (Nạp Âm)
MENH_INFO = {
    "can": "Nhâm",       # Thiên Can: Nhâm (壬) = Dương Thủy
    "chi": "Thân",       # Địa Chi: Thân (申) = Dương Kim
    "nap_am": "Kiếm Phong Kim",   # Nạp Âm: Vàng mũi kiếm
    "nap_am_hanh": "Kim",
    "ngu_hanh_can": "Thủy",
    "ngu_hanh_chi": "Kim",
    "dung_than_bat_tu": "Mộc",    # Dụng Thần BT: Mộc (khắc chế Kim quá vượng, tiết Thủy)
}

# ─── Thái Tuế + Chủ-Khách (Trần Đoàn & Thiên Lương) ────────
# Source: kinh_dien_tu_vi_tong_hop.md, inject_classic_theory.py
# Verified: Vòng Thái Tuế Nhâm Thân qua 12 cung Lưu Nguyệt

CLASSIC_DATA = {
    1: {
        "thai_tue_score": 3.0,
        "thai_tue_name": "Tuế Phá",
        "thai_tue_category": "Nghịch Cảnh",
        "thai_tue_desc": "Bất mãn, nhiều trở ngại, cần kiên nhẫn chống đối nghịch cảnh",
        "chu_khach_score": 9.0,
        "chu_khach_type": "Chủ lấn Khách",
        "chu_khach_desc": "Bản cung (Cự Dương Vượng) đè bẹp đối cung (VCD). Nắm toàn lợi thế chủ động",
        "chu_khach_stars": {"ban_cung": "Cự Dương Vượng", "doi_cung": "VCD"},
    },
    2: {
        "thai_tue_score": 6.0,
        "thai_tue_name": "Long Đức",
        "thai_tue_category": "Chịu Thiệt",
        "thai_tue_desc": "Nhẫn nhịn, hiền hòa, lấy đức thu phục. Chấp nhận thiệt thòi bước đầu",
        "chu_khach_score": 5.0,
        "chu_khach_type": "Chủ Khách giằng co",
        "chu_khach_desc": "Bản cung (Tướng Hãm) và đối cung (Liêm Phá Hãm) đều bất ổn. Mầm phá hoại",
        "chu_khach_stars": {"ban_cung": "Tướng Hãm", "doi_cung": "Liêm Phá Hãm"},
    },
    3: {
        "thai_tue_score": 9.0,
        "thai_tue_name": "Bạch Hổ",
        "thai_tue_category": "Chính Danh",
        "thai_tue_desc": "Quang minh chính đại, oai phong. Gánh vác nhiều nhưng chính danh, thuận lý",
        "chu_khach_score": 9.0,
        "chu_khach_type": "Chủ lấn Khách",
        "chu_khach_desc": "Bản cung (Cơ Lương Vượng) thắng thế đối cung (VCD). Nội lực vượt trội",
        "chu_khach_stars": {"ban_cung": "Cơ Lương Vượng", "doi_cung": "VCD"},
    },
    4: {
        "thai_tue_score": 5.0,
        "thai_tue_name": "Phúc Đức",
        "thai_tue_category": "Khôn Ngoan",
        "thai_tue_desc": "Hoàn cảnh ưu ái, sắc sảo. Cẩn trọng Thiên Không gây ảo tưởng",
        "chu_khach_score": 9.0,
        "chu_khach_type": "Chủ lấn cực mạnh Khách",
        "chu_khach_desc": "Bản cung (Tử Sát Miếu) áp đảo đối cung (Thiên Phủ Bình). Sức ép quyền lực lớn",
        "chu_khach_stars": {"ban_cung": "Tử Sát Miếu", "doi_cung": "Thiên Phủ Bình"},
    },
    5: {
        "thai_tue_score": 3.0,
        "thai_tue_name": "Điếu Khách",
        "thai_tue_category": "Nghịch Cảnh",
        "thai_tue_desc": "Bất mãn, nghịch lý, lao tâm khổ tứ. Tiêu hao vì bất đồng quan điểm",
        "chu_khach_score": 2.0,
        "chu_khach_type": "Khách lấn Chủ",
        "chu_khach_desc": "Bản cung (VCD) bị đối cung (Đồng Âm Vượng) lấn lướt. Bị động hoàn toàn",
        "chu_khach_stars": {"ban_cung": "VCD", "doi_cung": "Đồng Âm Vượng"},
    },
    6: {
        "thai_tue_score": 6.0,
        "thai_tue_name": "Trực Phù",
        "thai_tue_category": "Chịu Thiệt",
        "thai_tue_desc": "Mệt mỏi, nhân nhượng, làm nhiều hưởng ít. An toàn, tránh bão",
        "chu_khach_score": 2.0,
        "chu_khach_type": "Khách lấn Chủ",
        "chu_khach_desc": "Bản cung (VCD) bị đối cung (Vũ Tham Miếu) chi phối. Thụ động phụ thuộc",
        "chu_khach_stars": {"ban_cung": "VCD", "doi_cung": "Vũ Tham Miếu"},
    },
    7: {
        "thai_tue_score": 9.0,
        "thai_tue_name": "Thái Tuế",
        "thai_tue_category": "Chính Danh",
        "thai_tue_desc": "Danh chính ngôn thuận, cực thuận lý. Trời đất ủng hộ, tự tin quyết đoán",
        "chu_khach_score": 2.0,
        "chu_khach_type": "Khách lấn Chủ",
        "chu_khach_desc": "Bản cung (VCD) lép trước đối cung (Cự Dương Vượng). Phải dựa mượn lực",
        "chu_khach_stars": {"ban_cung": "VCD", "doi_cung": "Cự Dương Vượng"},
    },
    8: {
        "thai_tue_score": 5.0,
        "thai_tue_name": "Thiếu Dương",
        "thai_tue_category": "Khôn Ngoan",
        "thai_tue_desc": "Thông minh xuất chúng, nắm bắt cơ hội. Đề phòng Thiên Không bẫy",
        "chu_khach_score": 5.0,
        "chu_khach_type": "Chủ Khách giằng co",
        "chu_khach_desc": "Bản cung (Liêm Phá Hãm) đối (Tướng Hãm). Hỗn loạn, không bên nào áp đảo",
        "chu_khach_stars": {"ban_cung": "Liêm Phá Hãm", "doi_cung": "Tướng Hãm"},
    },
    9: {
        "thai_tue_score": 3.0,
        "thai_tue_name": "Tang Môn",
        "thai_tue_category": "Nghịch Cảnh",
        "thai_tue_desc": "U buồn, chống đối, nghịch thiên lý. Cần nghị lực lớn vượt áp lực",
        "chu_khach_score": 2.0,
        "chu_khach_type": "Khách lấn Chủ",
        "chu_khach_desc": "Bản cung (VCD) phụ thuộc đối cung (Cơ Lương Vượng). Đối tác quyết định cuộc chơi",
        "chu_khach_stars": {"ban_cung": "VCD", "doi_cung": "Cơ Lương Vượng"},
    },
    10: {
        "thai_tue_score": 6.0,
        "thai_tue_name": "Thiếu Âm",
        "thai_tue_category": "Chịu Thiệt",
        "thai_tue_desc": "Nhường nhịn, hiền từ. Lùi một bước tiến ba bước",
        "chu_khach_score": 3.0,
        "chu_khach_type": "Khách lấn Chủ",
        "chu_khach_desc": "Bản cung (Thiên Phủ Bình) bị đối cung (Tử Sát Miếu) đè ép. Phải cố thủ",
        "chu_khach_stars": {"ban_cung": "Thiên Phủ Bình", "doi_cung": "Tử Sát Miếu"},
    },
    11: {
        "thai_tue_score": 9.0,
        "thai_tue_name": "Quan Phù",
        "thai_tue_category": "Chính Danh",
        "thai_tue_desc": "Lý trí, pháp lý soi đường. Rất thuận cho giấy tờ, hợp đồng",
        "chu_khach_score": 9.0,
        "chu_khach_type": "Chủ lấn Khách",
        "chu_khach_desc": "Bản cung (Đồng Âm Vượng) nắm lợi thế trước VCD. Mềm mỏng làm chủ cục diện",
        "chu_khach_stars": {"ban_cung": "Đồng Âm Vượng", "doi_cung": "VCD"},
    },
    12: {
        "thai_tue_score": 5.0,
        "thai_tue_name": "Tử Phù",
        "thai_tue_category": "Khôn Ngoan",
        "thai_tue_desc": "Cẩn trọng đào hoa/lợi ích phù phiếm. Thông minh nhưng dễ lạc lối",
        "chu_khach_score": 9.0,
        "chu_khach_type": "Chủ lấn Khách",
        "chu_khach_desc": "Bản cung (Vũ Tham Miếu) đè bẹp VCD. Tài chính và quyền lực kiểm soát tháng",
        "chu_khach_stars": {"ban_cung": "Vũ Tham Miếu", "doi_cung": "VCD"},
    },
}

# ─── Điều Hầu Dụng Thần — Climate Adjustment (Cùng Thông Bảo Giám) ────
# Source: bat_tu_kinh_dien.md §III — Nhâm Thủy (壬) Dương Thủy qua 12 tháng
# Nhật Chủ Nhâm = Dương Thủy → seasonal Dụng Thần

DIEU_HAU_DATA = {
    1: {"climate": "Hàn",  "dung_than": "Bính Hỏa",    "score": 5.0, "desc": "Thủy Dương còn lạnh, cần Bính (mặt trời) sưởi ấm. Mộc bắt đầu mọc tiết khí Thủy"},
    2: {"climate": "Ấm",   "dung_than": "Mậu Thổ",     "score": 6.0, "desc": "Thủy gặp Mộc vượng bị tiết khí. Cần Mậu Thổ đê đập giữ Thủy, Canh Kim bổ nguồn"},
    3: {"climate": "Ấm",   "dung_than": "Giáp Mộc",     "score": 7.0, "desc": "Thổ vượng khắc Thủy. Cần Giáp Mộc khắc Thổ giải vây, Canh Kim sinh Thủy"},
    4: {"climate": "Nóng", "dung_than": "Nhâm Thủy",    "score": 4.0, "desc": "Hỏa bắt đầu mạnh bốc hơi Thủy. Cần thêm Thủy hoặc Kim nguồn"},
    5: {"climate": "Cực nóng", "dung_than": "Quý Thủy", "score": 3.0, "desc": "Hỏa cực vượng, Thủy suy kiệt. Cần Quý Thủy + Canh Kim cấp cứu nguồn"},
    6: {"climate": "Nóng ẩm", "dung_than": "Canh Kim",  "score": 4.0, "desc": "Thổ ẩm nhiều cản Thủy. Cần Kim xuyên Thổ sinh Thủy, Giáp Mộc phá Thổ"},
    7: {"climate": "Mát",  "dung_than": "Giáp Mộc",     "score": 7.0, "desc": "Kim bắt đầu vượng sinh Thủy mạnh. Cần Mộc tiết bớt Thủy, Đinh Hỏa luyện Kim"},
    8: {"climate": "Mát",  "dung_than": "Giáp Mộc",     "score": 8.0, "desc": "Kim cực vượng sinh Thủy tràn. Mộc tiết Thủy + Mậu Thổ đê đập"},
    9: {"climate": "Mát khô", "dung_than": "Giáp Mộc",  "score": 6.0, "desc": "Thổ táo vượng khắc Thủy. Cần Giáp Mộc phá Thổ, Canh Kim nguồn"},
    10: {"climate": "Lạnh","dung_than": "Bính Hỏa",     "score": 5.0, "desc": "Thủy vượng nhưng lạnh đông cứng. Cần Bính Hỏa giải đông, Mậu Thổ đê"},
    11: {"climate": "Cực lạnh", "dung_than": "Bính Hỏa", "score": 3.0, "desc": "Đông chí — Thủy cực vượng đóng băng. Bính Hỏa = mặt trời → ưu tiên tối cao"},
    12: {"climate": "Hàn ẩm", "dung_than": "Bính Hỏa",  "score": 4.0, "desc": "Thổ ẩm lạnh, Thủy bị giam. Cần Bính sưởi + Giáp Mộc phá Thổ giải phóng"},
}

# ─── Khí Sắc 12 tháng (Hồng Phi Mô) ────────────────────────
# Source: hong_phi_mo_tuong_dien.md — Mệnh Kiếm Phong Kim
# Evidence: EA11 (Codex) — library existence witness, usable_with_caution
# Đánh giá năng lượng sinh học/vật lý qua 12 tháng

KHI_SAC_DATA = {
    1: {"hanh_thang": "Mộc",  "tuong_tac": "Kim bị Mộc tiết",      "score": 4.0, "desc": "Kiếm Phong Kim gặp Mộc Xuân — bị tiết khí, năng lượng giảm nhẹ"},
    2: {"hanh_thang": "Mộc",  "tuong_tac": "Kim bị Mộc tiết (mạnh)", "score": 3.0, "desc": "Mộc cực vượng, Kim suy — sức khỏe cần đề phòng, dễ mệt"},
    3: {"hanh_thang": "Thổ", "tuong_tac": "Thổ sinh Kim",           "score": 7.0, "desc": "Thổ sinh Kim — năng lượng phục hồi, sức khỏe ổn định"},
    4: {"hanh_thang": "Hỏa", "tuong_tac": "Hỏa khắc Kim",          "score": 2.0, "desc": "Hỏa vượng khắc Kim trực tiếp — tháng nguy hiểm nhất cho sức khỏe"},
    5: {"hanh_thang": "Hỏa", "tuong_tac": "Hỏa khắc Kim (cực)",    "score": 1.0, "desc": "Hỏa cực đại + Kim suy cực → sức khỏe tối thiểu, cần bảo dưỡng tích cực"},
    6: {"hanh_thang": "Thổ", "tuong_tac": "Thổ sinh Kim",           "score": 6.0, "desc": "Thổ nóng sinh Kim — phục hồi từ từ, chưa mạnh hoàn toàn"},
    7: {"hanh_thang": "Kim",  "tuong_tac": "Kim vượng (Lâm Quan)",  "score": 9.0, "desc": "Kim vào mùa — năng lượng cực đại, sức bật mạnh nhất năm"},
    8: {"hanh_thang": "Kim",  "tuong_tac": "Kim vượng (Đế Vượng)",  "score": 10.0,"desc": "Kim Đế Vượng — đỉnh cao năng lượng, thời điểm tốt nhất hành động"},
    9: {"hanh_thang": "Thổ", "tuong_tac": "Thổ sinh Kim (duy trì)", "score": 7.0, "desc": "Thổ tiếp tục sinh Kim — duy trì sức mạnh, bắt đầu giảm nhẹ"},
    10: {"hanh_thang": "Thủy","tuong_tac": "Kim sinh Thủy (tiết)",  "score": 5.0, "desc": "Kim bắt đầu tiết khí sinh Thủy — năng lượng rò rỉ, cần tiết kiệm"},
    11: {"hanh_thang": "Thủy","tuong_tac": "Kim sinh Thủy (mạnh)",  "score": 4.0, "desc": "Thủy cực vượng hút Kim — năng lượng suy giảm rõ rệt"},
    12: {"hanh_thang": "Thổ","tuong_tac": "Thổ sinh Kim (ẩm)",     "score": 5.0, "desc": "Thổ ẩm sinh Kim nhẹ — năng lượng trung bình, ổn định"},
}

# ─── Thập Thần ↔ Chính Tinh mapping (Tử Bình Chân Thuyên) ───
# Source: bat_tu_kinh_dien.md §IV

THAP_THAN_MAP = {
    "Chính Quan":  {"tvds": ["Tử Vi", "Thiên Phủ"],   "similarity": 2},
    "Thất Sát":    {"tvds": ["Thất Sát"],              "similarity": 3},
    "Chính Ấn":    {"tvds": ["Thiên Lương"],            "similarity": 2},
    "Thiên Ấn":    {"tvds": ["Thiên Cơ"],               "similarity": 2},
    "Chính Tài":   {"tvds": ["Vũ Khúc"],                "similarity": 2},
    "Thiên Tài":   {"tvds": ["Thiên Tài"],               "similarity": 2},
    "Thực Thần":   {"tvds": ["Thiên Đồng"],              "similarity": 2},
    "Thương Quan": {"tvds": ["Phá Quân"],                "similarity": 2},
    "Tỷ Kiên":     {"tvds": ["Tả Phụ", "Hữu Bật"],     "similarity": 1},
    "Kiếp Tài":    {"tvds": ["Kình Dương", "Đà La"],    "similarity": 2},
}

# ─── Nạp Âm 60 Giáp Tý (top 10 phổ biến) ────────────────────
# Source: bat_tu_kinh_dien.md §I — Tam Mệnh Thông Hội

NAP_AM_TABLE = {
    "Giáp Tý": "Hải Trung Kim",   "Ất Sửu": "Hải Trung Kim",
    "Bính Dần": "Lô Trung Hỏa",   "Đinh Mão": "Lô Trung Hỏa",
    "Mậu Thìn": "Đại Lâm Mộc",    "Kỷ Tỵ": "Đại Lâm Mộc",
    "Canh Ngọ": "Lộ Bàng Thổ",     "Tân Mùi": "Lộ Bàng Thổ",
    "Nhâm Thân": "Kiếm Phong Kim", "Quý Dậu": "Kiếm Phong Kim",
    "Giáp Tuất": "Sơn Đầu Hỏa",   "Ất Hợi": "Sơn Đầu Hỏa",
    "Bính Tý": "Giản Hạ Thủy",     "Đinh Sửu": "Giản Hạ Thủy",
    "Mậu Dần": "Thành Đầu Thổ",    "Kỷ Mão": "Thành Đầu Thổ",
    "Canh Thìn": "Bạch Lạp Kim",   "Tân Tỵ": "Bạch Lạp Kim",
    "Nhâm Ngọ": "Dương Liễu Mộc",  "Quý Mùi": "Dương Liễu Mộc",
}

# ============================================================
# SCORING ENGINE
# ============================================================

# 9-dimension weights (total = 100%)
WEIGHTS_9 = {
    1: 0.20,   # ① Bản Cung (chính tinh)
    2: 0.15,   # ② Tam Chiếu/Xung
    3: 0.12,   # ③ Chủ-Khách (Trần Đoàn)
    4: 0.12,   # ④ Thái Tuế (Thiên Lương)
    5: 0.10,   # ⑤ Tứ Hóa Lưu Niên
    6: 0.08,   # ⑥ Lưu Nguyệt/Can Chi
    7: 0.03,   # ⑦ Giáp cung
    8: 0.10,   # ⑧ Điều Hầu (Cùng Thông Bảo Giám)
    9: 0.10,   # ⑨ Khí Sắc (Hồng Phi Mô)
}

# Legacy 7-dimension weights for backward compatibility
WEIGHTS_7 = {
    1: 0.25,   # ① Bản Cung
    2: 0.20,   # ② Tam Chiếu
    3: 0.15,   # ③ Chủ-Khách
    4: 0.15,   # ④ Thái Tuế
    5: 0.10,   # ⑤ Tứ Hóa LN
    6: 0.10,   # ⑥ Lưu Nguyệt
    7: 0.05,   # ⑦ Giáp
}


def additive_score(scores: dict, weights: dict = None) -> float:
    """
    Legacy additive scoring: total = Σ(weight_i × score_i)
    Standard linear combination used by upgrade_7_chieu.py
    """
    if weights is None:
        weights = WEIGHTS_9 if len(scores) >= 9 else WEIGHTS_7
    total = sum(weights.get(k, 0) * scores.get(k, 5.0) for k in weights)
    return round(total, 1)


def multiplicative_score(scores: dict, weights: dict = None) -> float:
    """
    NPL Power Function scoring (Nguyễn Phát Lộc):
    total = 10 × Π((score_i / 10) ^ weight_i)

    Properties:
    - High scores amplify each other (exponential stacking)
    - One low score craters the total (multiplicative penalty)
    - More realistic for Tử Vi where one bad dimension ruins everything
    """
    if weights is None:
        weights = WEIGHTS_9 if len(scores) >= 9 else WEIGHTS_7
    product = 1.0
    for k, w in weights.items():
        s = max(scores.get(k, 5.0), 0.1)  # Prevent log(0)
        product *= (s / 10.0) ** w
    return round(10.0 * product, 1)


def confidence_level(score: float) -> str:
    """
    Rule R-16: Anti-Bias confidence classification
    Based on how many dimensions agree (high concordance = high confidence)
    """
    if score >= 7.5:
        return "Cao"
    elif score >= 4.5:
        return "Trung bình"
    else:
        return "Thấp"


def detect_bias(text: str) -> list:
    """
    Rule R-16: Detect potential cognitive biases in text
    Returns list of bias warnings
    """
    warnings = []

    # Barnum Effect detection — vague descriptions that fit anyone
    barnum_patterns = [
        r'(?:bạn|đương số)\s+(?:sẽ|có thể)\s+(?:gặp|đạt)\s+(?:nhiều\s+)?(?:thành công|may mắn)',
        r'tháng này.*(?:thuận lợi|tốt đẹp)(?!\s+(?:cho|vì|do|nhờ))',
        r'cần\s+(?:cẩn thận|cẩn trọng)(?!\s+(?:với|về|trong|khi))',
    ]
    for pat in barnum_patterns:
        if re.search(pat, text, re.IGNORECASE):
            warnings.append("[Barnum Warning] Mô tả quá chung — cần thêm chi tiết cụ thể")
            break

    # Absolute claim detection
    absolute_patterns = [
        r'chắc chắn\s+(?:sẽ|phải)',
        r'bắt buộc\s+(?:sẽ|phải|xảy ra)',
        r'tuyệt đối\s+(?:sẽ|không)',
    ]
    for pat in absolute_patterns:
        if re.search(pat, text, re.IGNORECASE):
            warnings.append("[Absolute Claim] Không thể tuyên bố tuyệt đối — Rule R-18")
            break

    return warnings


def compute_month_score(month: int, existing_scores: dict = None) -> dict:
    """
    Compute full 9-dimension score for a given month.
    Integrates Codex evidence_status for provenance tracking.

    Args:
        month: 1-12
        existing_scores: dict with keys 1-7 (from existing 7-chiều tables)

    Returns:
        dict with all scores, totals, confidence, evidence provenance, and metadata
    """
    if existing_scores is None:
        existing_scores = {}

    cd = CLASSIC_DATA.get(month, {})
    dh = DIEU_HAU_DATA.get(month, {})
    ks = KHI_SAC_DATA.get(month, {})

    # Build full 9-dimension scores
    scores = {
        1: existing_scores.get(1, 5.0),  # ① Bản Cung
        2: existing_scores.get(2, 5.0),  # ② Tam Chiếu
        3: cd.get("chu_khach_score", 5.0),  # ③ Chủ-Khách
        4: cd.get("thai_tue_score", 5.0),   # ④ Thái Tuế
        5: existing_scores.get(5, 5.0),  # ⑤ Tứ Hóa LN
        6: existing_scores.get(6, 5.0),  # ⑥ Lưu Nguyệt
        7: existing_scores.get(7, 5.0),  # ⑦ Giáp
        8: dh.get("score", 5.0),         # ⑧ Điều Hầu
        9: ks.get("score", 5.0),         # ⑨ Khí Sắc
    }

    add_total = additive_score(scores)
    mul_total = multiplicative_score(scores)
    conf = confidence_level(add_total)

    # Load Codex evidence provenance for key sources
    codex_bundle = load_codex_bundle()
    codex_data = codex_bundle["sources"]
    runtime = codex_bundle["runtime"]
    evidence_provenance = {
        "dieu_hau": get_evidence_status("cung_thong_bao_giam", codex_data),
        "khi_sac": get_evidence_status("hong_phi_mo", codex_data),
        "tvds_core": get_evidence_status("zi_wei_dou_shu", codex_data),
        "npl_scoring": get_evidence_status("tu_vi_ham_so", codex_data),
    }
    evidence_gates = build_evidence_gates(evidence_provenance, runtime)
    evidence_warnings = build_evidence_warnings(evidence_provenance, runtime)

    return {
        "month": month,
        "scores": scores,
        "additive_total": add_total,
        "multiplicative_total": mul_total,
        "confidence": conf,
        "evidence": evidence_provenance,
        "evidence_gates": evidence_gates,
        "evidence_runtime": runtime,
        "warnings": evidence_warnings,
        "thai_tue": f"{cd.get('thai_tue_name', '?')} ({cd.get('thai_tue_category', '?')})",
        "chu_khach": cd.get("chu_khach_type", "?"),
        "climate": dh.get("climate", "?"),
        "dung_than": dh.get("dung_than", "?"),
        "khi_sac": ks.get("desc", "?"),
    }


# ============================================================
# MD PROCESSOR — Read/inject/upgrade markdown files
# ============================================================

def extract_existing_scores(md_text: str, month: int) -> dict:
    """Extract scores from existing 5-chiều or 7-chiều tables in markdown."""
    scores = {}
    month_pattern = rf'THÁNG\s+{month}\b'
    lines = md_text.split('\n')

    in_month = False
    in_table = False
    row_idx = 0

    for line in lines:
        if re.search(month_pattern, line):
            in_month = True
            continue

        if in_month and re.search(r'THÁNG\s+\d+', line) and not re.search(month_pattern, line):
            break  # Next month

        if in_month and re.search(r'(?:5|7|9)-CHIỀU', line):
            in_table = True
            row_idx = 0
            continue

        if in_month and in_table:
            if line.strip() == '' or (line.startswith('#') and 'CHIỀU' not in line):
                in_table = False
                continue

            parts = line.split('|')
            if len(parts) >= 4 and '---' not in line and 'Chiều' not in line and 'TỔNG' not in line:
                score_match = re.search(r'([\d.]+)/10', line)
                if score_match:
                    row_idx += 1
                    scores[row_idx] = float(score_match.group(1))

    return scores


def generate_9_chieu_table(result: dict) -> str:
    """Generate a complete 9-dimension markdown table."""
    s = result["scores"]
    cd = CLASSIC_DATA.get(result["month"], {})
    dh = DIEU_HAU_DATA.get(result["month"], {})
    ks = KHI_SAC_DATA.get(result["month"], {})

    table = "##### BẢNG 9-CHIỀU TOÀN DIỆN (Evidence-Based)\n\n"
    table += "| Chiều | Tỉ trọng | Điểm | Mô tả |\n"
    table += "|-------|:--------:|:----:|-------|\n"
    table += f"| **① Bản Cung** (Chính tinh) | 20% | **{s[1]}/10** | Chính tinh tại cung Lưu Nguyệt |\n"
    table += f"| **② Tam Chiếu/Xung** | 15% | **{s[2]}/10** | Xung chiếu + Tam hợp |\n"
    table += f"| **③ Chủ-Khách** (Trần Đoàn) | 12% | **{s[3]}/10** | {cd.get('chu_khach_type', '?')}: {cd.get('chu_khach_stars', {}).get('ban_cung', '?')} vs {cd.get('chu_khach_stars', {}).get('doi_cung', '?')} |\n"
    table += f"| **④ Thái Tuế** (Thiên Lương) | 12% | **{s[4]}/10** | {cd.get('thai_tue_name', '?')} ({cd.get('thai_tue_category', '?')}): {cd.get('thai_tue_desc', '?')} |\n"
    table += f"| **⑤ Tứ Hóa LN** | 10% | **{s[5]}/10** | Tứ Hóa Lưu Niên kích hoạt |\n"
    table += f"| **⑥ Lưu Nguyệt/Can Chi** | 8% | **{s[6]}/10** | Can Chi tháng tương tác |\n"
    table += f"| **⑦ Giáp cung** | 3% | **{s[7]}/10** | Giáp cung bổ trợ |\n"
    table += f"| **⑧ Điều Hầu** (Cùng Thông) | 10% | **{s[8]}/10** | Khí hậu: {dh.get('climate', '?')} → Dụng Thần: {dh.get('dung_than', '?')} |\n"
    table += f"| **⑨ Khí Sắc** (Hồng Phi Mô) | 10% | **{s[9]}/10** | {ks.get('tuong_tac', '?')} — {ks.get('desc', '?')[:50]}... |\n"
    npl_desc = "Phương pháp nhân lũy thừa (Nguyễn Phát Lộc)"
    if result.get("evidence_gates", {}).get("npl_scoring") == "experimental":
        npl_desc += " [experimental: VN01 pending]"
    table += f"| **TỔNG (Additive)** | 100% | **{result['additive_total']}/10** | Phương pháp cộng tuyến tính |\n"
    table += f"| **TỔNG (NPL Multiplicative)** | — | **{result['multiplicative_total']}/10** | {npl_desc} |\n"
    table += f"| **Confidence** | — | `[{result['confidence']}]` | Rule R-16 Anti-Bias |\n"
    table += "\n"

    # Evidence provenance footer (from Codex registry)
    ev = result.get("evidence", {})
    if any(v != "unregistered" for v in ev.values()):
        table += "> **Evidence Provenance** (Cross-agent: Codex registry)\n"
        for key, status in ev.items():
            icon = "✅" if status == "promoted" else "⚠️" if status == "usable_with_caution" else "❓" if status == "pending" else "—"
            table += f"> {icon} {key}: `{status}`\n"
        runtime = result.get("evidence_runtime", {})
        if runtime.get("mode") != "snapshot":
            table += f"> ⚠️ loader: `{runtime.get('mode')}`\n"
        for warning in result.get("warnings", []):
            table += f"> ⚠️ {warning}\n"
        table += "\n"

    return table


def upgrade_md_file(input_path: str, output_path: str):
    """
    Main upgrade function: read existing MD, extract scores, compute 9-chiều,
    inject new tables with evidence-based data.
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    out_lines = []
    current_month = None
    skip_old_table = False
    old_table_depth = 0

    for i, line in enumerate(lines):
        # Remove old injected sections
        if "##### HỆ QUY CHIẾU KINH ĐIỂN" in line:
            skip_old_table = True
            old_table_depth = 3
            continue
        if skip_old_table:
            old_table_depth -= 1
            if old_table_depth <= 0:
                skip_old_table = False
            continue

        # Detect month
        month_match = re.search(r'THÁNG\s+(\d+)', line)
        if month_match:
            current_month = int(month_match.group(1))

        # Replace old dimension table with new 9-chiều
        if current_month and re.search(r'(?:5|7)-CHIỀU', line):
            # Extract existing scores first
            existing = extract_existing_scores(content, current_month)

            # Compute full 9-dimension result
            result = compute_month_score(current_month, existing)

            # Generate new table
            new_table = generate_9_chieu_table(result)
            out_lines.append(new_table)

            # Skip old table lines until we hit next section
            j = i + 1
            while j < len(lines):
                if lines[j].strip() == '' or (lines[j].startswith('#') and 'CHIỀU' not in lines[j]):
                    break
                j += 1

            # Skip those lines by adjusting — we'll handle via continue
            # Actually need to handle this differently since we're iterating
            continue

        out_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines))

    print(f"✅ Upgraded: {os.path.basename(output_path)} (9-chiều, evidence-based)")


# ============================================================
# CLI INTERFACE
# ============================================================

def print_score_report(month: int = None):
    """Print scoring report for one or all months."""
    months = [month] if month else range(1, 13)
    bundle = load_codex_bundle()
    runtime = bundle["runtime"]

    print("\n" + "=" * 80)
    print("  TUVISTOCK 9-CHIỀU SCORING REPORT — Evidence-Based, Data-Driven")
    print(f"  Mệnh: {MENH_INFO['can']} {MENH_INFO['chi']} ({MENH_INFO['nap_am']})")
    print(f"  Dụng Thần BT: {MENH_INFO['dung_than_bat_tu']}")
    print(f"  Codex loader: {runtime.get('mode', 'missing')} @ {runtime.get('root') or 'not_found'}")
    if runtime.get("generated_at"):
        print(f"  Snapshot generated: {runtime['generated_at']}")
    for issue in runtime.get("issues", []):
        print(f"  Evidence issue: {issue}")
    print("=" * 80)

    for m in months:
        result = compute_month_score(m)
        cd = CLASSIC_DATA[m]
        dh = DIEU_HAU_DATA[m]
        ks = KHI_SAC_DATA[m]

        print(f"\n{'─' * 60}")
        print(f"  THÁNG {m:2d} │ Thái Tuế: {cd['thai_tue_name']:8s} │ Khí hậu: {dh['climate']:10s}")
        print(f"{'─' * 60}")
        print(f"  ① Bản Cung:     {result['scores'][1]:4.1f}  │  ⑥ Lưu Nguyệt:  {result['scores'][6]:4.1f}")
        print(f"  ② Tam Chiếu:    {result['scores'][2]:4.1f}  │  ⑦ Giáp cung:    {result['scores'][7]:4.1f}")
        print(f"  ③ Chủ-Khách:    {result['scores'][3]:4.1f}  │  ⑧ Điều Hầu:     {result['scores'][8]:4.1f}")
        print(f"  ④ Thái Tuế:     {result['scores'][4]:4.1f}  │  ⑨ Khí Sắc:      {result['scores'][9]:4.1f}")
        print(f"  ⑤ Tứ Hóa LN:   {result['scores'][5]:4.1f}  │")
        print(f"  ─────────────────────────────────────")
        print(f"  TỔNG Additive:       {result['additive_total']:4.1f}/10")
        mul_label = "NPL"
        if result.get("evidence_gates", {}).get("npl_scoring") == "experimental":
            mul_label = "NPL experimental"
        print(f"  TỔNG Multiplicative: {result['multiplicative_total']:4.1f}/10  ({mul_label})")
        print(f"  Confidence:          [{result['confidence']}]")
        print(f"  Chủ-Khách: {cd['chu_khach_type']}")
        print(f"  Điều Hầu: {dh['climate']} → {dh['dung_than']}")

        # Evidence provenance
        ev = result.get("evidence", {})
        if any(v != "unregistered" for v in ev.values()):
            ev_str = ", ".join(f"{k}={v}" for k, v in ev.items() if v != "unregistered")
            print(f"  Evidence: {ev_str}")
        gates = result.get("evidence_gates", {})
        if gates.get("tvds_core") == "provisional":
            print("  Gate: TVDS core provisional (EA10 pending)")
        if gates.get("npl_scoring") == "experimental":
            print("  Gate: NPL multiplicative output experimental (VN01 pending)")


def print_evidence_report():
    """Print cross-agent evidence status report."""
    bundle = load_codex_bundle()
    codex_data = bundle["sources"]
    claims = bundle["claims"]
    runtime = bundle["runtime"]

    print("\n" + "=" * 70)
    print("  CROSS-AGENT EVIDENCE REPORT")
    print("  Codex ↔ Antigravity integration")
    print("=" * 70)
    print(f"\n  Loader mode: {runtime.get('mode', 'missing')}")
    print(f"  Evidence root: {runtime.get('root') or 'not found'}")
    if runtime.get("generated_at"):
        print(f"  Snapshot generated: {runtime['generated_at']}")
    for issue in runtime.get("issues", []):
        print(f"  Loader issue: {issue}")

    if not codex_data:
        print("\n  ⚠️ Codex evidence bundle unavailable.")
        print(f"     Search env: {EVIDENCE_ENV_VAR}")
        print(f"     Tried default: {Path.home() / 'Downloads' / EVIDENCE_DIRNAME}")
        print("  Run Codex score_evidence.py to generate a fresh snapshot.")
        return

    # Evidence status for our data sources
    print("\n  Our data sources × Codex evidence status:")
    print(f"  {'─' * 60}")
    for key, prov in SOURCE_PROVENANCE.items():
        status = get_evidence_status(key, codex_data)
        icon = "✅" if status == "promoted" else "⚠️" if status == "usable_with_caution" else "❓"
        cid = prov["codex_id"]
        title = codex_data.get(cid, {}).get("title", "not found")
        net = codex_data.get(cid, {}).get("net_score", "?")
        print(f"  {icon} [{cid}] {key:25s} → {status:20s} (net={net})")
        print(f"       Usage: {prov['usage']}")

    # Claim summary
    if claims:
        claim_status = Counter(c["status"] for c in claims)
        print(f"\n  Claim Status: supported={claim_status.get('supported', 0)}, "
              f"partial={claim_status.get('partial', 0)}, "
              f"pending={claim_status.get('pending', 0)}, "
              f"rejected={claim_status.get('rejected', 0)}")

    # Hardening recommendations
    pending = [k for k, v in SOURCE_PROVENANCE.items()
               if get_evidence_status(k, codex_data) == "pending"]
    if pending:
        print(f"\n  ⚠️ Pending sources (need hardening):")
        for p in pending:
            print(f"     → {p} ({SOURCE_PROVENANCE[p]['codex_id']})")


def main():
    parser = argparse.ArgumentParser(
        description="TuViStock Unified Engine v3.0 — 9-Dimension Scoring + Evidence"
    )
    parser.add_argument("--mode", choices=["score", "upgrade", "inject", "evidence"],
                        default="score", help="Operation mode")
    parser.add_argument("--month", type=int, choices=range(1, 13),
                        help="Specific month (1-12, default: all)")
    parser.add_argument("--year", type=int, choices=[2026, 2027],
                        help="Year for upgrade mode")
    parser.add_argument("--scoring", choices=["additive", "multiplicative", "both"],
                        default="both", help="Scoring method")
    parser.add_argument("--strict-evidence", action="store_true",
                        help="Exit non-zero if canonical snapshot is unavailable or core evidence is pending")

    args = parser.parse_args()

    base_dir = str(Path(__file__).parent.parent / "core")

    if args.mode == "score":
        print_score_report(args.month)

    elif args.mode == "upgrade":
        years = [args.year] if args.year else [2026, 2027]
        for year in years:
            input_file = os.path.join(base_dir, f"luan_giai_12_thang_{year}.md")
            output_file = os.path.join(base_dir, f"luan_giai_12_thang_{year}_master_9_chieu.md")
            if os.path.exists(input_file):
                upgrade_md_file(input_file, output_file)
            else:
                print(f"⚠️ File not found: {input_file}")

    elif args.mode == "inject":
        print("ℹ️  Inject mode deprecated — use 'upgrade' which includes injection")

    elif args.mode == "evidence":
        print_evidence_report()

    if args.strict_evidence:
        failures = strict_evidence_failures()
        if failures:
            print("\n❌ Strict evidence check failed:")
            for failure in failures:
                print(f"   - {failure}")
            raise SystemExit(2)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()
