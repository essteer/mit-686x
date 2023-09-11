# Linear Separation

Take a training set and ask whether there is a linear classifier that can successfully divide the positive and negative labels.

Perhaps this can be done via a linear classifier through the origin, but if not, it may still be possible to correctly separate the labels via a linear classifier with an offset.

But, there do exist datasets for which there is no linear classifier that can correctly label the points contained.

For example:

^ x2
|
| \+ \-
|
| \- \+
|
|\_\_\_\_\_\_> x1

The + and - values here cannot be separated linearly.

Thus this is not a linear classification problem.

It also illustrates that linear classifiers are a relatively small subset of possible circumstances.

**Definition**

Training examples `S_n = {(x^(i), y^(i)), i=1,...,n}` are linearly separable if there exists a parameter vector ^ϴ and offset parameter ^ϴ_0 such that:

- `y(i)(^ϴ • x^(i) + ^ϴ_0) > 0` for all i=1,...,n.

Given ϴ and ϴ_0, a linear classifier `h: X -> {-1, 0, +1}` is a function that outputs +1 if ϴ•x+ϴ_0 is positive, 0 if it is zero, and -1 if it is negative. In other words, h(x) = sign(ϴ•x+ϴ_0).
