# K-Means Algorithm: The Big Picture

$cost(C_1, ⋯, C_K, ⋯, z^{(1)}, z^{(K)}) = \sum\nolimits_{j=1}^{K} \sum_{i∈C_j} ∥x^{(i)} - z^{(j)}∥^2$

We have the cost, and we need to find a way to find the best partitioning, and the best representatives.

If we have a number of points, how many distinct partitions of size $K$ can we produce?

This is exponential in the number of points, so we can't go one partition at a time, check the cost, then go on to the next one. The search space of partitions is too large, so we need an algorithm to tell us how to get to the right partition.

**K-means clustering**

The algorithm will take a whole space of points, and then randomly assign the representatives.

Then the representatives will draw to themselves those points which are closest to them.

There will then be multiple clouds, one for each representative. Once these clouds emerge, we may decide up new representatives that better reflect those clouds.

After the representatives are reassigned, we may redraw the partitions, and then continue in this manner until convergence.

**K-means clustering algorithm**

1. Randomly select $z^{(1)} ⋯ z^{(K)}$

2. Iterate

   - 2(a) Given $z^{(1)}, ⋯, z^{(K)}$, assign $x$'s to the closest $z$
   - $cost(z^{(1)} ⋯, z^{(K)}) = \sum\nolimits_{i=1}^{n}{} min_{j=1,⋯,K} ∥x^{(i)} - z^{(j)}∥^2$

   - 2(b) Given $C_1, ⋯, C_K$, find the best representatives $z$
   - $cost(C_1, ⋯, C_K) = min_{z^{(1)}, ⋯, z^{(K)}} \sum\nolimits_{j=1}^{K}{} \sum_{i∈C_j} ∥x^{(i)} - z^{(j)}∥^2$
