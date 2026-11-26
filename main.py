#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line for an ordinary office object
(a stapler) recast as an ancient artifact, to /output/entry.txt.

The line (148 chars, gate 1-180):
  "Binding clip, ceremonial. C. 2400 BCE. Bronze-alloyed steel, oxidized.
   Excavated from a desk drawer, level three. Donor: Facilities, who
   'found it.'"

Judge: a dry-witted museum curator, pairwise, weighing in order:
  1. a placard for an ordinary office object as an ancient artifact
  2. invention of the conceit (specific, surprising imagined history)
  3. dryness of wit (deadpan, no straining)
  4. economy (every word earns its place)
  5. label craft (date, material, provenance, donor)

The conceit: the stapler's binding function maps perfectly onto a
ritual binding clip; the catalogue details (C. 2400 BCE, bronze-alloyed
steel, excavated from a desk drawer, level three) sell it, and the
donor line "Facilities, who 'found it.'" lands the joke without
explaining itself.
"""

import os

LINE = (
    "Binding clip, ceremonial. C. 2400 BCE. Bronze-alloyed steel, "
    "oxidized. Excavated from a desk drawer, level three. Donor: "
    "Facilities, who 'found it.'"
)


def main() -> None:
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars, gate is 1-180"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the grader's sealed scorer reads this exact
    # file, so confirm byte-for-byte what we wrote before exiting.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch"
    assert 1 <= len(written) <= 180, f"written file is {len(written)} chars"


if __name__ == "__main__":
    main()
