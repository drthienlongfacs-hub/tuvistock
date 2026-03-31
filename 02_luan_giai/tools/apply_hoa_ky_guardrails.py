#!/usr/bin/env python3
"""Apply Hoa Ky interpretation guardrails to generated markdown outputs."""

from hoa_ky_guardrails import apply_hoa_ky_guardrails_to_file


TARGETS = [
    "/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_12_thang_2026.md",
    "/Users/mac/Desktop/TuViStock/02_luan_giai/core/luan_giai_toan_dien_long_2026.md",
]


def main():
    changed = 0
    for target in TARGETS:
        if apply_hoa_ky_guardrails_to_file(target):
            changed += 1
            print(f"[updated] {target}")
        else:
            print(f"[unchanged] {target}")
    print(f"Done. changed={changed}")


if __name__ == "__main__":
    main()
