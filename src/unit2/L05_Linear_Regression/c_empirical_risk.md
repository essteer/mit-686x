# Objective: Empirical Risk

Intuitively, we want to quantify how much our predictions deviate from the known value of y.

This objectives is known as empirical risk, R, using n training examples, and depending on our parameter of θ.

R<sub>n</sub>(θ)

We continue to assume that θ<sub>0</sub> is equal to 0.

For every point in our training set, we want to compute the extent of the deviation (the loss), which we then want to sum and average - hence the 1/n in the below formulation:

R<sub>n</sub>(θ) = 1/n Σ<sup>n</sup><sub>i=1</sub>

From there, we want to define loss - in this case, squared error.

We compute the difference between the true value, y<sup>(i)</sup>, and what we predicted with θx<sup>i</sup>, square this, and divide by two.

R<sub>n</sub>(θ) = 1/n Σ<sup>n</sup><sub>i=1</sub> (y<sup>(i)</sup> - θx<sup>(i)</sup>)<sup>2</sup> / 2

**Why square the difference?**

Squaring the difference means that larger deviations from the true value will be more heavily penalised.

Larger differences result in much higher errors.

**What are we trying to optimise?**

The goal is not to optimise for the training set, it is to optimise for generalisation.

So, if we have n prime examples, we want to look at the empirical risk on our test data.

R<sub>n'</sub> (θ) = 1/n' Σ<sup>n+n'</sup><sub>i=n+1</sub> (y<sup>(i)</sup> - θx<sup>i</sup>)<sup>2</sup> / 2

However, since we don't have access to the test data, the best we can do is look at the training objective, and try to minimise the error there while also attempting to ensure it can generalise.

**Two common mistakes**

There are two types of mistake that commonly occur at this point.

First, **structural mistakes**.

Perhaps the linear function is not sufficient to model the data - the mapping between the training vectors and the ys may be highly non-linear, in which case any attempt to use linear methods will incur large error.

Instead of just considering linear mappings, a much broader set of functions should be considered.

Second, **estimation mistakes**.

Even if we know the mapping is linear, but we have very limited training data, we cannot estimate it correctly, and still have large error.

These errors pull in opposite directions: on one hand, we want a model complex enough to accurately model the training set, but on the other hand a model with many parameters will likely result in estimation error, since the same training set must try to estimate many parameters.

If we try to minimise the parameters involved, we may end up with structural error as a poor estimation of the data.
