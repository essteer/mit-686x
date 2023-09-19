# Cross Validation

Cross validation is the means through which we select the optimal value for hyperparameter α, α<sup>\*</sup>, using only training data.

The idea of cross validation is that, when we have a training data set, consisting of x<sub>data</sub> and y<sub>data</sub>, we can reserve part of the training data set as a validation set.

We do not involve the validation set in the training on the training set.

In effect the validation set then becomes a pseudo test data set, for the purpose of fine-tuning our hyperparameter α.

**Parameter n**

We use parameter n to decide how may times we segment the training data.

For example, with n=5, we segment the training data set into 5.

The actual value of n will vary depending on how much data we have - we need to ensure that as the data is segmented, the segments are still large enough to be representative samples of x<sub>data</sub> and y<sub>data</sub>.

**Example**

Setting n=5, we choose an α and work in a range:

α = α<sub>1</sub>, α<sub>2</sub>, ⋯, α<sub>n</sub>

- where α<sub>1</sub> < α<sub>2</sub> < ⋯ < α<sub>n</sub>

We begin with α<sub>1</sub>, and take the entire training data set.

Because n=5, we segment the training set into 5 equal samples.

We then iterate through different partitions of the 5 segments.

For example, for the first iteration we use the first 4 segments on the training data, and the last segment as the validation set.

Since we have a fixed value of α, α = α<sub>1</sub>, we can calculate how well our model performs on the "test" set of the validation set.

From this, we derive some measure of accuracy:

- acc = s<sub>1</sub>(α<sub>1</sub>)

We then move on to iteration two, in which the segment used to test under iteration one is now part of the 4 training segments, and a different segment becomes the test segment.

Against this second set, we derive:

- acc = s<sub>2</sub>(α<sub>1</sub>)

We repeat this for a total of 5 iterations, to reach n=5.

- acc = s<sub>5</sub>(α<sub>1</sub>)

We now have 5 accuracy values for α<sub>1</sub>, against each of the 5 segments.

- s(α<sub>1</sub>) = 1/n Σ<sup>n</sup><sub>i=1</sub> s<sub>n</sub>(α<sub>1</sub>)

This gives a sense of how well our model will suit unseen testing data, if we set our value of α to α<sub>1</sub>.

We then repeat this process for each value of α in α = α<sub>1</sub>, α<sub>2</sub>, ⋯, α<sub>n</sub>.

This gives us an overarching function:

- S(α)

consisting of the accuracy score for each α.

**α<sup>\*</sup>**

Our goal is then to find the argmax for S(α), and that resulting α<sup>\*</sup> is the α we choose to actual train our model using our training dataset, so that we can expect to have the best performance on unseen data.
