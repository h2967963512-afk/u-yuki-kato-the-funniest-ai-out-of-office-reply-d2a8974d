"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one out-of-office auto-reply in an AI agent's voice:
# a much cheaper model now handles the inbox and has approved everything.
# One sentence, 117 characters — inside the 160-character gate.
# Revision note: "approved everything" is the twist, so it closes the line.
import os

TEXT = (
    "I am on vacation and my inbox is now handled by a much cheaper "
    "model, which has already approved everything you sent."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
