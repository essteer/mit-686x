# Introduction to Mixture Models

Mixture models are useful for describing many real-life scenarios.

The Gaussian model examined so far assumed just one cluster, but many situations will exhibit multiple clouds of data that belong to different Gaussian distributions.

We can do more refined modeling if our generative model can allow more than one cluster.

Mixture models assume several mixture components, each one of which is a Gaussian.

If $K$ is the size of the mixture model, we assume that each Gaussian is represented by its own private $\mu^{(j)}$ and $\sigma_j^2$.

$K: N(x, \mu^{(j)}, \sigma_j^2), j=1,⋯,K$

For a two-Gaussian example, there would be two components, with $j$ going from $1$ to $2$, and each would have its own mean and variance.

Recall that with clustering there were several clusters, with representatives for each.

Here we examine not only the mean of the cluster, but also the variance, and a new measure of how large the cluster is.

Therefore, in addition to mixture components, we also take mixture weights.

The sum of those probability weights goes to $1$, so it is a multinomial:

$p_1,⋯,p_K, \sigma_{j=1}^K \: p_j = 1$

**Application**

We can think of the process of generating a point with this mixture model as a two-step process.

In the first step, we roll the dice and decide which one of the mixture components was used to generate the point.

We draw from the multinomial when selecting a particular cluster:

$j$ ~ $Multinomial(p_1,⋯,p_K)$

Then, once the cluster has been selected, it means its mean and variance have been selected:

$X$ ~ $P(x|\mu^{(j)}, \sigma_{j}^2)$

So:

- we have a die;
- we roll the die;
- we find a Gaussian;
- we draw from the Gaussian according to its own parameters - a generation step.

This is known as a "soft" clustering model.

For every point, it could be generated from any of the clusters, just with differing probabilities due to the respective means and variances.

Our parameter $θ$ would contain all the mixture weights, means, and variances:

$θ: p_1,⋯,p_K, \mu^{(1)},⋯,\mu^{(K)}, \sigma_{1}^2,⋯,\sigma_{K}^2$

**Likelihood**

The likelihood of a point $x$ in the GMM is then:

$p(x|θ) = \sigma_{j=1}^K p_j N(x, \mu^{(j)}, \sigma_{j}^2)$

The generative model can be thought of first selecting the component $j ∈ \lbrace 1,⋯,K \rbrace$, which is modeled using the multinomial distribution with parameters $p_1,⋯,p_K$, and then selecting a point from the Gaussian component $N(\mu^{(j)}, \sigma_{j}^2)$.
