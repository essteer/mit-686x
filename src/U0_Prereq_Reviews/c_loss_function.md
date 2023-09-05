# Loss Function

**Loss function**: a way to value how far our model is from the data we have.

_y^ = ϴ1x + ϴ2_

- x is an input value
- ϴ1 and ϴ2 are parameters
- We want to "learn" ϴ1 and ϴ2, to predict y.

**Error measurement**

One way to measure error is to take the vertical distance between our prediction for y^, and the true value for y observed.

_y^ - yi_

Our loss function will be simply the vertical distance between y^i and yi:

_L(xiyiϴ)_ = _(1/n n Σ i=1) |y^ - y|_ = _1/n Σ |ϴ1x + ϴ2 - y|_

We want to minimise the loss function; at that point, our model best describes the data.

Doing so can be complex.

The most common means to achieve it is to use an iterative algorithm, **gradient descent**.

**Gradient descent**

- Given a point, we compute the gradient - the derivative of the function for that point.
- We want to move against the direction of the gradient.

New value for ϴ = old value - some gamma (γ) times the gradient (∇ϴ) of the loss function:
_ϴ^ = ϴ - γ ∇ϴ L(x1yiϴ)_

The gamma (γ) is the learning rate.

- If gamma is high, we may dart around the curve.
- If gamma is very small, we may converge slowly on the optimum - but could also be more prone to becoming stuck in a local minimum.

## Example with Chain Rule

We have a model which is:
_y^ = 1 / (1 + e^-(ϴ1x + ϴ2))_

- We want to derive it in terms of ϴ1.

The **chain rule** tells us that if we have a function we would like to derive according to x, _dy / dx_:

_dy/dx_ = _dy/dz • dz/dx_

Applied to our model:

_dy^/dϴ1_ = _dy^/dz • dz/dϴ1_

What is the _z_ of _dz_?

1. We define it to be the _z = ϴ1x + ϴ2_ part of the equation.

- We now have a linear function.

2. Our model takes in _x_, to which we apply a linear transformation to get _z_.
3. We then apply our sigmoid function to _z_ to get our prediction, _y^_.

4. We then just need to solve _dy^/dϴ1_ = _dy^/dz • dz/dϴ1_ to a derivative.

- _dz/dϴ1_ = _x_
- _dy^/dz_ = _d/dz_ _1/(1+e^-z)_ (sigmoid function)
- = _e^-z / (1 + e^z)^2_ (the derivative)

Applying the chain rule:

_dy^/dϴ1_ = _x • e^-z / (1 + e^z)^2_

- Plug in our value of _z = ϴ1x + ϴ2_ to get the derivative.

For _ϴ2_:

- _dy^/dϴ2_ = _e^-z / (1 + e^z)^2_
