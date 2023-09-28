# Equivalance of regularization to a Gaussian Prior on Weights

The regularized linear regression can be interpreted from a probabilistic point of view.

Suppose we are fitting a linear regression model with n data points (x<sub>1</sub>, y<sub>1</sub>), (x<sub>2</sub>, y<sub>2</sub>), ⋯, (x<sub>n</sub>, y<sub>n</sub>). Let's assume the ground truth is that y is linearly related to x but we also observed some noise for ε:

y<sub>i</sub> = θ•x<sub>i</sub> + ε

where ε ~ N (0, σ<sup>2</sup>)

Then the likelihood of our observed data is

Π<sup>n</sup><sub>i=1</sub> N (y<sub>i</sub>|θ•x<sub>i</sub>, σ<sup>2</sup>)

Now, if we impose a Gaussian prior N (θ|0,λ<sup>-1</sup>), the likelihood will change to

Π<sup>n</sup><sub>i=1</sub> N (y<sub>i</sub>|θ•x<sub>i</sub>, σ<sup>2</sup>) N (θ|0,λ<sup>-1</sup>)

Take the logarithim of the likelihood, we will end up with

Σ<sup>n</sup><sub>i=1</sub> - 1/(2σ<sup>2</sup>)(y<sub>i</sub> - θ•x<sub>i</sub>)<sup>2</sup> - 1/2 λ∥θ∥<sup>2</sup> + constant
