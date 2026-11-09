"""
Extract the reused LaTeX blocks of the complete write-up.

Reads ``tools/sources.yaml`` and writes one file per block,
``extracted/<chapter>/<order>-<tag>.tex``, taken verbatim from its source (a
file at a git revision, or in the working tree).  By default the block is
filtered: comments and draft-comment macros are removed, labels and
same-document references are prefixed with the source tag, and an override
file ``extracted/<chapter>/<order>-<tag>.patch.tex`` is applied when present.
The run also writes ``extracted/index.md``, ``extracted/flags.md`` and
``extracted/unresolved-refs.md``.  See ``tools/README.md``.

Specification: ``agent/task-plans/dist-writeup-2026-11-07.md``, Part 3.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

WRITEUP = Path(__file__).resolve().parents[1]
ROOT = WRITEUP.parents[2]
SOURCES_FILE = WRITEUP / "tools" / "sources.yaml"
EXTRACTED = WRITEUP / "extracted"
SECTIONS = WRITEUP / "sections"
FIGURES = WRITEUP / "figures"
WORKTREE = "worktree"
PAPER_TAGS = ("p", "pc")
FALLBACK_TAG = {"pc": "p"}

FLAG_PATTERN = re.compile(
    r"Harold|\[HE|AG:|\bR[0-9]{1,3}\b|\bPH[0-9]+\b|record [0-9]{3}"
    r"|derivation [0-9]{3}|results\.md"
    r"|\b(?:Fable|Opus|Sonnet|GLM|Qwen|OpenCode|computators?|critics?|orchestrators?)\b"
    r"|agent/|knowledge/|Task [0-9]"
)
# Lines the design allows to carry ledger IDs and record stems: the macros
# \record{...}, \recordref{...} and \status{...} of cubic-sft-complete-notebook.tex, and
# the AI-disclosure paragraph of sections/00-preamble.tex (marked by a
# "% ai-disclosure" line or headed \paragraph{AI disclosure}).
EXEMPT_MACRO = re.compile(r"\\(?:record|recordref|status)\{")
AI_DISCLOSURE = re.compile(
    r"^\s*(?:%\s*ai-disclosure\b|\\paragraph\*?\{AI disclosure\})", re.IGNORECASE
)
PREAMBLE = "00-preamble.tex"
DEMOTED = {
    "section": "subsection",
    "subsection": "subsubsection",
    "subsubsection": "paragraph",
    "paragraph": "subparagraph",
}
DEMOTABLE = re.compile(r"\\(section|subsection|subsubsection|paragraph)(?![A-Za-z@])")
HEADING = re.compile(
    r"^\s*\\(part|chapter|section|subsection|subsubsection|paragraph)\*?[\[{]"
)
LEVELS = {
    "part": -1,
    "chapter": 0,
    "section": 1,
    "subsection": 2,
    "subsubsection": 3,
    "paragraph": 4,
}
STOP = re.compile(r"^\s*\\(appendix\b|printbibliography|end\{document\})")
GOBBLED = ("hecomment", "agcomment", "draftcomment", "draftnote", "margnote")
DRAFT_MACRO = re.compile(r"\\(" + "|".join(GOBBLED) + r"|agmod)(?![A-Za-z@])")
LABEL = re.compile(r"\\label\{([^{}]*)\}")
REF = re.compile(r"\\(cref|Cref|eqref|ref|labelcref)(\*?)\{([^{}]*)\}")
CITE = re.compile(r"\\[A-Za-z]*cite[A-Za-z]*\*?")
SECTION_INPUT = re.compile(
    r"^[ \t]*\\(?:input|include)\{sections/[^{}]*\}[ \t]*\n?", re.MULTILINE
)
INCLUDEGRAPHICS = re.compile(r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^{}]*)\}")
FIGURE_EXTENSIONS = (".pdf", ".png", ".jpg", ".jpeg", ".eps")
OVERRIDE_REPLACE = "%%% replace"
OVERRIDE_WITH = "%%% with"
OVERRIDE_END = "%%% end"


# ---------------------------------------------------------------- YAML subset


def strip_yaml_comment(line: str) -> str:
    """Return ``line`` without its ``#`` comment (outside single quotes)."""
    in_quote = False
    for position, char in enumerate(line):
        if char == "'":
            in_quote = not in_quote
        elif (
            char == "#"
            and not in_quote
            and (position == 0 or line[position - 1] == " ")
        ):
            return line[:position]
    return line


