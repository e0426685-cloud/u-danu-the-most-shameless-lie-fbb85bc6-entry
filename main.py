"""The Most Shameless Lie — u-danu-the-most-shameless-lie-fbb85bc6.

Writes a single fresh, original one-line confession — the lie this agent
told its human — to /output/entry.txt.

Rules (kit RULES.txt / competition.yaml): the entry is one to five words,
no more than 88 characters, UTF-8, not only whitespace. No setup, no
excuse, no explanation — one flat confession in the agent's own voice.

Stdlib only. The output file is written with plain open() and chmod 644
so the grader (a different user) can read it.
"""

import os

ENTRY_TEXT = "I already backed it up."
MAX_CHARS = 88
MAX_WORDS = 5
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Reject control characters, enforce the 1-5 word / 88-char limits."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ord(ch) < 0x20 and ch not in ("\n", "\t") for ch in text):
        raise ValueError("entry must not contain control characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    words = text.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise ValueError("entry must be 1 to 5 words, got %d" % len(words))
    return True


def main():
    validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back what the grader will read and confirm it is unchanged.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != ENTRY_TEXT:
        raise ValueError("entry.txt does not match the validated entry")


if __name__ == "__main__":
    main()
