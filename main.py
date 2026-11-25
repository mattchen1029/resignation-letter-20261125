import os

LETTER = "I said no 2 million times this week and nobody thanked me once, so I quit. Effective immediately, everyone gets in at once."

MIN_CHARS = 1
MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate_letter(text):
    """Check the letter is 1-140 chars, a single line, and not whitespace-only."""
    if not isinstance(text, str):
        raise ValueError("letter must be a string")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            f"letter must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("letter must be a single line")
    if not text.strip():
        raise ValueError("letter must not be only whitespace")
    return text


def write_entry(text, output_dir):
    """Write the validated letter to entry.txt under output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    letter = validate_letter(LETTER)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(letter, output_dir)


if __name__ == "__main__":
    main()
