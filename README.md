# A cubic closed string field theory – complete write-up and records

This repository accompanies the paper *A cubic closed string field theory* by Harold Erbin.
The paper rewrites the classical action of closed bosonic string field theory as a cubic action, through a Hubbard–Stratonovich transformation with multilocal auxiliary string fields.

The repository holds everything the project behind the paper produced: the derivations the paper only states, results too weak or too far from its line to be in it, and the computations that support its statements.

**Everything here is AI-generated and has not been reviewed by a human.**
The research was carried out by AI agents under the direction of the author; the paper is the account the author has checked.
Use this material as a map of what was derived and how, and check any statement against its derivation record and its script before relying on it.

## Contents

| Folder | Content |
| --- | --- |
| `writeup/` | The complete write-up: a LaTeX document (`cubic-sft-complete-notebook.tex`, about 450 pages) collecting every valid result with its derivation, its status and pointers to its record and script. Start here. |
| `agent/derivations/` | The derivation records: one Markdown file per derivation, as written by the agents, with what was established, under which assumptions and how it was checked. The write-up's `Derivation record` footnotes point to these files. |
| `knowledge/results.md` | The results ledger: one entry per result (`R1`, `R2`, …) with its statement, status tag and sources. Hypotheses are `PH1`, `PH2`, …. |
| `knowledge/conventions.md` | The conventions used throughout (ghost number, normalization of correlators, reality conditions). |
| `codes/` | The verification scripts (`verify-*.py`, Python with sympy, numpy, jax, mpmath). Each checks one claim of a record and prints PASS/FAIL per check. See `codes/README.md`. |

## Status labels

Each result carries the status tag of the ledger, printed in a box in the write-up: *Proven* (a complete argument), *Verified* (checked symbolically or numerically to the order stated), *Numerical*, *Argued* (a heuristic argument), *Open*, and *mixed* when parts of a statement have different status.
*Conditional(PH1, …)* means the result holds under the hypotheses named, listed in the hypotheses appendix of the write-up.
Results *superseded* or *withdrawn* by later work are flagged, and wrong directions are collected in the dead-ends chapter of the write-up; *no ledger entry* marks a record whose result was not entered in the ledger.
The definitions in the preamble chapter of the write-up are authoritative.

## Building the write-up

```bash
cd writeup
latexmk -pdf -interaction=nonstopmode cubic-sft-complete-notebook.tex
```

It needs a TeX Live distribution with `biber`.
The extraction tools in `writeup/tools/` document how the document was assembled from the project sources; they run only inside the source project.

## Running the scripts

```bash
cd codes
uv sync
uv run python verify-<name>.py
```

`codes/README.md` lists each script, the claim it verifies and the result of a reference run.

## Limitations

- Some records, ledger entries and scripts refer to files that are not published (agent reports, notes, the paper sources); these links are dead.
- Numbers from a companion project on the explicit SL(2,C) quartic vertex are not included until that work is public; the records and scripts that depend on them are withheld, and the places where they were used say so.

## License and reuse

You are free to reuse, adapt and build on this material.

- The code in `codes/` is released under the MIT License (`codes/LICENSE`).
- Everything else (the write-up, the derivation records, the ledgers and the conventions) is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0, `LICENSE`).

If you use it in your work, please cite the paper *A cubic closed string field theory* by Harold Erbin.
