# Planes

Planes and other low-dimensional subspaces of higher n-dimensional space.

_x = `[x1; x2; x3]` ∈ ℝ^3_ (3x1 matrix)

We refer to x as living in ℝ^3.

We may be interested in points in relation to x, for example, in ℝ^3, a plane would be all of the points that fit on a slice.

In 2D, we may have a line.

This is relevant in ML, when we want to be able to describe the way that points are arranged in a space, and what side of the space they fall on.

**Example**: trying to draw classification boundaries.

- We may have some points, which are x's, and some points, which are o's.
- We want to ask what the separating hyperplane is, i.e., a line that separates the two sets of points.
- That hyperplane would then demarcate the sets so that points above it are x's, and points below are o's.

How do we define what the line is?

- There is a particular definition used to define what a plane is.

**Defining a plane**

If we have a plane in e.g., in 3D, we define the plane as having a "**normal**": there is a vector taken to be perpendicular to all other points on the plane.

- We call the vector of the normal theta **θ**.

Additionally, this plane has an offset _0'_ from the origin, _0_.

We want to find all lines, all points, which fall on this plane.

If we take another point, _x_, it will only be on this plane if its vector is perpendicular to theta _θ_.

_(x - x^)•θ = 0_
_x•θ - x^•θ = 0_

_((- x^•θ) is always a constant)_

We can define the plane as all of the points that satisfy:

_x•θ + θ0 = 0_ (_θ0_ is an offset equivalent to _-x^•θ_)

This is the definition of the plane.

- Any point that satisfies this linear relationship, lies on this plane.
