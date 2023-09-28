# Error Decomposition and the Bias-Variance Trade-Off

In the lecture, we intuitively defined the structural and estimation mistakes. Here we provide a more formal definition of these ideas for a regression problem.

Suppose we want to learn the relationship between random variables x ∈ ℝ<sup>d</sup> and y ∈ ℝ, where the ground truth relationship is y = f(x).

Of course f is unknown to us, but we observe a training set (x<sub>1</sub>, y<sub>1</sub>), (x<sub>2</sub>, y<sub>2</sub>), ⋯, (x<sub>n</sub>, y<sub>n</sub>) and we hope to find a function f^ to approximate the true function f.

However, our observed data might not be accurate as there can be many kinds of noise and uncertainty containing in the data.

Thus, we further assume a random noise variable ε is added on top of y:

y = f(x) + ε

where ε ~ N (0, σ<sup>2</sup>)

We learned from the lecture that we can find f^ by minimizing the empirical risk on the training set. As we know the training set is a random observation of the underlying relationship and contains noise, different training set will give us different estimator f^(x).

Hence, we can define 𝔼 [f^ (x)] to be the expected estimator over all possible training sets.

Now let's look at when we have a new x with unknown y, what the expected prediction error looks like for our estimator given all possible training sets:

𝔼 [(y - f^(x))] = 𝔼 [(f(x) + ε - f^(x))<sup>2</sup>]

= (f(x) - 𝔼 [f^ (x)])<sup>2</sup> + 𝔼 [(f^ (x) - 𝔼 [f^ (x)])<sup>2</sup>] + 𝔼 [ ε<sup>2</sup> ]

We skip some derivations of this result, can you get this result on your own?

As we can see, there are three terms in this error decomposition:

The first term is the square of the difference between the true f(x) and the expected estimation over all possible training sets. This term is usually called **bias** and it describes how much the average estimator fitted over all datasets deviates from the underlying true f(x). This corresponds to the structural mistake in the lecture.

(f(x) - 𝔼 [f^ (x)])<sup>2</sup>

The second term is the variance of the estimator (recall variance definition in statistics). It describes on average how much a single estimator deviates from the expected estimator over all data sets. This corresponds to the estimation error in the lecture.

𝔼 [(f^ (x) - 𝔼 [f^ (x)])<sup>2</sup>]

The third term 𝔼 [ ε<sup>2</sup> ] = σ <sup>2</sup> is the error from the inherent noise of the data and we can do nothing to minimize it, thus it is sometimes called **irreducible error**. The irreducible error gives a lower bound on the expected prediction error.

𝔼 [ ε<sup>2</sup> ]

Question to think about:

Apparently, the empricial risk is just an approximation of the true risk (i.e. 𝔼 [(f(x) - f^(x))<sup>2</sup>]). If we were able to learn the model by minimizing the true risk, which part of the error decomposition will become 0?

The task of supervised learning is to reduce the bias and variance at the same time, but because of the noise in the training data, it is not possible to simultaneously minimize these two sources of errors. This is known as the **bias-variance trade-off**.

To reduce bias, we can assume a more complex hypothesis space and fit a more powerful model. The model will be able to fit even the noise in the training set. However, this increases the error from variance because given another training set, the randomness of the noise will result in a very different model.

This situation is often called '**overfitting**'.

On the other hand, we can have a more simple model to reduce the variance, but this can make the bias very large.

For example, in the extreme case, let our model be f^(x) = c, where c is a constant. This will give us 0 variance but you can imagine it can hardly makes any correct predictions.

This situation is known as '**underfitting**'.

We will see how regularization can be used to restrict the complexity for linear regression so that we will be able to search for a sweet spot where the total error from variance and bias is the minimum.
