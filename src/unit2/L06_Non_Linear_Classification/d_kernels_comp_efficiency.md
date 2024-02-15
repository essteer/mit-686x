# Motivation for Kernels: Computational Efficiency

Computing the inner products of vectors can be cheap, even if the vectors are high-dimensional.

$\phi(x) = [x_1, x_2, x_1^2, \sqrt{2} x_1x_2, x_2^2]^T$

$\phi(x') = [x_1^{\prime}, x_2^{\prime}, x_1^{\prime 2}, \sqrt{2} x_1^{\prime} x_2^{\prime}, x_2^{\prime 2}]^T$

**Evaluating the inner products of these two feature vectors**

The first part, consisting of monomials only ($[x_1, x_2]$ and $[x_1^{\prime}, x_2^{\prime}]$) evaluates to:

$\phi(x) • \phi(x^{\prime}) = (x • x^{\prime})$

The inner product of the remaining parts is a quadratic expression, and becomes $(x • x^{\prime})$ plus the scalar value to the power of $2$: $(x • x^{\prime})^2$:

$\phi(x) • \phi(x^{\prime}) = (x • x^{\prime}) + (x • x^{\prime})^2$

If we added third order terms, we could just add a further $x$ and $x^{\prime}$ product term to the power of $3$, and so on:

$\phi(x) • \phi(x^{\prime}) = (x • x^{\prime}) + (x • x^{\prime})^2 + (x • x^{\prime})^3$

The computation therefore does not become more complicated, even despite the number of feature vectors added by moving from order $2$ to order $3$.

This is function is known as a **kernel function**. Kernel functions always correspond to inner products between some feature vectors.

$K(x, x^{\prime}) = \phi(x) • \phi(x^{\prime}) = (x • x^{\prime}) + (x • x^{\prime})^2 + (x • x^{\prime})^3$

**Kernels vs features**

For some feature maps, the inner product can be evaluated very cheaply, e.g. an any-order polynomial feature transformation:

$K(x, x^{\prime}) = \phi(x) • \phi(x^{\prime}) = (1 + x • x^{\prime})^P, P = 1, 2, ⋯$

In those cases, it is advantageous to express the linear classifiers (regression methods) in terms of kernels rather than explicitly constructing feature vectors.

**Application**

The task is then to turn our linear model, e.g. $sign(θ• \phi(x) + θ_0)$, into a classifier that only depends on the inner products.

Kernel perceptron is one example of how this can be done.
