# Introduction to the K-Medoids Algorithm

K-medoids is derived almost directly from the K-means algorithm.

It seeks to resolve the two constraints referenced previously:

1. That K-means can choose z's that don't belong to the set of points x.
2. That K-means depends on squared Euclidean means being the function.

**K-medoids**

The first step to change is, rather than randomly selecting the best z, randomly select the best z from among the actual data points x.

1. Randomly initialise {z<sup>(1)</sup> ⋯ z<sup>(K)</sup>} <= {x<sup>(1)</sup> ⋯ x<sup>n</sup>}

2. Iterate until there is no change in cost

   - 2(a) for i = 1, ⋯, n
   - C<sub>j</sub> = { i | such that z<sup>(j)</sup> is closest to x<sup>(i)</sup> }

   Note that step 2(a) remains unchanged.

   - 2(b) for j = 1, ⋯, K
   - z<sup>(j)</sup> ∈ {x<sup>(1)</sup> ⋯ x<sup>n</sup>} such that Σ<sub>x<sup>(i)</sup>∈C<sub>j</sub></sub> dist(x<sup>(i)</sup>, z<sup>(j)</sup>) is minimal

   I.e., such that the sum of distances from all of the other points in that cluster to the chosen representative point, is minimal.
