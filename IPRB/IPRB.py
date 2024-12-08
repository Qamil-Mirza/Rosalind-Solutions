def p_possess_dominant_allele(k, m, n):
    N = k + m + n
    
    p_present_AA_AA = 1
    p_present_AA_Aa = 1
    p_present_AA_aa = 1
    p_present_Aa_Aa = 0.75
    p_present_Aa_aa = 0.5
    p_present_aa_aa = 0

    p_AA_AA = k/N * (k-1)/(N-1) * p_present_AA_AA
    p_AA_Aa = (k/N * m/(N-1) + (m/N * k/(N-1))) * p_present_AA_Aa
    p_AA_aa = (k/N * n/(N-1) + (n/N * k/(N-1))) * p_present_AA_aa
    p_Aa_Aa = m/N * (m-1)/(N-1) * p_present_Aa_Aa
    p_Aa_aa = (m/N * n/(N-1) + (n/N * m/(N-1))) * p_present_Aa_aa
    p_aa_aa = n/N * (n-1)/(N-1) * p_present_aa_aa

    return p_AA_AA + p_AA_Aa + p_AA_aa + p_Aa_Aa + p_Aa_aa + p_aa_aa

file_path = 'rosalind_iprb.txt'

with open(file_path, 'r') as file:
    k, m, n = map(int, file.read().split())

with open("output.txt", "w") as output:
    output.write(str(p_possess_dominant_allele(k, m, n)))