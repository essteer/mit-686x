# Generative vs Discriminative Models

Models examined so far have been discriminative.

We can imagine in the case of a simple +ve -ve linear classification problem, that the linear decision boundary for two different problems might be the same, even if the structure of the points on either side differed significantly.

With generative models, we will look at much broader sets of data, and will also add a probabilistic component.

- Generative models model the probability distribution of each class.
- Discriminative models learn the decision boundary between the classes.

**Two common generative models**

- Multinomials
- Guassians

**Two questions**

- How do we estimate?
- How do we predict?

**High-level note on prediction**

Given our training data for +ve and -ve points, we will fit a probability distribution for the +ve and -ve classes.

Then, given a new point, we can calculate how likely it was generated for each class, then compare the probability to deduce the correct label.
