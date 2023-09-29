# Introduction to Non-Linear Classification

**Polynomial features**

We can add more polynomial terms:

x ∈ ℝ, φ(x) = [x, x<sup>2</sup>, x<sup>3</sup>, x<sup>4</sup>, ⋯]

and so on - we can always add additional feature coordinates, resulting in an ever-more powerful feature representation, and ever-more powerful classifier, that operates linearly in the expanded feature vectors.

When x is 2-dimensional:

x = [x<sub>1</sub>, x<sub>2</sub>] ∈ ℝ<sup>2</sup>

Including second-order features, we expand to:

φ(x) = [x<sub>1</sub>, x<sub>2</sub>, x<sub>1</sub><sup>2</sup>, x<sub>2</sub><sup>2</sup>, √2 x<sub>1</sub>x<sub>2</sub>] ∈ ℝ<sup>5</sup>

So our new feature-vector resides in five-dimensional space.

**Non-linear classification**

h(x; θ, θ<sub>0</sub>) = sign(θ•φ(x) + θ<sub>0</sub>)

**Non-linear regression**

f(x; θ, θ<sub>0</sub>) = θ•φ(x) + θ<sub>0</sub>

E.g. φ(x) = [x, x<sup>2</sup>]<sup>T</sup>

**Drawbacks of feature vectors**

The mappings to feature vectors described above provide expressive power.

However, they also result in vectors that can be high-dimensional.

For example, take x ∈ ℝ<sup>d</sup>:

φ(x) = [x<sub>1</sub>, ⋯, x<sub>d</sub>, {x<sub>i</sub>x<sub>j</sub>}, {x<sub>i</sub>x<sub>j</sub>x<sub>k</sub>}, ⋯]<sup>T</sup>

Resulting in complexity for the corresponding parts of O(d), O(d<sup>2</sup>), O(d<sup>3</sup>), and so on.
