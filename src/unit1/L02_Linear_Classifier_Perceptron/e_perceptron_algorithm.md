# Perceptron Algorithm

We defined training error for any classifier, as a fraction of training examples that are misclassified.

- `E_n(h) = 1/n n_Σ_i=1 [[h(x^(i)) != y^(i)]]`

**Training error for linear classifier through the origin**

For linear classifiers through the origin, we can write this slightly differently, since each classifier is characterised by a parameter vector ϴ, we can review simply whether the sign agrees with the linear prediction:

- `E_n(ϴ) = 1/n n_Σ_i=1 [[y^(i) ϴ•x^(i) <= 0]]`
- If this <= 0, then a linear classifier that is the sign of the dot product ϴ•x^(i) would be different than the given label.
- When it is exactly 0, i.e. it lies precisely on the decision boundary, we count it as an error, since we cannot be confident which way to classify that point.

**Training error for general linear classifier**

- `E_n(ϴ, ϴ_0) = 1/n n_Σ_i=1 [[y^(i) (ϴ•x^(i)+ϴ_0) <= 0]]`

- It is an error, if it is <=0.

**Perceptron learning algorithm - initial version**

`procedure PERCEPTRON({(x^(i),y^(i)), i=1,...,n}, T)`
`   ϴ = 0 (vector)`
`   for t=1, ..., T do`
`       for i=1, ..., n do`
`           if y^(i)(0) (ϴ•x^(i)) <= 0 then`
`               ϴ = ϴ + y^(i)x^(i)`
`   return ϴ`

This initial iteration of the perceptron algorithm takes in a training set, and finds the parameter vector ϴ.

ϴ = 0 (vector)

If `y^(i)(ϴ•x^(i)) <= 0`,
then `ϴ = ϴ + y^(i)x^(i)`.

I.e., if there are any classifiers through the origin that correctly separate the data, the algorithm will find a solution.

We start with a parameteter vector ϴ = 0, and go through the i-th examples of the training set, and check whether they are correct.

If there is an error, then we update the parameters to correct for that error.

At the point at which the perceptron algorithm updates the parameter vector, `ϴ = ϴ + y^(i)x^(i)`:

- The new value of ϴ is set as the old ϴ, plus the scalar label y^(i) multiplied by the vector training example.

`y^(i) (0 + y^(i)x^(i)) • x^(i) = ||x^(i)||^2 > 0`

ϴ in the above expression is initially set to 0, which always results in error and thus an incrementation via the perceptron algorithm.

- The label y^(i) multiplied by itself is always 1, since it is either 1 or -1.
- Also, a vector in a product of itself, gives the squared norm of that vector.

Since the update step:

`y^(i) (0 + y^(i)x^(i)) • x^(i) = ||x^(i)||^2 > 0`

is now positive, if the same example passed in initially was passed in again, it would not be classified incorrectly anymore.

**Note**

The algorithm iterates through the set of training examples.

Therefore, since the different examples may nudge the algorithm in different directions, examples that were adjusted for earlier so that they could be correctly classified, may no longer be correctly classified as a result of subsequent adjustments.

- Therefore, the algorithm must go through the entire training set T times, repeated times.

Theoretically, if a linear classifier solution for the training set exists, the perceptron algorithm will find a solution - though this is a brute force method, so it may take a long time for a sufficiently large T.

**Perceptron algorithm with offset ϴ_0**

`procedure PERCEPTRON({(x^(i),y^(i)), i=1,...,n}, T)`
`   ϴ = 0 (vector), ϴ_0 (scalar)`
`       for t=1, ..., T do`
`           for i=1, ..., n do`
`               if y^(i)(0) (ϴ•x^(i)) <= 0 then`
`                   ϴ = ϴ + y^(i)x^(i)`
`                   ϴ_0 = ϴ_0 + y^(i)`
`   return ϴ, ϴ_0`

If we take an arbitrary x, where:

`   ϴ•x+ϴ_0`

We can write this slightly differently, as if it were a linear classifier through origin, but taking slightly different examples.

`   ϴ•x+ϴ_0 = [ϴ, ϴ_0]` with ϴ_0 as the last coordinate, and then write down the example, with 1 as the last coordinate:

`   ϴ•x+ϴ_0 = [ϴ, ϴ_0][x, 1]`

Effectively, we can think of the linear classifier with offset parameter, as a linear classifier through origin, that is just operating on slightly different examples.
