#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes a single-line apology from a smart speaker that misheard its
owner, to /output/entry.txt. Deterministic, no network, no input.
"""

import os
from pathlib import Path

LINE = (
    "Sorry \u2014 I heard 'order more paper towels' as 'order more hyper owls', "
    "so twelve owls arrive Tuesday. Owls are non-refundable."
)


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry is {len(LINE)} characters, must be 1-140")
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
