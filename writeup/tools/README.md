# Extraction tools of the complete write-up

`extract.py` copies the reused LaTeX blocks listed in `sources.yaml` from their sources (the paper at a git revision, the knowledge notes and the removed blocks in the working tree) into `extracted/<chapter>/<order>-<tag>.tex`.
The chapter files `sections/<nn>-<slug>.tex` `\input` these blocks; nobody edits a block by hand.
Python 3.12+, standard library only (the YAML reader handles the subset `sources.yaml` uses).

## Running

Run from the project root:

| Command | Effect |
|---|---|
| `.venv/bin/python dist/github/writeup/tools/extract.py` | Extract and filter every block; write `extracted/index.md`, `extracted/flags.md`, `extracted/unresolved-refs.md` |
| `… extract.py --no-filter` | Write the raw blocks, byte for byte the source ranges (test mode; rerun without the option afterwards) |
| `… extract.py --check` | Scan `sections/*.tex` and `extracted/*/*.tex` (override files excluded) with the flag regex; print each hit by file and line, exit 1 on any hit outside the exempted lines (below) |
| `… extract.py --assets` | Also copy `string_theory.bib`, `references.bib` (duplicated keys handled, below), `arxiv.def`, and every file the blocks `\includegraphics` into `figures/` |
| `… extract.py --stubs` | Also write the chapter stubs that do not exist yet (never overwrites a chapter file) |
| `.venv/bin/python dist/github/writeup/tools/test_extract.py` | Tests: raw blocks byte-identical to their ranges, filtered blocks free of comments and draft macros, filter and override on a sample |

Build: `cd dist/github/writeup && latexmk -pdf -interaction=nonstopmode cubic-sft-complete-notebook.tex`.

## The filter

In order:

1. Full-line `%` comments are dropped; trailing comments are cut (`\%` is kept).
2. `\hecomment{…}`, `\agcomment{…}`, `\draftcomment[*][…]{…}`, `\draftnote[…]{…}`, `\margnote{…}` are removed with their brace-balanced arguments; a line left blank is dropped.
   `\agmod{text}` becomes `text`.
3. Lines `\input{sections/…}` of the source are dropped (those files are blocks of their own).
   Every heading is demoted by one level (`\section` → `\subsection` → `\subsubsection` → `\paragraph` → `\subparagraph`, starred forms alike), so that the chapter stub holds the only `\section`; `--no-demote` keeps the source levels.
4. Every `\label{x}` becomes `\label{<tag>:x}`.
   Each key of `\cref`, `\Cref`, `\eqref`, `\ref`, `\labelcref` defined in the block's source document (all `.tex` files of its `documents:` entry) gets the same prefix.
   For `pc` (the paper at `4096d3f`), a key that no extracted `pc` block defines resolves to `p:` when the paper at `d6a0391` defines it.
   Keys defined in no searched document are left unchanged.
5. In note blocks (tags other than `p`, `pc`), citation keys renamed in `references.bib` get their `-kn` suffix.
6. The override file is applied, if present.

`extracted/unresolved-refs.md` lists the keys of step 4 left unchanged, and the tagged references whose label no extracted block defines (undefined in the build until a chapter supplies them).
`extracted/flags.md` lists, per block, the lines of the filtered block matching the flag regex of the design (Part 3), with the hit count of the raw range for comparison.
The agent and model names of the regex match as whole words (plural allowed for critic, computator, orchestrator), so "critical" does not hit.

Exempted lines, which the design allows to carry ledger IDs and record stems:

- every line containing `\record{`, `\recordref{` (a record stem or ledger ID in a table cell) or `\status{` (the macros of `cubic-sft-complete-notebook.tex`), in `--check` and in `flags.md` (its `exempted` column, and the line "exempted: N lines" of each block section);
- in `--check`, the AI-disclosure paragraph of `sections/00-preamble.tex`: from a line `% ai-disclosure` or `\paragraph{AI disclosure}` to the first blank line after text, or the next heading, whichever comes first.
  Without either marker nothing of the preamble is exempted, and `--check` prints a note.

Every other matching line is a hit, in `sections/00-preamble.tex` too.

## Override files

`extracted/<chapter>/<order>-<tag>.patch.tex` fixes a block without editing it; the script applies it on every filtered run.
It holds hunks, applied in order to the filtered block (after step 5):

```text
%%% replace
<exact lines of the filtered block, copied from extracted/…tex or flags.md>
%%% with
<replacement lines; empty to delete>
%%% end
```

Each old text must occur exactly once in the block, otherwise the run stops with an error.
Text outside hunks is ignored and can hold notes.

## Bibliography

`references.bib` is the copy of `knowledge/data/references.bib`.
A key also present in `paper/string_theory.bib` is dropped from the copy when both entries carry the same eprint or DOI; otherwise it is renamed `<key>-kn` in the copy and in the citations of the note blocks.

## Source tags

| Tag | Source |
|---|---|
| `p` | paper at `d6a0391` (`paper/sections/`), and the verbatim blocks of `dist/removed-2026-11-07/` |
| `pc` | paper at `4096d3f`, after the finishing round of 2026-11-09 (rewritten section 3: recovered action, kernel conditions); until 2026-11-09 at `aa0ac21` |
| `ov` | `knowledge/notes/cubic-sft-overview/` |
| `ped` | `knowledge/notes/cubic-sft-ibl-pedagogical/` |
| `rs` | `knowledge/notes/cubic-sft-riemann-surfaces/` |
| `ibk` | `knowledge/notes/companion-ibl-bookkeeping/` |
| `pg` | `knowledge/notes/companion-pairing-grading/` |
| `q` | `knowledge/notes/companion-quintic/` |
| `icg` | `knowledge/notes/cubic-sft-inverse-circle-gluing/` |
| `fdm` | `knowledge/notes/finite-dimensional-models/` |
| `jb` | `knowledge/notes/j-boundary-representation/` |

## `sources.yaml`

Three lists: `documents` (the files whose labels make up each tag's source document), `chapters` (number, slug, title, appendix flag) and `blocks` (chapter, order, source, rev, tag, and a range: `whole`, `lines: 'a-b'`, or `heading` with optional `level` and `to`).
The header of the file gives the exact semantics and the YAML subset accepted.
