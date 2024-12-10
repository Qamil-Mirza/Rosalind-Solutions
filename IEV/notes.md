# General Steps

1. Determine probability that an offspring from each couple will display the dominant phenotype.
2. Calculate expected number of dominant offspring for each couple type
3. Sum the expected numbers from all couple types to get the total expected number of dominant offspring

## Genotypes And Their Probabilities
For each genotype couple, their probabilties of producing an offspring that will dispaly the dominant phenotype is as follows:

- AA x AA: 1.0
- AA x Aa: 1.0
- AA x aa: 1.0
- Aa x Aa: 0.75
- Aa x aa: 0.50
- aa x aa: 0

## General Formula For Expected Dominant Offspring Per Couple

$\mathbb{E}[\text{Dominant Offspring}] = \text{number of couples} \cdot \text{number of offspring per couple} \cdot P(\text{Dominant Phenotype Offspring Produced})$

## Generalized Formula For Total Expected Dominant Offspring
Given some dataset with six integers $n_1, n_2, n_3, n_4, n_5, n_6$ which each represent the number of couples for each genotype pairing, we can get the total expected number of dominant offpsring as:


$\text{Total Expected Dominant Offspring} = 2 \times \left(n_1 \times 1.0 + n_2 \times 1.0 + n_3 \times 1.0 + n_4 \times 0.75 + n_5 \times 0.5 + n_6 \times 0\right)$