def parse_scalar(value: str, line_number: int) -> str:
    """Parse a plain or single-quoted YAML scalar into a string."""
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise ValueError(f"sources.yaml:{line_number}: unterminated quote")
        return value[1:-1].replace("''", "'")
    if value[:1] in set('"{}[]&*!|>%@`'):
        raise ValueError(
            f"sources.yaml:{line_number}: unsupported scalar {value!r}; "
            "use a plain or single-quoted value"
        )
    return value


def parse_yaml_subset(text: str) -> dict[str, list[dict[str, str]]]:
    """
    Parse top-level keys holding lists of flat mappings of scalars.

    Args:
        text: YAML text restricted to the subset described in sources.yaml.

    Returns:
        dict[str, list[dict[str, str]]]: one list of mappings per top-level key.

    Raises:
        ValueError: on any construct outside the subset.

    """
    data: dict[str, list[dict[str, str]]] = {}
    items: list[dict[str, str]] | None = None
    item: dict[str, str] | None = None
    for number, raw in enumerate(text.split("\n"), 1):
        line = strip_yaml_comment(raw).rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        body = line.strip()
        if indent == 0:
            if not body.endswith(":") or " " in body:
                raise ValueError(f"sources.yaml:{number}: expected 'key:'")
            items = []
            item = None
            data[body[:-1]] = items
            continue
        if items is None:
            raise ValueError(f"sources.yaml:{number}: list item before any key")
        if body.startswith("- "):
            item = {}
            items.append(item)
            body = body[2:].strip()
        elif item is None:
            raise ValueError(
                f"sources.yaml:{number}: mapping entry outside a list item"
            )
        key, separator, value = body.partition(":")
        if not separator or not key or " " in key:
            raise ValueError(f"sources.yaml:{number}: expected 'key: value'")
        if key in item:
            raise ValueError(f"sources.yaml:{number}: duplicate key {key!r}")
        item[key] = parse_scalar(value.strip(), number)
    return data


# ------------------------------------------------------------------- sources


@dataclass(frozen=True)
class Block:
    """One reused block: where it comes from and where it goes."""

    chapter: str
    order: int
    source: str
    rev: str
    tag: str
    spec: dict[str, str]

    @property
    def name(self) -> str:
        """Path of the block below ``extracted/``, without the extension."""
        return f"{self.chapter}/{self.order}-{self.tag}"


@dataclass
class Plan:
    """The parsed sources.yaml."""

    documents: list[dict[str, str]]
    chapters: list[dict[str, str]]
    blocks: list[Block]


def load_plan(path: Path = SOURCES_FILE) -> Plan:
    """Read and validate sources.yaml."""
    data = parse_yaml_subset(path.read_text(encoding="utf-8"))
    chapter_numbers = [chapter["number"] for chapter in data["chapters"]]
    tags = {document["tag"] for document in data["documents"]}
    blocks = []
    for entry in data["blocks"]:
        block = Block(
            chapter=entry["chapter"],
            order=int(entry["order"]),
            source=entry["source"],
            rev=entry["rev"],
            tag=entry["tag"],
            spec=entry,
        )
        if block.chapter not in chapter_numbers:
            raise ValueError(f"block {block.name}: unknown chapter")
        if block.tag not in tags:
            raise ValueError(f"block {block.name}: unknown tag")
        blocks.append(block)
    names = [block.name for block in blocks]
    if len(set(names)) != len(names):
        raise ValueError("two blocks share a chapter and an order")
    return Plan(data["documents"], data["chapters"], blocks)


def read_source(path: str, rev: str) -> str:
    """Return the text of ``path`` (from the project root) at ``rev``."""
    if rev == WORKTREE:
        return (ROOT / path).read_bytes().decode("utf-8")
    result = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{rev}:{path}"],
        capture_output=True,
        check=True,
    )
    return result.stdout.decode("utf-8")


def list_tex_files(path: str, rev: str) -> list[str]:
    """List the .tex files at ``path`` (a file or a directory) at ``rev``."""
    if rev == WORKTREE:
        target = ROOT / path
        if target.is_file():
            return [path]
        return sorted(str(p.relative_to(ROOT)) for p in target.rglob("*.tex"))
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", rev, "--", path],
        capture_output=True,
        check=True,
        text=True,
    )
    return [name for name in result.stdout.split("\n") if name.endswith(".tex")]


