# Cross Validation

Cross validation is the means through which we select the optimal value for hyperparameter $α$, $α^{*}$, using only training data.

The idea of cross validation is that, when we have a training data set, consisting of $x_{data}$ and $y_{data}$, we can reserve part of the training data set as a validation set.

We do not involve the validation set in the training on the training set.

In effect the validation set then becomes a pseudo test data set, for the purpose of fine-tuning our hyperparameter $α$.

**Parameter $n$**

We use parameter $n$ to decide how may times we segment the training data.

For example, with $n=5$, we segment the training data set into 5 subsets.

The actual value of n will vary depending on how much data we have - we need to ensure that as the data is segmented, the segments are still large enough to be representative samples of $x_{data}$ and $y_{data}$.

**Example**

Setting $n=5$, we choose an α and work in a range:

$α = α_1, α_2, ⋯, α_n$

- where $α_1 < α_2 < ⋯ < α_n$

We begin with $α_1$, and take the entire training data set.

Because $n=5$, we segment the training set into 5 equal samples.

We then iterate through different partitions of the 5 segments.

For example, for the first iteration we use the first 4 segments on the training data, and the last segment as the validation set.

Since we have a fixed value of $α$, $α = α_1$, we can calculate how well our model performs on the "test" set of the validation set.

From this, we derive some measure of accuracy:

- $acc = s_1(α_1)$

We then move on to iteration two, in which the segment used to test under iteration one is now part of the 4 training segments, and a different segment becomes the test segment.

Against this second set, we derive:

- $acc = s_2(α_1)$

We repeat this for a total of 5 iterations, to reach $n=5$.

- $acc = s_5(α_1)$

We now have 5 accuracy values for $α_1$, against each of the 5 segments.

- $s(α_1) = \frac{1}{n} \sum_{i=1}^{n} s_n(α_1)$

This gives a sense of how well our model will suit unseen testing data, if we set our value of $α$ to $α_1$.

We then repeat this process for each value of $α$ in $α = α_1, α_2, ⋯, α_n$.

This gives us an overarching function:

- $S(α)$

consisting of the accuracy score for each $α$.

**$α^{*}$**

Our goal is then to find the $argmax$ for $S(α)$, and that resulting $α^{*}$ is the $α$ we choose to actual train our model using our training dataset, so that we can expect to have the best performance on unseen data.
