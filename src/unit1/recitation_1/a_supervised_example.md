# Supervised Learning Example

We begin with $x$ and $y$, which are connected via $f$, a function that determines their relationship.

It may be that $x$ represents tumour size, or tumour texture, and $y$ is benign or malignant.

Our goal is to derive a function, $f_{est}$, that approximates $f$.

**Preparing the training set**

First of all, we must obtain data to build a model on; we collect data from $x$, and observe the corresponding outputs from $y$.

Let's call those sets $x_{data}$ and $y_{data}$; these constitute the training dataset of our model.

The relationship between $x_{data}$ and $y_{data}$ is $f_{data}$.

Given our objective, to identify $f_{est}$ that approximates $f$, we can first try to establish an $f_{est}$ that approximates $f_{data}$, since $f_{data}$ is based on subsets of $x$ and $y$.

**Note**: this is an asssumption, and not necessarily the best means to approach the problem.

- assume: $f_{est} ≈ f_{data}$

**Parameterise**

We then set some guidelines, stating that $f_{est}$ is dependent on parameters $θ$ and $θ_0$:

- $f_{est} (θ, θ_0)$

To find $f_{est}$, we can take an optimisation approach: we seek to find $θ$ and $θ_0$ such that they minimise some objective function, $J$.

**Objective function**

The objective function $J$ is equal to a loss term that describes how different our function $f_{est}$ is from $f_{data}$:

- $J = L(f_{est}, f_{data})$

The loss term is therefore actually dependent on $θ$ and $θ_0$, which describe $f_{est}$, and our training data, $x_{data}$ and $y_{data}$, which describe $f_{data}$:

- $J = L(θ, θ_0, x_{data}, y_{data})$

If the goal was solely to find an approximation to $f_{data}$, then this approximation would suffice.

However, $f_{data}$ may differ from $f$, our true goal:

- $f_{data} ≠ f$

**Regularisation term**

For this reason, we must add a regularisation term to the objective function $J$, since currently we may do a poor job of deriving $f_{est}$ that approximates $f$:

- $J = L(θ, θ_0, x_{data}, y_{data}) + R(θ)$

This regularisation term, $R$, constrains $f_{est}$, so that it does not become too similar to $f_{data}$, and thereby become unable to generalise to data not included in the training dataset; i.e., $x$'s that are not in $x_{data}$.

**Note**: the loss and regularisation terms will vary depending on their application.

**Hyperparameter α**

To balance the loss and regularisation terms, $L$ and $R$, we introduce the hyperparameter $α$:

- $J = L(θ, θ_0, x_{data}, y_{data}) + αR(θ)$

This $α$ is unique, in that it is a value we must choose.

It determines how much weight we place on the loss term, and how much weight we place on the regularisation term.

**Note**: unlike $θ$ and $θ_0$, $α$ is not determined by the objective function $J$.

To determine the value of $α$ appropriate to our model, we use **cross validation**.
