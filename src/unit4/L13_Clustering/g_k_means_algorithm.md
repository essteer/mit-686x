# K-Means Algorithm: The Specifics

**K-means clustering algorithm**

1. Randomly select z<sup>(1)</sup> ⋯ z<sup>(K)</sup>

2. Iterate

   - 2(a) Given z<sup>(1)</sup> ⋯ z<sup>(K)</sup>, assign x's to the closest z
   - cost(z<sup>(1)</sup> ⋯, z<sup>(K)</sup>) = Σ<sub>i=1</sub><sup>n</sup> min<sub>j=1⋯K</sub> ∥x<sup>(i)</sup> - z<sup>(j)</sup>∥<sup>2</sup>

   - 2(b) Given C<sub>1</sub> ⋯ C<sub>K</sub>, find the best representatives z
   - cost(C<sub>1</sub>, ⋯, C<sub>K</sub>) = min<sub>z<sup>(1)</sup>⋯z<sup>(K)</sup></sub> Σ<sub>j=1</sub><sup>K</sup> Σ<sub>i∈C<sub>j</sub></sub> ∥x<sup>(i)</sup> - z<sup>(j)</sup>∥<sup>2</sup>

**Gradient**

We need to take the gradient at 2(b), in order to determine what should be computed.

Notice that every cluster selects its representative independently.

So we want to look at a specific cluster, such as cluster j C<sub>j</sub>, and find the representative that will minimise the sum.

Σ<sub>i∈C<sub>j</sub></sub> ∥x<sup>(i)</sup> - z<sup>(j)</sup>∥<sup>2</sup>

We want to find the z<sub>j</sub> that will minimise the sum, so we take the derivative with respect to z, make it equal to 0, and it will tell us about the z.

d/dz<sup>(j)</sup> Σ<sub>i∈C<sub>j</sub></sub> ∥x<sup>(i)</sup> - z<sup>(j)</sup>∥<sup>2</sup> = 0

Through the answer, we discover that the z<sup>(j)</sup> is the centroid of the group.

z<sup>(j)</sup> = Σ x<sup>(i)</sup> / |C<sub>j</sub>|

Note that the computation evaluates to this in the case of square Euclidean distance - for other similarity measures, the result would not be the same.

This form of the algorithm only works if the distance measure being use is square Euclidean distance.

**Iterations**

How do we know how many times to iterate?

We can guarantee that the algorithm converges, and that it converges to a local minimum.

We cannot guarantee it will converge to the global minimum.

Through every iteration, the cost either remains the same, or decreases.

Since the number of partitions is finite, we are guaranteed to converge.

But the convergence is local - starting with a different initialisation, we could arrive at a different partitioning.
