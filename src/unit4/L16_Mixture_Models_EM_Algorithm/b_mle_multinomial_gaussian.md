# MLE for Multinomial and Gaussian Models

So far we have examined two forms of distribution: multinomials and Gaussians.

**Multinomials**

We have some set of probable outcomes - if talking about language, it could be the vocabulary, $W$. (Another example could be a six-sided die, with probabilities for the roll outcomes from that die.)

We assume a certain likelihood to generate a particular word $w$ from this vocabulary; and the sum of the parameters must be $1$, since it is a probability distribution.

$P(w|θ) = θ_w; \sum_{w∈W} θ_w 1, θ_w \geq 0$

Given this multinomial, we can compute the likelihood of a given document $D$.

Since all the words in $D$ are generated independently of each other, the likelihood of $D$ is the product of all of the $θ$'s. We go through each word in the vocabulary and look at how many times each would appear, and multiply the $θ$'s accordingly to get the likelihood of $D$.

$P(D|θ) = \prod_{w∈W} θ_w^{n(w)}$

**Gaussians**

We can think of Gaussians in terms of the geometric view, with $\mu$ at the centre of the data cloud, and the variance given by $\sigma^2$, where $\sigma$ is the radius of the data cloud.

We can then look at the probability of a given point $x$ to be generated by a given Gaussian:

$P(x|\mu, \sigma^2)$

This may also be expressed with the following notation:

$P(x|\mu, \sigma^2) = N(x, \mu, \sigma^2I) = \frac{1}{(2 \pi \sigma^2)^{d \over 2}} \exp^{- \frac{1}{2 \sigma^2}∥x - \mu∥^2}$

The points located further from the centre will have lower probability than the points closer to the centre.

**Questions related to these distributions**

Taking the multinomial and Gaussian distributions, the first question to then ask is how we estimate the parameters - $θ$ in the former case, and $\mu$ and $\sigma^2$ in the latter.

The criterion we use is Maximum Likelihood Estimator. Given some document $D$, we are looking for the parameters that give the highest likelihood of observing our data.

In the case of Gaussians, we demonstrated that the estimated \mu would simply be the mean of all the points.

$\hat{\mu} = \frac{1}{n} \sigma_{i=1}^n x^{(i)}$

$\hat{\sigma}^2 = \frac{1}{nd} \sigma_{i=1}^n ∥x - \mu∥^2$
