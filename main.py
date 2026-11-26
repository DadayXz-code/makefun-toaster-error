"""makefun-toaster-error: writes one funny toaster error message.

Stdlib only. Deterministic: the same single line on every run, written
to /output/entry.txt as required by the bounty contract.
"""

import os
import shutil

LINE = "ERROR E12: The bread has unionized. It refuses to brown until its demands are met."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 120:
        raise ValueError("entry line must be 1 to 120 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear the output directory's contents, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
