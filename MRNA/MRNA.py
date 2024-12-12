file_path = "rosalind_mrna.txt"

# Read the protein sequence from the file
with open(file_path, 'r') as file:
    protein_seq = file.read().strip()

# Build Codon Frequency Table
codon_table = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2, '*': 3
}

# Initialize result
result = 1
mod = 1_000_000

# Calculate the total number of RNA strings
for seq in protein_seq:
    result = (result * codon_table[seq]) % mod

# Account for the stop codon at the end of the protein sequence
result = (result * codon_table['*']) % mod


with open('output.txt', 'w') as file:
    file.write(str(result))
    print(result)
