# to calculate the total number of rabbits after n months
# given that each pair of rabbits produces k pair of rabbits every month

def total_rabbits(n, k):
    # base case
    if n == 1 or n == 2:
        return 1
    else:
        return total_rabbits(n-1, k) + k * total_rabbits(n-2, k)
    

file_path = 'rosalind_fib.txt'

with open(file_path, 'r') as file:
    n, k = map(int, file.read().split())

total_num_rabbits = total_rabbits(n, k)

with open('output.txt', 'w') as file:
    file.write(str(total_num_rabbits))