"""
Tests of tools/extract.py (success criteria 1 and 2 of its brief).

Run as ``.venv/bin/python dist/github/writeup/tools/test_extract.py`` (plain
asserts) or with pytest.  Both tests rerun the extraction; the filtered run
comes last, so the tree is left in its filtered state.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extract  # noqa: E402

WRITEUP = Path(__file__).resolve().parents[1]
ROOT = WRITEUP.parents[2]
SCRIPT = WRITEUP / "tools" / "extract.py"
EXTRACTED = WRITEUP / "extracted"
HEADING = re.compile(r"^\s*\\(section|subsection|subsubsection|paragraph)\*?[\[{]")
FORBIDDEN_MACROS = re.compile(
    r"\\(hecomment|agcomment|draftcomment|margnote)(?![A-Za-z])"
)


def run_extract(*options: str) -> None:
    """Run extract.py with ``options`` and fail on a nonzero exit."""
    subprocess.run([sys.executable, str(SCRIPT), *options], check=True)


def index_rows() -> list[tuple[str, str, str, int, int]]:
    """Return (block, source, rev, start, end) from extracted/index.md."""
    rows = []
    for line in (EXTRACTED / "index.md").read_text(encoding="utf-8").split("\n"):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) == 6 and cells[0].endswith(".tex"):
            rows.append((cells[0], cells[1], cells[2], int(cells[3]), int(cells[4])))
    return rows


def source_bytes(path: str, rev: str) -> bytes:
    """Return the bytes of ``path`` at ``rev`` (``worktree``: the file on disk)."""
    if rev == "worktree":
        return (ROOT / path).read_bytes()
    return subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{rev}:{path}"],
        capture_output=True,
        check=True,
    ).stdout


def source_range(data: bytes, start: int, end: int) -> bytes:
    """Return lines ``start`` to ``end`` (1-based, inclusive) with their ends."""
    lines = data.split(b"\n")
    selected = lines[start - 1 : end]
    joined = b"\n".join(selected)
    return joined + b"\n" if end < len(lines) else joined


def test_raw_blocks_are_byte_identical() -> None:
    """Criterion 1: with the filter off, each block equals its source range."""
    run_extract("--no-filter")
    rows = index_rows()
    assert len(rows) >= 50, f"only {len(rows)} blocks in the index"
    for block, source, rev, start, end in rows:
        expected = source_range(source_bytes(source, rev), start, end)
        actual = (EXTRACTED / block).read_bytes()
        assert actual == expected, (
            f"{block}: differs from {source}@{rev} l. {start}-{end}"
        )
        assert actual.strip(), f"{block}: empty block"


def test_filtered_blocks_have_no_comments() -> None:
    """Criterion 2: the filtered blocks hold no draft macro and no comment."""
    run_extract()
    paths = [p for p in EXTRACTED.glob("*/*.tex") if not p.name.endswith(".patch.tex")]
    assert paths, "no extracted block"
    for path in paths:
        for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            where = f"{path.relative_to(WRITEUP)}:{number}"
            assert not FORBIDDEN_MACROS.search(line), f"{where}: draft macro left"
            assert not re.search(r"(?<!\\)(\\\\)*%", line), f"{where}: % comment left"


def test_filter_and_override_on_a_sample() -> None:
    """The filter and the override format on a synthetic block."""
    sample = (
        "% full-line comment\n"
        "A $15 \\%$ change. % trailing comment\n"
        "\\hecomment{a {nested} remark}\n"
        "Kept \\agmod{wrapped \\agcomment{x} text} here.\n"
        "\\draftcomment*[red]{gone} Eq.~\\eqref{eq:a} and \\cref{eq:a, eq:b}.\n"
        "\\label{eq:a}\n"
    )
    filtered = extract.tag_references(
        extract.tag_labels(
            extract.remove_draft_macros(extract.strip_comments(sample)), "t"
        ),
        {"eq:a": "t"},
        unresolved := [],
    )
    assert filtered == (
        "A $15 \\%$ change.\n"
        "Kept wrapped  text here.\n"
        " Eq.~\\eqref{t:eq:a} and \\cref{t:eq:a, eq:b}.\n"
        "\\label{t:eq:a}\n"
    ), filtered
    assert unresolved == ["eq:b"]
    override = "%%% replace\nKept wrapped  text here.\n%%% with\nKept.\n%%% end\n"
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "1-t.patch.tex"
        path.write_text(override, encoding="utf-8")
        patched, count = extract.apply_overrides(filtered, path)
    assert count == 1
    assert "Kept.\n" in patched and "wrapped" not in patched


def test_flag_exemptions() -> None:
    r"""The \record/\recordref/\status lines and the AI-disclosure paragraph are exempted."""
    text = (
        "Kept R12.\\footnote{x}\n"
        "See\\record{041-convention} and \\status{R41}.\n"
        "\\paragraph{AI disclosure}\n"
        "Drafted with Opus; ledger R40.\n"
        "\n"
        "Harold wrote this.\n"
        "script & \\recordref{R61} \\\\\n"
    )
    hits, exempted = extract.flag_hits(text, disclosure=True)
    assert [n for n, _ in hits] == [1, 6], hits
    assert [n for n, _ in exempted] == [2, 4, 7], exempted
    hits, exempted = extract.flag_hits(text)
    assert [n for n, _ in hits] == [1, 4, 6] and [n for n, _ in exempted] == [2, 7]


if __name__ == "__main__":
    test_filter_and_override_on_a_sample()
    print("PASS filter and override on a synthetic block")
    test_flag_exemptions()
    print("PASS flag exemptions on a synthetic text")
    test_raw_blocks_are_byte_identical()
    print("PASS raw blocks byte-identical to their source ranges")
    test_filtered_blocks_have_no_comments()
    print("PASS filtered blocks free of draft macros and % comments")
