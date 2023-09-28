# Gradient-based Approach

The empirical risk function is differentiable everywhere.

R<sub>n</sub>(θ) = 1/n Σ<sup>n</sup><sub>i=1</sub> (y<sup>(i)</sup> - θx<sup>(i)</sup>)<sup>2</sup> / 2

R<sub>n'</sub> (θ) = 1/n' Σ<sup>n+n'</sup><sub>i=n+1</sub> (y<sup>(i)</sup> - θx<sup>i</sup>)<sup>2</sup> / 2

We randomly select one example, then look at the direction of the gradient.

Since we are trying to minimise, we will slightly nudge the parameters in the correct direction (the correct direction being determined by the gradient).

∇<sub>θ</sub> (y<sup>(i)</sup> - θ•x<sup>(i)</sup>)<sup>2</sup> / 2

= (y<sup>(i)</sup> - θ•x<sup>(i)</sup>) ∇<sub>θ</sub> (y<sup>(i)</sup> - θ•x<sup>(i)</sup>)

= - (y<sup>(i)</sup> - θ•x<sup>(i)</sup>) • x<sup>(i)

**Algorithm**

1. initialise θ = 0
2. randomly pick some example i from 1 to n (i = {1, ⋯, n})
3. update theta θ = θ + η (y<sup>(i)</sup> - θ•x<sup>(i)</sup>) • x<sup>(i)

where η<sub>k</sub> = 1 / (1 + k)

**Note 1**

Note a difference with the classification model, that here we will correct at every step where there is some discrepancy.

We are not just examining whether there is a mistake, but how much of a mistake there is.

If the values are far apart, we correct more.
If the values are close, we correct less.

**Note 2**

The algorithm is to an extent self-correcting.

For example, if our prediction was smaller than the true value y, then the update expression would be positive and we would be pushing in the positive direction of point x.

y<sup>(i)</sup> > x<sup>(i)</sup>
