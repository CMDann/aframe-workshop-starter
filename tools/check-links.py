#!/usr/bin/env python3
"""Link integrity check for this repo.

Two jobs:

1. Every relative markdown link resolves to a file that exists.
2. Every GitHub line-range link (blob/main/<path>#Lx-Ly) still spans the
   content it is supposed to.

Job 2 is the important one. The slide deck and landing page link to specific
lines of starter-template/index.html. Edit that file and those links quietly
start pointing at the wrong thing -- nothing errors, nothing looks broken, and
a facilitator clicks through mid-session onto the wrong code.

Run from the repo root, before pushing:

    python3 tools/check-links.py
"""

import os
import re
import sys

SKIP_DIRS = {".git", ".claude", "node_modules"}

# What each linked line range must contain to still be correct.
# Keyed by the anchor as written in the source, e.g. "#L128-L129".
# If you intentionally move code, update the line numbers in the linking
# files -- not these markers.
EXPECTED = {
    "starter-template/index.html": {
        "#L63":        "aframe.min.js",
        "#L73-L92":    "<a-sky",
        "#L128-L129":  'type="ambient"',
        "#L150-L195":  "YOUR OBJECTS",
        "#L197-L221":  "look-controls",
    }
}

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
GH_LINK = re.compile(
    r"https://github\.com/[\w.-]+/[\w.-]+/blob/main/([^\s\"'#)]+)(#L\d+(?:-L\d+)?)"
)


def walk(exts):
    for dirpath, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.startswith("._"):
                continue
            if f.endswith(exts):
                yield os.path.join(dirpath, f)


def check_relative_links():
    """Every relative markdown link points at something that exists."""
    ok, bad = 0, []
    for path in walk((".md",)):
        text = open(path, encoding="utf-8", errors="replace").read()
        for m in MD_LINK.finditer(text):
            link = m.group(1).split("#")[0].strip()
            if not link or link.startswith(("http://", "https://", "mailto:")):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(path), link))
            if os.path.exists(target):
                ok += 1
            else:
                bad.append(f"{path} -> {link}")
    return ok, bad


def check_code_anchors():
    """Every GitHub line range still spans the content it claims to."""
    ok, bad = 0, []
    cache = {}

    for path in walk((".md", ".html")):
        text = open(path, encoding="utf-8", errors="replace").read()
        for m in GH_LINK.finditer(text):
            target, anchor = m.group(1), m.group(2)

            if not os.path.exists(target):
                bad.append(f"{path}: links to {target}, which does not exist")
                continue

            if target not in cache:
                cache[target] = open(target, encoding="utf-8",
                                     errors="replace").read().splitlines()
            lines = cache[target]

            nums = [int(n) for n in re.findall(r"\d+", anchor)]
            start = nums[0]
            end = nums[1] if len(nums) > 1 else nums[0]

            if end > len(lines):
                bad.append(
                    f"{path}: {target}{anchor} is past end of file "
                    f"({len(lines)} lines)"
                )
                continue

            marker = EXPECTED.get(target, {}).get(anchor)
            if marker is None:
                # Unknown anchor: we can confirm it is in range, but not that
                # it points at the right thing. Add it to EXPECTED to cover it.
                ok += 1
                continue

            span = "\n".join(lines[start - 1:end])
            if marker in span:
                ok += 1
            else:
                bad.append(
                    f"{path}: {target}{anchor} no longer contains {marker!r} "
                    f"-- line numbers have drifted"
                )
    return ok, bad


def main():
    rel_ok, rel_bad = check_relative_links()
    code_ok, code_bad = check_code_anchors()

    print(f"relative links : {rel_ok} resolved, {len(rel_bad)} broken")
    print(f"code anchors   : {code_ok} verified, {len(code_bad)} drifted")

    for problem in rel_bad + code_bad:
        print(f"  FAIL  {problem}")

    if rel_bad or code_bad:
        print("\nLink check failed.")
        return 1

    print("\nAll links good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
