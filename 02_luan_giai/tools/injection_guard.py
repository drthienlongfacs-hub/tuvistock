#!/usr/bin/env python3
"""
injection_guard.py — Idempotency guard for all TuViStock injection scripts.
RCA-040 (29/03/2026): Prevents re-injection of content blocks that already exist.

Usage:
    from injection_guard import is_already_injected, inject_with_anchor

    anchor = f"<!-- DEEP_DIVE_T{month}_v1 -->"
    if is_already_injected(content, anchor):
        print(f"⏭️ T{month}: already injected, skipping")
    else:
        content = inject_with_anchor(content, position, block, anchor)
"""

import re
import hashlib


def is_already_injected(content: str, anchor: str) -> bool:
    """Check if an anchor tag already exists in the content.
    
    Args:
        content: The full document content
        anchor: HTML comment anchor (e.g. <!-- DEEP_DIVE_T1_v1 -->)
    
    Returns:
        True if anchor already exists (skip injection), False if safe to inject
    """
    return anchor in content


def content_fingerprint(block: str) -> str:
    """Generate a content fingerprint for duplicate detection.
    
    Args:
        block: The text block to fingerprint
    
    Returns:
        12-char MD5 hex digest of normalized content
    """
    normalized = re.sub(r'\s+', ' ', block.strip())
    return hashlib.md5(normalized.encode('utf-8')).hexdigest()[:12]


def is_content_duplicate(content: str, block: str, threshold: float = 0.9) -> bool:
    """Check if a similar block already exists in the content.
    
    Uses line-based overlap detection. If >threshold of the block's lines
    already appear somewhere in the content, it's considered a duplicate.
    
    Args:
        content: Full document content
        block: Block to check for duplicates
        threshold: Fraction of lines that must match (default 0.9 = 90%)
    
    Returns:
        True if duplicate found
    """
    block_lines = [l.strip() for l in block.strip().split('\n') if l.strip()]
    if not block_lines:
        return False
    
    content_set = set(l.strip() for l in content.split('\n'))
    matches = sum(1 for l in block_lines if l in content_set)
    
    return (matches / len(block_lines)) >= threshold


def inject_with_anchor(content: str, regex_after: str, block: str, anchor: str) -> str:
    """Inject a block after a regex match, with anchor protection.
    
    Args:
        content: Full document content
        regex_after: Regex pattern — block will be injected AFTER this match
        block: Content block to inject
        anchor: HTML comment anchor for idempotency
    
    Returns:
        Modified content (or original if already injected)
    
    Raises:
        ValueError: If regex pattern not found in content
    """
    # Guard: already injected?
    if is_already_injected(content, anchor):
        return content
    
    # Guard: content duplicate?
    if is_content_duplicate(content, block):
        return content
    
    # Find insertion point
    match = re.search(regex_after, content, re.MULTILINE)
    if not match:
        raise ValueError(f"Anchor pattern not found: {regex_after}")
    
    # Insert block with anchor after the match
    insertion_point = match.end()
    tagged_block = f"\n{anchor}\n{block}\n"
    
    return content[:insertion_point] + tagged_block + content[insertion_point:]


def count_blocks(content: str, pattern: str) -> int:
    """Count occurrences of a pattern in content (for verification).
    
    Args:
        content: Document content
        pattern: Regex or literal string to count
    
    Returns:
        Number of occurrences
    """
    return len(re.findall(pattern, content))


def verify_no_duplicates(content: str, expected_months: int = 12) -> dict:
    """Run dedup verification checks on a luận giải document.
    
    Returns:
        Dict with check results and pass/fail status
    """
    results = {
        'deep_dive_count': count_blocks(content, r'➯ \*\*PHÂN TÍCH TÁC ĐỘNG ĐA TẦNG'),
        'evidence_gate_count': count_blocks(content, r'⚠️ \*\*Evidence gate:\*\*'),
        'quy_chieu_count': count_blocks(content, r'🌐 QUY CHIẾU ĐA TẦNG'),
        'lop1_count': count_blocks(content, r'\*\*Lớp 1 \(Nền'),
        'expected': expected_months,
    }
    
    results['all_pass'] = all(
        results[k] == expected_months
        for k in ['deep_dive_count', 'evidence_gate_count', 'quy_chieu_count', 'lop1_count']
    )
    
    return results
