# Points and Vectors

In ML, there are points (data points) in the data sets we work with, and which we want to be able to describe in terms of how they relate in n-dimensional space.

If _x = (3, 2, 2)_, then x belongs in R^3, denoted as _∈ ℝ^3_.

_x_ can also be written as a vector starting from origin _(0, 0, 0)_; we view x as a displacement from _(0, 0, 0)_.

_xi_ would be the ith coordinate in this vector. E.g., _xi = x2 = 2_.

**Magnitude / norm**

The magnitude of _x = sqrt(3^2 + 2^2 + 2^2)_

Two definitions for a dot product, which are equivalent to each other and used interchangeably:

1. **Algebraic definition**: _x•y = (n Σ i=1) xi•yi_, for example:

x = `[3; 2; 2]` (3x1 matrix)
y = `[1; 1; 1]` (3x1 matrix)
_x•y = 3•1 + 2•1 + 2•1_
_x•y = 7_

2. **Geometric definition**: _x•y = |x||y|cosθ_

I.e., the magnitude / norm of x, times magnitude / norm of y, times the cosine of the angle between them.
