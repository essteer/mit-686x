# Points and Vectors

In ML, there are points (data points) in the data sets we work with, and which we want to be able to describe in terms of how they relate in n-dimensional space.

If $x = (3, 2, 2)$, then $x$ belongs in $R^3$, denoted as $∈ ℝ^3$.

$x$ can also be written as a vector starting from origin $(0, 0, 0)$; we view $x$ as a displacement from $(0, 0, 0)$.

$x_i$ would be the ith coordinate in this vector. E.g., $x_i = x_2 = 2$.

**Magnitude / norm**

The magnitude of $x = sqrt(3^2 + 2^2 + 2^2)$

Two definitions for a dot product, which are equivalent to each other and used interchangeably:

**Algebraic definition**: $x•y = Σ_{i=1}^{n} x_i•y_i$, for example:

$x = [3; 2; 2]$ (3x1 matrix)

$y = [1; 1; 1]$ (3x1 matrix)

$x•y = 3•1 + 2•1 + 2•1$

$x•y = 7$

**Geometric definition**: $x•y = |x||y|cosθ$

I.e., the magnitude / norm of $x$, times magnitude / norm of $y$, times the cosine of the angle between them.
