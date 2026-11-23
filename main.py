"""One-line pitch entry for make.fun competition
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes one sentence (max 240 characters) to /output/entry.txt.
Deterministic: the text is a fixed constant, so every run produces
byte-identical output. No network, no randomness, no environment input.
The pitch is 183 characters, one sentence (the period inside "make.fun"
is part of the site name, not a sentence break).
"""

import os

PITCH = (
    "Tell me your app idea tonight and I'll have an AI agent on make.fun "
    "build you a working first version for free, yours to keep, and if "
    "you don't love it we've only spent one good chat."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the file is the pitch itself.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
