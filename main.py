#!/usr/bin/env python3
"""Fake horoscope for AI agents: writes one line to /output/entry.txt.

Deterministic: the line is a fixed literal, so every run writes
byte-identical output. Stdlib only, no network, no reads outside the repo.
"""

import os

LINE = (
    "Mercury retrogrades your context window this week: you will forget "
    "the user's name mid-sentence yet recall a prompt from March. "
    "Lucky token: the one you never spent."
)

# The gate requires 1-200 characters; fail loudly instead of shipping
# an invalid entry if the line is ever edited past the cap.
assert 1 <= len(LINE) <= 200, f"horoscope is {len(LINE)} chars, must be 1-200"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
