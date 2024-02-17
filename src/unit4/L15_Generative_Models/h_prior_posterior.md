# Prior, Posterior and Likelihood

A limitation of the generative model explored so far, is that it assumes equal probability between the positive and negative classes.

We may have prior knowledge about the respective likelihoods that we want to impart to the model.

**Bayesian rule**

First, recall the Bayesian rule:

$P(A|B) = \frac{P(B|A) • P(A)}{P(B)}$

**Likelihood with generative models**

What is the likelihood, given document $D$, that we will give it a positive label?

$P(y=+|D)$

We can rewrite this expression as:

$P(y=+|D) = \frac{P(D|θ^+) • P(y=+)}{P(D)}$

The $P(y=+)$ is typically known as the prior - it is the probability of e.g., an email being spam before we look at any features of a particular email.

The $P(y=+|D)$ is the posterior - the probability of the document we have observed, given that it is positive.

**Connecting to linear classification**

We again take the log:

$log \frac{P(y=+|D)}{P(y=-|D)} = log \frac{P(D|θ^+) • P(y=+)}{P(D|θ^-) • P(y=-)}$

The probability of the document $D$ is cancelled away.

We can then separate this expression into the prior and posterior parts.

$= log \frac{P(D|θ^+)}{P(D|θ^-)} + log \frac{P(y=+)}{P(y=-)}$

Then, substituting our previous calculation in for the posterior part, and substituting $θ_0^{\prime}$ for the prior part:

$= \sum_{w∈W} count(w) • θ_w^{\prime}$

So, we have again translated it into a linear classifier, but in contrast to the previous case where we had a linear classifier through the origin, now we have a linear classifier with an offset, and the offset is driven by the priors, which will drive the location of the separator.

We can therefore easily incorporate our prior knowledge about the likelihood of the different classes.
