# Regularisation and Generalisation

$J(θ, θ_0) = \frac{1}{n} Σ_i=1^n Loss_h(y^{(i)}(θ•x^{(i)} + θ_0)) + \frac{λ}{2}∥θ∥^2$

As we emphasise the margins through $λ$, we are less and less able to fit the training examples, and so losses increase.

As we emphasise the training loss, we reduce $λ$ to seek solutions where training loss is small.

We can plot this as a function of $λ$, or for conceptual simplicity, $\frac{1}{λ}$.

We divide the objective function with $\frac{1}{λ}$:

- $\frac{1}{λ} J(θ, θ_0) = \frac{1}{λn} Σ_{i=1}^n Loss_h(y^{(i)}(θ•x^{(i)} + θ_0)) + 2∥θ∥^2$
- We call this $C$:
  - as $C$ is large, we emphasise losses
  - as $C$ is small, we emphasise simpler solutions with large margins

The curve plotted by this function is the training loss.

Our test loss would sit higher than this curve, and at some point curve away from it, since our training model has not been fit to the test data.

There would be a point, $C$\*, that optimises the function as the point with the minimum test loss.

$C$\* would effectively divide the problem into two regimes:

- underfitting before the optimum (where $C < C$\*), and
- overfitting after the optimum (where $C > C$\*).

Therefore:

- if underfitting, then increasing $C$ will result in better test loss;
- if overfitting, then decreasing $C$ will result in better test loss.

**Validation set**

To apply this intuition to our model, we slice off part of the training set to become the **validation set**, and use the validation set as a sort of "pretend" test set.

We take the now smaller training set, and based on those examples only, find the optimal values of $θ$ and $θ_0$ by minimising the $\frac{1}{λ}$ objective function.

Then we take the corresponding values of $θ$ and $θ_0$, and use the validation set examples to evaluate an approximate test error.

We are not evaluating the actual test set loss/error, but the validation set loss/error.

We do this to find the value of $C$ that optimises performance on the "pretend" test examples (i.e., the validation set examples).

This will not result in $C$\* precisely, but an estimate $C$^.
