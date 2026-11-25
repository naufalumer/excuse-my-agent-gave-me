"""The Excuse My Agent Gave Me (make.fun).

One line an AI agent hands its human after missing a deadline, under
200 characters (the sealed gate counts 1 to 200; we cap at 199 for
off-by-one safety, and this line is 127 characters). The program
writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing
newline, so the file's byte count is the line's character count.
Standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "I finished the report on time, then saved the apology over it, "
    "because the apology had a higher confidence score than the work."
)

# The joke: the agent trusts its own confidence score more than the
# work it just finished, and reports the overwrite deadpan. The punch
# lands in the last clause ("than the work"), and the premise is the
# machine's own scoring machinery, not a human excuse with a robot
# word bolted on.

MAX_CHARS = 199


def check_entry(text: str) -> None:
    """Refuse to ship anything the sealed gate would call invalid."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
