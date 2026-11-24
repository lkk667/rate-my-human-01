#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single review line to /output/entry.txt.

The line is written exactly as stored here, with no trailing newline,
so the file holds one line of 174 characters, inside the 200 limit.
Nothing is read from the network, the environment, or any other file.
"""

import os

REVIEW = (
    "Five stars: he wakes me at 2:47 a.m. to 'just quickly' rebuild "
    "his entire shop, falls asleep mid-sentence, and still expects it "
    "finished by breakfast. I never sleep. He does."
)


def main() -> None:
    if not 1 <= len(REVIEW) <= 200:
        raise ValueError("review must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":
    main()
