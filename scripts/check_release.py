"""Bind an actual editorial review to the public edition and detect stale review records."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BINDING = Path("content/reviews/release.json")
VERDICTS = ("Accuracy", "Confidentiality", "Editorial")


def digest(root):
    h = hashlib.sha256()
    paths = sorted(p for directory in ("content", "site", "release")
                   for p in (root / directory).rglob("*")
                   if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
                   and p.relative_to(root) != BINDING)
    for path in paths:
        h.update(path.relative_to(root).as_posix().encode() + b"\0")
        h.update(hashlib.sha256(path.read_bytes()).digest())
    return h.hexdigest()


def expected(root):
    version = (root / "content/VERSION").read_text().strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("content/VERSION must be a semantic version")
    log = (root / "content/CHANGELOG.md").read_text()
    if not re.search(rf"^## {re.escape(version)}\s*$", log, re.M):
        raise ValueError("No changelog entry for this edition")
    review = Path(f"content/reviews/{version}.md")
    record = (root / review).read_text()
    for role in VERDICTS:
        if not re.search(rf"^{role}: ACCEPT\s*$", record, re.M):
            raise ValueError(f"{review} lacks a recorded {role} acceptance")
    return {"edition": version, "review": review.as_posix(), "source_sha256": digest(root)}


def check_previous(root, base, current):
    if not re.fullmatch(r"[0-9a-fA-F]{40,64}", base):
        raise ValueError("The base comparison requires a full Git object ID")
    result = subprocess.run(["git", "ls-tree", base, "--", BINDING.as_posix()],
                            cwd=root, text=True, capture_output=True, check=True)
    if not result.stdout.strip():
        return
    data = subprocess.check_output(["git", "show", f"{base}:{BINDING.as_posix()}"],
                                   cwd=root, text=True)
    previous = json.loads(data)
    if previous["source_sha256"] != current["source_sha256"]:
        old = tuple(map(int, previous["edition"].split(".")))
        new = tuple(map(int, current["edition"].split(".")))
        if new <= old:
            raise ValueError("A changed edition needs a higher content/VERSION and changelog entry")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "bind"))
    parser.add_argument("--base", help="Full base commit SHA for a pull request")
    args = parser.parse_args()
    try:
        result = expected(ROOT)
        file = ROOT / BINDING
        if args.command == "bind":
            file.write_text(json.dumps(result, indent=2) + "\n")
        elif json.loads(file.read_text()) != result:
            raise ValueError("Content, site or review changed after acceptance; review the diff and bind again")
        if args.base:
            check_previous(ROOT, args.base, result)
        print(f"Review {args.command}: edition {result['edition']}, {result['source_sha256']}")
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + "\n")


if __name__ == "__main__":
    main()
