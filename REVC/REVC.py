file_path = 'rosalind_revc.txt'

# Open a file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    content = file.read()
    print(content)

# Reverse the string
reverse = content[::-1]

# Iterate through the string and replace with complement
complement = ''
for char in reverse:
    if char == 'A':
        complement += 'T'
    elif char == 'T':
        complement += 'A'
    elif char == 'C':
        complement += 'G'
    elif char == 'G':
        complement += 'C'

with open('output.txt', 'w') as file:
    file.write(complement)
    print(complement)