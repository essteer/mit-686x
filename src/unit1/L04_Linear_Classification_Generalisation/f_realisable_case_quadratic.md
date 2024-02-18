# Realisable Case - Quadratic Program

We can also solve the problem, via the optimisation problem.

**Support Vector Machine (SVM)**

SVM finds the maximum margin linear separator by solving the quadratic problem that relates to $J(θ, θ_0)$.

In the realisable case, if we disallow any margin violations, then the quadratic program we must solve is:

- Find $θ$ and $θ_0$ that minimise $\frac{1}{2}∥θ∥^2$ subject to:
  - $(y^{(i)}(θ•x^{(i)} + θ_0)) \geq 1$
  - $i = 1, ⋯, n$

(It is $\geq 1$ since we want all training examples to have $0$ hinge loss, i.e. no margin violations.)

We are trying to:

- minimise the norm/magnitude of the parameter vector
- maximise the margin
- subject to having the training examples on the correct sides of the margin boundaries.

This gives us a quadratic program.

**Solution**

The solution for this case is that there will always be a subset of points that lie exactly on the margin boundaries, because the MBs are at the full extent possible without resulting in loss.
