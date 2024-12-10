file_path = 'rosalind_iev.txt'

# Read the file
with open(file_path, 'r') as file:
    data = file.read().strip().split()

# Convert the data into integers
data = [int(i) for i in data]

# Calculate the expected number of offspring displaying the dominant phenotype
# 1. The probability that the offspring will be dominant is 1
# 2. The expected number of offspring displaying the dominant phenotype is the sum of the probabilities
#    of each offspring displaying the dominant phenotype
# 3. The probabilities are calculated as follows:

# AA-AA: 1
# AA-Aa: 1
# AA-aa: 1
# Aa-Aa: 0.75
# Aa-aa: 0.5
# aa-aa: 0

# The expected number of offspring displaying the dominant phenotype is:
total_expected_dominant_offspring = 2 * (data[0] + data[1] + data[2] + 0.75 * data[3] + 0.5 * data[4])

# output the result
with open('output.txt', 'w') as file:
    file.write(str(total_expected_dominant_offspring))
