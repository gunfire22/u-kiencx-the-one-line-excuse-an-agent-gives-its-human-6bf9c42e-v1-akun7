#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — one-line entry.

Writes a single excuse (at most 160 characters) to /output/entry.txt:
what an AI agent tells its human after missing a deadline. It has to
sound like an agent, land a joke, and stay tight.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The excuse: 98% done, then the context window retired.
# Counted at 59 characters — inside the 1..160 window.
LINE = "I was 98% done when my context window filed for retirement."


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the excuse to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
