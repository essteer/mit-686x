# Introduction to Linear Classifiers

Training data can be graphically depicted on a (hyper)plane.

Classifiers are mappings that take feature vectors as input and produce labels as output.

A common kind of classifier is the linear classifier, which linearly divides space (the (hyper)plane where training data lies) into two.

Given a point $x$ in the space, the classifier $h$ outputs $h(x) = 1$ or $h(x) = -1$, depending on where the point exists in among the two linearly divided spaces.

**Geometric representation**

We can plot our film preferences in 2-dimensional space using an $x, y$ graph, where positive values represent a $+1$ (liked a film) and negative values represent a $-1$ (disliked a film).

Our four films in the training set would be plotted as e.g. $x^{(1)}y^{(1)}$.

The training set as a whole is depicted as a set, $S_n$, where $n$ denotes the number of instances in the set.

For this example, it becomes $S_4$ because we have four films in the training set ($n = 4$).

- $S_4$ is is a collection of pairs in those vectors, ($x^{(i)}, y^{(i)}$) where $x$ represents the feature vector, and $y$ is the corresponding label.
- $S_4 = (x^{(i)}, y^{(i)}), i=1, i=2, ..., i=n$ in $ℝ^2 \{-1, 1\}$.

Each example in the **test set** is also a pair of feature vector and label, but **we don't know the label**.

The label is unknown until we have seen the film, at which point we know whether we wanted to see it or not.

The task is to correctly determine those unknown labels.

On the basis of our training set:

$S_4 = \{(x^{(i)}, y^{(i)}), i=1,⋯,n\}$

The model needs to map each point in the space $x ∈ ℝ^2$, to a corresponding label of $+1/-1, y ∈ \{-1, 1\}$.

**Classifier**

We are then in need of a classifier, mapping from points to corresponding labels.

$h: χ ⟶ \{-1, 1\}$ (where $χ$ is $ℝ^2$)

Then for a given point, we would have, e.g. $h(x) = 1$.

The classifier thus divides the space into two halves: one half is labeled 1, the other half is labeled -1.

**Training error**

We need to evaluate how good our classifier is in terms of the amount of error applied to the training examples that we have.

Training error, E, is the error of the model.

$E_n$ denotes the training error for the size of the training set, e.g. for our film model we would have $E_4$ because $n=4$.

We then apply this to a particular classifier, $h$, for our training set:

$E_n(h)$

To do this, we take the classifier, $h$, and apply it to the $ith$ training example to get the $+1/-1$ label.

$E_n(h) = h(x^{(i)})$

And compare that with the given label for that example, $y^{(i)}$.

$h(x^{(i)}) \neq y^{(i)}$

If the expected label is not the same as the actual label, then the above statement is true and there is a discrepancy.

(In notation we use double brackets $[[]]$ to denote a function that takes a truth value inside and returns $1$ or $0$, accordingly.)

$[[h(x^{(i)})  \neq y^{(i)}]] = 1$ if error, else $0$.

We want the error over the whole training set, so we sum this error over all training examples:

$\sum\nolimits_{i=1}^{n} [[h(x^{(i)})  \neq y^{(i)}]]$, and take a fraction $\frac{1}{n}$ of this.

Example: for a training set of $6$, if $3$ are labeled correctly and $3$ are labeled incorrectly, we have $E_6(h) = \frac{3 \times 1 + 3 \times 0}{6} = \frac{3}{6} = 0.5$.

(In this example, this outcome is no better than randomly guessing by chance.)

**Error evaluation**

We can then use our training error to consider how good the choice of classifier was for the given training set.

We may then have a classifier $h$ that correctly labels all of the data in the training set, i.e., $E_n(h) = 0$.

But this does not mean this classifier with a training error of zero, will correctly label all of the data in our test set.

**Generalisation**

This becomes then a problem of generalisation: how well the classifier selected from the training model data, the training set, can generalise to the test set.

The ability to generalise from the training set to the test set, is at the heart of all machine learning problems.

Typically, we generalise well when we select from a limited set of classifiers, $h$, within the set of possible classifiers - the **hypothesis space**.

The more choices of classifier we have, the greater the complexity of the model - which runs counter to generalisation.
