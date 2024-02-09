# Planes

Planes and other low-dimensional subspaces of higher $n$-dimensional space.

$x = [x1; x2; x3] ∈ ℝ^3$ (3x1 matrix)

We refer to $x$ as living in $ℝ^3$.

We may be interested in points in relation to $x$, for example, in $ℝ^3$, a plane would be all of the points that fit on a slice.

In 2D, we may have a line.

This is relevant in ML, when we want to be able to describe the way that points are arranged in a space, and what side of the space they fall on.

**Example**: trying to draw classification boundaries.

- We may have some points, which are $x$'s, and some points, which are $o$'s.
- We want to ask what the separating hyperplane is, i.e., a line that separates the two sets of points.
- That hyperplane would then demarcate the sets so that points above it are $x$'s, and points below are $o$'s.

How do we define what the line is?

- There is a particular definition used to define what a plane is.

**Defining a plane**

If we have a plane in e.g., in 3D, we define the plane as having a "**normal**": there is a vector taken to be perpendicular to all other points on the plane.

- We call the vector of the normal theta $θ$.

Additionally, this plane has an offset $θ'$ from the origin, $0$.

We want to find all lines, all points, which fall on this plane.

If we take another point, $x$, it will only be on this plane if its vector is perpendicular to theta $θ$.

$(x - x̂)•θ = 0$
$x•θ - x̂•θ = 0$

($(- x̂•θ)$ is always a constant)

We can define the plane as all of the points that satisfy:

$x•θ + θ_0 = 0$ ($θ_0$ is an offset equivalent to $-x̂•θ$)

This is the definition of the plane.

- Any point that satisfies this linear relationship, lies on this plane.