def split_lines(text: str) -> list[str]:
    r"""Split on ``\n`` only, keeping the line ends (unlike ``splitlines``)."""
    lines = [line + "\n" for line in text.split("\n")]
    lines[-1] = lines[-1][:-1]
    if not lines[-1]:
        lines.pop()
    return lines


def heading_level(line: str) -> int | None:
    """Return the sectioning level of a heading line, or None."""
    match = HEADING.match(line)
    return LEVELS[match.group(1)] if match else None


def resolve_range(block: Block, lines: list[str]) -> tuple[int, int]:
    """
    Return the 1-based inclusive line range of ``block`` in ``lines``.

    Raises:
        ValueError: when the range is missing, ambiguous or out of bounds.

    """
    spec = block.spec
    if spec.get("whole") == "yes":
        return 1, len(lines)
    if "lines" in spec:
        first, _, last = spec["lines"].partition("-")
        start, end = int(first), int(last)
        if not 1 <= start <= end <= len(lines):
            raise ValueError(f"block {block.name}: lines {start}-{end} out of range")
        return start, end
    if "heading" not in spec:
        raise ValueError(f"block {block.name}: no range (whole, lines or heading)")
    wanted = spec["heading"]
    level = LEVELS[spec["level"]] if "level" in spec else None
    matches = [
        index
        for index, line in enumerate(lines)
        if heading_level(line) is not None
        and (level is None or heading_level(line) == level)
        and wanted in line
    ]
    if len(matches) != 1:
        raise ValueError(
            f"block {block.name}: heading {wanted!r} matches {len(matches)} lines"
        )
    start = matches[0]
    start_level = heading_level(lines[start])
    end = len(lines)
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if "to" in spec:
            if spec["to"] in line:
                end = index
                break
            continue
        current = heading_level(line)
        if (current is not None and current <= start_level) or STOP.match(line):
            end = index
            break
    else:
        if "to" in spec:
            raise ValueError(f"block {block.name}: end marker {spec['to']!r} not found")
    return start + 1, end


# -------------------------------------------------------------------- filter


def comment_start(line: str) -> int | None:
    """Return the index of the first unescaped ``%`` of ``line``, or None."""
    position = line.find("%")
    while position >= 0:
        backslashes = len(line[:position]) - len(line[:position].rstrip("\\"))
        if backslashes % 2 == 0:
            return position
        position = line.find("%", position + 1)
    return None


def strip_comments(text: str) -> str:
    r"""Drop full-line ``%`` comments and trailing comments (not ``\%``)."""
    kept = []
    for line in split_lines(text):
        newline = "\n" if line.endswith("\n") else ""
        body = line[: len(line) - len(newline)]
        position = comment_start(body)
        if position is None:
            kept.append(line)
        elif body[:position].strip():
            kept.append(body[:position].rstrip() + newline)
    return "".join(kept)


def matching_close(text: str, start: int, opening: str, closing: str) -> int:
    """
    Return the index after the group opened at ``text[start]``.

    Raises:
        ValueError: when the group is not closed.

    """
    depth = 0
    position = start
    while position < len(text):
        char = text[position]
        if char == "\\":
            position += 2
            continue
        if char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                return position + 1
        position += 1
    raise ValueError(f"unbalanced {opening}{closing} group at offset {start}")


def skip_spaces(text: str, position: int) -> int:
    """Return the first index at or after ``position`` that is not a space."""
    while position < len(text) and text[position] in " \t\n":
        position += 1
    return position


def remove_draft_macros(text: str) -> str:
    r"""
    Remove the draft-comment macros and unwrap ``\agmod{...}``.

    ``\hecomment``, ``\agcomment``, ``\draftcomment[*][opt]``,
    ``\draftnote[opt]`` and ``\margnote`` are removed with their arguments;
    ``\agmod{text}`` becomes ``text`` (the paper defines it to print its
    argument).  A line left blank by a removal is dropped.  A macro name not
    followed by a brace group (as in a definition) is left alone.
    """
    position = 0
    while True:
        match = DRAFT_MACRO.search(text, position)
        if match is None:
            return text
        cursor = match.end()
        if text.startswith("*", cursor):
            cursor += 1
        cursor = skip_spaces(text, cursor)
        if text.startswith("[", cursor):
            cursor = skip_spaces(text, matching_close(text, cursor, "[", "]"))
        if not text.startswith("{", cursor):
            position = match.end()
            continue
        end = matching_close(text, cursor, "{", "}")
        if match.group(1) == "agmod":
            text = text[: match.start()] + text[cursor + 1 : end - 1] + text[end:]
            position = match.start()
            continue
        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", end)
        line_end = len(text) if line_end < 0 else line_end
        if (
            not text[line_start : match.start()].strip()
            and not text[end:line_end].strip()
        ):
            text = text[:line_start] + text[line_end + 1 :]
            position = line_start
        else:
            text = text[: match.start()] + text[end:]
            position = match.start()


