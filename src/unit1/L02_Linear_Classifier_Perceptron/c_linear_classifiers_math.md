# Linear Classifiers Mathematically Revisited

In a 2-dimensional space, the **decision boundary** is a line that divides the space into two.

For 1-dimension, the decision boundary would be a point; for 3-dimensions, a plane; and for n-dimensions, a hyperplane.

For our 2-dimensional example, drawing different lines gives the set of linear classifiers over the plane.

**Linear classfiers through the origin**

A linear classifier in a given direction, that passes through the origin (0, 0). A more restricted set of linear classifiers than the full possible set.

The dividing line of the decision boundary is not arbitrarily placed in 2-dimensional space, but must pass through the origin.

The equation for this line would be the set of all points that satisfy the equation for a line through the origin.

To define this, we need to introduce parameters ϴ_1, which multiplies the x_1 coordinate, and ϴ_2, which multiplies the x_2 coordinate.

`ϴ_1x_1 +  ϴ_2x_2 = 0`

We fix the parameters for ϴ_1 and ϴ_2; all points that satisfiy the equation:

- `{X: ϴ_1x_1 + ϴ_2x_2 = 0}`, X being a vector, all of the x's are points along the line fixed by ϴ_1 and ϴ_2.

This can be written as:

`ϴ = [ϴ_1, ϴ_2]`
`X = [x_1, x_2]`

The decision boundary can be written as all X for which the inner product (dot product) between ϴ and X = 0:

`{X: ϴ•x = 0}` (linear function)

Therefore, parameter ϴ is **orthogonal** to all of the points that lie on the decision boundary.

ϴ varies, but X varies, so it is a linear function of X.

**Two sides of the decision boundary**

On one side of the decision boundary, ϴ • x > 0, and on the other side ϴ • x < 0.

Given our decision of which side of the boundary is positive, for simplicity here ϴ • x > 0, we know that ϴ is then in a positive direction on that side of the line.

We now have a parametric way of writing the decision boundaries.

**Linear classifiers through the origin**

Back to linear classifiers through the origin: knowing our parameters for the decision boundary enables us to define the set of linear classifiers through the origin.

`h(x; ϴ)`

Each choice of ϴ defines one classifier; a different choice of ϴ gives us a different classifier.

- Though that classifier also goes through the origin (0, 0).

- That classifier is now simply the sign of ϴ • x:

  - `h(x; ϴ) = sign(ϴ • x)`
  - the label that it returns is the sign of the linear function ϴ • x.

- In general, ϴ lives in the set of R^d, as does x:
  - `ϴ ∈ R^d`
  - so `{h(x; ϴ) = sign(ϴ • x) ϴ ∈ R^d}` gives us our set of linear classifiers through the origin.

This includes each of the different linear classifiers we can obtain through adjusting the value of ϴ.

**Note**

The association between the classifiers and the parameter vector ϴ is not unique:

- there are multiple parameter vectors ϴ that define exactly the same classifier
- each linear classifier through origin has at least one parameter vector ϴ - **in fact, many** - that correspond to the same decision boundary.

ϴ•x relates to the degree to which we classify a point as either positive or negative. That degree only changes when we move orthogonally to the decision boundary.

**Linear classifiers**

We can then apply the same logic to linear classifiers that do not cross through the origin, in which case we include the offset ϴ_0, a scalar parameter:

- `{X: ϴ • x + ϴ_0 = 0}`, this is now the decision boundary.
- It is ϴ_0 that controls the location of the boundary, where it is in relation to the origin.
- ϴ controls the orientation of that boundary, and is orthogonal to the boundary.

Now:

- `h(x; ϴ, ϴ_0) = sign(ϴ • x + ϴ_0)`
- with the set of linear classifiers given by `{h(x; ϴ, ϴ_0) = sign(ϴ • x), ϴ ∈ R^d, ϴ_0 ∈ R}`