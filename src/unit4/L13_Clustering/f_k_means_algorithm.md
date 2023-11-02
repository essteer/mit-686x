# K-Means Algorithm: The Big Picture

cost(C<sub>1</sub>, ⋯, C<sub>K</sub>, ⋯, z<sup>(1)</sup>, z<sup>(K)</sup>) = Σ<sub>j=1</sub><sup>K</sup> Σ<sub>i∈C<sub>j</sub></sub> ∥x<sup>( i )</sup> - z<sup>( j )</sup>∥<sup>2</sup>

We have the cost, and we need to find a way to find the best partitioning, and the best representatives.

If we have a number of points, how many distinct partitions of size K can we produce?

This is exponential in the number of points, so we can't go one partition at a time, check the cost, then go on to the next one. The search space of partitions is too large, so we need an algorithm to tell us how to get to the right partition.

**K-means clustering**

The algorithm will take a whole space of points, and then randomly assign the representatives.

Then the representatives will draw to themselves those points which are closest to them.

There will then be multiple clouds, one for each representative. Once these clouds emerge, we may decide up new representatives that better reflect those clouds.

After the representatives are reassigned, we may redraw the partitions, and then continue in this manner until convergence.

**K-means clustering algorithm**

1. Randomly select z<sup>(1)</sup> ⋯ z<sup>(K)</sup>

2. Iterate

   - 2(a) Given z<sup>(1)</sup> ⋯ z<sup>(K)</sup>, assign x's to the closest z
   - cost(z<sup>(1)</sup> ⋯, z<sup>(K)</sup>) = Σ<sub>i=1</sub><sup>n</sup> min<sub>j=1⋯K</sub> ∥x<sup>(i)</sup> - z<sup>(j)</sup>∥<sup>2</sup>

   - 2(b) Given C<sub>1</sub> ⋯ C<sub>K</sub>, find the best representatives z
   - cost(C<sub>1</sub>, ⋯, C<sub>K</sub>) = min<sub>z<sup>(1)</sup>⋯z<sup>(K)</sup></sub> Σ<sub>j=1</sub><sup>K</sup> Σ<sub>i∈C<sub>j</sub></sub> ∥x<sup>(i)</sup> - z<sup>(j)</sup>∥<sup>2</sup>
