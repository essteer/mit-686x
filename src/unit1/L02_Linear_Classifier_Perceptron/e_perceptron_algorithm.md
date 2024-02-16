# Perceptron Algorithm

We defined training error for any classifier, as a fraction of training examples that are misclassified.

$E_n(h) = \frac{1}{n} \sum_{i=1}^{n} [[h(x^{(i)}) \neq y^{(i)}]]$

### Training error for linear classifier through the origin

For linear classifiers through the origin, we can write this slightly differently, since each classifier is characterised by a parameter vector θ, we can review simply whether the sign agrees with the linear prediction:

- $E_n(θ) = \frac{1}{n} \sum_{i=1}^{n} [[y^{(i)} θ•x^{(i)} <= 0]]$
- If this $<= 0$, then a linear classifier that is the sign of the dot product $θ•x^{(i)}$ would be different than the given label.
- When it is exactly $0$, i.e. it lies precisely on the decision boundary, we count it as an error, since we cannot be confident which way to classify that point.

### Training error for general linear classifier

$E_n(θ, θ_0) = \frac{1}{n} \sum_{i=1}^{n} [[y^{(i)} (θ•x^{(i)}+θ_0) <= 0]]$

It is an error, if it is $<=0$.

### Perceptron learning algorithm - initial version

- procedure $PERCEPTRON(\{(x^{(i)},y^{(i)}), i=1,⋯,n\}, T)$
  - $θ = 0$ (vector)
  - for $t=1, ⋯, T$ do
    - for $i=1, ⋯, n$ do
      - if $y^{(i)}(0) (θ•x^{(i)}) <= 0$ then
      - $θ = θ + y^{(i)}x^{(i)}$
  - return $θ$

This initial iteration of the perceptron algorithm takes in a training set, and finds the parameter vector $θ$.

$θ = 0$ (vector)

If $y^{(i)}(θ•x^{(i)}) <= 0$,
then $θ = θ + y^{(i)}x^{(i)}$.

I.e., if there are any classifiers through the origin that correctly separate the data, the algorithm will find a solution.

We start with a parameteter vector $θ = 0$, and go through the $i$-th examples of the training set, and check whether they are correct.

If there is an error, then we update the parameters to correct for that error.

At the point at which the perceptron algorithm updates the parameter vector, $θ = θ + y^{(i)}x^{(i)}$:

- The new value of θ is set as the old θ, plus the scalar label $y^{(i)}$ multiplied by the vector training example.

$y^{(i)} (0 + y^{(i)}x^{(i)}) • x^{(i)} = ∥x^{(i)}∥^2 > 0$

$θ$ in the above expression is initially set to $0$, which always results in error and thus an incrementation via the perceptron algorithm.

- The label $y^{(i)}$ multiplied by itself is always 1, since it is either 1 or -1.
- Also, a vector in a product of itself, gives the squared norm of that vector.

Since the update step:

$y^{(i)} (0 + y^{(i)}x^{(i)}) • x^{(i)} = ∥x^{(i)}∥^2 > 0$

is now positive, if the same example passed in initially was passed in again, it would not be classified incorrectly anymore.

### Note

The algorithm iterates through the set of training examples.

Therefore, since the different examples may nudge the algorithm in different directions, examples that were adjusted for earlier so that they could be correctly classified, may no longer be correctly classified as a result of subsequent adjustments.

- Therefore, the algorithm must go through the entire training set $T$ times, repeated times.

Theoretically, if a linear classifier solution for the training set exists, the perceptron algorithm will find a solution - though this is a brute force method, so it may take a long time for a sufficiently large $T$.

### Perceptron algorithm with offset $θ_0$

- procedure $PERCEPTRON({(x^{(i)},y^{(i)}), i=1,⋯,n}, T)$
  - $θ = 0$ (vector), $θ_0$ (scalar)
  - for $t=1, ⋯, T$ do
    - for $i=1, ⋯, n$ do
      - if $y^{(i)}(0) (θ•x^{(i)} + θ_0) <= 0$ then
        - $θ = θ + y^{(i)}x^{(i)}$
        - $θ_0 = θ_0 + y^{(i)}$
  - return $θ, θ_0$

If we take an arbitrary $x$, where $θ•x+θ_0$:

We can write this slightly differently, as if it were a linear classifier through origin, but taking slightly different examples.

$θ•x+θ_0 = [θ, θ_0]$ with $θ_0$ as the last coordinate, and then write down the example, with 1 as the last coordinate:

$θ•x+θ_0 = [θ, θ_0][x, 1]$

Effectively, we can think of the linear classifier with offset parameter, as a linear classifier through origin, that is just operating on slightly different examples.
