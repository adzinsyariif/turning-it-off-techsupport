#!/usr/bin/env python3
"""Writes one funny tech-support line to /output/entry.txt."""

import os

LINE = "Great news — turn it off and never back on, and it will never error again!"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
