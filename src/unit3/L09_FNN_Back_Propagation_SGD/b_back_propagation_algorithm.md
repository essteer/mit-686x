# Back Propagation Algorithm

Fee\partial{for}ward Neural Networks with multiple hidden layers, are complex models that try capture the representation of the examples toward the output unit in such a way as to facilitate the prediction task.

The representation aspect - learning the feature representation, as well as how to make use of it - makes the learning problem difficult.

**Stochastic Gradient Descent**

SGD can succeed at this task, provided a given level of overcapacity for the model.

In applying SGD, our task it to evaluate for each example pair $(x, y)$, to adjust the parameters of the model so as to nudge them in the reverse direction of the gradient.

We must measure loss, that measures by how much our predicted output differs from the desired target.

We take a derivative of that loss with respect to each of the parameters.

Then, we apply a stochastic gradient descent algorithm by nudging those parameters in the reverse direction to the gradient.

$\frac{\partial{Loss( y, f( x; w ) )}}{\partial{w_{ij}^l}}$

The weights are update as follows: $w_{ij}^l ← w_{ij}^l - η$

**Example**

Here we use the example of a very deep, chain-like NN, with just one unit per hidden layer:

$x ◯ w_1 ⟶ z_1 ◯ f_1 w_2 ⟶ z_2 ◯ f_2 ⟶ ◯$

Where $x ∈ ℝ$, and this network continues on to an output $f_L ∈ ℝ$:

$w_L ⟶ z_L ◯ f_L ⟶$

$z_1 = x w_1$, an aggregate input of the signal from before, leaving out offset for simplicity.

$f_1 = tanh(x w_1)$, the activation function.

and so on, to:

$f_L = tanh( f_L-1 w_L )$

(Typically the final unit could be linear, but we retain the same form here for simplicity.)

Given $y$, we must evaluate the loss between the desired output, and the network prediction.

$Loss ( y, f_L )$

The network output is a function of all of the weights in the model, plus the input $x$.

The loss could be squared loss, for a regression problem, or hinge loss for a classification, and so on.

In order to get from where we observe the outcome, down to the parameters we are interested in modifying, we need to understand the individual mappings between the layers.

How the previous layer output is transformed into the next output, using the parameters $w_L$.

In order to do so, we need only understand how the output has changed as a function of the input, the derivative with respect to the input.

**Taking derivatives**

We want to get:

$\frac{\partial{Loss}}{\partial{w_1}} = \frac{\partial{f_1}}{\partial{w_1}} \frac{\partial{Loss}}{\partial{f_1}}$

For $\frac{\partial{f_1}}{\partial{w_1}}$, since the activation is a function of $tanh(xw_1)$, the derivative of tanh is $1 - tanh^2$, or $(1 - f_1^2)x$.

$\frac{\partial{Loss}}{\partial{f_1}} = \frac{\partial{f_2}}{\partial{f_1}} \frac{\partial{Loss}}{\partial{f_2}}$

**How we back propagate**

We can take the derivative of the loss with respect to $L$:

$\frac{\partial{Loss (y, f_L)}}{\partial{f_L}} = \frac{d \frac{1}{2} (y - f_L)^2}{\partial{f_L}} = - (y - f_L)$

(In the squared loss example.)

**Caveats**

The nature of the derivation highlights how things can go wrong: if the Jacobians of the layer-wise mappings are very small, then the gradient vanishes very quickly as the depth of the architecture increases.

If these derivatives are large, the gradients can also explode.
