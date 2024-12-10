file_path = 'rosalind_fibd.txt'

# Read the file
with open(file_path, 'r') as file:
    data = file.read().split()

# Assign the variables
n = int(data[0])
m = int(data[1])

# keep track of the rabbit pairs of a specific age
rabbit_pair = [1] + [0] * (m - 1)

for i in range(1, n):
    # rabbits aged 1 and older produce new pairs
    new_rabbit_pairs = sum(rabbit_pair[1:])
    # shift the rabbit pairs to the right and remove the oldest rabbit pairs
    rabbit_pair = [new_rabbit_pairs] + rabbit_pair[:-1]

total_rabbit_pairs = sum(rabbit_pair)

with open('output.txt', 'w') as file:
    file.write(str(total_rabbit_pairs))
    print(total_rabbit_pairs)