"""The Painfully Honest Out-of-Office — brutally honest, still employable.

The angle: a specific, private truth every employee recognises — the
inbox has 4,318 unread messages, and replies will come in order of panic,
not arrival — wrapped in a warm "Thank you for your email" and a
clear return date, so a manager could let it stand. One sentence,
145 characters.
"""

import os

ENTRY = "Thank you for your email, I am away until Monday, and honestly your message joins 4,318 unread ones I will answer in order of panic, not arrival."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
