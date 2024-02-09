# A Concrete Example of a Supervised Learning Task

An example of how to:

- specify a machine learning task, and
- how to solve it.

**Movie recommender problem**

We have a set of films already seen, and want to use our experience of those films to predict which films we will like out of a set of many unseen films.

1. First, we must illustrate the task for the ML algorithm. In the case of films, we annotate each film to highlight our preferences, e.g., giving +1 or -1 to a set of four films we have seen.

2. The task is then to recommend correctly out of n films, films that will be "liked".

Note that the computer can understand the $+1/-1$ labels applied to the films, but cannot truly understand anything about the films themselves.

3. We therefore need to construct a **feature vector** to put the films into a form that the computer can understand.

For example, asking these questions of a film:

- Is it a comedy?
- Is it an action film?
- Is it a Werner Herzog film?
- Is Robert de Niro in the film?
- Is it a Pixar film?

Could result in the feature vector:

$x^{(1)} = [0, 0, 1, 1, 0]^T$

For a film directed by Werner Herzog starring de Niro, that is neither a comedy nor an action film, and is not produced by Pixar.

Then we might have $x^{(2)} = [1, 0, 0, 0, 1]^T$, and so on.

This feature vector can be applied to all of the unseen films, with the goal of determining which films fit with the given feature vectors we have expressed a preference for.

The mapping from feature vector to labels is known as the **classifier**.

**Training set and test set**

The set of films we have seen, and given preference labels to, become the training set.

The test set is the set of n films not seen, that we want to apply our model to and obtain recommendations from.

We wish to generalise what understanding we can extract from the training set, and apply this to the test set.
