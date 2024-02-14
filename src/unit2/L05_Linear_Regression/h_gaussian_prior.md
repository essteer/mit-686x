# Equivalance of regularization to a Gaussian Prior on Weights

The regularized linear regression can be interpreted from a probabilistic point of view.

Suppose we are fitting a linear regression model with n data points $(x_1, y_1), (x_2, y_2), ⋯, (x_n, y_n)$. Let's assume the ground truth is that $y$ is linearly related to $x$ but we also observed some noise for $ε$:

$y_i = θ•x_i + ε$

where $ε ~ N (0, σ^2)$

Then the likelihood of our observed data is

$Π_{i=1}^n N (y_i|θ•x_i, σ^2)$

Now, if we impose a Gaussian prior $N (θ|0,\hat{λ}-1)$, the likelihood will change to

$Π_{i=1}^n N (y_i|θ•x_i, σ^2) N (θ|0,\hat{λ}-1)$

Take the logarithim of the likelihood, we will end up with

$Σ_{i=1}^n - \frac{1}{2σ^2}(y_i - θ•x_i)^2 - \frac{1}{2} λ∥θ∥^2 + constant$
