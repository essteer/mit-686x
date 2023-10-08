# Back Propagation Algorithm

Feedforward Neural Networks with multiple hidden layers, are complex models that try capture the representation of the examples toward the output unit in such a way as to facilitate the prediction task.

The representation aspect - learning the feature representation, as well as how to make use of it - makes the learning problem difficult.

**Stochastic Gradient Descent**

SGD can succeed at this task, provided a given level of overcapacity for the model.

In applying SGD, our task it to evaluate for each example pair (x, y), to adjust the parameters of the model so as to nudge them in the reverse direction of the gradient.

We must measure loss, that measures by how much our predicted output differs from the desired target.

We take a derivative of that loss with respect to each of the parameters.

Then, we apply a stochastic gradient descent algorithm by nudging those parameters in the reverse direction to the gradient.

- dLoss(y, f(x; w)) / dw<sup>l</sup><sub>ij<sub>

The weights are update as follows:

w<sup>l</sup><sub>ij<sub> ← w<sup>l</sup><sub>ij<sub> - η

**Example**

Here we use the example of a very deep, chain-like NN, with just one unit per hidden layer:

x ◯ w<sub>1</sub>⟶ z<sub>1</sub>◯f<sub>1</sub> w<sub>2</sub>⟶ z<sub>2</sub>◯f<sub>2</sub> ⟶ ◯

Where x ∈ ℝ, and this network continues on to an output f<sub>L</sub> ∈ ℝ:

w<sub>L</sub>⟶ z<sub>L</sub>◯f<sub>L</sub> ⟶

z<sub>1</sub> = xw<sub>1</sub>, an aggregate input of the signal from before, leaving out offset for simplicity.

f<sub>1</sub> = tanh(xw<sub>1</sub>), the activation function.
⋮
f<sub>L</sub> = tanh(f<sub>L-1</sub>w<sub>L</sub>)

(Typically the final unit could be linear, but we retain the same form here for simplicity.)

Given y, we must evaluate the loss between the desired output, and the network prediction.

Loss(y, f<sub>L</sub>)

The network output is a function of all of the weights in the model, plus the input x.

The loss could be squared loss, for a regression problem, or hinge loss for a classification, and so on.

In order to get from where we observe the outcome, down to the parameters we are interested in modifying, we need to understand the individual mappings between the layers.

How the previous layer output is transformed into the next output, using the parameters w<sub>L</sub>.

In order to do so, we need only understand how the output has changed as a function of the input, the derivative with respect to the input.

**Taking derivatives**

We want to get:

dLoss / dw<sub>1</sub> = df<sub>1</sub>/dw<sub>1</sub> dLoss / df<sub>1</sub>

For df<sub>1</sub>/dw<sub>1</sub>, since the activation is a function of tanh(xw<sub>1</sub>), the derivative of tanh is 1 - tanh<sup>2</sup>, or (1 - f<sup>2</sup><sub>1</sub>)x.

dLoss / df<sub>1</sub>:

dLoss / df<sub>1</sub> = df<sub>2</sub> / df<sub>1</sub> dLoss / df<sub>2</sub>

**How we back propagate**

We can take the derivative of the loss with respect to L:

dLoss (y, f<sub>L</sub>) / df<sub>L</sub>

= (d 1/2 (y - f<sub>L</sub>)<sup>2</sup>) / df<sub>L</sub>

= - (y - f<sub>L</sub>)

(In the squared loss example.)

**Caveats**

The nature of the derivation highlights how things can go wrong: if the Jacobians of the layer-wise mappings are very small, then the gradient vanishes very quickly as the depth of the architecture increases.

If these derivatives are large, the gradients can also explode.
