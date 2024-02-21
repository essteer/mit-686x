# Hidden Layer Models

See notes for graphical representation.

Take our basic model, with $x_1, x_2$, which each feed via two weights $w_{11}$ and $w_{12}$, $w_{21}$ and $w_{22}$, to two nodes $z_1, z_2$ at layer $1$ ($tanh$).

Layer $1$ is a hidden layer.

Layer $1$ outputs two functions $f_1, f_2$ (one from each node) which both go to node $z$, which outputs function $f$.

For instance:

$z_1 = \sum\nolimits_{j=1}^{2} x_j w_{j1} + w_{01}$

$f_1 = f(z) = tanh(z_1)$

We can envisage layers $0$ and $1$ as a box, with inputs $x_1, x_2$, a component $w$ that is the weight, and outputs $f_1, f_2$.

In this way we can think of them, and visualise them, as if they were linear classifiers.

For instance:

$z_1 = w_1$ (vector of $[w_{11}, w_{21}]$) $• x + w_{01}$

We can understand this as a linear classifier, with a decision boundary and offset.

The decision boundary corresponds to when the aggregate input to that unit = $0$.

**Redundancy**

Take a simple example with +ve points clustered around the origin, and -ve points clustered around larger positive and negative points.

Draw two parallel decision boundaries pointing inwards either side of the +ve points.

While not linearly separable, they may become so through tanh activation.

In this example, they are not separable with ReLU.

However, reorienting the decision boundaries to point outwards instead of inwards, means that they points remain linearly separable with tanh, and become linearly separable with ReLU because with ReLU the +ve points are squeezed into the origin.

In another example, with badly selected decision boundaries that cut across +ve and -ve points, we cannot separate them with tanh or ReLU.

However, we can map to a feature representation with, say, 10 dimensions, and find that they become linearly separable in the 10th dimension.

These are examples of adding redundancy to help distinguish between the two groups.
