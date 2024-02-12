# Gradient Descent

Plotting a curve of the objective function $J(θ)$ against $θ$, where $θ ∈ ℝ$, we begin with an arbitrary value of $θ$.

We try to change the parameter value $θ$, to get closer to the minimum of the function (i.e., the optimum).

At any point, we can compute the slope of the function, given by:

- $\frac{∂J(θ)}{∂(θ)}$ - i.e., the derivative of the objective function $J(θ)$ with respect to the parameter value $θ$.

If that slope is positive, and we move in the same direction of the function, we will increase the function.

If we move in the opposite direction of the function, we will decrease the function.

So, our gradient descent update rule is that we take a new parameter value $θ$ in terms of the old $θ$, by moving in a negative direction of the derivative of the gradient of the function $\frac{∂J(θ)}{∂(θ)}$.

**Step size / learning rate: $η$**

We also include a step size (or learning rate) parameter, $η$.

The purpose of $η$ is to avoid taking too large a step, that would result in a larger value of $θ$ than our current value for this parameter.

**Multi-dimensional case**

For multi-dimensional cases, e.g. with $θ_1$ and $θ_2$, we are trying to get to the minimum of the (here) bowl-shaped function.

We then move each of the parameters $θ_j$, exactly as before when the function was a function of only a single scalar.

With respect to each of the parameters, we move in the negative direction of the derivative of the function with respect to that particular parameter.

**In vector form**

For all coordinates of $θ$, now as a vector, we are updating by taking the old vector and moving in the opposite direction of the gradient with respect to the parameters:

- $θ_j ← θ - η∇J(θ)$

This gradient is simply a concatenation of individual derivatives with respect to the parameters, e.g.:

- $∇J(θ) = [\frac{∂J(θ)}{∂(θ)_1}, ⋯, \frac{∂J(θ)}{∂(θ_d)}]$ (for $d$ coordinates in $θ$)
