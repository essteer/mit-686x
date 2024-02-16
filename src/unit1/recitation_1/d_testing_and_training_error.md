# Testing and Training Error as Regularisation Increases

Objective function J:

$J = L_h(θ, θ_0, x_{data}, y_{data}) + αR(θ)$

When training our objective function, as $α$ increases from $0$, we should see an increase of our objective function.

In terms of accuracy, which is proportional to the inverse of our objective function (since we are trying to minimise our objective function), this will decrease over higher values of $α$.

For the test set, when α is very small, as we increase α we increase the amount of regularisation that has been put on the model, which means our model will generalise better to unseen data.

However, beyond a certain point, we may place too much value on the regularisation term, and make the model so general that it can no longer classify any data set.

We want to find an $α$, $α^{*}$, at which the objective function value is minimised, and the accuracy against the test data performance is maximised.

This is the optimal α we want to use.

The question is how to find $α^{*}$, with only training set data.

The method used is **cross validation**.
