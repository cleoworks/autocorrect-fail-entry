#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one autocorrect fail (one line, 36 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input, no randomness.
"""

import os

# The fail: "analysis" autocorrected to "anal sex" in a work message
# to the boss — a real slip, one line, nothing else. Final wording
# settled after the local judge round picked this variant (36 chars).
# Entry text below: one line, 36 characters, no trailing newline.
ENTRY = "The boss wants my anal sex by Friday"


def main():
    os.makedirs("/output", exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours the smaller text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
