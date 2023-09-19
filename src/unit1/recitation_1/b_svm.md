# Support Vector Machine

Objective function J (from a_supervised_example.md):

- J = L (θ, θ<sub>0</sub>, x<sub>data</sub>, y<sub>data</sub>) + αR(θ)

**Goal**

The goal of the support vector machine (SVM) is to maximise the margin of the decision boundary (DB).

**Margin**

The margin is defined as follows: consider a dataset D, with points x<sup>(i)</sup> and y<sup>(i)</sup>:

- D: { (x<sup>(i)</sup> and y<sup>(i)</sup>) }, i=1,⋯,n

We calculate the distance from point i to the DB, γ:

- γ = (y<sup>(i)</sup> (θ•x<sup>(i)</sup> + θ<sub>0</sub>)) / ∥θ∥

This γ therefore represents the distance between each of the points in D, and the DB.

The margin, d, is defined as the minimum distance between any of the points and the DB:

- d = min (x<sup>(i)</sup>, y<sup>(i)</sup>) ∈ D γ (x<sup>(i)</sup>,y<sup>(i)</sup>,θ,θ<sub>0</sub>)

Where γ is a function of x<sup>(i)</sup>, y<sup>(i)</sup>, θ, and θ<sub>0</sub>.

In SVM, we want to maximise the margin, d, since at the point when d is maximised, our model has greater ability to generalise.

**Hinge loss for SVM**

For SVM, the loss term is equal to the **hinge loss**.

- L<sub>h</sub> = f (γ / γ<sub>ref</sub>), specifically:

  - 1 - (γ / γ<sub>ref</sub>), for γ < γ<sub>ref</sub>
  - 0, otherwise

**What happens to the loss for different values of γ?**

When γ > γ<sub>ref</sub>, we are in the second condition above, and the loss = 0.

When 0 < γ < γ<sub>ref</sub>, then 0 <= L<sub>h</sub> <= 1

- When γ = γ<sub>ref</sub>, then 1 - (γ / γ<sub>ref</sub>) = 0.
- When γ = 0, then 1 - (γ / γ<sub>ref</sub>) = 1.
- For even smaller values of γ, the loss will continue to grow linearly.

**What is γ<sub>ref</sub>?**

γ<sub>ref</sub> is the margin of the DB.

When a negative point is beyond the margin, i.e. γ > γ<sub>ref</sub>:

- then the classification of that point is correct,
- it is outside of the support vectors, and
- we incur 0 loss.

When 0 < γ < γ<sub>ref</sub>, such that the negative point is between the support vector and the DB:

- we begin to incur loss, between 0 and 1.

When the negative point is actually mislabeled, and is on the positive side of the DB:

- γ < 0, and
- we begin to incur even more loss > 1.

**Regularisation term for SVM**

Recall that the goal of the regularisation term, is to allow our model to be more generalisable.

To become more generalisable, we want a large margin.

Above we defined γ<sub>ref</sub> as our margin:

- ∴ we want to maximise γ<sub>ref</sub>.

- Put another way, we want to minimise (1 / γ<sub>ref</sub>).

We rephrase in this way because in our objective function J, we are seeking minimisation - so this puts the goals on the same terms.

In practice, what we actually do is:

- minimise (1 / γ<sub>ref</sub><sup>2</sup>)

This achieves the same goal, but squaring γ<sub>ref</sub> is the convention.

## Objective function for SVM

Putting the pieces together, we arrive at our objective function for SVM:

Loss term:

- 1/n Σ<sup>n</sup><sub>i=1</sub> L<sub>h</sub> (γ / γ<sub>ref</sub>)

(1/n because we want the average over the data points.)

Regularisaton term:

- α (1 / γ<sub>ref</sub><sup>2</sup>)

Together form the SVM objective function:

J = 1/n Σ<sup>n</sup><sub>i=1</sub> L<sub>h</sub> (γ / γ<sub>ref</sub>) + α (1 / γ<sub>ref</sub><sup>2</sup>)

Recall that we can define γ<sub>ref</sub> in terms of θ and θ<sub>0</sub>.

We then need to examine what γ<sub>ref</sub> is in terms of θ and θ<sub>0</sub>.
