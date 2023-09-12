# Hinge Loss

Our goal is to maximise the distance from the margin boundaries (MBs) to the decision boundary (DB).

I.e., to **maximise** `1/∥θ∥` - this is our regularisation term.

Our objective function is comprised of two parts:

- hinge loss, defined by Loss<sub>h</sub>(y<sup>(i)</sup>(θ•x<sup>(i)</sup> + θ<sub>0</sub>))
- regularisation

**Hinge loss**

We know that we get a positive value from the loss function when the prediction agrees with the label:

- (y<sup>(i)</sup>(θ•x<sup>(i)</sup> + θ<sub>0</sub>))
- we call this argument, **agreement**
- we denote this as _z_

We also know that if a point lies exactly on the MB, e.g. a positive example on the positive MB, then the agreement value _z_ = 1:

- if on the correct side of the DB, the agreement value = 1, since 1\*1 = 1;
- if on the incorrect side of the DB, the agreement value = 1, since -1\*-1 = 1.

- If the example lies on the correct side of the DB, but beyond the MB, then the value of z (agreement) will be > 1.

We can then define the loss in terms of how much our preference to keep the points outside of the MBs is violated:

- Loss<sub>h</sub>(y<sup>(i)</sup>(θ•x<sup>(i)</sup> + θ<sub>0</sub>)) = 0 if z >= 1

We then penalise any values that penetrate into the MBs.

- Loss<sub>h</sub>(y<sup>(i)</sup>(θ•x<sup>(i)</sup> + θ<sub>0</sub>)) = 1-z if z < 1

So 1-z is a positive value that increases as the agreement decreases below 1.

**Regularisation**

As stated before, for regularisation we want to maximise `1/∥θ∥`, i.e. find the values of θ and θ<sub>0</sub> that increase `1/∥θ∥`, 1/ the norm/magnitude of parameter vector θ.

Maximising `1/∥θ∥` is the same as minimising `∥θ∥` (the norm of θ), which is the same as minimising `∥θ∥^2` (the squared norm of θ).

- (The smaller the denominator, the larger the value of the fraction `1/∥θ∥` - e.g., 1/3 > 1/5.)

We write this as:

- max `1/∥θ∥` min `1/2∥θ∥^2`

We can regularise the solutions by trying to penalise large values of ∥θ∥ and ∥θ∥^2.
