# Loss Function

**Loss function**: a way to value how far our model is from the data we have.

$\hat{y} = \theta_1x + \theta_2$

- $x$ is an input value
- $\theta_1$ and $\theta_2$ are parameters
- We want to "learn" $\theta_1$ and $\theta_2$, to predict $y$.

**Error measurement**

One way to measure error is to take the vertical distance between our prediction for $\hat{y}$, and the true value for $y$ observed.

$\hat{y} - y_i$

Our loss function will be simply the vertical distance between $\hat{y}_i$ and $y_i$:

$L(x_iy_iθ) = \frac{1}{n} \sum_{i=1}^{n} |\hat{y} - y| = \frac{1}{n} \sum{|\theta_1x + \theta_2 - y|}$

We want to minimise the loss function; at that point, our model best describes the data.

Doing so can be complex.

The most common means to achieve it is to use an iterative algorithm, **gradient descent**.

**Gradient descent**

- Given a point, we compute the gradient - the derivative of the function for that point.
- We want to move against the direction of the gradient.

New value for $θ$ = old value - some gamma ($γ$) times the gradient ($∇_θ$) of the loss function:
$θ^{\prime} = θ - γ ∇_θ L(x_1 y_i θ)$

The gamma ($γ$) is the learning rate.

- If gamma is high, we may dart around the curve.
- If gamma is very small, we may converge slowly on the optimum - but could also be more prone to becoming stuck in a local minimum.

## Example with Chain Rule

We have a model which is:
$\hat{y} = \frac{1}{1 + e^{-(\theta_1x + \theta_2)}}$

- We want to derive it in terms of $\theta_1$.

The **chain rule** tells us that if we have a function we would like to derive according to $x$, $\frac{\partial{y}}{\partial{x}}$:

$\frac{\partial{y}}{\partial{x}}$ = $\frac{\partial{y}}{\partial{z}} • \frac{\partial{z}}{\partial{x}}$

Applied to our model:

$\frac{\partial{\hat{y}}}{\partial{\theta_1}} = \frac{\partial{\hat{y}}}{\partial{z}} • \frac{\partial{z}}{\partial{\theta_1}}$

What is the $z$ of $\partial{z}$?

1. We define it to be the $z = \theta_1x + \theta_2$ part of the equation - and now have a linear function.
2. Our model takes in $x$, to which we apply a linear transformation to get $z$.
3. We then apply our sigmoid function to $z$ to get our prediction, $\hat{y}$.
4. We then just need to solve $\frac{\partial{\hat{y}}}{\partial{\theta_1}} = \frac{\partial{\hat{y}}}{\partial{z}} • \frac{\partial{z}}{\partial{\theta_1}}$ to a derivative.

$\frac{\partial{z}}{\partial{\theta_1}} = x$

$\frac{\partial{\hat{y}}}{\partial{z}} = \frac{d}{\partial{z}} \frac{1}{1+e^{-z}}$ (sigmoid function)

$= \frac{e^{-z}}{1 + e^{z^2}}$ (the derivative)

Applying the chain rule:

$\frac{\partial{\hat{y}}}{\partial{\theta_1}} = x • \frac{e^{-z}}{1 + e^{z^2}}$

- Plug in our value of $z = \theta_1x + \theta_2$ to get the derivative.

For $\theta_2$:

- $\frac{\partial{\hat{y}}}{d\theta_2} = \frac{e^{-z}}{1 + e^{z^2}}$
