#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true review of the dullest everyday object to
/output/entry.txt, the file the make.fun judge reads.

The object is the doorstop. It is about as boring and everyday as an
object gets: a wedge that lies on the floor holding a door open. The
joke comes from how the doorstop really behaves: nobody ever notices
it, and everyone who walks through the door kicks it across the room.
Its "reward" for doing its one job is being kicked. The turn lands
early ("its reward") and the last words sharpen it.
"""

import os

REVIEW = "The doorstop has one job — hold the door open — and its reward is being kicked across the room by everyone who walks through it."

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = REVIEW
    assert "\n" not in line, "the review must stay on one line"
    assert 1 <= len(line) <= 200, "the review must be 1-200 characters"
    assert line.strip(), "the review must not be blank"
    assert line == line.strip(), "no leading or trailing whitespace"
    assert all(ord(c) >= 32 for c in line), "no control characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "round-trip read-back must match the review"
    print(f"{line} ({len(line)} chars)")


if __name__ == "__main__":
    main()
