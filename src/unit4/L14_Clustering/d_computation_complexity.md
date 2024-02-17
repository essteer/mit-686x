# Computation Complexity of $K$-Means and $K$-Medoids

Comparing the differences between $K$-Means and $K$-Medoids, we can see that $K$-Medoids is more expensive than $K$-Means.

We don't know how many steps each algorithm will take to find the best partitioning, but we can look at the cost of one iteration of each algorithm.

**Step 2(a)**

For an iteration of each algorithm at step 2(a), we can see the complexity $O(n•K•d)$ where $n$ is the number of data points, $K$ is the number of clusters, and $d$ is the size of the clusters.

In step 2(a) - which is the same in $K$-Means and $K$-Medoids:

- 2(a) for $i=1, ⋯, n$
- $C_j = \lbrace \: i \: | \: such \: that \: z^{(j)} \: is \: closest \: to \: x^{(i)} \rbrace$

We need to go through each point and find the closest representative.

So the complexity of the computation is $O$(n•K•d), since we have $n$ points, $K$ representatives, and we multiply by $d$ because our instances - our x's - may be very high dimensional vectors.

**Step 2(b)**

Here, the $K$-Medoids algorithm becomes more expensive than $K$-Means.

$K$-Means:

- $z^{(j)} = \sum{\frac{x^{(i)}}{|C_j|}}$

$K$-Medoids:

- $z^{(j)} ∈ \lbracex^{(1)}, ⋯, x^n \rbrace \: such \: that \: \sum_{x^{(i)}∈C_j} dist(x^{(i)}, z^{(j)}) \: is \: minimal$

For $K$-Medoids at step 2(b), because each point must be compared with the other in the cluster, the complexity becomes $O(n^2•K•d)$.
