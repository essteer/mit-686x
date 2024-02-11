# Introduction

Exploring how to turn ML problems into optimisation problems.

For linear classification, there may be many correct solutions that the perceptron algorithm could arrive at; each of them correctly divides the positive and negative labels, but there is no bias towards which of these divisions is "better".

However, we would want to favour the solution that was drawn between the two sets, thus providing a margin between them.

This solution is known as the **large margin classifier**.

**Learning as optimisation**

So, the optimal decision boundary will be the linear classifier such that it lies equidistant from positive and negative margin boundaries, each of which represents the line of the nearest positive (negative) examples to the decision boundary.

We use positive and negative margin boundaries to define a **"fat" decision boundary**, that we will try to fit within the training examples.

As we push out the positive and negative margin boundaries from the decision boundary, we carve out a space between the positive and negative examples.

The decision boundary will be shifted to the centre of this space, to arrive at the optimla decision boundary.

**Problem features**

There are two aspects to this problem, when cast into an optimisation problem:

1. Favouring margin boundaries that are far apart from their decision boundaries - **regularisation**.

2. A counterweight to this, that as we begin to push the margin boundaries apart and try to still fit the decision boundary within the set of training examples, we might violate the preference that all training examples are outside of the fat decision boundary.

   - This counterweight is quantified in terms of a **loss function**.

The objective function for selecting the parameters $θ$ and $θ_0$, is therefore a balance between:

- loss (how the examples fit into our solution), and
- regularisation (our preference for large-margin solutions).

We want to find values of $θ$ and $θ_0$ that minimise our objective function.