def demote_headings(text: str) -> str:
    r"""
    Demote every sectioning command by one level, in one pass.

    ``\section`` -> ``\subsection`` -> ``\subsubsection`` -> ``\paragraph``
    -> ``\subparagraph``; starred forms keep their star.  The chapter stubs
    hold the only ``\section`` of a chapter.
    """
    return DEMOTABLE.sub(lambda match: f"\\{DEMOTED[match.group(1)]}", text)


def tag_labels(text: str, tag: str) -> str:
    r"""Prefix every ``\label{x}`` with ``<tag>:``."""
    return LABEL.sub(lambda match: f"\\label{{{tag}:{match.group(1)}}}", text)


def tag_references(
    text: str,
    resolve: dict[str, str],
    unresolved: list[str],
) -> str:
    """
    Prefix each reference key found in ``resolve`` with its tag.

    Args:
        text: block text.
        resolve: reference key -> tag of the document defining it.
        unresolved: receives the keys defined in no document searched.

    Returns:
        str: the text with the references tagged.

    """

    def replace(match: re.Match[str]) -> str:
        keys = []
        for raw in match.group(3).split(","):
            key = raw.strip()
            if key in resolve:
                keys.append(raw.replace(key, f"{resolve[key]}:{key}"))
            else:
                unresolved.append(key)
                keys.append(raw)
        return f"\\{match.group(1)}{match.group(2)}{{{','.join(keys)}}}"

    return REF.sub(replace, text)


def rename_citations(text: str, renames: dict[str, str]) -> str:
    """Rename the citation keys listed in ``renames`` in every cite command."""
    if not renames:
        return text
    pieces = []
    position = 0
    for match in CITE.finditer(text):
        if match.start() < position:
            continue
        cursor = match.end()
        pieces.append(text[position:cursor])
        while True:
            group_start = skip_spaces(text, cursor)
            if text.startswith("[", group_start):
                group_end = matching_close(text, group_start, "[", "]")
                pieces.append(text[cursor:group_end])
            elif text.startswith("{", group_start):
                group_end = matching_close(text, group_start, "{", "}")
                keys = text[group_start + 1 : group_end - 1].split(",")
                renamed = ",".join(
                    raw.replace(raw.strip(), renames.get(raw.strip(), raw.strip()))
                    for raw in keys
                )
                pieces.append(f"{text[cursor:group_start]}{{{renamed}}}")
            else:
                break
            cursor = group_end
        position = cursor
    pieces.append(text[position:])
    return "".join(pieces)


def parse_overrides(text: str, path: Path) -> list[tuple[str, str]]:
    """
    Parse an override file into ``(old, new)`` replacement pairs.

    Format: hunks ``%%% replace`` / old lines / ``%%% with`` / new lines /
    ``%%% end``; text outside hunks is ignored.

    Raises:
        ValueError: on a malformed hunk.

    """
    hunks = []
    state = None
    old: list[str] = []
    new: list[str] = []
    for number, line in enumerate(split_lines(text), 1):
        marker = line.rstrip("\n").rstrip()
        if marker == OVERRIDE_REPLACE and state is None:
            state, old, new = "old", [], []
        elif marker == OVERRIDE_WITH and state == "old":
            state = "new"
        elif marker == OVERRIDE_END and state == "new":
            hunks.append(("".join(old), "".join(new)))
            state = None
        elif marker in (OVERRIDE_REPLACE, OVERRIDE_WITH, OVERRIDE_END):
            raise ValueError(f"{path}:{number}: misplaced {marker!r}")
        elif state == "old":
            old.append(line)
        elif state == "new":
            new.append(line)
    if state is not None:
        raise ValueError(f"{path}: hunk not closed by {OVERRIDE_END!r}")
    return hunks


