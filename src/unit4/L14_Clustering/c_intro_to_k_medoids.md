# Introduction to the $K$-Medoids Algorithm

$K$-medoids is derived almost directly from the $K$-means algorithm.

It seeks to resolve the two constraints referenced previously:

1. That $K$-means can choose $z$'s that don't belong to the set of points $x$.
2. That $K$-means depends on squared Euclidean means being the function.

**$K$-medoids**

The first step to change is, rather than randomly selecting the best $z$, randomly select the best $z$ from among the actual data points $x$.

1. Randomly initialise $\lbrace z^{(1)}, ⋯, z^{(K)}\rbrace \leq \lbrace x^{(1)}, ⋯, x^n \rbrace$

2. Iterate until there is no change in cost

   - 2(a) for $i = 1, ⋯, n$
   - $C_j = \lbrace  \: i \: | \: such \: that \: z^{(j)} \: is \: closest \: to \: x^{(i)} \rbrace$

   Note that step 2(a) remains unchanged.

   - 2(b) for $j=1, ⋯, K$
   - $z^{(j)} ∈ \lbrace x^{(1)}, ⋯, x^n \rbrace \: such \: that \: \sum_{x^{(i)}∈C_j} dist(x^{(i)}, z^{(j)})$ is minimal

   I.e., such that the sum of distances from all of the other points in that cluster to the chosen representative point, is minimal.
