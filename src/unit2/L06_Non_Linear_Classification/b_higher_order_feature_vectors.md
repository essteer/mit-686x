# Higher Order Feature Vectors

**Real line example**

Linear classifiers on a real line.

A 1D line with origin at the centre: imagine a point at positive 1 on the right of the origin, and another point at the origin (negative).

h(x; θ, θ<sub>0</sub>) = sign(θx + θ<sub>0</sub>)

(Here theta and theta0 are just scalars, in 1D).

For these two points, this can easily be classified using a linear classifier.

A line drawn across that line, separating the two points, would serve this purpose and denote points above or below the line as either positive or negative.

If we then introduced a new positive point, located at -1, the points would cease to be linearly separable, and our linear classifier no longer correctly classifies the points.

**Feature transformation**

The situation can be remedied through the introduction of feature transformation.

| x   | ⟹   | φ(x) = [x, x<sup>2</sup>]          |
| --- | --- | ---------------------------------- |
| ∈ℝ  | ⟹   | ∈ℝ<sup>2</sup>                     |
| θ   | ⟹   | θ = [θ<sub>1</sub>, θ<sub>2</sub>] |

x is a scalar, the feature vector φ(x) lies in a higher-dimensional space.

Our θ was previously a scalar, but not also has two coordinates, θ<sub>1</sub> and θ<sub>2</sub>

**Note**: we always retain the original feature (in this case x) in the transformed feature vector, so as to retain the power that was available prior to transformation.

After the transformation, we input the transformed features into the linear classifier as though they were our original examples.

Now we have a quadratic function:

h(x; θ, θ<sub>0</sub>) = sign(θ•φ(x) + θ<sub>0</sub>) = sign(θ<sub>1</sub>x + θ<sub>2</sub>x<sup>2</sup> + θ<sub>0</sub>)

But our classifier regards these new vectors as the original examples.

As the examples are mapped into the feature coordinates in feature space, they now lie on a parabola (touching the origin, in the above example).

Our positive point previously at 1 now lies at [1, 1], our negative point previously at the origin 0, now lies at the origin [0, 0], and our positive point at -1 now lies at [-1, 1].

These points are now easily separable via linear classifier.

**Back to the real line**

The quadratic function permits us to separate the points on our real line, with a decision boundary at the two points at which the parabola crosses the line (left and right of our negative point).

Points to the left of the left-hand DB, and to the right of the right-hand DB, are now correctly classified as positive, and those inbetween as negative.

**2-dimensional example**

Now imagine a 2D example, with e.g. positive points at [1, 1] and [-1, -1], and negative points at [1, -1] and [-1, 1].

We again want to retain the original x1 x2 in the transformed feature vector so that we do not lose this power, but now we also add x1x2, which is the product of the two coordinates:

φ(x) = [x<sub>1</sub>, x<sub>2</sub>, x<sub>1</sub>x<sub>2</sub>]

Our theta previously had two coordinates, but now has three coordinates plus the offset:

θ = [θ<sub>1</sub>, θ<sub>2</sub>, θ<sub>3</sub>] + θ<sub>0</sub>

(See notebook for graphical representation.)

So now in 3D space, relative to the φ<sub>1</sub> φ<sub>2</sub> plane, the positive points lie above the plane, and the negative points lie below it along φ<sub>3</sub>.

The φ<sub>1</sub> φ<sub>2</sub> plane is therefore an appropriate means of separating the examples.

The decision boundary is represented by θ which points upwards, orthogonal to the decision boundary, can be selected to be simply:

θ = [0, 0, 1], θ<sub>0</sub> = 0

And we make decisions only based on the third θ coordinate.
