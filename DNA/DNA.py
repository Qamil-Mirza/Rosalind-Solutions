file_path = 'rosalind_dna.txt'

# Open a file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    content = file.read()
    print(content)

# We will create a hash map to store counts of A C G T
nucleotide_count = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}

# Iterate over the content of the file and count
for nucleotide in content:
    if nucleotide in nucleotide_count:
        nucleotide_count[nucleotide] += 1

with open('output.txt', 'w') as file:
    for key, value in nucleotide_count.items():
        file.write(f'{value} ')