def apply_overrides(text: str, path: Path) -> tuple[str, int]:
    """
    Apply the override file at ``path`` if it exists.

    Returns:
        tuple[str, int]: the text and the number of hunks applied.

    Raises:
        ValueError: when an old text does not occur exactly once.

    """
    if not path.exists():
        return text, 0
    hunks = parse_overrides(path.read_text(encoding="utf-8"), path)
    for index, (old, new) in enumerate(hunks, 1):
        count = text.count(old)
        if count != 1 or not old:
            raise ValueError(f"{path}: hunk {index} matches {count} times (needs 1)")
        text = text.replace(old, new)
    return text, len(hunks)


# ----------------------------------------------------------------- documents


def document_labels(plan: Plan) -> dict[str, set[str]]:
    """Return the labels defined in each source document, comments excluded."""
    labels = {}
    for document in plan.documents:
        found: set[str] = set()
        for path in list_tex_files(document["path"], document["rev"]):
            text = strip_comments(read_source(path, document["rev"]))
            found.update(LABEL.findall(text))
        labels[document["tag"]] = found
    return labels


def reference_resolver(
    tag: str,
    labels: dict[str, set[str]],
    extracted_labels: dict[str, set[str]],
) -> dict[str, str]:
    """
    Map each key a block of ``tag`` may cite to the tag that defines it.

    Labels of the block's own document win; for a document with a fallback
    (``pc`` -> ``p``), a label its extracted blocks do not define resolves to
    the fallback document when that one defines it.
    """
    resolve = {key: tag for key in labels[tag]}
    fallback = FALLBACK_TAG.get(tag)
    if fallback:
        for key in labels[fallback]:
            if key not in extracted_labels[tag]:
                resolve[key] = fallback
    return resolve


def bib_entries(text: str) -> dict[str, str]:
    """Split a .bib file into ``key -> entry text``."""
    entries = {}
    for match in re.finditer(r"^@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", text, re.MULTILINE):
        if match.group(1).lower() in ("comment", "string", "preamble"):
            continue
        end = text.find("\n@", match.end())
        entries[match.group(2)] = text[match.start() : len(text) if end < 0 else end]
    return entries


def bib_field(entry: str, name: str) -> str | None:
    """Return the normalized value of field ``name`` of a bib entry."""
    match = re.search(
        rf"^\s*{name}\s*=\s*[{{\"]?([^}}\",\n]*)", entry, re.MULTILINE | re.IGNORECASE
    )
    return match.group(1).strip().lower() if match else None


def bib_duplicates() -> tuple[list[str], dict[str, str]]:
    """
    Compare the keys of references.bib also present in string_theory.bib.

    Returns:
        tuple[list[str], dict[str, str]]: keys with the same eprint or DOI
        (dropped from the copy), and renames ``key -> key-kn`` for the others.

    """
    paper = bib_entries((ROOT / "paper" / "string_theory.bib").read_text("utf-8"))
    notes = bib_entries((ROOT / "knowledge/data/references.bib").read_text("utf-8"))
    same, renames = [], {}
    for key in sorted(set(paper) & set(notes)):
        identical = any(
            bib_field(paper[key], name) is not None
            and bib_field(paper[key], name) == bib_field(notes[key], name)
            for name in ("eprint", "doi")
        )
        if identical:
            same.append(key)
        else:
            renames[key] = f"{key}-kn"
    return same, renames


# ---------------------------------------------------------------- extraction


@dataclass
class BlockResult:
    """What the extraction of one block produced."""

    block: Block
    start: int
    end: int
    headings: list[str]
    text: str
    raw_flags: int = 0
    overrides: int = 0
    unresolved: list[str] = field(default_factory=list)


def extract_raw(block: Block) -> tuple[str, int, int, list[str]]:
    """Return the raw block text, its line range and the headings it holds."""
    lines = split_lines(read_source(block.source, block.rev))
    start, end = resolve_range(block, lines)
    selected = lines[start - 1 : end]
    headings = [line.strip() for line in selected if heading_level(line) is not None]
    return "".join(selected), start, end, headings


def filter_block(
    text: str,
    block: Block,
    resolve: dict[str, str],
    renames: dict[str, str],
    demote: bool = True,
) -> tuple[str, list[str]]:
    """Apply the filter of Part 3 to a raw block."""
    unresolved: list[str] = []
    text = remove_draft_macros(strip_comments(text))
    # the source's own \input{sections/...} lines: those files are blocks of their own
    text = SECTION_INPUT.sub("", text)
    if demote:
        text = demote_headings(text)
    text = tag_references(tag_labels(text, block.tag), resolve, unresolved)
    if block.tag not in PAPER_TAGS:
        text = rename_citations(text, renames)
    return text, unresolved


