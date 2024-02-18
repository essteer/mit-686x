# Support Vector Machine

Objective function $J$ (from a_supervised_example.md):

- $J = L(θ, θ_0, x_{data}, y_{data}) + αR(θ)$

**Goal**

The goal of the support vector machine (SVM) is to maximise the margin of the decision boundary (DB).

**Margin**

The margin is defined as follows: consider a dataset $D$, with points $x^{(i)}$ and $y^{(i)}$:

- $D: { (x^{(i)}~ and ~y^{(i)}) }, i=1,⋯,n$

We calculate the distance from point $i$ to the DB, $\gamma$:

- $\gamma = \frac{(y^{(i)} (θ•x^{(i)} + θ_0))}{∥θ∥}$

This $\gamma$ therefore represents the distance between each of the points in $D$, and the DB.

The margin, $d$, is defined as the minimum distance between any of the points and the DB:

- $d = min(x^{(i)}, y^{(i)}) ∈ D~\gamma(x^{(i)},y^{(i)},θ,θ_0)$

Where $\gamma$ is a function of $x^{(i)}$, $y^{(i)}$, $θ$, and $θ_0$.

In SVM, we want to maximise the margin, $d$, since at the point when $d$ is maximised, our model has greater ability to generalise.

**Hinge loss for SVM**

For SVM, the loss term is equal to the **hinge loss**.

- $L_h = f (\frac{\gamma}{\gamma_{ref}})$, specifically:

  - $1 - (\frac{\gamma}{\gamma_{ref}})$, for $\gamma < \gamma_{ref}$
  - $0$, otherwise

**What happens to the loss for different values of $\gamma$?**

When $\gamma > \gamma_{ref}$, we are in the second condition above, and the loss = $0$.

When $0 < \gamma < \gamma_{ref}$, then $0 \leq L_h \leq 1$

- When $\gamma = \gamma_{ref}$, then $1 - (\frac{\gamma}{\gamma_{ref}}) = 0$.
- When $\gamma = 0$, then $1 - (\frac{\gamma}{\gamma_{ref}}) = 1$.
- For even smaller values of $\gamma$, the loss will continue to grow linearly.

**What is $\gamma_{ref}$?**

$\gamma_{ref}$ is the margin of the DB.

When a negative point is beyond the margin, i.e. $\gamma > \gamma_{ref}$:

- then the classification of that point is correct,
- it is outside of the support vectors, and
- we incur 0 loss.

When $0 < \gamma < \gamma_{ref}$, such that the negative point is between the support vector and the DB:

- we begin to incur loss, between 0 and 1.

When the negative point is actually mislabeled, and is on the positive side of the DB:

- $\gamma < 0$, and
- we begin to incur even more loss $> 1$.

**Regularisation term for SVM**

Recall that the goal of the regularisation term, is to allow our model to be more generalisable.

To become more generalisable, we want a large margin.

Above we defined $\gamma_{ref}$ as our margin:

- ∴ we want to maximise $\gamma_{ref}$.

- Put another way, we want to minimise $\frac{1}{\gamma_{ref}}$.

We rephrase in this way because in our objective function $J$, we are seeking minimisation - so this puts the goals on the same terms.

In practice, what we actually do is:

- minimise $\frac{1}{\gamma_{ref}^2}$

This achieves the same goal, but squaring $\gamma_{ref}$ is the convention.

## Objective function for SVM

Putting the pieces together, we arrive at our objective function for SVM:

Loss term:

- $\frac{1}{n} \sum_{i=1}^{n} L_h(\frac{\gamma}{\gamma_{ref}})$

($\frac{1}{n}$ because we want the average over the data points.)

Regularisaton term:

- $α (\frac{1}{\gamma_{ref}^2})$

Together form the SVM objective function:

$J = \frac{1}{n} \sum_{i=1}^{n} L_h(\frac{\gamma}{\gamma_{ref}}) + α (\frac{1}{\gamma_{ref}^2})$

Recall that we can define $\gamma_{ref}$ in terms of $θ$ and $θ_0$.

We then need to examine what $\gamma_{ref}$ is in terms of $θ$ and $θ_0$.
