# Limitations of the K-Means Algorithm

Recall the $K$-means algorithm:

Our cost function is given by:

$cost(C_1, ⋯, C_K) = min_{z^{(1)},⋯,z^{(K)}} \sum_{j=1}^K \sum_{i∈C_j} ∥x^{(i)} - z^{(j)}∥^2$

The algorithm proceeds through the following steps:

1. Randomly initialise $z^{(1)}, ⋯, z^{(K)}$

2. Iterate until no change in cost

   - 2(a) for $i = 1, ⋯, n$
   - $C_j = \{\: i \:| such \: that \: z^{(j)} \: is \: closest \: to \: x^{(i)} \}$

   - 2(b) for $j = 1, ⋯, K$
   - $z^{(j)} = \sum{\frac{x^{(i)}}{|C_j|}}$

**Limitations**

1. Under step 2(b), there is no guarantee that the $z$'s will be members of a regional set of points $x$. In some circumstances this may not matter, but in others it could be critical.

In the Google News example, if the $z$ in a cluster of news stories was not an actual story, there would be nothing to show.

This is a key concern for visual use-cases of $K$-means clustering.

2. Again under step 2(b), in order to say that the representative is a centroid of the points, we have to utilise the squared Euclidean distance.

The cost function applied here to compute the gradient, will only work with Euclidean distance, but in many applications of clustering we would prefer to work with other functions.

**K-medoids**

$K$-medoids resolves the two constraints related above.
