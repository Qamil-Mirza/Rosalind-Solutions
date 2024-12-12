from math import comb

file_path = "rosalind_lia.txt"

# Read input values
with open(file_path, "r") as file:
    k, N = map(int, file.readline().strip().split())

# Total number of offspring in the k-th generation
n = 2**k

# Probability that a single offspring is Aa Bb
p = 1/4

# Calculate probability that X >= N
# This is 1 - sum_{x=0}^{N-1} P(X=x)
prob_less_than_N = 0.0

for x in range(N):
    prob_less_than_N += comb(n, x) * (p**x) * ((1 - p)**(n - x))

prob_at_least_N = 1 - prob_less_than_N

# Print result rounded to three decimal places
with open("output.txt", "w") as file:
    file.write(f"{prob_at_least_N:.3f}")

print(f"{prob_at_least_N:.3f}")
