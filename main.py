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


# =====================================================================
# Task 1: Read and clean the FASTA sequence file
# =====================================================================
# FASTA is a standard bioinformatics text format.
# The first line (header) starts with '>' and contains metadata.
# All subsequent lines contain the actual nucleotide sequence.
print("=" * 60)
print("Task 1: Reading FASTA File")
print("=" * 60)

# The name of our FASTA file containing the cDNA sequence
fasta_filename = "rubisco.fasta"

# Initialise an empty list to collect each sequence line.
# We will append one line at a time as we read through the file.
sequence_lines = []

# open() takes two arguments: the filename, and the mode ('r' = read).
# Using 'with' ensures the file is automatically closed after reading.
with open(fasta_filename, "r") as file:
    for line in file:
        # .strip() removes invisible whitespace at both ends of the line,
        # including '\n' (newline) characters that Python reads from the file.
        line = line.strip()
        # The header line starts with '>'. We skip it because it is
        # descriptive metadata, not part of the nucleotide sequence.
        if not line.startswith(">"):
            sequence_lines.append(line)

# "".join() concatenates all strings in the list using "" as the separator,
# producing one unbroken string of nucleotide characters.
clean_sequence = "".join(sequence_lines)

# Confirm the file was successfully read, and report the sequence length
print("File successfully read and loaded:", fasta_filename)
print("Total sequence length:           ", len(clean_sequence), "bases")


# =====================================================================
# Task 2: Calculate GC content
# =====================================================================
# GC content is the percentage of nucleotides in a DNA sequence that
# are either Guanine (G) or Cytosine (C). It is a fundamental measure
# used to characterise genomes and assess sequence quality.
print()
print("=" * 60)
print("Task 2: GC Content")
print("=" * 60)

# .count() is a built-in string method that returns how many times
# a given character (or substring) appears in the string.
g_count = clean_sequence.count("G")
c_count = clean_sequence.count("C")

# GC % = ((number of G + number of C) / total number of bases) × 100
total_bases = len(clean_sequence)
gc_content = ((g_count + c_count) / total_bases) * 100

print("G count:    ", g_count)
print("C count:    ", c_count)
print("GC Content: {:.2f}%".format(gc_content))


# =====================================================================
# Task 3: Extract the CDS (Coding DNA Sequence)
# =====================================================================
# The CDS is the portion of the mRNA that is actually translated into
# protein. It begins at the start codon (ATG) and ends at a stop codon.
# We isolate it by slicing the full sequence using known coordinates.
print()
print("=" * 60)
print("Task 3: CDS Extraction")
print("=" * 60)

# The biological coordinates are 1-based (position 88 to 1602).
# Python uses 0-based indexing, so position 88 becomes index 87.
# The end index 1602 is exclusive in Python slicing, which is correct here.
cds_sequence = clean_sequence[87:1602]

print("CDS sequence isolated. Length:", len(cds_sequence), "bases")


# =====================================================================
# Task 4: Translate CDS to protein
# =====================================================================
# Translation converts a nucleotide sequence into an amino acid sequence.
# The ribosome reads codons (groups of 3 nucleotides) from the CDS and
# maps each codon to an amino acid using the genetic code.
print()
print("=" * 60)
print("Task 4: Translation")
print("=" * 60)

protein_sequence = []  # Initiate an empty list to collect amino acids

# range(0, length, 3) generates start positions: 0, 3, 6, 9 ...
# Each iteration extracts one codon of exactly 3 characters.
for i in range(0, len(cds_sequence), 3):
    codon = cds_sequence[i:i + 3]

    # Discard any incomplete codon at the very end of the sequence
    if len(codon) < 3:
        break

    # .get(codon, "?") looks up the codon; returns "?" if not found
    amino_acid = codon_table.get(codon, "?")

    # A STOP codon signals the ribosome to release the protein chain
    if amino_acid == "STOP":
        break

    protein_sequence.append(amino_acid)

# Join the amino acid list into a single protein string
final_protein = "".join(protein_sequence)

print("Final Protein Length:", len(final_protein), "amino acids.")
print("Protein Sequence:")
print(final_protein)
print("=" * 60)
