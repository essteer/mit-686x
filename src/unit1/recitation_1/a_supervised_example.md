# Supervised Learning Example

We begin with x and y, which a connected via f, a function that determines their relationship.

It may be that x represents tumour size, or tumour texture, and y is benign or malignant.

Our goal is to derive a function, f<sub>est</sub>, that approximates f.

**Preparing the training set**

First of all, we must obtain data to build a model on; we collect data from x, and observe the corresponding outputs from y.

Let's call those sets x<sub>data</sub> and y<sub>data</sub>; these constitute the training dataset of our model.

The relationship between x<sub>data</sub> and y<sub>data</sub> is f<sub>data</sub>.

Given our objective, to identify f<sub>est</sub> that approximates f, we can first try to establish an f<sub>est</sub> that approximates f<sub>data</sub>, since f<sub>data</sub> is based on subsets of x and y.

**Note**: this is an asssumption, and not necessarily the best means to approach the problem.

- assume: f<sub>est</sub> ~ f<sub>data</sub>

**Parameterise**

We then set some guidelines, stating that f<sub>est</sub> is dependent on parameters θ and θ<sub>0</sub>:

- f<sub>est</sub> (θ, θ<sub>0</sub>)

To find f<sub>est</sub>, we can take an optimisation approach: we seek to find θ and θ<sub>0</sub> such that they minimise some objective function, J.

**Objective function**

The objective function J is equal to a loss term that describes how different our function f<sub>est</sub> is from f<sub>data</sub>:

- J = L (f<sub>est</sub>, f<sub>data</sub>)

The loss term is therefore actually dependent on θ and θ<sub>0</sub>, which describe f<sub>est</sub>, and our training data, x<sub>data</sub> and y<sub>data</sub>, which describe f<sub>data</sub>:

- J = L (θ, θ<sub>0</sub>, x<sub>data</sub>, y<sub>data</sub>)

If the goal was solely to find an approximation to f<sub>data</sub>, then this approximation would suffice.

However, f<sub>data</sub> may differ from f, our true goal:

- f<sub>data</sub> ≠ f

**Regularisation term**

For this reason, we must add a regularisation term to the objective function J, since currently we may do a poor job of deriving f<sub>est</sub> that approximates f:

- J = L (θ, θ<sub>0</sub>, x<sub>data</sub>, y<sub>data</sub>) + R(θ)

This regularisation term, R, constrains f<sub>est</sub>, so that it does not become too similar to f<sub>data</sub>, and thereby become unable to generalise to data not included in the training dataset; i.e., x's that are not in x<sub>data</sub>.

**Note**: the loss and regularisation terms will vary depending on their application.

**Hyperparameter α**

To balance the loss and regularisation terms, L and R, we introduce the hyperparameter α:

- J = L (θ, θ<sub>0</sub>, x<sub>data</sub>, y<sub>data</sub>) + αR(θ)

This α is unique, in that it is a value we must choose.

It determines how much weight we place on the loss term, and how much weight we place on the regularisation term.

**Note**: unlike θ and θ<sub>0</sub>, α is not determined by the objective function J.

To determine the value of α appropriate to our model, we use **cross validation**.
