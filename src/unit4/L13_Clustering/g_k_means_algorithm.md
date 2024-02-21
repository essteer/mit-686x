# K-Means Algorithm: The Specifics

**K-means clustering algorithm**

1. Randomly select $z^{(1)}, ⋯, z^{(K)}$

2. Iterate

   - 2(a) Given $z^{(1)}, ⋯, z^{(K)}$, assign $x$'s to the closest $z$
   - $cost(z^{(1)}, ⋯, z^{(K)}) = \sum\nolimits_{i=1}^{n} min_{j=1,⋯,K} ∥x^{(i)} - z^{(j)}∥^2$

   - 2(b) Given $C_1, ⋯, C_K$, find the best representatives $z$
   - $cost(C_1, ⋯, C_K) = min_{z^{(1)}⋯z^{(K)}} \sum\nolimits_{j=1}^{K} \sum_{i∈C_j} ∥x^{(i)} - z^{(j)}∥^2$

**Gradient**

We need to take the gradient at 2(b), in order to determine what should be computed.

Notice that every cluster selects its representative independently.

So we want to look at a specific cluster, such as cluster $j$ $C_j$, and find the representative that will minimise the sum.

$\sum_{i∈C_j} ∥x^{(i)} - z^{(j)}∥^2$

We want to find the $z_j$ that will minimise the sum, so we take the derivative with respect to $z$, make it equal to $0$, and it will tell us about the $z$.

$\frac{\partial{}}{\partial z^{(j)}} \sum_{i∈C_j} ∥x^{(i)} - z^{(j)}∥^2 = 0$

Through the answer, we discover that the $z^{(j)}$ is the centroid of the group.

$z^{(j)} = \sum{\frac{x^{(i)}}{|C_j|}}$

Note that the computation evaluates to this in the case of square Euclidean distance - for other similarity measures, the result would not be the same.

This form of the algorithm only works if the distance measure being use is square Euclidean distance.

**Iterations**

How do we know how many times to iterate?

We can guarantee that the algorithm converges, and that it converges to a local minimum.

We cannot guarantee it will converge to the global minimum.

Through every iteration, the cost either remains the same, or decreases.

Since the number of partitions is finite, we are guaranteed to converge.

But the convergence is local - starting with a different initialisation, we could arrive at a different partitioning.
