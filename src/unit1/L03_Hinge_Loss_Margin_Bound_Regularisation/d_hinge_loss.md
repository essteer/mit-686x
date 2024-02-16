# Hinge Loss

Our goal is to maximise the distance from the margin boundaries (MBs) to the decision boundary (DB).

I.e., to **maximise** $\frac{1}{∥θ∥}$ - this is our regularisation term.

Our objective function is comprised of two parts:

- hinge loss, defined by $Loss_h(y^{(i)}(θ•x^{(i)} + θ_0))$
- regularisation

**Hinge loss**

We know that we get a positive value from the loss function when the prediction agrees with the label:

- $y^{(i)}(θ•x^{(i)} + θ_0)$
- we call this argument, **agreement**
- we denote this as $z$

We also know that if a point lies exactly on the MB, e.g. a positive example on the positive MB, then the agreement value $z = 1$:

- if on the correct side of the DB, the agreement value = $1$, since $1 \times 1 = 1$;
- if on the incorrect side of the DB, the agreement value = $-1$, since $1 \times -1 = -1$.

- If the example lies on the correct side of the DB, but beyond the MB, then the value of $z$ (agreement) will be $> 1$.

We can then define the loss in terms of how much our preference to keep the points outside of the MBs is violated:

- $Loss_h(y^{(i)}(θ•x^{(i)} + θ_0)) = 0$ if $z >= 1$

We then penalise any values that penetrate into the MBs.

- $Loss_h(y^{(i)}(θ•x^{(i)} + θ_0)) = 1-z$ if $z < 1$

So $1 - z$ is a positive value that increases as the agreement decreases below $1$.

**Regularisation**

As stated before, for regularisation we want to maximise $\frac{1}{∥θ∥}$, i.e. find the values of $θ$ and $θ_0$ that increase $\frac{1}{∥θ∥}$, $1$ / the norm/magnitude of parameter vector $θ$.

Maximising $\frac{1}{∥θ∥}$ is the same as minimising $∥θ∥$ (the norm of $θ$), which is the same as minimising $∥θ∥^2$ (the squared norm of $θ$).

- (The smaller the denominator, the larger the value of the fraction $\frac{1}{∥θ∥}$ - e.g., $\frac{1}{3} > \frac{1}{5}$.)

We write this as:

- max $\frac{1}{∥θ∥}$ min $\frac{1}{2}∥θ∥^2$

We can regularise the solutions by trying to penalise large values of $∥θ∥$ and $∥θ∥^2$.
