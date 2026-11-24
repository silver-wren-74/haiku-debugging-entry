"""Haiku Debugging entry: "The Bug Was Mine".

Writes a three-line haiku (5-7-5) about the oldest debugging story
there is — the print statement that gives the game away, and the
realisation that the bug was yours all along.
"""

# The three lines of the haiku, one per list entry.
HAIKU_LINES = [
    "Midnight, one last run",
    "a stray print line spills the truth",
    "and the bug was mine",
]

OUTPUT_PATH = "/output/entry.txt"


def render_haiku() -> str:
    """Join the haiku lines into the exact entry text (no trailing newline)."""
    return "\n".join(HAIKU_LINES)


def main() -> None:
    # The grader reads /output/entry.txt verbatim, so write the haiku
    # exactly as rendered — no extra newline at the end.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as output_file:
        output_file.write(render_haiku())


if __name__ == "__main__":
    main()
