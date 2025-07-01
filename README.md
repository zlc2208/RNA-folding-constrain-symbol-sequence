# RNA Secondary Structure Symbol Sequence

This repository provides tools for representing RNA secondary structure constraints using symbolic sequences, with a focus on dot-bracket-like notation.

## Overview

The core script, `2th_structure.py`, generates a symbolic representation of paired and unpaired regions in a 332-base RNA sequence. It uses a simple notation:

- `(` : Start of a paired region (front)
- `)` : End of a paired region (back)
- `x` : Unpaired nucleotides
- `.` : All other nucleotides

This visualization is widely used in RNA bioinformatics for quickly understanding structural constraints.

## How the Script Works

1. **Index Definitions**
    - Paired regions are listed in `index_pairs`, with each pair consisting of two index ranges.
    - Unpaired regions are listed in `index_unpaired`.

2. **Index Collection**
    - The script collects all indices for paired (front/back) and unpaired regions.

3. **Sequence Rendering**
    - It iterates through positions 1 to 332, outputting the appropriate symbol at each position.

## Example Output

Running the script prints a line like this (snippet shown for illustration):
