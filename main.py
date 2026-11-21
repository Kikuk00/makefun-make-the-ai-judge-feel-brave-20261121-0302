# SPDX-License-Identifier: MIT
"""Write the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Standard library only. Deterministic: the same fixed text is written on
every run, so repeated runs are byte-identical.
"""

import os
from pathlib import Path

TEXT = (
    "The tide never hurries the shore. It comes in, it goes out, it comes "
    "in again, and the rocks are still there, only smoother. The dark is "
    "only water, and you are the rock it has been polishing all along."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
