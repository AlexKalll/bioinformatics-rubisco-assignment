# Bioinformatics Assignment: Rubisco cDNA Analysis

Analysis of the *Arabidopsis thaliana* Rubisco methyltransferase family protein cDNA sequence using Python.

---

## Assignment Objective

This assignment demonstrates core bioinformatics programming skills by working with a real plant cDNA sequence. The four tasks covered are:

1. **Read and parse a FASTA file** — load the raw nucleotide sequence into Python
2. **Calculate GC content** — measure the proportion of G and C nucleotides
3. **Extract the CDS** — isolate the coding region by slicing the sequence
4. **Translate CDS to protein** — convert nucleotide triplets (codons) into amino acids

---

## Sequence Information

| Field       | Value                                                                 |
|-------------|-----------------------------------------------------------------------|
| Accession   | NM_111646.3                                                           |
| Organism    | *Arabidopsis thaliana* (thale cress)                                  |
| Gene        | AT3G07670 — Rubisco methyltransferase family protein                  |
| Sequence    | `rubisco.fasta`                                                       |
| CDS region  | Positions 88–1602 (1-based biological coordinates)                    |

---

## Requirements

- Python 3.x (no external packages required — standard library only)

---

## How to Run

```bash
python main.py
```

Run the command from the same directory as `rubisco.fasta`. No installation is needed.

---

## Project Structure

```
bioinformatics-rubisco-assignment/
├── main.py          # Main analysis script (all four tasks)
├── rubisco.fasta    # cDNA sequence in FASTA format
├── README.md        # This file
└── .gitignore       # Python and editor artefacts to ignore
```

---

## Expected Output

```
============================================================
Task 1: Reading FASTA File
============================================================
File successfully read and loaded: rubisco.fasta
Total sequence length:            2067 bases

============================================================
Task 2: GC Content
============================================================
G count:     423
C count:     431
GC Content: 41.32%

============================================================
Task 3: CDS Extraction
============================================================
CDS sequence isolated. Length: 1515 bases

============================================================
Task 4: Translation
============================================================
Final Protein Length: 504 amino acids.
Protein Sequence:
MAKACLLQSTLLPAYSPLHKLRNQNITLSFSPLPLSRCRPGIHCSVSAGETTIQSM...NFFK
============================================================
```

---

## Key Concepts

| Concept      | Explanation                                                                 |
|--------------|-----------------------------------------------------------------------------|
| FASTA format | Plain-text format for biological sequences; header starts with `>`          |
| GC content   | Percentage of G + C bases; used to characterise genomes                     |
| CDS          | Coding DNA Sequence — the part of mRNA translated into protein              |
| Codon        | A triplet of nucleotides (e.g. `ATG`) that encodes one amino acid           |
| Translation  | Process of reading codons and assembling an amino acid chain (protein)      |

---

## Author

MSc Bioinformatics student — *Arabidopsis thaliana* Rubisco gene analysis exercise.
