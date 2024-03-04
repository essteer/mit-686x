# Estimating the Parameters in the Observed Case

$p(S_n|θ) = \prod\nolimits_{i=1}^{n} \sum\nolimits_{j=1}^{K} p_j N(x, \mu^{(j)}, \sigma_{j}^2 I)$

The next question we must address is how we can find all of the parameters we are interested in - the mixture weights, mean and variance for each mixture component.

The simple case is to start with an example for which we know to which cluster belongs - the observed case.

The notation is more complex than it could be, but this is to facilitate direct translation to the more complex unobserved case.

**Observed case**

The first piece of notation tells us that this is an indicator function, which would be equal to $1$ when we know that point $x^{(i)}$ is assigned to mixture component $j$, and zero otherwise.

$δ(j|i) = \lbrace 1, x^{(i)} assigned ~ to ~ j; 0, otherwise \rbrace$

Since this is the observed case, for every point $i$, there will be just one $j$ to which it belongs.

We then use this notation to rewrite the likelihood expression at the top of this page.

Recall we are trying to find $p$, $\mu$, and $\sigma^2$.

We take the likelihood expression and log it so that it becomes a sum.

$\sigma_{i=1}^n$

Then, we go through each point and look at which cluster it belongs to:

$\sigma_{i=1}^n [ \sigma_{j=1}^K ]$

Within that cluster, we take only points that are hard-assigned to that cluster:

$\sigma_{i=1}^n [ \sigma_{j=1}^K δ (j|i) \log p_j N(x^{(i)}, \mu^{(j)}, \sigma_{j}^2 I) ]$

We then change the summation, since we can change the computation to instead of going through points and then clusters, we independently do the computation for each individual cluster.

$= \sigma_{j=1}^K [ \sigma_{i=1}^n \log p_j N(x^{(i)}, \mu^{(j)}, \sigma_{j}^2 I) ]$

Whenever we try to find the parameters that optimise for each mixture component, we can do this computation for each cluster independently.

Due to the fact that the points are observed, we already know to which cluster they belong. We can therefore separately find the mean and variance.

**Computing quantities**

First, compute how many members belong to each cluster using the delta notation:

${\hat{n}}_{j}$ is the number of points that belong to cluster $j$.

${\hat{n}}_{j} = \sigma_{i=1}^n δ(j|i)$

For all the points that belong to cluster $j$, and only for those points, this would be equal to $1$.

We can then compute the parameter for the mixture weights of cluster $j$ using MLE:

$\hat{p}_{j} = \frac{\hat{n}_{j}}{n}$

The result is intuitive: $\hat{p}_{j}$ is the number of points in the cluster $j$, divided by the total number of points. This is the weight for the mixture component $j$.

Similarly, we can compute the mean of cluster $j$; differentiating the likelihood expression with respect to $\mu$ would find a similar shape as with the case of individual Gaussians - we sum up all of the points and divide by the size of the cluster.

In this particular case, we get the sum of all the points that belong to this cluster, going through all of the points from $1$ to $n$, and divided by the size of the cluster:

$\hat{\mu}^{(j)} = \frac{1}{ \hat{n}_{j} } \sigma_{i=1}^n δ(j|i) • x^{(i)}$

This would be our MLE for the centre of the component $\lbrace j \rbrace$.

We then need to compute the variance.

$\hat{\sigma}_{j}^2 = \frac{1}{\hat{n}_{jd}} \sigma_{i=1}^n δ(j|i) • ∥x^{(i)} - \mu^{(j)}∥^2$

Once again, the indicator function serves the purpose of ensuring that the point being selected really belongs to this specific cluster.
