# Stochastic Gradient Descent

`J(θ, θ`<sub>`0`</sub>`) =`

`1/n Σ`<sup>`n`</sup><sub>`i=1`</sub>` Loss`<sub>`h`</sub>`(y`<sup>`(i)`</sup>`(θ•x`<sup>`(i)`</sup>` + θ`<sub>`0`</sub>`)) + λ/2∥θ∥`<sup>`2`</sup>

An average of the training losses, plus the regularisation term.

We can write the regularisation term **inside the average**, since it doesn't depend on the training examples, so any average over the regularisation term will return the same thing.

`J(θ, θ`<sub>`0`</sub>`) = 1/n Σ`<sup>`n`</sup><sub>`i=1`</sub>` [Loss`<sub>`h`</sub>`(y`<sup>`(i)`</sup>`(θ•x`<sup>`(i)`</sup>` + θ`<sub>`0`</sub>`)) + λ/2∥θ∥`<sup>`2`</sup>`]`

We can then further simplify the expression by omitting the offset parameter, θ<sub>0</sub>:

`J(θ) = 1/n Σ`<sup>`n`</sup><sub>`i=1`</sub>` [Loss`<sub>`h`</sub>`(y`<sup>`(i)`</sup>`(θ•x`<sup>`(i)`</sup>`)) + λ/2∥θ∥`<sup>`2`</sup>`]`

We now have an average of simpler objective functions:

`1/n Σ`<sup>`n`</sup><sub>`i=1`</sub>` J`<sub>`i`</sub>`(θ)`

This contains a simplified loss function, plus the regularisation term.

**Applying stochasticity**

Since the objective function is actually an average of expectation over the individual terms, we can update the parameters stochastically by taking each individual term individually, **with training examples sampled at random**, to get each individual objective function, and not the parameters in the direction that optimise that particular term.

On average, we will move in the direction that optimises what we want.

**Why stochastic gradient descent?**

Stochastic gradient descent (SGD) is selected over full gradient descent, because it is more efficient.

1. We sample a training example, i, at random from the set of possible indices of the training examples.

- `i ∈ {1, ⋯, n}` at random

2. Then, we perform a gradient descent update with respect to the selected sampled term.

3. We move parameters in the direction that seem to optimise that particular term in the objective function.

Since we are doing this stochastically, we have introduced randomness, and so must decrease the learning rate parameter in order for this to converge.

- η → 0

The learning rate must go to 0 as a result of iterations of this update.

Put another way, we want the sum of the learning rate to go to infinity, if we sum over all iterations:

- `Σ`<sup>`∞`</sup><sub>`i=1`</sub>` η = ∞`

But we need to reduce the variance from the stochasticity we introduced, so have the parameters be square summable:

- `Σ`<sup>`∞`</sup><sub>`t=1`</sub>` η`<sup>`2`</sup><sub>`t`</sub>` < ∞`

So that the squared values of those parameters are finite.

For example:

- `η`<sub>`t`</sub>`= 1 / (1 + t)`, suffices to satisfy these constraints.

**Computing the gradient**

Returning to our objective function without the offset parameter, and with the regularisation term within the average loss summation:

`J(θ) = 1/n Σ`<sup>`n`</sup><sub>`i=1`</sub>` [Loss`<sub>`h`</sub>`(y`<sup>`(i)`</sup>`(θ•x`<sup>`(i)`</sup>`)) + λ/2∥θ∥`<sup>`2`</sup>`]`

Our update with SGD is to sample i at random, then take the old parameter value θ and nudge it in the direction of the gradient with respect to the parameters of the hinge loss of that particular training example plus their regularisation:

- `θ ← θ - η∇`<sub>`θ`</sub>` [Loss`<sub>`h`</sub>`(y`<sup>`(i)`</sup>`θ•x`<sup>`(i)`</sup>`) + λ/2∥θ∥`<sup>`2`</sup>`]`

To see what this amounts to, take the gradient with respect to both of the terms here:

- `θ ← θ - η∇ [ {0, loss=0; -y`<sup>`(i)`</sup>`x`<sup>`(i)`</sup>`, loss>0} + λθ]`

When the loss is 0, then the gradient is also 0 as a vector, and nothing will come out of that gradient - (θ - η∇ will be equal to θ)

When the loss is nonzero (!= 0), then the hinge loss is actually 1 minus its argument `(y`<sup>`(i)`</sup>`(θ•x`<sup>`(i)`</sup>`)`, which is just a linear function of θ:

- minus because of the `1 -`,
- label = `y`<sup>`(i)`</sup>, a scalar
- multiplied by `x`<sup>`(i)`</sup>, a vector

We then have the regularisation term, which is just λ multiplied by the parameter vector θ itself.

- `+ λθ`

**Differences between SGD and perceptron algorithm:**

1. We use a decreasing learning rate, due to the stochasticity.

2. We perform an update, even if we correctly classify the example, because the regularisation term will always yield an update regardless of what the loss is.

3. The role of that regularisation term is to nudge the parameters a little bit backwards, so decrease the norm of the parameter vector, at every step that corresponds to trying to maximise the margin.

4. To counterbalance that, we get a nonzero derivative from the loss terms, if the loss is nonzero.
