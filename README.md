# RNA Secondary Structure Symbol Sequence
When we use website tools to predict a RNA secondary structure, it's cumbersome and error-prone to print structure symbol equence manually.

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
    - Ensure the RNA length in `len_all`.
    - Paired regions are listed in `index_pairs`, with each pair consisting of two index ranges.
    - Unpaired regions are listed in `index_unpaired`.
      <pre>
          len_all = 332
          index_pairs = {
          1: [np.arange(24, 31), np.arange(81, 88)],
          2: [np.arange(37, 40), np.arange(68, 71)],
          3: [np.arange(42, 46), np.arange(64, 68)],
          4: [np.arange(46, 49), np.arange(60, 63)],
          }
          index_unpaired = {
          1: np.arange(34, 38),
          2: np.arange(40, 42),
          3: np.arange(49, 60),
          4: np.arange(63, 64),
          5: np.arange(71, 78),
          }
      </pre>

3. **Index Collection**
    - The script collects all indices for paired (front/back) and unpaired regions.

4. **Sequence Rendering**
    - It iterates through positions 1 to 332, outputting the appropriate symbol at each position.

## Example Output

Running the script prints a line like this (snippet shown for illustration):
<pre>   
.......................(((((((...xxx(((xx(((((((xxxxxxxxxxx)))x)))))))xxxxxxx...))))))).....................................................................................................................................................................................................................................................
</pre>
Corresponding RNA sequence:
<pre>
    GGAUGUGAGGGCGAUCUGGCUGCGACAUCUGUCACCCCAUUGAUCGCCAGGGUUGAUUCGGCUGAUCUGGCUGGCUAGGCGGGUGUCCCCUUCCUCCCUCACCGCUCCAUGUGCGUCCCUCCCGAAGCUGCGCGCUCGGUCGAAGAGGACGACCAUCCCCGAUAGAGGAGGACCGGUCUUCGGUCAAGGGUAUACGAGUAGCUGCGCUCCCCUGCUAGAACCUCCAAACAAGCUCUCAAGGUCCAUUUGUAGGAGAACGUAGGGUAGUCAAGCUUCCAAGACUCCAGACACAUCCAAAUGAGGCGCUGCAUGUGGCAGUCUGCCUUUCUUUU
</pre>
