# Breaking Down The Problem
- **k**: number of homozygous dominant individuals (\(AA\))
- **m**: number of heterozygous individuals (\(Aa\))
- **n**: number of homozygous recessive individuals (\(aa\))

Total Population:
\[
N = k + m + n
\]

**Goal**: Find the probability that two randomly selected individuals will produce an individual possessing a dominant allele. (Assuming any two organisms can mate)

---

## Approach

First, we identify all pairings and their probabilities of producing an individual possessing a dominant allele:

1. \(P(\text{Dominant Allele Present} \mid AA \times AA) = 1\)
2. \(P(\text{Dominant Allele Present} \mid AA \times Aa) = 1\)
3. \(P(\text{Dominant Allele Present} \mid AA \times aa) = 1\)
4. \(P(\text{Dominant Allele Present} \mid Aa \times Aa) = 0.75\)
5. \(P(\text{Dominant Allele Present} \mid Aa \times aa) = 0.5\)
6. \(P(\text{Dominant Allele Present} \mid aa \times aa) = 0\)

---

For each pair, we calculate the probability of selecting the pair:

1. \(P(AA \times AA) = \frac{k}{N} \cdot \frac{k-1}{N-1}\)
2. \(P(AA \times Aa) = \frac{k}{N} \cdot \frac{m}{N-1} + \frac{m}{N} \cdot \frac{k}{N-1}\)
3. \(P(AA \times aa) = \frac{k}{N} \cdot \frac{n}{N-1} + \frac{n}{N} \cdot \frac{k}{N-1}\)
4. \(P(Aa \times Aa) = \frac{m}{N} \cdot \frac{m-1}{N-1}\)
5. \(P(Aa \times aa) = \frac{m}{N} \cdot \frac{n}{N-1} + \frac{n}{N} \cdot \frac{m}{N-1}\)
6. \(P(aa \times aa) = \frac{n}{N} \cdot \frac{n-1}{N-1}\)

---

Finally, the probability of producing a dominant phenotype is calculated as:

\[
P(\text{Dominant Phenotype}) = 
\sum_{\text{pairs}}P(pair) \cdot P(\text{dominant phenotype | pair})
\]
