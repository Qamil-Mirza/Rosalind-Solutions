file_path = 'rosalind_hamm.txt'

with open(file_path, 'r') as file:
    data = file.read().split('\n')
    s = data[0]
    t = data[1]

def hamming_distance(s, t):
    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1
    return distance

distance = hamming_distance(s, t)

with open('output.txt', 'w') as file:
    file.write(str(distance))
