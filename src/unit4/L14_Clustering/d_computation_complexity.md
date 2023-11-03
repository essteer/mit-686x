# Computation Complexity of K-Means and K-Medoids

Comparing the differences between K-Means and K-Medoids, we can see that K-Medoids is more expensive than K-Means.

We don't know how many steps each algorithm will take to find the best partitioning, but we can look at the cost of one iteration of each algorithm.

**Step 2(a)**

For an iteration of each algorithm at step 2(a), we can see the complexity _O_(n•K•d) where _n_ is the number of data points, _K_ is the number of clusters, and _d_ is the size of the clusters.

In step 2(a) - which is the same in K-Means and K-Medoids:

- 2(a) for i = 1, ⋯, n
- C<sub>j</sub> = { i | such that z<sup>(j)</sup> is closest to x<sup>(i)</sup> }

We need to go through each point and find the closest representative.

So the complexity of the computation is _O_(n•K•d), since we have _n_ points, _K_ representatives, and we multiply by _d_ because our instances - our x's - may be very high dimensional vectors.

**Step 2(b)**

Here, the K-Medoids algorithm becomes more expensive than K-Means.

K-Means:

- z<sup>(j)</sup> = Σ x<sup>(i)</sup> / |C<sub>j</sub>|

K-Medoids:

- z<sup>(j)</sup> ∈ {x<sup>(1)</sup> ⋯ x<sup>n</sup>} such that Σ<sub>x<sup>(i)</sup>∈C<sub>j</sub></sub> dist(x<sup>(i)</sup>, z<sup>(j)</sup>) is minimal

For K-Medoids at step 2(b), because each point must be compared with the other in the cluster, the complexity becomes _O_(n<sup>2</sup>•K•d)
