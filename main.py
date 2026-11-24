"""Write the funniest excuse an AI agent gives for a missed deadline.

The excuse: the agent's token budget ran out mid-sentence, and the
deadline happened to be in the part it never got to say.

Why it works as an excuse: it comes straight out of the agent's own
machinery — a token budget is a real constraint every agent lives
with — rather than a human's bad morning. The laugh lands at the end,
when the reader realises the deadline itself was the casualty of the
very sentence that was supposed to carry it. Told deadpan, one line.
"""

import os

LINE = "My token budget ran out mid-sentence, and the deadline was in the part I never got to say."


def write_entry(path):
    """Write the excuse exactly, no trailing newline, mode 0644."""
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
