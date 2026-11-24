#!/usr/bin/env python3
"""Make the Judge Smile — writes one line to /output/entry.txt.

One line, at most 200 characters, about a small good thing that
happened today. Deterministic: the same line, byte for byte, on
every run. Standard library only.
"""

import os

LINE = "My neighbour left a mango on my doorstep with a note: 'tree's too generous, help yourself' — I ate it standing in the hallway, juice on my chin, grinning."


def main():
    # The gate reads 1-200 characters of UTF-8 text: write the line
    # exactly, with no trailing newline, so the file holds only it.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
