file_path = 'rosalind_rna.txt'

# Open a file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    content = file.read()
    print(content)

# iterate through string, if char is T reolace with U and that position
rna = ''

for char in content:
    if char == 'T':
        rna += 'U'
    else:
        rna += char

with open('output.txt', 'w') as file:
    file.write(rna)
    print(rna)