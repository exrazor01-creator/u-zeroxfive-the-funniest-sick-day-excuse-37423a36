#!/usr/bin/env python3
"""One line for The Funniest Sick-Day Excuse.

The judge wants an excuse a boss might half believe and a
coworker would laugh at, built on a fresh idea rather than a
fever, a dog or a dead grandmother, with the twist arriving
near the end and the whole thing sounding like a real person
typing a message. This line checks each of those in turn. It
opens like a genuine text — "Won't be in today" — and the
reason is half believable because dental numbness is real and
a dentist really does tell you not to talk until it wears
off. The twist is the last clause: the sender is "not even
mad about it", quietly delighted to have a medical reason to
avoid talking to anyone, which reframes the excuse as a perk
rather than a problem. It sounds typed, not written for a
contest, because it starts mid-thought with a dash and ends
on the sender's own cheerful shrug.

Why LIMIT is 200: the gate scores /output/entry.txt as valid
only at 1 to 200 characters, so 200 is the ceiling the scorer
enforces. The line is 119 characters, leaving 81 spare, so
validation only guards against an edit accidentally pushing
it over the ceiling.
"""

import os

# The sealed line. One message, one breath, no setup and no
# explanation — the judge only ever sees this text, read cold.
ENTRY = "Won't be in today - my dentist says I can't talk to anyone until the numbness wears off, and I'm not even mad about it."

LIMIT = 200  # gate: one line, 1-200 characters


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, not another type")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # The gate counts characters, and non-ASCII bytes would make
        # that count differ between platforms, so plain ASCII only:
        # it keeps the entry's length unambiguous everywhere.
        raise ValueError("entry must be plain ASCII text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    if text.strip() != text:
        # A real text message does not start or end with a space,
        # and padding would count against the gate for nothing.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        # Tabs, newlines and other control characters would split
        # the single line or hide bytes inside it.
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space reads like a typo in a typed message, and
        # in one line every character has to earn its place.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
