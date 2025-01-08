file_path = 'rosalind_grph.txt'

def parse_fasta(file_path):
    """
    Reads a FASTA file and returns a dictionary {label: sequence}.
    """
    seq_dict = {}
    current_label = None
    current_seq = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                # If there's an existing label, store the sequence
                if current_label is not None:
                    seq_dict[current_label] = ''.join(current_seq)
                # Start a new sequence
                current_label = line[1:]  # remove '>'
                current_seq = []
            else:
                current_seq.append(line)

        # Save the last sequence if present
        if current_label is not None:
            seq_dict[current_label] = ''.join(current_seq)

    return seq_dict

def overlap_graphs(seq_dict, k=3):
    """
    Build a directed overlap graph O_k from seq_dict (label -> DNA sequence).
    We add an edge from label1 to label2 if:
    - suffix_k(seq_dict[label1]) == prefix_k(seq_dict[label2]), and
    - label1 != label2
    """
    prefix = {}
    suffix = {}

    # Precompute prefixes and suffixes of length k for each sequence
    for label, sequence in seq_dict.items():
        prefix[label] = sequence[:k]
        suffix[label] = sequence[-k:]

    # Build edges
    edges = []
    for label1, sequence1 in seq_dict.items():
        for label2, sequence2 in seq_dict.items():
            if label1 != label2 and suffix[label1] == prefix[label2]:
                edges.append((label1, label2))

    return edges

def main():
    seq_dict = parse_fasta(file_path)

    edges = overlap_graphs(seq_dict, k=3)

    with open('output.txt', 'w') as file:
        for edge in edges:
            file.write(f'{edge[0]} {edge[1]}\n')

if __name__ == "__main__":
    main()
