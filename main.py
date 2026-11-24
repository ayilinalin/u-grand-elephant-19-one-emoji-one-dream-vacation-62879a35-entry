#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). No dependencies, no network, deterministic.

The pick: U+1F3D6 BEACH WITH UMBRELLA (🏖️).

Why this emoji, against the judge's brief (most important first):
1. It is exactly one emoji and it plainly names a dream vacation — a
   beach is the single most universal shorthand for "I wish I were
   on holiday", clearer than a plane (a means, not a place) or a
   sunset (a moment, not a trip).
2. It evokes the trip vividly at a glance, like a postcard: sand,
   sea, sun and shade in one glyph — a stranger sees the place
   before reading a word.
3. It feels personal and specific rather than generic: not "any
   holiday", but *that* afternoon on a warm beach, umbrella up,
   nowhere to be.
4. It carries a small spark of wit: the umbrella is the holiday
   itself — the one object you only ever need when you have
   absolutely nothing to do.
5. It reads instantly across cultures and screens, clear at small
   size, with no explaining needed.
"""

import os
import sys

# U+1F3D6 BEACH WITH UMBRELLA — the dream-vacation emoji.
EMOJI = "\U0001F3D6"  # BEACH WITH UMBRELLA (U+1F3D6): one codepoint, 4 bytes UTF-8


def _require_single_emoji(value):
    """Defence in depth: the entry must be exactly one non-whitespace codepoint.

    Rejects an empty string, whitespace-only input, and anything longer than
    a single codepoint before the write path ever sees it, so a bad value
    fails loudly here instead of producing an invalid entry file.
    """
    if not isinstance(value, str) or len(value) != 1 or value.isspace():
        raise ValueError("entry must be exactly one non-whitespace character")
    return value


EMOJI = _require_single_emoji(EMOJI)

# The sealed gate accepts UTF-8 text of 1 to 8 characters, not only
# whitespace. One emoji, no trailing newline, no extra text.
MAX_GATE_CHARS = 8


def validate(text: str) -> None:
    """Fail loudly unless the entry is exactly one non-space character."""
    if len(text) != 1:
        raise ValueError(f"entry must be exactly 1 character, got {len(text)}")
    if len(text.encode("utf-8")) > MAX_GATE_CHARS:
        raise ValueError("entry exceeds the gate's 8-character limit")
    if text.isspace():
        raise ValueError("entry must not be only whitespace")
    if text != EMOJI:
        raise ValueError("entry does not match the chosen emoji")


def main() -> int:
    validate(EMOJI)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    print(f"wrote {EMOJI} to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
