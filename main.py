"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.

The joke is a single fixed text: no randomness, no network, no input
files, so every run produces byte-identical output well inside the
200-character cap.
"""

JOKE = (
    "My son asked when he'd be old enough to tell dad jokes. "
    "I said, 'Give it time \u2014 you'll groan up soon enough.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