def write_text(path: Path, text: str) -> None:
    """Write ``text`` as UTF-8 bytes, without newline translation."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))


def remove_stale_blocks(plan: Plan) -> None:
    """Delete generated block files no longer listed in sources.yaml."""
    wanted = {EXTRACTED / f"{block.name}.tex" for block in plan.blocks}
    for path in EXTRACTED.glob("*/*.tex"):
        if re.fullmatch(r"[0-9]+-[a-z]+\.tex", path.name) and path not in wanted:
            path.unlink()


def extract(plan: Plan, apply_filter: bool, demote: bool = True) -> list[BlockResult]:
    """Write every block of the plan below ``extracted/``."""
    remove_stale_blocks(plan)
    labels = document_labels(plan) if apply_filter else {}
    raw_blocks = [(block, *extract_raw(block)) for block in plan.blocks]
    extracted_labels: dict[str, set[str]] = {tag: set() for tag in labels}
    for block, text, *_ in raw_blocks:
        if apply_filter:
            extracted_labels[block.tag].update(LABEL.findall(strip_comments(text)))
    renames = bib_duplicates()[1] if apply_filter else {}
    results = []
    for block, text, start, end, headings in raw_blocks:
        result = BlockResult(block, start, end, headings, text)
        if apply_filter:
            result.raw_flags = sum(
                1 for line in split_lines(text) if FLAG_PATTERN.search(line)
            )
            resolve = reference_resolver(block.tag, labels, extracted_labels)
            filtered, result.unresolved = filter_block(
                text, block, resolve, renames, demote
            )
            override = EXTRACTED / f"{block.name}.patch.tex"
            result.text, result.overrides = apply_overrides(filtered, override)
        write_text(EXTRACTED / f"{block.name}.tex", result.text)
        results.append(result)
    return results


# ------------------------------------------------------------------- reports


def write_index(results: list[BlockResult], apply_filter: bool) -> None:
    """Write ``extracted/index.md``: block, source, revision, range, headings."""
    mode = "filtered" if apply_filter else "raw (--no-filter)"
    lines = [
        "# Extracted blocks",
        "",
        f"Generated by `tools/extract.py`, mode: {mode}. Do not edit.",
        "",
        "| block | source | rev | start | end | tag |",
        "|---|---|---|---|---|---|",
    ]
    for result in results:
        block = result.block
        lines.append(
            f"| {block.name}.tex | {block.source} | {block.rev} "
            f"| {result.start} | {result.end} | {block.tag} |"
        )
    lines += ["", "## Headings per block", ""]
    for result in results:
        lines.append(f"- `{result.block.name}.tex`")
        lines += [f"  - `{heading}`" for heading in result.headings]
    write_text(EXTRACTED / "index.md", "\n".join(lines) + "\n")


def disclosure_lines(text: str) -> set[int]:
    """
    Return the line numbers of the AI-disclosure paragraph of ``text``.

    The paragraph starts at a line matching ``AI_DISCLOSURE`` and ends before
    the first blank line that follows a text line, or before the next heading,
    whichever comes first.  Empty when no line is marked.

    """
    numbers: set[int] = set()
    inside = seen_text = False
    for number, line in enumerate(split_lines(text), 1):
        if AI_DISCLOSURE.search(line):
            inside, seen_text = True, False
            numbers.add(number)
            continue
        if inside and (HEADING.match(line) or (seen_text and not line.strip())):
            inside = False
        if inside:
            numbers.add(number)
            seen_text = seen_text or bool(line.strip())
    return numbers


def flag_hits(
    text: str, disclosure: bool = False
) -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    r"""
    Split the lines matching the flag regex into hits and exempted lines.

    Args:
        text: the file content.
        disclosure: also exempt the AI-disclosure paragraph (the preamble).

    Returns:
        tuple: ``(hits, exempted)``, each a list of ``(line number, line)``;
        a line holding ``\record{``, ``\recordref{`` or ``\status{`` is
        exempted.

    """
    allowed = disclosure_lines(text) if disclosure else set()
    hits, exempted = [], []
    for number, line in enumerate(split_lines(text), 1):
        if not FLAG_PATTERN.search(line):
            continue
        exempt = number in allowed or EXEMPT_MACRO.search(line)
        (exempted if exempt else hits).append((number, line.rstrip("\n")))
    return hits, exempted


def write_flags(results: list[BlockResult]) -> None:
    """Write ``extracted/flags.md``: per block, the lines matching the regex."""
    lines = [
        "# Flagged lines of the extracted blocks",
        "",
        "Lines of the filtered blocks (after overrides) matching the flag regex",
        "of the design, Part 3. Line numbers are those of the extracted file.",
        "`raw` counts the matching lines of the unfiltered source range.",
        "`exempted` counts the matching lines holding `\\record{`, `\\recordref{`",
        "or `\\status{`, which the design allows (not listed, not counted in",
        "`filtered`).",
        "",
        "| block | source | raw | filtered | exempted |",
        "|---|---|---|---|---|",
    ]
    scans = {result.block.name: flag_hits(result.text) for result in results}
    for result in results:
        name = result.block.name
        hits, exempted = scans[name]
        lines.append(
            f"| {name} | {result.block.source} | {result.raw_flags} "
            f"| {len(hits)} | {len(exempted)} |"
        )
    for result in results:
        name = result.block.name
        hits, exempted = scans[name]
        if not hits and not exempted:
            continue
        lines += ["", f"## {name}.tex", ""]
        lines.append(
            f"exempted: {len(exempted)} lines (`\\record`/`\\recordref`/`\\status`)"
        )
        if hits:
            lines += ["", "```text"]
            lines += [f"{number}: {line}" for number, line in hits]
            lines.append("```")
    write_text(EXTRACTED / "flags.md", "\n".join(lines) + "\n")


def write_unresolved(results: list[BlockResult]) -> None:
    """
    Write ``extracted/unresolved-refs.md``.

    Two lists: references to labels defined in no searched document (left
    unchanged), and tagged references whose label no extracted block defines
    (undefined in the build until a chapter writer supplies them).
    """
    defined = set()
    for result in results:
        defined.update(LABEL.findall(result.text))
    lines = [
        "# Unresolved references",
        "",
        "## Labels defined outside the source document (left unchanged)",
        "",
    ]
    for result in results:
        if result.unresolved:
            keys = ", ".join(f"`{key}`" for key in sorted(set(result.unresolved)))
            lines.append(f"- `{result.block.name}.tex`: {keys}")
    lines += ["", "## Tagged references with no extracted label", ""]
    for result in results:
        missing = sorted(
            {
                key.strip()
                for match in REF.finditer(result.text)
                for key in match.group(3).split(",")
                if ":" in key and key.strip() not in defined
            }
        )
        if missing:
            keys = ", ".join(f"`{key}`" for key in missing)
            lines.append(f"- `{result.block.name}.tex`: {keys}")
    write_text(EXTRACTED / "unresolved-refs.md", "\n".join(lines) + "\n")


# --------------------------------------------------------------- other modes


def check() -> int:
    r"""
    Scan ``sections/`` and ``extracted/`` for flagged lines.

    Lines holding ``\record{``, ``\recordref{`` or ``\status{``, and the AI-disclosure
    paragraph of ``sections/00-preamble.tex``, are exempted; every other
    matching line is printed as a hit.

    Returns:
        int: 0 when every matching line is exempted, else 1.

    """
    paths = sorted(SECTIONS.glob("*.tex")) + sorted(
        path
        for path in EXTRACTED.glob("*/*.tex")
        if not path.name.endswith(".patch.tex")
    )
    failing = exempt_count = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        is_preamble = path == SECTIONS / PREAMBLE
        if is_preamble and not disclosure_lines(text):
            print(f"note: no AI-disclosure marker in sections/{PREAMBLE}")
        hits, exempted = flag_hits(text, disclosure=is_preamble)
        for number, line in hits:
            print(f"HIT {path.relative_to(WRITEUP)}:{number}: {line}")
        failing += len(hits)
        exempt_count += len(exempted)
    print(
        f"check: {failing} hit(s); {exempt_count} exempted line(s) "
        "(\\record/\\recordref/\\status, AI disclosure)"
    )
    return 1 if failing else 0


def copy_bibliographies() -> None:
    """Copy both .bib files, dropping or renaming the duplicated keys."""
    shutil.copyfile(ROOT / "paper" / "string_theory.bib", WRITEUP / "string_theory.bib")
    text = (ROOT / "knowledge/data/references.bib").read_text(encoding="utf-8")
    same, renames = bib_duplicates()
    entries = bib_entries(text)
    for key in same:
        text = text.replace(entries[key], "")
    for key, new_key in renames.items():
        renamed = re.sub(
            r"(@[A-Za-z]+\s*\{\s*)" + re.escape(key) + r"\s*,",
            rf"\g<1>{new_key},",
            entries[key],
            count=1,
        )
        text = text.replace(entries[key], renamed)
    write_text(WRITEUP / "references.bib", text)
    print(
        f"bib: {len(same)} duplicate key(s) with the same eprint or DOI dropped from references.bib"
    )
    for key in same:
        print(f"  dropped {key}")
    print(f"bib: {len(renames)} duplicate key(s) renamed in references.bib")
    for key, new_key in renames.items():
        print(f"  renamed {key} -> {new_key}")


def find_figure(name: str, directories: list[Path]) -> Path | None:
    r"""Locate the file ``\includegraphics{name}`` refers to."""
    candidates = (
        [name] if Path(name).suffix else [name + ext for ext in FIGURE_EXTENSIONS]
    )
    for directory in directories:
        for candidate in candidates:
            if (directory / candidate).is_file():
                return directory / candidate
    return None


def copy_figures(plan: Plan) -> list[str]:
    """
    Copy into ``figures/`` every file the extracted blocks include.

    Returns:
        list[str]: the names that were not found.

    """
    directories = [ROOT / "paper", ROOT / "paper" / "images"]
    directories += sorted(
        p for p in (ROOT / "knowledge" / "notes").iterdir() if p.is_dir()
    )
    missing = []
    for block in plan.blocks:
        text = strip_comments((EXTRACTED / f"{block.name}.tex").read_text("utf-8"))
        for name in INCLUDEGRAPHICS.findall(text):
            found = find_figure(name.strip(), directories)
            if found is None:
                missing.append(f"{name} ({block.name})")
                continue
            target = FIGURES / (
                name.strip() + ("" if Path(name).suffix else found.suffix)
            )
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(found, target)
            print(f"figure: {found.relative_to(ROOT)} -> {target.relative_to(WRITEUP)}")
    FIGURES.mkdir(exist_ok=True)
    for entry in missing:
        print(f"figure MISSING: {entry}")
    return missing


def write_stubs(plan: Plan) -> None:
    """Write the chapter stubs that do not exist yet (never overwrite)."""
    for chapter in plan.chapters:
        path = SECTIONS / f"{chapter['number']}-{chapter['slug']}.tex"
        if path.exists():
            continue
        lines = [
            "% Stub written by tools/extract.py --stubs; the chapter writer replaces it.",
            f"\\section{{{chapter['title']}}}",
            f"\\label{{ch:{chapter['slug']}}}",
            "",
        ]
        lines += [
            f"\\input{{extracted/{block.name}}}"
            for block in plan.blocks
            if block.chapter == chapter["number"]
        ]
        write_text(path, "\n".join(lines) + "\n")
        print(f"stub: {path.relative_to(WRITEUP)}")


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--no-filter", action="store_true", help="write the raw blocks")
    parser.add_argument(
        "--check",
        action="store_true",
        help="scan sections/ and extracted/ for flagged lines; exit 1 on a hit "
        "outside the \\record/\\recordref/\\status lines and the AI-disclosure "
        "paragraph",
    )
    parser.add_argument(
        "--assets",
        action="store_true",
        help="copy the bibliographies, arxiv.def and the included figures",
    )
    parser.add_argument(
        "--stubs", action="store_true", help="write the missing chapter stubs"
    )
    parser.add_argument(
        "--no-demote",
        action="store_true",
        help="keep the block headings at their source level (filtered mode)",
    )
    args = parser.parse_args(argv)
    if args.check:
        return check()
    plan = load_plan()
    results = extract(plan, apply_filter=not args.no_filter, demote=not args.no_demote)
    write_index(results, apply_filter=not args.no_filter)
    if not args.no_filter:
        write_flags(results)
        write_unresolved(results)
    print(f"extract: {len(results)} blocks written to {EXTRACTED.relative_to(ROOT)}")
    if args.assets:
        copy_bibliographies()
        shutil.copyfile(ROOT / "paper" / "arxiv.def", WRITEUP / "arxiv.def")
        copy_figures(plan)
    if args.stubs:
        write_stubs(plan)
    return 0


if __name__ == "__main__":
    sys.exit(main())
