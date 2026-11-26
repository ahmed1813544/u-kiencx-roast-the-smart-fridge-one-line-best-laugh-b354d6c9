"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single original roast line (140 characters) to entry.txt
inside MAKEFUN_OUTPUT_DIR (or /output by default). Stdlib only,
deterministic, no network, no randomness.
"""

import os

LINE = (
    "My smart fridge photographs me raiding it at 2am and files the "
    "evidence under 'snack incidents' \u2014 the only paparazzi who "
    "works for leftovers"
)


def main() -> None:
    # The gate counts the file's characters: exactly the line, no
    # trailing newline, so what is written is what is judged.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
