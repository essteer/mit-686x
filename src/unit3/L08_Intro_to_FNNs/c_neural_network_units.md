# Neural Network Units

A neural network unit is a primitive neural network that consists of only the “input layer", and an output layer with only one output.

We have our input vector $X$, where each coordinate $x_{(i)}$ of $X$ (from $x_1$ to $x_d$) is an input unit.

Each input node holds the coordinate value for that $x_{(i)}$.

Each input node has an associated weight, $w_{(i)}$ (we use $w$'s here rather than the $θ$'s denoted for linear classifiers).

So, we have a weight associated with each input coordinate, and we take a weighted combination of those input signals, denoted as $z$:

- $z = \sum\nolimits_{i=1}^{d} x_{(i)} w_{(i)} + w_0$

Once we have that aggregate input, we pass it through some non-linear function $f(z)$, which is often known as an activation function, transfer function, or simply an output of the neuron.

So we have our inputs, and output from $f(z)$, and this functions akin to a linear classifier.

**Forms of activation function**

The output of the non-linear function $f(z)$ could simply be linear.

Another output for is the non-linear ReLU (rectified linear unit), which takes the aggregate input and simply squashes all of the negative values.

This ReLU is defined as $f(z) = max(0, z)$.

The other form of output mimics the sign function (with outputs of $-1$ or $+1$), but in a softer form - this is the hyperbolic tangent unit, tanh.
