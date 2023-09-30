# Collaborative Filtering: Naive Approach

Think of the problem of recommendation as a standard objective-driven algorithm.

We have our matrix Y, with n users and m movies, with sparse entries.

The goal of our computation is to build a new matrix, X, of the same size n and m, and in which every entry is filled, i.e. has a prediction for every combination of user and movie.

**Empirical risk**

We want to minimise empirical risk, so that for each possible matrix X, we want to know how "good" that matrix is.

Our objective should record the fact, that for data points already known in Y, the predicted value in X for the same element should be the same (or very similar).

So we first write that we progress through all pairs of users and movies that belong to D, where D is all the pairs (a, i) such that the entry y<sub>ai</sub> is given.

That is, the loss on elements we already know should be minimal.

But, we also want regularisation so that we can generalise to the unknown entries.

**Objective**

J(X) = Σ<sub>(a,i)∈D</sub> (Y<sub>ai</sub> - X<sub>ai</sub>)<sup>2</sup>/2 + λ/2 Σ<sub>(a,i)</sub> X<sub>(a,i)</sub><sup>2</sup>

Note that Σ<sub>(a,i)</sub> X<sub>(a,i)</sub><sup>2</sup> is equivalent to ∥X∥, and we want the norm to be minimal.

So, we go through all possible matrix Xs, and we want to select the one that makes empirical risk the smallest.

For those entries that are in D, the set of known entries, we look at both factors, but for entries not in D, we look only at the second factor, the regularisation term, since the Y<sub>ai</sub> is not known for those entries.

Also note that the entries are independent of one another, so we can look at individual Y<sub>ai</sub> values and do not need to work with the sum in aggregate.

**Examples**

1. We assume that the particular (a, i) we are looking at belongs to D:

(a, i) ∈ D

So we take the objective function for that particular (a, i), and differentiate (no sum, because we are looking at an individual (a, i)):

dJ(X<sub>ai</sub>) / dX<sub>ai</sub>

= d((Y<sub>ai</sub> - X<sub>ai</sub>)<sup>2</sup>/2 + λ/2 X<sub>(a,i)</sub><sup>2</sup>) / dX<sub>ai</sub>

So we will take this derivative and set it equal to 0.

The derivative will show that X<sub>ai</sub> in this case would be equal to:

X<sub>ai</sub> = Y<sub>ai</sub> / (1 + λ)

2. We assume that the particular (a, i) we are looking at does not belong to D:

(a, i) ∉ D

In this case we look only at the derivative of the regularisation factor:

dJ(X<sub>ai</sub>) / dX<sub>ai</sub>

= d(λ/2 X<sub>(a,i)</sub><sup>2</sup>) / dX<sub>ai</sub>

In this case, then X<sub>ai</sub> is equal to 0:

X<sub>ai</sub> = 0

**Implication**

For all entries for which the values are not known (the second case, taking the derivative of only the lambda function), just put 0s there.

For those entries for which we knew the value in advance (the first case), you actually corrupt the value by taking the true value Y<sub>ai</sub>, and dividing it by (1 + λ).

Then, depending on how much regularisation is applied via λ, the more corruption is introduced.

The solution is therefore even worse than what we started with!

There is something wrong with this approach exported from the supervised learning approach.

The problem arises from taking our 500,000 users and 18,000 movies (with many resulting parameters) and treating them all independently. This means we lose significant information about possible underlying connections between the data.

Hence this is known as the **naive approach**.
