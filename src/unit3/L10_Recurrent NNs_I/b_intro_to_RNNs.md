# Introduction to Recurrent Neural Networks

**Temporal / Sequence Problems**

Take an example problem, such as USD to EUR exchange rates from 2012 to 2017; we want to predict the exchange rates for the next (unknown) time period.

This can be cast as a supervised learning problem.

Historical data can be broken down into feature vectors and target values - known as a **sliding window**.

$\phi(t) = [0.82, 0.80, 0.73, 0.72]^T$

$y(t) = 0.89$

Where the values in $\phi(t)$ correspond to $y(t-1), y(t-2)$, and so on.

This feature vector, $\phi(t)$, is based on the previous values, and we use it to produce a prediction for the next value at time $t$.

**Language modeling**

Predicting what comes next in a sentence:

"$This \; course \; has \; been \; a \; tremendous...$"

We translate the history of what has been seen into a feature vector, and try to use the feature vector to make a prediction.

We might look back, e.g., 2 words, and translate each of those into vectors, which are concatenated to create a feature vector that can be used for prediction.

The words are one-hot encoded with sparse vectors:

$tremendous: [0 \; 0 \; ... \; 1 \; 0]$  
$a: [1 \; 0 \; ... \; 0]$

We concatenate these word vectors into our feature vector $\phi(t)$, a long sparse feature vector we can now use to relate to possible outcomes - what comes next.

We can also continue to work backwords and construct training examples by using e.g. "$been$" and "$a$" to train on predicting "$tremendous$".

**Issues with this approach**

Sequence prediction problems can be recast in a form amenable to feed-forward NNs.

But, we must engineer how "history" is mapped to a vector representation.

This vector is then fed into a NN.

But how many steps back should be considered?

How do we retain important items mentioned far back in the sequence? The sequences will be of variable length, but key terms may be mentioned early on, and so must somehow be retained.

Instead, we need a more flexible way to encode "history" (sequences) into feature vectors.
