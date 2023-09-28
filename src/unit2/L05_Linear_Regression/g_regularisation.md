# Regularisation

We optimise empirical risk for the training set, because we don't have access to the test set.

But how can we know whether we are doing this well, or simply fitting the peculiarities and noise of our training set?

Regularation discourages the model from perfectly fitting the training set, since that would include mistakes and errors.

The regulariser pushes the thetas to be close to zero.

It becomes only worthwhile to move the parameters if there is a strong pattern suggested by the move.

**Ridge regression**

With ridge regression, in addition to n, we add lambda to our objective function.

We want the loss to capture how well we fit the training examples, which is what our empirical risk component tells us.

But now we want to add a new component, the relative contribution of which will be determined by the parameter lambda:

J<sub>λ,n</sub>(θ) = λ/2∥θ∥<sup>2</sup> + R<sub>n</sub>(θ)

The two parts are in balance: R<sub>n</sub>(θ) wants to find thetas that match the training set; λ/2∥θ∥<sup>2</sup> wants to keep the thetas closer to zero.

There must then be significant reason for the function to deviate from the origin.

A higher lambda stresses the importance of remaining close to zero, and reduces the importance of fitting the training examples.

A lower lambda relaxes the constraint on deviating from the origin.

So we arrive at:

J<sub>λ,n</sub>(θ) = λ/2∥θ∥<sup>2</sup> + R<sub>n</sub>(θ)

Another way to write this is:

J<sub>λ,n</sub>(θ) = λ/2∥θ∥<sup>2</sup> + 1/n Σ<sup>n</sup><sub>i=1</sub> (y<sup>(i)</sup> - θ•x<sup>(i)</sup>)<sup>2</sup> / 2

A benefit of expressing it in this form, is that the gradient based approach and closed form solution can be easily adjusted to fit this expression.

**For the gradient based approach**

∇<sub>θ</sub> (λ/2∥θ∥<sup>2</sup> + (y<sup>(i)</sup> - θ•x<sup>(i)</sup>)<sup>2</sup> / 2)

= λθ - (y<sup>(i)</sup> - θ•x<sup>(i)</sup>)x<sup>(i)</sup>

Algorithm:

1. Initialise thetas to 0
2. Randomly select a point i from 1 to n (i = {1, ⋯, n})

Now we want to nudge the parameters against the direction of the gradient of that point.

We update theta against the direction of the gradient, hence we subtract in the expression below.

The gradient tells us only the direction, but not how large the step is, so as before we use a learning rate parameter to determine the size of the step.

3. Update theta: θ = θ - η(λθ - (y<sup>(i)</sup> - θ•x<sup>(i)</sup>)x<sup>(i)</sup>)

It is possible to stop at (3), but we can simplify it further.

= (1 - ηλ)θ + η(y<sup>(i)</sup> - θ•x<sup>(i)</sup>)x<sup>(i)</sup>
