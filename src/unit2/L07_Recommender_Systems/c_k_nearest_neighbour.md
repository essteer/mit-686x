# K-Nearest Neighbour Method

$K$ refers to the size of the advisory pool, how many neighbours we want to compare with. It may serve as a hyperparameter of the algorithm.

Say that we wish to predict user $a$'s rating for film $01$ in the table below, we might look at their similarity to other users, and identify user $b$ as a close neighbour in terms of preferences.

| User | 01  | 02  | 03  | 04  | 05  | 06  |
| ---- | --- | --- | --- | --- | --- | --- |
| $a$  | ?   | -   | 5   | 4   | -   | 1   |
| $b$  | 1   | -   | 4   | 4   | -   | 2   |
| $c$  | 5   | 5   | 5   | 5   | 5   | 5   |

From this, we might infer a likelihood for $a$ to give film $01$ a low rating.

In reality, we would not want to base the prediction on just one neighbour, but rather take an average from an aggregate of neighbours.

$\hat{y}_{ai} =$ predicted $y$ for user $a$ and film $i$

We proceed through all users $b$, our $k$-nearest neighbours, who did watch film $i$.

$\hat{y}_{ai} = \frac{\sum_{b} ∈ KNN (a, i) y_{bi}}{K}$

With $\sum_{b} ∈ KNN (a, i)$ we denote all users $b$ similar to $a$, who did watch film $i$.

We take their score for that film, $y_{bi}$, then divide by $K$.

**Defining similarity**

There are several ways that similarity could be defined, for example:

- cosine similarity: $cosθ = \frac{x_a • x_b}{∥ x_a ∥ ∥ x_b ∥}$
- Euclidian distance: $∥ x_a - x_b ∥$

Since users are represented by vectors, any method that measures similarity between vectors could be applied.

**Refining KNN**

From the starting point of:

$\hat{y}_{ai} = \frac{\sum_{b} ∈ KNN (a, i) y_{bi}}{K}$

we might want to not just take the score of the user, but weight the score based on how similar the user is to user $a$.

$\hat{y}_{ai} = \frac{\sum_{b} ∈ KNN (a, i) sim(a, b) y_{bi}}{Σ_b ∈ KNN (a, i) |sim(a, b)|}$

There is also the problem of each user applying a different internal logic to their ratings: one user may give a $\frac{3}{5}$ to films they enjoy, and reserve $\frac{5}{5}$ for only those they regard as exceptional films, whereas another user might apply $\frac{5}{5}$ in general, and deduct stars for films they dislike.

This issue can be mitigated by comparing not the score itself, but how a user has deviated from the average score they apply.

**Drawback**

Even with refinements, the KNN method is still far behind the state-of-the-art methods in use today.

A drawback of KNN is that its success depends heavily on the choice of the similarity measure.

KNN does not enable use to detect hidden structures within the data.
