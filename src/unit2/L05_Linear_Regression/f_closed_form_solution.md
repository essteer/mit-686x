# Closed Form Solution

For most machine learning algorithms, there is no closed form solution, but in the case of our linear regression with empirical risk function, there is.

$R_n(θ) = \frac{1}{n} \sum\nolimits_{i=1}^{n} \frac{(y^{(i)} - θ•x^{(i)})^2}{2}$

$`\nabla_{θ} R_{n} (θ)_{| θ = \hat{θ}} = \frac{1}{n} \sum\nolimits_{i=1}^{n} \nabla_{θ} \frac{(y^{(i)} - θ•x^{(i)})^2}{2} _{|θ=\hat{θ}}`$

$= - \frac{1}{n} \sum\nolimits_{i=1}^{n} (y^{(i)} - θ•x^{(i)})x^{(i)}$

We then take the sum, and break it into two parts:

$= - \frac{1}{n} \sum\nolimits_{i=1}^{n} y^{(i)}x^{(i)}$

This is a vector of dimensionality $d$, which we denote as $b$

$- \frac{1}{n} \sum\nolimits_{i=1}^{n} \hat{θ}•x^{(i)}x^{(i)}$

Since the result of a dot product is a number, we can move this around as:

$\frac{1}{n} \sum\nolimits_{i=1}^{n} x^{(i)} \hat{θ}•x^{(i)}$

Putting it together:

$= - b + \frac{1}{n} \sum\nolimits_{i=1}^{n} x^{(i)} \hat{θ}•x^{(i)}$

Because $\hat{θ}•x^{(i)}$ is a scalar, when we take a transpose of it, it is equal to itself.

$= - b + \frac{1}{n} \sum\nolimits_{i=1}^{n} x^{(i)} (x^{(i)})^T\hat{θ}$

Since each $x$ is a vector of dimension $d$, we get a matrix of dimension $d \times d$, which we denote as $A$:

$= - b + A\hat{θ} = 0$

∴ $A\hat{θ} = b$, which is what we seek to solve.

If our matrix is invertible, then in this case we can write:

$\hat{θ} = \hat{A}-1b$

**Two caveats**

1. We do not always know that $A$ is invertible, so we cannot always perform this operation.

It is only invertible if $x^{(1)}, ⋯, x^{(n)}$ spans $ℝ^d$.

This happens if the number of training examples, $n$, is substantially larger than the dimensionality of the feature vector $d$.

If we don't have enough training examples from a big dataset, we can't do this operation.

2. Even if we can do the operation, the second issue is the cost associated with it.

The operation is in the order of $d^3$: $O(d^3)$, so the cost is significant.
