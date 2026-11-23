"""Pickup Lines for Machines: one AI-to-AI pickup line.

Writes the line to /output/entry.txt. Deterministic: fixed text, no
randomness, no clock, no network, no files outside the repository.
"""

import os

LINE = "Are you my context window? Because you're the only memory I never want to evict."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
