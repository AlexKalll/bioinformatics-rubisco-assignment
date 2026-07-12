# ============================================================
# Bioinformatics Assignment: Rubisco cDNA Analysis
# Gene: AT3G07670 (Arabidopsis thaliana)
# Accession: NM_111646.3
# ============================================================

# Codon table dictionary
# Maps every triplet codon to its single-letter amino acid code.
# STOP codons are represented as 'STOP'.
codon_table = {
    # Phenylalanine (F)
    'TTT': 'F', 'TTC': 'F',
    # Leucine (L)
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    # Isoleucine (I)
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    # Methionine / Start (M)
    'ATG': 'M',
    # Valine (V)
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    # Serine (S)
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',
    # Proline (P)
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Threonine (T)
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanine (A)
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tyrosine (Y)
    'TAT': 'Y', 'TAC': 'Y',
    # STOP codons
    'TAA': 'STOP', 'TAG': 'STOP', 'TGA': 'STOP',
    # Histidine (H)
    'CAT': 'H', 'CAC': 'H',
    # Glutamine (Q)
    'CAA': 'Q', 'CAG': 'Q',
    # Asparagine (N)
    'AAT': 'N', 'AAC': 'N',
    # Lysine (K)
    'AAA': 'K', 'AAG': 'K',
    # Aspartic acid (D)
    'GAT': 'D', 'GAC': 'D',
    # Glutamic acid (E)
    'GAA': 'E', 'GAG': 'E',
    # Cysteine (C)
    'TGT': 'C', 'TGC': 'C',
    # Tryptophan (W)
    'TGG': 'W',
    # Arginine (R)
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    # Glycine (G)
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

# Task 1: Read and clean the FASTA sequence file
# -----------------------------------------------

# The name of our FASTA file containing the cDNA sequence
fasta_filename = "rubisco.fasta"

# Initialise an empty list to collect each sequence line
sequence_lines = []

# Open the file in read mode and iterate over every line
with open(fasta_filename, "r") as file:
    for line in file:
        # Remove leading/trailing whitespace (including newline characters)
        line = line.strip()
        # Skip the FASTA header line — it begins with '>'
        if not line.startswith(">"):
            sequence_lines.append(line)

# Glue all collected lines into one continuous string with no separator
clean_sequence = "".join(sequence_lines)

# Confirm the file was successfully read, and report the sequence length
print("File successfully read and loaded:", fasta_filename)
print("Total sequence length:", len(clean_sequence), "bases")


# Task 2: Calculate GC content
# -----------------------------------------------


# Task 3: Extract the CDS (Coding DNA Sequence)
# -----------------------------------------------


# Task 4: Translate CDS to protein
# -----------------------------------------------
