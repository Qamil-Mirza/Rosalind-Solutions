file_path = 'rosalind_gc.txt'

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    fasta = {}
    for line in lines:
        if line.startswith('>'):
            key = line.strip()[1:]
            fasta[key] = ''
        else:
            fasta[key] += line.strip()
    return fasta

def calculate_gc_content(fasta):
    gc_content = {}
    for key, value in fasta.items():
        gc_content[key] = (value.count('G') + value.count('C')) / len(value) * 100
    return gc_content

def get_max_gc_content(gc_content):
    max_key = max(gc_content, key=gc_content.get)
    return max_key, gc_content[max_key]

fasta = read_fasta(file_path)
gc_content = calculate_gc_content(fasta)
max_key, max_gc_content = get_max_gc_content(gc_content)


with open('output.txt', 'w') as file:
    file.write(max_key + '\n')
    file.write(str(max_gc_content))