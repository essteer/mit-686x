# Similarity Measures - Cost Functions

If we have data points that appear to form three rough groups, but must group them into just two clusters, we need a means of evaluating which partitioning is preferable.

Cost functions are used to determine which clustering has the lowest cost.

We assume that the cost will be the sum of the cost of the individual clusters:

$cost(C_1, ⋯, C_K) = \sum\nolimits_{j=1}^{K}{cost(C_j)}$

This is intuitive, since the best clustering should have the lowest aggregate cost across the clusters.

There are different options for how to determine the cost of an individual cluster.

1. Diameter - the distance between the furthest two points.
2. Average distance between each point.

With diameter, the cost is determined by outliers.

With average distance, all of the points contribute to the cost.

3. Use of representatives.

This measures the cost of a cluster by comparing the distance between all of the points and a specific representative.

Therefore whenever a cluster is given, a representative must also be given in order to compute the cost.

This is expressed as:

$cost(C, z) = \sum_{i∈C} dist(x^{(i)}, z)$

The specific distance measurement used could be cosine similarity or Euclidean square distance, for example.

**Cosine similarity**

Takes two vectors, and looks at the angle between those two vectors.

$cos(x^{(i)}, x^{(j)}) = \frac{x^{(i)} • x^{(j)}}{∥x^{(i)}∥ • ∥x^{(j)}∥}$

**Euclidean square distance**

$dist(x^{(i)}, x^{(j)}) = ∥x^{(i)} - x^{(j)}∥^2$

**Comparison**

Cosine similarity is not sensitive to the magnitude of the vectors.

In terms of the Google News application, if we chose the cosine for two vectors representing different stories, cosine similarity would not take note of how long the stories were.

Euclidean square distance would be sensitive to the lengths of the stories.

The question to consider is, what makes the match between the similarity measure and the algorithm? When is it important, and when is it not important?

**Determining the cost**

To get the cost, we need the representatives as well as the partitions.

We use Euclidean square distance to go over every cluster, from cluster $1$ to cluster $K$, and within each cluster we take the points that belong to that clusts, and compute the Euclidean square distance between those points and the representative of that cluster.

$cost(C_1, ⋯, C_K, ⋯, z^{(1)}, z^{(K)}) = \sum\nolimits_{j=1}^K \sum_{i∈C_j} ∥x^{(i)} - z^{(j)}∥^2$
