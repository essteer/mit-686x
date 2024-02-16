# Linear Regression

**Classification**

Recap: the classification model used so far involved a training set consisting of pairs of examples.

The examples were feature vectors associated with labels.

There were n examples, and the goal of the classifier was to learn the mapping between the feature vectors.

$S_n = \{ ( x^{(i)}, y^{(i)}) | i=1, ⋯, n \}$

$x^{(i)} ∈ ℝ^d, y^{(i)} ∈ \{ -1, +1 \}$

Example use: decision over whether to buy or sell a stock. Perhaps the price of a stock is tracked every minute, regarding whether it rises or falls in price. The model has access to historic data in terms of d days of data, and uses this to recommend a buy or sell action (+1 or -1) based on the current situation.

In many problems, it is not enough to have a binary yes/no question, we may want to know the extent of what is happening - e.g., how much do we expect the price to increase, rather than just whether it is predicted to increase.

This is where regression comes in: when we are interested in a **continuous value**. It could be cost, or temperature, etc.

**Regression**

The setup is similar to that of classification, we are provided with n examples of feature vectors, and in this case, values.

Instead of assuming that y comes from +1 or -1, we now assume that:

$y^{(i)} ∈ ℝ$

We then must learn how to map feature vectors into those continuous values.

**Linear Regression**

What is the significance of it being "linear" regression?

We can write, for example a function $f$ that takes $x$, and has parameter values such as $θ$ and $θ_0$:

$f(x; θ, θ_0)$

We then add in linear weighting of the $x$ coordinates.

This can be written explicitly as:

$f(x; θ, θ_0) = \sum_{i=1}^{d} θ_i x_i + θ_0$

So, we sum all of the coordinates from $1$ to $d$, weigh them by the corresponding parameters, and add an offset $θ_0$.

This can also be written compactly as:

$f(x; θ, θ_0) = θx + θ_0$

As before, we make the assumption that $θ_0 = 0$.

**Question**

So, we have a linear function, but what if the values we are interested in observing are complex? Will the model be weak because we have limited ourselves to a linear function?

In practice, we can still use a linear classifier, by ensuring appropriate representation over the feature vector.

If the feature vectors are constructed carefully, then linear regression may be sufficient.

For now, assume that appropriate feature vectors have been provided.

**Finding the appropriate linear regression**

How can we know whether our function is doing the right thing? There are many $θ$, how do we know which one is correct?

We need an appropriate objective that can quantify the extent of our mistakes.

The second problem to address, is how we do the learning; even with an appropriate objective, we still need to be able to effectively utilise our training data to find the best parameters.

We will examine two algorithms for this purpose: a gradient-based algorithm, seen in the classification example, and an algorithm that can solve the problem directly in closed form (without approximation).

Finally, we need to determine regularisation.

When training on our objective, we want to know how well we fit the data, but there could be issues such as not having enough data.

There could also be noise in the data; straining to fit to the data could then cause overfitting to the training data.

In summary, the three key factors to determine are:

1. Objective
2. Learning algorithm: gradient-based / closed-form
3. Regularisation
