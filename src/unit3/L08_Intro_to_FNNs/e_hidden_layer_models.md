# Hidden Layer Models

See notes for graphical representation.

Take our basic model, with x<sub>1</sub>, x<sub>2</sub>, which each feed via two weights w<sub>11</sub> and w<sub>12</sub>, w<sub>21</sub> and w<sub>22</sub>, to two nodes z<sub>1</sub>, z<sub>2</sub> at layer 1 (tanh).

Layer 1 is a hidden layer.

Layer 1 outputs two functions f<sub>1</sub>, f<sub>2</sub> (one from each node) which both go to node z, which outputs function f.

For instance:

z<sub>1</sub> = Σ<sup>2</sup><sub>j=1</sub> x<sub>j</sub>w<sub>j1</sub> + w<sub>01</sub>

f<sub>1</sub> = f(z) = tanh(z<sub>1</sub>)

We can envisage layers 0 and 1 as a box, with inputs x<sub>1</sub>, x<sub>2</sub>, a component w that is the weight, and outputs f<sub>1</sub>, f<sub>2</sub>.

In this way we can think of them, and visualise them, as if they were linear classifiers.

For instance:

z<sub>1</sub> = w<sub>1</sub> (vector of [w<sub>11</sub>, w<sub>21</sub>]) • x + w<sub>01</sub>

We can understand this as a linear classifier, with a decision boundary and offset.

The decision boundary corresponds to when the aggregate input to that unit = 0.

**Redundancy**

Take a simple example with +ve points clustered around the origin, and -ve points clustered around larger positive and negative points.

Draw two parallel decision boundaries pointing inwards either side of the +ve points.

While not linearly separable, they may become so through tanh activation.

In this example, they are not separable with ReLU.

However, reorienting the decision boundaries to point outwards instead of inwards, means that they points remain linearly separable with tanh, and become linearly separable with ReLU because with ReLU the +ve points are squeezed into the origin.

In another example, with badly selected decision boundaries that cut across +ve and -ve points, we cannot separate them with tanh or ReLU.

However, we can map to a feature representation with, say, 10 dimensions, and find that they become linearly separable in the 10th dimension.

These are examples of adding redundancy to help distinguish between the two groups.
