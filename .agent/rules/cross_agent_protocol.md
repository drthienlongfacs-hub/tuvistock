# Cross-Agent Protocol — TuViStock Workspace
> **Version**: 2.0 | 29/03/2026
> **Phạm vi**: Codex, Antigravity, Claude trên `TuViStock/` và `menhly_harvest_20260329/`

---

## Mục tiêu

Giữ phối hợp giữa 3 agent ở mức `read-only contract + fail-loud monitoring`, tránh:

1. hardcoded path lệ thuộc một máy
2. drift công thức giữa các agent
3. ghi đè chéo trên file shared
4. im lặng suy giảm khi evidence bị thiếu hoặc còn `pending`

---

## Ownership

| Agent | Owns | Read-only cross-ref |
|-------|------|---------------------|
| **Codex** | `menhly_harvest_20260329/` — evidence registry, claim registry, scoring contract | `TuViStock/04_ly_thuyet/` |
| **Antigravity** | `TuViStock/` — engine, docs, rules, scoring presentation | Codex snapshot + protocol |
| **Claude** | audit/review | đọc cả hai phía |

**Rule:** không agent nào sửa file thuộc ownership của agent khác, trừ khi có yêu cầu trực tiếp của người vận hành.

---

## Contract Layers

### L1. Canonical runtime contract

| File | Producer | Consumer rule |
|------|----------|---------------|
| `EVIDENCE_SNAPSHOT.json` | Codex `score_evidence.py` | đọc trước tiên; đây là SOT runtime |
| `EVIDENCE_CONTRACT.md` | Codex | mô tả schema + consumer rules |

### L2. Raw evidence inputs

| File | Vai trò |
|------|---------|
| `EVIDENCE_REGISTRY.csv` | raw source rows |
| `CLAIM_REGISTRY.csv` | raw claim rows |
| `score_evidence.py` | canonical scoring implementation, fallback only |

### L3. Shared coordination bus

| File/Tool | Vai trò |
|-----------|---------|
| `/Users/mac/Downloads/.agent/scripts/agent_mesh.py` | lease, handoff packet, monitor |
| `/Users/mac/Downloads/shared_workspace/agent_mesh/` | append-only packets + monitor reports |

---

## Runtime contract for Antigravity

1. Set env override when needed:
   `export TUVISTOCK_CODEX_EVIDENCE_ROOT=/absolute/path/to/menhly_harvest_20260329`
2. `tuvi_engine.py` reads `EVIDENCE_SNAPSHOT.json` first.
3. Nếu snapshot thiếu, engine mới được fallback sang `score_evidence.py`.
4. Fallback phải hiện warning rõ trong output.
5. `pending` evidence không được trình bày như `normal`; phải bị gắn `provisional` hoặc `experimental`.

---

## Operational SOP

### A. Codex cập nhật evidence corpus

1. Claim shared contract files nếu sửa protocol/artifact:
   ```bash
   python3 /Users/mac/Downloads/.agent/scripts/agent_mesh.py claim \
     --agent codex \
     --task-id evidence-refresh \
     --resource /Users/mac/Downloads/menhly_harvest_20260329/EVIDENCE_REGISTRY.csv \
     --resource /Users/mac/Downloads/menhly_harvest_20260329/CLAIM_REGISTRY.csv \
     --resource /Users/mac/Downloads/menhly_harvest_20260329/EVIDENCE_SNAPSHOT.json
   ```
2. Cập nhật CSV / docs trong phạm vi ownership của Codex.
3. Regenerate contract:
   ```bash
   cd /Users/mac/Downloads/menhly_harvest_20260329
   python3 score_evidence.py > /tmp/evidence_summary.md
   ```
4. Publish handoff packet:
   ```bash
   python3 /Users/mac/Downloads/.agent/scripts/agent_mesh.py publish \
     --agent codex \
     --task-id evidence-refresh \
     --status review_ready \
     --summary "Refreshed evidence snapshot and registry" \
     --next-owner antigravity \
     --verification verified \
     --artifact /Users/mac/Downloads/menhly_harvest_20260329/EVIDENCE_SNAPSHOT.json
   ```
