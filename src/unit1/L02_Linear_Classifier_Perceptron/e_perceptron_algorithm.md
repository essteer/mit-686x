# Perceptron Algorithm

We defined training error for any classifier, as a fraction of training examples that are misclassified.

- `E`<sub>`n`</sub>`(h) = 1/n Σ`<sup>`n`</sup><sub>`i=1`</sub>` [[h(x`<sup>`(i)`</sup>`) != y`<sup>`(i)`</sup>`]]`

**Training error for linear classifier through the origin**

For linear classifiers through the origin, we can write this slightly differently, since each classifier is characterised by a parameter vector ϴ, we can review simply whether the sign agrees with the linear prediction:

- `E`<sub>`n`</sub>`(ϴ) = 1/n Σ`<sup>`n`</sup><sub>`i=1`</sub>` [[y`<sup>`(i)`</sup>` ϴ•x`<sup>`(i)`</sup>` <= 0]]`
- If this <= 0, then a linear classifier that is the sign of the dot product ϴ•x<sup>(i)</sup> would be different than the given label.
- When it is exactly 0, i.e. it lies precisely on the decision boundary, we count it as an error, since we cannot be confident which way to classify that point.

**Training error for general linear classifier**

- `E`<sub>`n`</sub>`(ϴ, ϴ`<sub>`0`</sub>`) = 1/n Σ`<sup>`n`</sup><sub>`i=1`</sub>` [[y`<sup>`(i)`</sup>` (ϴ•x`<sup>`(i)`</sup>`+ϴ`<sub>`0`</sub>`) <= 0]]`

- It is an error, if it is <=0.

**Perceptron learning algorithm - initial version**

- procedure PERCEPTRON({(x<sup>(i)</sup>,y<sup>(i)</sup>), i=1,⋯,n}, T)
  - ϴ = 0 (vector)
  - for t=1, ⋯, T do
    - for i=1, ⋯, n do
      - if y<sup>(i)</sup>(0) (ϴ•x<sup>(i)</sup>) <= 0 then
      - ϴ = ϴ + y<sup>(i)</sup>x<sup>(i)</sup>
  - return ϴ

This initial iteration of the perceptron algorithm takes in a training set, and finds the parameter vector ϴ.

ϴ = 0 (vector)

If `y`<sup>`(i)`</sup>`(ϴ•x`<sup>`(i)`</sup>`) <= 0`,
then `ϴ = ϴ + y`<sup>`(i)`</sup>`x`<sup>`(i)`</sup>``.

I.e., if there are any classifiers through the origin that correctly separate the data, the algorithm will find a solution.

We start with a parameteter vector ϴ = 0, and go through the i-th examples of the training set, and check whether they are correct.

If there is an error, then we update the parameters to correct for that error.

At the point at which the perceptron algorithm updates the parameter vector, `ϴ = ϴ + y`<sup>`(i)`</sup>`x`<sup>`(i)`</sup>``:

- The new value of ϴ is set as the old ϴ, plus the scalar label y`<sup>`(i)`</sup>` multiplied by the vector training example.

`y`<sup>`(i)`</sup>` (0 + y`<sup>`(i)`</sup>`x`<sup>`(i)`</sup>`) • x`<sup>`(i)`</sup>` = ∥x`<sup>`(i)`</sup>`∥`<sup>`2`</sup>` > 0`

ϴ in the above expression is initially set to 0, which always results in error and thus an incrementation via the perceptron algorithm.

- The label y<sup>(i)</sup> multiplied by itself is always 1, since it is either 1 or -1.
- Also, a vector in a product of itself, gives the squared norm of that vector.

Since the update step:

`y`<sup>`(i)`</sup>` (0 + y`<sup>`(i)`</sup>`x`<sup>`(i)`</sup>`) • x`<sup>`(i)`</sup>` = ∥x`<sup>`(i)`</sup>`∥`<sup>`2`</sup>` > 0`

is now positive, if the same example passed in initially was passed in again, it would not be classified incorrectly anymore.

**Note**

The algorithm iterates through the set of training examples.

Therefore, since the different examples may nudge the algorithm in different directions, examples that were adjusted for earlier so that they could be correctly classified, may no longer be correctly classified as a result of subsequent adjustments.

- Therefore, the algorithm must go through the entire training set T times, repeated times.

Theoretically, if a linear classifier solution for the training set exists, the perceptron algorithm will find a solution - though this is a brute force method, so it may take a long time for a sufficiently large T.

**Perceptron algorithm with offset ϴ<sub>0</sub>**

- procedure PERCEPTRON({(x<sup>(i)</sup>,y<sup>(i)</sup>), i=1,⋯,n}, T)
  - ϴ = 0 (vector), ϴ<sub>0</sub> (scalar)
  - for t=1, ⋯, T do
    - for i=1, ⋯, n do
      - if y<sup>(i)</sup>(0) (ϴ•x<sup>(i)</sup>) <= 0 then
        - ϴ = ϴ + y<sup>(i)</sup>x<sup>(i)</sup>
        - ϴ<sub>0</sub> = ϴ<sub>0</sub> + y<sup>(i)</sup>
  - return ϴ, ϴ<sub>0</sub>

If we take an arbitrary x, where:

`   ϴ•x+ϴ`<sub>`0`</sub>``

We can write this slightly differently, as if it were a linear classifier through origin, but taking slightly different examples.

`   ϴ•x+ϴ`<sub>`0`</sub>` = [ϴ, ϴ`<sub>`0`</sub>`]` with ϴ<sub>0</sub> as the last coordinate, and then write down the example, with 1 as the last coordinate:

`   ϴ•x+ϴ`<sub>`0`</sub>` = [ϴ, ϴ`<sub>`0`</sub>`][x, 1]`

Effectively, we can think of the linear classifier with offset parameter, as a linear classifier through origin, that is just operating on slightly different examples.
