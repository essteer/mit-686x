# MLE for Multinomial and Gaussian Models

So far we have examined two forms of distribution: multinomials and Gaussians.

**Multinomials**

We have some set of probable outcomes - if talking about language, it could be the vocabulary, _W_. (Another example could be a six-sided die, with probabilities for the roll outcomes from that die.)

We assume a certain likelihood to generate a particular word _w_ from this vocabulary; and the sum of the parameters must be 1, since it is a probability distribution.

P(w|θ) = θ<sub>w</sub>; Σ<sub>w∈W</sub> θ<sub>w</sub> 1, θ<sub>w</sub> >= 0

Given this multinomial, we can compute the likelihood of a given document _D_.

Since all the words in D are generated independently of each other, the likelihood of D is the product of all of the θ's. We go through each word in the vocabulary and look at how many times each would appear, and multiply the θ's accordingly to get the likelihood of D.

P(D|θ) = Π<sub>w∈W</sub> θ<sub>w</sub><sup>n(w)</sup>

**Gaussians**

We can think of Gaussians in terms of the geometric view, with μ at the centre of the data cloud, and the variance given by σ<sup>2</sup>, where σ is the radius of the data cloud.

We can then look at the probability of a given point x to be generated by a given Gaussian:

P(x|μ, σ<sup>2</sup>)

This may also be expressed with the following notation:

P(x|μ, σ<sup>2</sup>) = N(x, μ, σ<sup>2</sup>I) = 1 / (2πσ<sup>2</sup>)<sup>d/2</sup> exp<sup>(-(1/(2σ<sup>2</sup>))∥x - μ∥<sup>2</sup>)</sup>

The points located further from the centre will have lower probability than the points closer to the centre.

**Questions related to these distributions**

Taking the multinomial and Gaussian distributions, the first question to then ask is how we estimate the parameters - θ in the former case, and μ and σ<sup>2</sup> in the latter.

The criterion we use is Maximum Likelihood Estimator. Given some document _D_, we are looking for the parameters that give the highest likelihood of observing our data.

In the case of Gaussians, we demonstrated that the estimated μ would simply be the mean of all the points.

μ^ = 1/n Σ<sub>i=1</sub><sup>n</sup> x<sup>(i)</sup>

σ<sup>2</sup>^ = 1/nd Σ<sub>i=1</sub><sup>n</sup> ∥x - μ∥<sup>2</sup>
