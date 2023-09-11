# Different Kinds of Supervised Learning: Classification vs Regression

A supervised learning task is one where we specify the correct behaviour.

I.e., we specify a feature vector, and what we want it to be associated with (the labels).

**Multi-way classification**

h([news article]) = politics -> h: X -> {sports, politics, other}

**Regression**

h([house]) = $1,345,222 -> h: X -> R

**Structured prediction**

h([image]) = [description] -> h: X -> {[English sentences]}

## Types of machine learning

Supervised learning

- prediction based on examples of correct behaviour

Unsupervised learning

- no explicit target, only data, goal to model / discover

Semi-supervised learning

- supplement limited annotations with unsupervised learning

Active learning

- learn to query the examples actually needed for learning; additional information can be requested by the computer if it thinks that this will help it to better train the model

Transfer learning

- how to apply what you have learned from A to B; e.g., we have machine translation from English to Spanish, and wish to apply the method to translate from English to Portuguese

Reinforcement learning

- learning to act, not just predict; goal to optimise the consequences of actions

And so on...
