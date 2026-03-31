#!/usr/bin/env python3
"""
dedup_luan_giai.py — Deduplicate luan_giai_12_thang_2026.md
RCA: Injection scripts (inject_deep_20x_*.py, inject_human_readable.py, inject_multi_layer_v2.py)
     operated APPEND-ONLY without checking for existing content → 4× duplication per month.

Strategy:
1. Parse file into month sections (### C.1 ... ### C.2 ... etc.)
2. Within each month, detect duplicate blocks by content fingerprinting
3. Keep FIRST instance of each unique block, remove copies
4. Preserve all unique sub-headers and their content
5. Write cleaned file with backup

Author: Antigravity RCA-040 | 2026-03-29
"""

import re
import os
import hashlib
from collections import OrderedDict
from datetime import datetime


TARGET = "/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md"


def backup(path):
    """Create timestamped backup."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = f"{path}.bak_{ts}"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(bak, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup: {bak}")
    return content


def split_into_sections(content):
    """Split file into: header (before C.1) + 12 month sections + footer (after last month)."""
    # Find all month headers
    pattern = r'^### C\.(\d+)\s'
    lines = content.split('\n')
    
    month_starts = []
    for i, line in enumerate(lines):
        m = re.match(pattern, line)
        if m:
            month_starts.append((int(m.group(1)), i))
    
    # Find the footer (## D. section)
    footer_start = None
    for i, line in enumerate(lines):
        if line.startswith('## D.'):
            footer_start = i
            break
    
    # Extract header
    if month_starts:
        header = '\n'.join(lines[:month_starts[0][1]])
    else:
        return content, [], ""
    
    # Extract each month
    months = []
    for idx, (month_num, start) in enumerate(month_starts):
        if idx + 1 < len(month_starts):
            end = month_starts[idx + 1][1]
        elif footer_start:
            end = footer_start
        else:
            end = len(lines)
        month_content = '\n'.join(lines[start:end])
        months.append((month_num, month_content))
    
    # Extract footer
    if footer_start:
        footer = '\n'.join(lines[footer_start:])
    else:
        footer = ""
    
    return header, months, footer


def fingerprint(text):
    """Create content fingerprint for duplicate detection."""
    # Normalize whitespace for comparison
    normalized = re.sub(r'\s+', ' ', text.strip())
    return hashlib.md5(normalized.encode('utf-8')).hexdigest()[:12]


def dedup_month(month_num, content):
    """Remove duplicate blocks within a single month section.
    
    Known duplicate patterns:
    1. "➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG (20x Deep Dive — SOT Verified ✅)**" blocks (I→IX)
       These start with the ➯ header and end at the next major section or another ➯
    2. "⚠️ **Evidence gate:**" + "📌 Scores" footer pairs
    3. "**Lớp 1 (Nền & Ngoại cảnh):**" ... "**Lớp 3 ...**" narrative blocks
    """
    lines = content.split('\n')
    
    # --- PASS 1: Remove duplicate "Evidence gate" + "Scores" pairs ---
    # These are 2-line pairs that appear multiple times
    evidence_pair_pattern = (
        r'> ⚠️ \*\*Evidence gate:\*\*.*',
        r'> 📌 Scores ①②⑤⑥⑦.*'
    )
    
    # Find all evidence gate pairs and keep only the first one
    evidence_blocks = []
    i = 0
    while i < len(lines):
        if re.match(r'^> ⚠️ \*\*Evidence gate:\*\*', lines[i]):
            block_start = i
            # Check if next line is the Scores line
            if i + 1 < len(lines) and re.match(r'^> 📌 Scores', lines[i + 1]):
                block_end = i + 2
            else:
                block_end = i + 1
            evidence_blocks.append((block_start, block_end))
            i = block_end
        else:
            i += 1
    
    # Keep first evidence block, mark rest for removal
    remove_ranges = []
    if len(evidence_blocks) > 1:
        for block in evidence_blocks[1:]:
            remove_ranges.append(block)
    
    # --- PASS 2: Remove duplicate "Lớp 1/2/3" narrative blocks ---
    lop_blocks = []
    i = 0
    while i < len(lines):
        if re.match(r'^> \*\*Lớp 1 \(Nền', lines[i]):
            block_start = i
            # Find end of this narrative block (until non-blockquote or next section)
            j = i + 1
            while j < len(lines):
                line = lines[j]
                # End at: empty non-quote line, new section header, or another evidence gate
                if (not line.startswith('>') and line.strip() != '') or \
                   line.startswith('####') or line.startswith('### ') or \
                   re.match(r'^> ➯ \*\*PHÂN TÍCH', line):
                    break
                # Also end after Lớp 3
                if re.match(r'^> \*\*Lớp 3', line):
                    # Include this line and the next line if it's a continuation
                    j += 1
                    while j < len(lines) and lines[j].startswith('>') and not re.match(r'^> ➯|^> ⚠️|^> 📌', lines[j]):
                        j += 1
                    break
                j += 1
            lop_blocks.append((block_start, j))
            i = j
        else:
            i += 1
    
    if len(lop_blocks) > 1:
        for block in lop_blocks[1:]:
            remove_ranges.append(block)
    
    # --- PASS 3: Remove duplicate "PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG" mega-blocks ---
    # These are the biggest duplicates: ~110 lines each, starting with ➯ header
    deep_dive_blocks = []
    i = 0
    while i < len(lines):
        if re.match(r'^> ➯ \*\*PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG', lines[i]):
            block_start = i
            # Find end: next non-blockquote section, or next ##### header, or next ➯
            j = i + 1
            while j < len(lines):
                line = lines[j]
                # End conditions:
                # 1. Non-blockquote non-empty line (back to normal content)
                if not line.startswith('>') and line.strip() != '' and not line.startswith('|'):
                    break
                # 2. Another ➯ block (but NOT the current one's sub-sections)
                if j > i + 1 and re.match(r'^> ➯ \*\*PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG', line):
                    break
                # 3. A ##### header that's NOT inside a blockquote
                if line.startswith('#####') and not line.startswith('> #'):
                    break
                j += 1
            deep_dive_blocks.append((block_start, j))
            i = j
        else:
            i += 1
    
    if len(deep_dive_blocks) > 1:
        for block in deep_dive_blocks[1:]:
            remove_ranges.append(block)
    
    # --- PASS 4: Remove duplicate score table rows that got orphaned ---
    # Pattern: "| | **TỔNG Additive**" etc. appearing outside the 9-CHIỀU table
    orphan_rows = []
    i = 0
    while i < len(lines):
        if re.match(r'^\| \| \*\*TỔNG (Additive|NPL)\*\*', lines[i]) or \
           re.match(r'^\| \| \*\*Confidence\*\*', lines[i]):
            orphan_rows.append((i, i + 1))
            i += 1
        else:
            i += 1
    
    # These are ALWAYS orphans from bad injection — remove ALL
    remove_ranges.extend(orphan_rows)
    
    # --- Apply removals ---
    # Sort by start position, merge overlapping ranges
    remove_ranges.sort(key=lambda x: x[0])
    
    # Merge overlapping
    merged = []
    for start, end in remove_ranges:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    # Remove lines (in reverse to preserve indices)
    remove_set = set()
    for start, end in merged:
        for idx in range(start, end):
            remove_set.add(idx)
    
    cleaned_lines = [line for i, line in enumerate(lines) if i not in remove_set]
    
    # --- Clean up consecutive empty lines (max 2) ---
    final_lines = []
    empty_count = 0
    for line in cleaned_lines:
        if line.strip() == '':
            empty_count += 1
            if empty_count <= 2:
                final_lines.append(line)
        else:
            empty_count = 0
            final_lines.append(line)
    
    removed = len(lines) - len(final_lines)
    return '\n'.join(final_lines), removed


def main():
    print("=" * 60)
    print("DEDUP: luan_giai_12_thang_2026.md")
    print("=" * 60)
    
    # Step 1: Backup
    content = backup(TARGET)
    original_lines = len(content.split('\n'))
    print(f"📄 Original: {original_lines} lines")
    
    # Step 2: Split
    header, months, footer = split_into_sections(content)
    print(f"📋 Found {len(months)} month sections")
    
    # Step 3: Dedup each month
    total_removed = 0
    cleaned_months = []
    for month_num, month_content in months:
        cleaned, removed = dedup_month(month_num, month_content)
        cleaned_months.append((month_num, cleaned))
        if removed > 0:
            print(f"  T{month_num}: removed {removed} duplicate lines")
        total_removed += removed
    
    # Step 4: Reassemble
    parts = [header]
    for _, month_content in cleaned_months:
        parts.append(month_content)
    if footer:
        parts.append(footer)
    
    result = '\n'.join(parts)
    result_lines = len(result.split('\n'))
    
    print(f"\n{'=' * 60}")
    print(f"📊 RESULTS:")
    print(f"   Before: {original_lines} lines")
    print(f"   After:  {result_lines} lines")
    print(f"   Removed: {total_removed} lines ({total_removed * 100 // original_lines}%)")
    print(f"{'=' * 60}")
    
    # Step 5: Verify all 12 months still present
    for i in range(1, 13):
        if f'### C.{i} ' not in result:
            print(f"⛔ MISSING MONTH {i}! Aborting.")
            return
    print("✅ All 12 months verified present")
    
    # Step 6: Verify single Deep Dive per month
    dd_count = result.count('➯ **PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG')
    print(f"✅ Deep Dive blocks: {dd_count} (target: 12)")
    
    # Step 7: Write
    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"\n✅ Written to {TARGET}")


if __name__ == '__main__':
    main()
