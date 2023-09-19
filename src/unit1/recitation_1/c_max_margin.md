# Maximum Margin

We saw that for the SVM, γ<sub>ref</sub> is just the support vector of the decision boundary (DB).

How can we write γ<sub>ref</sub> in terms of what we know, i.e., θ and θ<sub>0</sub>?

**θ as a scalable constant**

First, observe that we can scale θ by any constant without changing our DB.

This is because θ describes the orientation of this normal vector, so if scaled by any constant, it will only change the magnitude, but not the orientation - therefore, the DB will not change.

We therefore have some flexibility to alter θ.

**γ<sub>ref</sub>**

γ<sub>ref</sub> is the margin, the distance between the DB and the point closest to the DB.

- Call this point i=m:
- γ<sub>ref</sub> = y<sup>m</sup>(θ•x<sup>m</sup> + θ<sub>0</sub>) / ∥θ∥

Since we can scale θ to any value, we follow convention and set θ such that:

- y<sup>m</sup>(θ•x<sup>m</sup> + θ<sub>0</sub>) = 1

In this case, we can write γ<sub>ref</sub> as:

- γ<sub>ref</sub> = 1 / ∥θ∥

Thereby rewriting γ<sub>ref</sub> in terms of something we know, i.e., θ.

**Plugging γ<sub>ref</sub> into the objective function**

We can now plug our value of γ<sub>ref</sub> into the objective function, and simplify.

J = 1/n Σ<sup>n</sup><sub>i=1</sub> L<sub>h</sub> (y<sup>(i)</sup> (θ•x<sup>(i)</sup> + θ<sub>0</sub>)) + α∥θ∥<sup>2</sup>

So we have our loss term, which is a function of θ, θ<sub>0</sub>, x<sub>data</sub>, and y<sub>data</sub>:

- 1/n Σ<sup>n</sup><sub>i=1</sub> L<sub>h</sub> (y<sup>(i)</sup> (θ•x<sup>(i)</sup> + θ<sub>0</sub>))

And our regularisation term, which is a function of θ alone, R(θ):

- ∥θ∥<sup>2</sup>

The **hyperparameter α** is then balancing these terms.

Different values of α will affect the performance of the model.
