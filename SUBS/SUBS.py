file_path = 'rosalind_subs.txt'

# Read file
with open(file_path, 'r') as file:
    data = file.read().split('\n')
    dna_string = data[0]
    motif = data[1]

# Find all occurrences of motif in dna_string using a sliding window
def find_motif(dna_string, motif):
    positions = []
    for i in range(len(dna_string)):
        if dna_string[i:i+len(motif)] == motif:
            positions.append(i+1)
    return positions

# Get positions of motif in dna_string
positions = find_motif(dna_string, motif)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, positions)))
