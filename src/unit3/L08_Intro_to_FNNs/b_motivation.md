# Motivation

Motivation to Neural Networks

So far, the ways we have performed non-linear classification involve either first mapping $x$ explicitly into some feature vectors $\phi(x)$ whose coordinates involve non-linear functions of $x$, or in order to increase computational efficiency, rewriting the decision rule in terms of a chosen kernel, i.e. the dot product of feature vectors, and then using the training data to learn a transformed classification parameter.

However, in both cases, the feature vectors are **chosen**. They are not learned in order to improve performance of the classification problem at hand.

Neural networks, on the other hand, are models in which the feature representation is learned jointly with the classifier to improve classification performance.

**Motivation**

So far our classifiers rely on pre-compiled features:

$\hat{y} = sign(\theta • \phi(X))$

This can be rewritten with each $x_{(i)}$ of $X$ (from $x_1$ to $x_d$) as a node for each of the input vector coordinates.

$X$ is mapped to the feature representation $\phi(X)$, which can also be written as nodes - and may contain many more nodes than $X$ (from $\phi(x_1)$ to $\phi (x_D)$), for instance in the case of polynomial expansion.

We can then take a linear combination of these coordinate values to produce the classification decision.

We then have a single node for the final operation that takes the sign, with inputs of a weighted combination of the features (from the $\phi(_{(i)})$ nodes).

Those weights are $θ_1$, $θ_2$, on to $θ_D$ - there are as many coordinates of $θ$ as there are coordinates in the expanded feature representation.

An aspect of this way of solving a non-linear classification problem, is that the mapping from $X$ to $\phi(X)$ is fixed, rather than being tailored to the particular problem we seek to solve.

A neural network tries to optimise the feature representation for the problem we seek to solve.

**Dilemma**

In order to do a good classification, and learn the parameters for the classification decision, we need to know what the feature representation is.

On the other hand, to know what a good feature representation would be, we need to know what constitutes a good classification for the task at hand.

So, we can try the harder problem of learning the feature representation and classification decision together.
