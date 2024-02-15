# Radial Basis Kernel

Feature vectors can be infinite dimensional, which means that they have unlimited expressive power.

$K(x, x^{\prime}) = \exp(-\frac{1}{2} ∥ x - x^{\prime} ∥^2)$

The radial basis kernel has a Gaussian 'bump' centred at $x$. Similarity decreases the further the kernel moves from $x$, and approaches $0$ as it moves away.

The radial basis kernel involves polynomial features up to infinite order, and is infinitely powerful.

The more difficult the task is, the more iterations it may take the kernel perceptron before it finds the radial basis solution, but it always will.

Recall that the original perceptron algorithm was limited, because when it couldn't separate the training examples, we did not know when the algorithm should be halted.

But there is not this problem with the kernel perceptron, since it will find a solution.

**Random forest**

Random forest is another type of non-linear classifier.

In brief, the procedure is:

- Bootstrap sample
- (Randomised) decision tree
- Average predictions (ensemble)
