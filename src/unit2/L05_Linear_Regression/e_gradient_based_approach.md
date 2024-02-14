# Gradient-based Approach

The empirical risk function is differentiable everywhere.

$R_n(θ) = \frac{1}{n} Σ_{i=1}^n \frac{(y^{(i)} - θx^{(i)})^2}{2}$

$R_n' (θ) = \frac{1}{n'} Σ_{i=n+1}^{n+n'} \frac{(y^{(i)} - θx^i)^2}{2}$

We randomly select one example, then look at the direction of the gradient.

Since we are trying to minimise, we will slightly nudge the parameters in the correct direction (the correct direction being determined by the gradient).

$∇_θ \frac{(y^{(i)} - θ•x^{(i)})^2}{2} = (y^{(i)} - θ•x^{(i)}) ∇_θ (y^{(i)} - θ•x^{(i)}) = - (y^{(i)} - θ•x^{(i)}) • x^{(i)}$

**Algorithm**

1. initialise $θ = 0$
2. randomly pick some example $i$ from $1$ to $n$ $(i = \{1, ⋯, n\})$
3. update theta $θ = θ + η (y^{(i)} - θ•x^{(i)}) • x^{(i)}$

where $η_k = \frac{1}{1 + k}$

**Note 1**

Note a difference with the classification model, that here we will correct at every step where there is some discrepancy.

We are not just examining whether there is a mistake, but how much of a mistake there is.

If the values are far apart, we correct more.
If the values are close, we correct less.

**Note 2**

The algorithm is to an extent self-correcting.

For example, if our prediction was smaller than the true value $y$, then the update expression would be positive and we would be pushing in the positive direction of point $x$.

$y^{(i)} > x^{(i)}$
