"""The Funniest Toaster Error Message — KA entry.

One line, at most 120 characters: the error message a kitchen toaster
shows its owner when something goes wrong. Deadpan appliance voice:
the toaster burned the bread because the dial was set to VOLCANO, and
it followed the order exactly. Reads like a real message on a real
appliance, with a concrete setting and a count, closed ending. The
joke is the obedience: it did exactly what the dial asked, in 47
seconds flat, and now it calmly asks the human to scrape.
"""

import os
import sys

TEXT = "ERROR E07: dial set to VOLCANO. Bread incinerated in 47 seconds, exactly as instructed. Please scrape."


def main() -> int:
    line = TEXT
    if not line or not line.strip():
        print("gate failed: empty line", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("gate failed: more than one line", file=sys.stderr)
        return 1
    if len(line) > 120:
        print(f"gate failed: {len(line)} chars > 120", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"ok: {len(line)} chars, 1 line, byte-for-byte verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
