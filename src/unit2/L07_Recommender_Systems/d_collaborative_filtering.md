# Collaborative Filtering: Naive Approach

Think of the problem of recommendation as a standard objective-driven algorithm.

We have our matrix $Y$, with $n$ users and m movies, with sparse entries.

The goal of our computation is to build a new matrix, $X$, of the same size $n$ and $m$, and in which every entry is filled, i.e. has a prediction for every combination of user and movie.

**Empirical risk**

We want to minimise empirical risk, so that for each possible matrix $X$, we want to know how "good" that matrix is.

Our objective should record the fact, that for data points already known in $Y$, the predicted value in $X$ for the same element should be the same (or very similar).

So we first write that we progress through all pairs of users and movies that belong to $D$, where $D$ is all the pairs $(a, i)$ such that the entry $y_{ai}$ is given.

That is, the loss on elements we already know should be minimal.

But, we also want regularisation so that we can generalise to the unknown entries.

**Objective**

$J(X) = \sum_{(a,i)∈D} \frac{(Y_{ai} - X_{ai})^2}{2} + \frac{λ}{2} \sum_{(a,i)} X_{(a,i)}^2$

Note that $\sum_{(a,i)} X_{(a,i)}^2$ is equivalent to $∥X∥$, and we want the norm to be minimal.

So, we go through all possible matrix $X$'s, and we want to select the one that makes empirical risk the smallest.

For those entries that are in $D$, the set of known entries, we look at both factors, but for entries not in $D$, we look only at the second factor, the regularisation term, since the $Y_{ai}$ is not known for those entries.

Also note that the entries are independent of one another, so we can look at individual $Y_{ai}$ values and do not need to work with the sum in aggregate.

**Examples**

1. We assume that the particular $(a, i)$ we are looking at belongs to $D$:

$(a, i) ∈ D$

So we take the objective function for that particular $(a, i)$, and differentiate (not sum, because we are looking at an individual $(a, i)$):

$\frac{dJ(X_{ai})}{dX_{ai}} = \frac{d(\frac{(Y_{ai} - X_{ai})^2}{2} + \frac{λ}{2} X_{(a,i)}^2)}{dX_{ai}}$

So we will take this derivative and set it equal to $0$.

The derivative will show that $X_{ai}$ in this case would be equal to:

$X_{ai} = \frac{Y_{ai}}{1 + λ}$

2. We assume that the particular $(a, i)$ we are looking at does not belong to $D$:

$(a, i) ∉ D$

In this case we look only at the derivative of the regularisation factor:

$\frac{dJ(X_{ai})}{dX_{ai}} = \frac{d(\frac{λ}{2} X_{ai}^2)}{dX_{ai}}$

In this case, then $X_{ai}$ is equal to $0$:

$X_{ai} = 0$

**Implication**

For all entries for which the values are not known (the second case, taking the derivative of only the lambda function), just put 0s there.

For those entries for which we knew the value in advance (the first case), you actually corrupt the value by taking the true value $Y_{ai}$, and dividing it by $(1 + \lambda)$.

Then, depending on how much regularisation is applied via $\lambda$, the more corruption is introduced.

The solution is therefore even worse than what we started with!

There is something wrong with this approach exported from the supervised learning approach.

The problem arises from taking our 500,000 users and 18,000 movies (with many resulting parameters) and treating them all independently. This means we lose significant information about possible underlying connections between the data.

Hence this is known as the **naive approach**.
