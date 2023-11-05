# Estimating the Parameters in the Observed Case

p(S<sub>n</sub>|θ) = Π<sub>i=1</sub><sup>n</sup>Σ<sub>j=1</sub><sup>K</sup> p<sub>j</sub> N(x, μ<sup>(j)</sup>, σ<sup>2</sup><sub>j</sub>_I_)

The next question we must address is how we can find all of the parameters we are interested in - the mixture weights, mean and variance for each mixture component.

The simple case is to start with an example for which we know to which cluster belongs - the observed case.

The notation is more complex than it could be, but this is to facilitate direct translation to the more complex unobserved case.

**Observed case**

The first piece of notation tells us that this is an indicator function, which would be equal to 1 when we know that point x<sup>(i)</sup> is assigned to mixture component j, and zero otherwise.

δ(j|i) = {1, x<sup>(i)</sup> is assigned to j; 0, otherwise}

Since this is the observed case, for every point i, there will be just one j to which it belongs.

We then use this notation to rewrite the likelihood expression at the top of this page.

Recall we are trying to find p, μ, and σ<sup>2</sup>.

We take the likelihood expression and log it so that it becomes a sum.

Σ<sub>i=1</sub><sup>n</sup>

Then, we go through each point and look at which cluster it belongs to:

Σ<sub>i=1</sub><sup>n</sup> [ Σ<sub>j=1</sub><sup>K</sup> ]

Within that cluster, we take only points that are hard-assigned to that cluster:

Σ<sub>i=1</sub><sup>n</sup> [ Σ<sub>j=1</sub><sup>K</sup> δ(j|i) log p<sub>j</sub> N(x<sup>(i)</sup>, μ<sup>(j)</sup>, σ<sup>2</sup><sub>j</sub>_I_) ]

We then change the summation, since we can change the computation to instead of going through points and then clusters, we independently do the computation for each individual cluster.

= Σ<sub>j=1</sub><sup>K</sup> [ Σ<sub>i=1</sub><sup>n</sup> log p<sub>j</sub> N(x<sup>(i)</sup>, μ<sup>(j)</sup>, σ<sup>2</sup><sub>j</sub>_I_) ]

Whenever we try to find the parameters that optimise for each mixture component, we can do this computation for each cluster independently.

Due to the fact that the points are observed, we already know to which cluster they belong. We can therefore separately find the mean and variance.

**Computing quantities**

First, compute how many members belong to each cluster using the delta notation:

n^<sub>j</sub> is the number of points that belong to cluster j.

n^<sub>j</sub> = Σ<sub>i=1</sub><sup>n</sup> δ(j|i)

For all the points that belong to cluster j, and only for those points, this would be equal to 1.

We can then compute the parameter for the mixture weights of cluster j using MLE:

p^<sub>j</sub> = n^<sub>j</sub> / n

The result is intuitive: p^<sub>j</sub> is the number of points in the cluster j, divided by the total number of points. This is the weight for the mixture component j.

Similarly, we can compute the mean of cluster j; differentiating the likelihood expression with respect to μ would find a similar shape as with the case of individual Gaussians - we sum up all of the points and divide by the size of the cluster.

In this particular case, we get the sum of all the points that belong to this cluster, going through all of the points from 1 to n, and divided by the size of the cluster:

μ^<sup>(j)</sup> = 1/n^<sub>j</sub> Σ<sub>i=1</sub><sup>n</sup> δ(j|i) • x<sup>(i)</sup>

This would be our MLE for the centre of the component j.

We then need to compute the variance.

σ<sup>2</sup><sub>j</sub>^ = 1/n^<sub>j</sub>d Σ<sub>i=1</sub><sup>n</sup> δ(j|i) • ∥x<sup>(i)</sup> - μ<sup>(j)</sup>∥<sup>2</sup>

Once again, the indicator function serves the purpose of ensuring that the point being selected really belongs to this specific cluster.
