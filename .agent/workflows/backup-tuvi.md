---
description: Backup và recovery protocol cho TuViStock — tag, checksum, phục hồi
---

# Workflow: TuViStock Backup & Recovery

> **Trigger:** Sau mỗi milestone (session kết thúc, module hoàn thành, feedback correction)

---

## 1. PRE-BACKUP CHECKLIST

// turbo
- [ ] `_REGISTRY.md` đã cập nhật file mới
- [ ] `_FEEDBACK_LOG.md` đã ghi correction (nếu có)
- [ ] Quality Gate chạy cho file vừa sửa

## 2. GENERATE CHECKSUMS

// turbo
```bash
cd /Users/mac/Desktop/TuViStock
find . -name "*.md" -not -path "./.git/*" | sort | xargs shasum -a 256 > .agent/source_of_truth/CHECKSUMS.sha256
```

## 3. GIT COMMIT + TAG

```bash
cd /Users/mac/Desktop/TuViStock
git add -A
git commit -m "[MILESTONE] <mô tả ngắn>"
git tag -a v<major>.<minor>-<YYYYMMDD> -m "<mô tả>"
```

**Naming convention:**
- `v1.0-20260315` — Major milestone (reorg, new skill)
- `v1.1-20260316` — Minor update (content enrichment)
- `v1.1.1-20260316` — Hotfix (feedback correction)

## 4. VERIFY BACKUP

// turbo
```bash
cd /Users/mac/Desktop/TuViStock
shasum -a 256 -c .agent/source_of_truth/CHECKSUMS.sha256
git log --oneline -5
git tag -l
```

## 5. RECOVERY PROTOCOL

Khi cần phục hồi:

```bash
# Xem danh sách tags
git tag -l

# Phục hồi về milestone cụ thể
git checkout v1.0-20260315

# Tạo branch recovery
git checkout -b recovery-from-v1.0

# Verify integrity
shasum -a 256 -c .agent/source_of_truth/CHECKSUMS.sha256
```

## 6. EMERGENCY: File bị hỏng

```bash
# Khôi phục 1 file cụ thể từ commit trước
git checkout HEAD~1 -- path/to/file.md

# Hoặc từ tag cụ thể
git checkout v1.0-20260315 -- 02_luan_giai/core/luan_giai_giai_than_master_2026.md
```
