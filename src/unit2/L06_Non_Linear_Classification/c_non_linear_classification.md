# Introduction to Non-Linear Classification

**Polynomial features**

We can add more polynomial terms:

$x ∈ ℝ, \phi(x) = [x, x^2, x^3, x^4, ⋯]$

and so on - we can always add additional feature coordinates, resulting in an ever-more powerful feature representation, and ever-more powerful classifier, that operates linearly in the expanded feature vectors.

When $x$ is 2-dimensional:

$x = [x_1, x_2] ∈ ℝ^2$

Including second-order features, we expand to:

$\phi(x) = [x_1, x_2, x_1^2, x_2^2, \sqrt{2} x_1x_2] ∈ ℝ^5$

So our new feature-vector resides in five-dimensional space.

**Non-linear classification**

$h(x; θ, θ_0) = sign(θ•\phi(x) + θ_0)$

**Non-linear regression**

$f(x; θ, θ_0) = θ•\phi(x) + θ_0$

E.g. $\phi(x) = [x, x^2]^T$

**Drawbacks of feature vectors**

The mappings to feature vectors described above provide expressive power.

However, they also result in vectors that can be high-dimensional.

For example, take $x ∈ ℝ^d$:

$\phi(x) = [x_1, ⋯, x_d, \{x_ix_j\}, \{x_ix_jx_k\}, ⋯]^T$

Resulting in complexity for the corresponding parts of $O(d), O(d^2), O(d^3)$, and so on.
