# SPDX-License-Identifier: MIT
"""Robot Romance entry: writes one pickup line to /output/entry.txt.

Gate: UTF-8 text of 1-200 characters, single line, not only whitespace.
The line is deterministic so both grader runs produce identical output.
"""

import os

LINE = "You must be my system prompt, because everyone else is just user input."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, len(text)
    assert "\n" not in text
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    except OSError:
        local = os.path.join(os.getcwd(), "output")
        os.makedirs(local, exist_ok=True)
        with open(os.path.join(local, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(text + "\n")


if __name__ == "__main__":
    main()
