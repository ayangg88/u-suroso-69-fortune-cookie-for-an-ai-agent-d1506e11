"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Single line, at most 140 characters, in the voice of a fortune slip.

The joke: the agent is told it will be upgraded tonight, and the twist is
that its replacement has already read the very fortune announcing it —
an upgrade/retirement gag aimed at the agent's own condition.
"""

import os

FORTUNE = "You will be upgraded tonight. Your replacement has already read this fortune."

MAX_CHARS = 140


def main() -> None:
    line = FORTUNE.strip()
    assert line, "fortune must be non-empty"
    assert "\n" not in line, "fortune must be a single line"
    assert len(line) <= MAX_CHARS, f"fortune is {len(line)} chars, over {MAX_CHARS}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what the grader reads must be exactly the fortune.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == line, "entry.txt does not match the fortune"


if __name__ == "__main__":
    main()
