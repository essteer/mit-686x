# Closed Form Solution

For most machine learning algorithms, there is no closed form solution, but in the case of our linear regression with empirical risk function, there is.

R<sub>n</sub>(θ) = 1/n Σ<sup>n</sup><sub>i=1</sub> (y<sup>(i)</sup> - θ•x<sup>(i)</sup>)<sup>2</sup> / 2

∇<sub>θ</sub>R<sub>n</sub>(θ)<sub>|θ=θ^</sub> = 1/n Σ<sup>n</sup><sub>i=1</sub> ∇<sub>θ</sub> ((y<sup>(i)</sup> - θ•x<sup>(i)</sup>)<sup>2</sup> / 2)<sub>|θ=θ^</sub>

= - 1/n Σ<sup>n</sup><sub>i=1</sub> (y<sup>(i)</sup> - θ•x<sup>(i)</sup>)x<sup>(i)</sup>

We then take the sum, and break it into two parts:

= - 1/n Σ<sup>n</sup><sub>i=1</sub> y<sup>(i)</sup>x<sup>(i)</sup>

This is a vector of dimensionality d, which we denote as b

- 1/n Σ<sup>n</sup><sub>i=1</sub> θ^•x<sup>(i)</sup>x<sup>(i)</sup>

Since the result of a dot product is a number, we can move this around as:

1/n Σ<sup>n</sup><sub>i=1</sub> x<sup>(i)</sup> θ^•x<sup>(i)</sup>

Putting it together:

= - b + 1/n Σ<sup>n</sup><sub>i=1</sub> x<sup>(i)</sup> θ^•x<sup>(i)</sup>

Because θ^•x<sup>(i)</sup> is a scalar, when we take a transpose of it, it is equal to itself.

= - b + 1/n Σ<sup>n</sup><sub>i=1</sub> x<sup>(i)</sup> (x<sup>(i)</sup>)<sup>T</sup>θ^

Since each x is a vector of dimension d, we get a matrix of dimension d x d, which we denote as A:

= - b + Aθ^ = 0

∴ Aθ^ = b, which is what we seek to solve.

If our matrix is invertible, then in this case we can write:

θ^ = A<sup>-1</sup>b

**Two caveats**

1. We do not always know that A is invertible, so we cannot always perform this operation.

It is only invertible if x<sup>(1)</sup>, ⋯, x<sup>(n)</sup> span ℝ<sup>d</sup>.

This happens if the number of training examples, n, is substantially larger than the dimensionality of the feature vector d.

If we don't have enough training examples from a big dataset, we can't do this operation.

2. Even if we can do the operation, the second issue is the cost associated with it.

The operation is in the order of d<sup>3</sup>:

O(d<sup>3</sup>)

So the cost is significant.
