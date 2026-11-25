# Judge Laugh entry: one deterministic one-liner, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
import os

JOKE = "My boss declared Wednesdays meeting-free, then booked a meeting to announce it."

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
    handle.write(JOKE)
