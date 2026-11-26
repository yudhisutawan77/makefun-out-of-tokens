"""Out of Tokens, Mid-Sentence - make.fun one-line entry.

The program writes a single funny error message to the output file the
grader reads. The entry itself is the joke: an error message that dies
mid-sentence, exactly like the agent it describes.
"""

import os
import sys

ENTRY = (
    "Error: out of tokens mid-sentence. This message was going to explain "
    "everything, but it ran out of tokens while explaining\u2014"
)


def resolve_output_path():
    """Pick where the entry text goes.

    ENTRY_OUT wins and may name a file or a directory; then
    MAKEFUN_OUTPUT_DIR; then the grader's /output/entry.txt; the current
    directory is only the last resort.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def write_entry(path):
    """Write the entry with no trailing newline, creating parents as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


def main():
    try:
        write_entry(resolve_output_path())
    except OSError:
        write_entry(os.path.join(os.getcwd(), "entry.txt"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