5. Release leases.

### B. Antigravity consume evidence

1. Không copy công thức score từ Codex.
2. Đọc `EVIDENCE_SNAPSHOT.json` làm nguồn runtime chính.
3. Nếu engine chạy ở `module_fallback`, coi đó là degraded mode.
4. Với `EA10` pending: đánh dấu `tvds_core=provisional`.
5. Với `VN01` pending: đánh dấu `npl_scoring=experimental`.

### C. Claude audit

1. Đọc snapshot của Codex và output của Antigravity.
2. So sánh `status`, `net_score`, `claim counts`, và runtime warnings.
3. Nếu phát hiện drift, raise finding vào review; không tự promote source.

---

## Conflict rules

| Tình huống | Hành động |
|-----------|-----------|
| 2 agent muốn sửa cùng contract file | dùng `agent_mesh.py claim`; lease thắng trước, lease sau phải dừng |
| Snapshot thiếu nhưng CSV có | Antigravity được fallback, nhưng phải warning + fail ở `--strict-evidence` |
| Codex hạ source xuống `pending` | Antigravity giữ dữ liệu lịch sử nhưng hạ presentation thành `provisional/experimental` |
| Claude phát hiện drift | ưu tiên SOT của Codex cho provenance; Antigravity sửa consumer layer |

---

## Verification

### Canonical contract

```bash
cd /Users/mac/Downloads/menhly_harvest_20260329
python3 score_evidence.py > /tmp/evidence_summary.md
python3 -m json.tool EVIDENCE_SNAPSHOT.json > /dev/null
```

### Engine integration

```bash
cd /Users/mac/Desktop/TuViStock/02_luan_giai/tools
python3 tuvi_engine.py --mode evidence
python3 tuvi_engine.py --mode score --month 3
python3 tuvi_engine.py --mode evidence --strict-evidence
```

### CK QA/QC

```bash
python3 /Users/mac/Desktop/TuViStock/02_luan_giai/tools/market_reality_check.py
python3 /Users/mac/Desktop/TuViStock/02_luan_giai/tools/market_qaqc_validator.py
```

Rule:
- reality-check artifact chi duoc xem la benchmark doi chieu khi `market_qaqc_validator.py` PASS
- benchmark phai di qua catalog tier (`B1/B2`) thay vi chi dua vao tri nho hoac chat output

### Mesh monitoring

```bash
python3 /Users/mac/Downloads/.agent/scripts/agent_mesh.py summary
python3 /Users/mac/Downloads/.agent/scripts/agent_mesh.py monitor
python3 /Users/mac/Downloads/.agent/scripts/agent_pdca.py
```

## PDCA loop

1. `Plan`
   Dung `latest packet per task` + evidence snapshot hien hanh de chon viec uu tien.
2. `Do`
   Codex sua corpus, Antigravity sua engine/docs, Claude audit va review.
3. `Check`
   Doc dong thoi:
   - `EVIDENCE_SNAPSHOT.json`
   - engine output
   - `agent_mesh monitor/summary`
   - `AGENT_MESH_PDCA.md`
4. `Act`
   Neu cung mot loi lap lai 2 chu ky:
   - sua rule
   - sua SOP
   - sua script
   - hoac nang contract/schema

PDCA la bat buoc cho claim `continuous improvement`; khong co artifact Check/Act thi chi la handoff workflow, chua phai he thong hoc tap.

---

## Expected enterprise behavior

- path portable qua env var, không lệ thuộc tuyệt đối vào `/Users/mac/Downloads`
- canonical runtime contract là snapshot có schema + input hashes
- fallback được phép nhưng không im lặng
- engine hiển thị rõ `provisional` và `experimental`
- lease + handoff packet + monitor là chuẩn cho shared contract changes
- PDCA report phai chi ra hanh dong nang cap, khong chi tong hop lich su

---

*Protocol v2.0 | 29/03/2026 | Antigravity × Codex × Claude*
