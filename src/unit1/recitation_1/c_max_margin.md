# Maximum Margin

We saw that for the SVM, $γ_{ref}$ is just the support vector of the decision boundary (DB).

How can we write $γ_{ref}$ in terms of what we know, i.e., $θ$ and $θ_0$?

**$θ$ as a scalable constant**

First, observe that we can scale $θ$ by any constant without changing our DB.

This is because $θ$ describes the orientation of this normal vector, so if scaled by any constant, it will only change the magnitude, but not the orientation - therefore, the DB will not change.

We therefore have some flexibility to alter $θ$.

**$γ_{ref}$**

$γ_{ref}$ is the margin, the distance between the DB and the point closest to the DB.

- Call this point $i=m$:
- $γ_{ref} = \frac{y^m(θ•x^m + θ_0)}{∥θ∥}$

Since we can scale $θ$ to any value, we follow convention and set $θ$ such that:

- $y^m(θ•x^m + θ_0) = 1$

In this case, we can write $γ_{ref}$ as:

- $γ_{ref} = \frac{1}{∥θ∥}$

Thereby rewriting $γ_{ref}$ in terms of something we know, i.e., $θ$.

**Plugging $γ_{ref}$ into the objective function**

We can now plug our value of $γ_{ref}$ into the objective function, and simplify.

$J = \frac{1}{n} \sum\nolimits_{i=1}^{n} L_h(y^{(i)} (θ•x^{(i)} + θ_0)) + α ∥θ∥^2$

So we have our loss term, which is a function of $θ$, $θ_0$, $x_{data}$, and $y_{data}$:

- $\frac{1}{n} \sum\nolimits_{i=1}^{n} L_h(y^{(i)} (θ•x^{(i)} + θ_0))$

And our regularisation term, which is a function of $θ$ alone, $R(θ)$:

- $∥θ∥^2$

The **hyperparameter $α$** is then balancing these terms.

Different values of α will affect the performance of the model.
