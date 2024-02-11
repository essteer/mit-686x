# Review of Basic Concepts

**Feature vectors, labels**:

$x ∈ ℝ^d$  
$y ∈ \{-1, 1\}$

**Training set** - task given to the algorithm:

$S_n = \{(x^{(i)}, y^{(i)}), i=1,⋯,n\}$

**Classifier**:

$h: ℝ^d ⟶ \{-1, 1\}$, e.g. $h(x) = 1$

A mapping of any point in $ℝ^d$ to $+1/-1$, divides the space into two halves so that we can observe shaded areas on the plane that relate to e.g., the positive set of results on the plane:

$X+ = \{x ∈ ℝ^d: h(x) = 1\}$ (positive half)  
$X- = \{x ∈ ℝ^d: h(x) = -1\}$ (negative half)

These together comprise the $R^d$ space.

**Two ways to evaluate the classifier**:

Training error, which we have access to:

- $E_n(h) = \frac{1}{n} Σ_{i=1}^n [[h(x^{(i)}) ~!= y^{(i)}]]$

  - $= 1$ if error
  - $= 0$ otherwise
  - A classifier that correctly identified all of the training set labels, would have $E_n(h) = 0$.

Test error, which we want to minimise the most:

- $E(h)$
- Essentially applying our training error evaluation to the model's performance on the test set (the $n$ is dropped here).
- I.e., the problem of **generalisation**.

**Generalisation**

We can affect generalisation by limiting the choices that we have, at the time of considering minimising the training error.

**Set of classifiers** - the choices we have, the set of hypotheses:

$h ∈ H$, since $h$ is a limited selection out of the full set of possible classifiers.

**Training set example**

$x = [x_1, x_2] ∈ ℝ^d, d = 2$
