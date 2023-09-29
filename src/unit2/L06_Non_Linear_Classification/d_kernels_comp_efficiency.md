# Motivation for Kernels: Computational Efficiency

Computing the inner products of vectors can be cheap, even if the vectors are high-dimensional.

φ(x) = [x<sub>1</sub>, x<sub>2</sub>, x<sub>1</sub><sup>2</sup>, √2 x<sub>1</sub>x<sub>2</sub>, x<sub>2</sub><sup>2</sup>]<sup>T</sup>

φ(x') = [x'<sub>1</sub>, x'<sub>2</sub>, x'<sub>1</sub><sup>2</sup>, √2 x'<sub>1</sub>x'<sub>2</sub>, x'<sub>2</sub><sup>2</sup>]<sup>T</sup>

**Evaluating the inner products of these two feature vectors**

The first part, consisting of monomials only ([x<sub>1</sub>, x<sub>2</sub>] and [x'<sub>1</sub>, x'<sub>2</sub>]) evaluates to:

φ(x) • φ(x') = (x • x')

The inner product of the remaining parts is a quadratic expression, and becomes (x • x') plus the scalar value to the power of 2: (x • x')<sup>2</sup>:

φ(x) • φ(x') = (x • x') + (x • x')<sup>2</sup>

If we added third order terms, we could just add a further x and x' product term to the power of 3, and so on:

φ(x) • φ(x') = (x • x') + (x • x')<sup>2</sup> + (x • x')<sup>3</sup>

The computation therefore does not become more complicated, even despite the number of feature vectors added by moving from order 2 to order 3.

This is function is known as a **kernel function**. Kernel functions always correspond to inner products between some feature vectors.

K(x, x') = φ(x) • φ(x') = (x • x') + (x • x')<sup>2</sup> + (x • x')<sup>3</sup>

**Kernels vs features**

For some feature maps, the inner product can be evaluated very cheaply, e.g. an any-order polynomial feature transformation:

K(x, x') = φ(x) • φ(x') = (1 + x • x')<sup>P</sup>, P = 1, 2, ⋯

In those cases, it is advantageous to express the linear classifiers (regression methods) in terms of kernels rather than explicitly constructing feature vectors.

**Application**

The task is then to turn our linear model, e.g. sign(θ• φ(x) + θ<sub>0</sub>), into a classifier that only depends on the inner products.

Kernel perceptron is one example of how this can be done.
