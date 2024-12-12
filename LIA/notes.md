# Independent Alleles
The problem is essentially asking us to calculate probabilities in a genetic familty tree with Mendelian inheritance. 

**Goal**: Determine the probability that at least $N$ organisms with the Aa Bb genotype exist in the $k$-th generation

## Breaking Down The Question Further
1. We have Tom of genotype Aa Bb in gen 0. Each gen doubles the number of descendants. We derive the following relation:

$\text{Number of descendants in kth generation}= 2^{k}$

2. We want to calculate the probability of Aa Bb for one Offspring:

- $Pr(AaBb) = Pr(Aa) \cdot Pr(Bb)$

When crossing Aa with Aa for gene A, we get the following distribution:

- $Pr(AA) = \frac{1}{4}$
- $Pr(Aa) = \frac{1}{2}$
- $Pr(aa) = \frac{1}{4}$

And similarly for gene B! 

Therefore we get that:

$Pr(AaBb) = Pr(Aa) \cdot Pr(Bb) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$

3. We can model the problem as a Binomial Distribution:

Let $X$ be the random variable representing the number of Aa Bb organisms in the k-th generation.

Mathematically speaking:

$X \sim Bin(2^k, \frac{1}{4})$

4. Now that we have the appropriate setup we can proceed with solving the problem:

$Pr(X \geq N) = 1 - Pr(X < N) = 1- \sum_{x=0}^{N-1} {2^k \choose x} \cdot (\frac{1}{4})^x \cdot (\frac{3}{4})^{2^k - x}$

And there you have it!