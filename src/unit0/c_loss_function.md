# Loss Function

**Loss function**: a way to value how far our model is from the data we have.

_y^ = θ1x + θ2_

- x is an input value
- θ1 and θ2 are parameters
- We want to "learn" θ1 and θ2, to predict y.

**Error measurement**

One way to measure error is to take the vertical distance between our prediction for y^, and the true value for y observed.

_y^ - yi_

Our loss function will be simply the vertical distance between y^i and yi:

_L(xiyiθ)_ = _(1/n n Σ i=1) |y^ - y|_ = _1/n Σ |θ1x + θ2 - y|_

We want to minimise the loss function; at that point, our model best describes the data.

Doing so can be complex.

The most common means to achieve it is to use an iterative algorithm, **gradient descent**.

**Gradient descent**

- Given a point, we compute the gradient - the derivative of the function for that point.
- We want to move against the direction of the gradient.

New value for θ = old value - some gamma (γ) times the gradient (∇θ) of the loss function:
_θ^ = θ - γ ∇θ L(x1yiθ)_

The gamma (γ) is the learning rate.

- If gamma is high, we may dart around the curve.
- If gamma is very small, we may converge slowly on the optimum - but could also be more prone to becoming stuck in a local minimum.

## Example with Chain Rule

We have a model which is:
_y^ = 1 / (1 + e^-(θ1x + θ2))_

- We want to derive it in terms of θ1.

The **chain rule** tells us that if we have a function we would like to derive according to x, _dy / dx_:

_dy/dx_ = _dy/dz • dz/dx_

Applied to our model:

_dy^/dθ1_ = _dy^/dz • dz/dθ1_

What is the _z_ of _dz_?

1. We define it to be the _z = θ1x + θ2_ part of the equation.

- We now have a linear function.

2. Our model takes in _x_, to which we apply a linear transformation to get _z_.
3. We then apply our sigmoid function to _z_ to get our prediction, _y^_.

4. We then just need to solve _dy^/dθ1_ = _dy^/dz • dz/dθ1_ to a derivative.

- _dz/dθ1_ = _x_
- _dy^/dz_ = _d/dz_ _1/(1+e^-z)_ (sigmoid function)
- = _e^-z / (1 + e^z)^2_ (the derivative)

Applying the chain rule:

_dy^/dθ1_ = _x • e^-z / (1 + e^z)^2_

- Plug in our value of _z = θ1x + θ2_ to get the derivative.

For _θ2_:

- _dy^/dθ2_ = _e^-z / (1 + e^z)^2_
