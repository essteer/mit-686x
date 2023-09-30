# K-Nearest Neighbour Method

K refers to the size of the advisory pool, how many neighbours we want to compare with. It may serve as a hyperparameter of the algorithm.

Say that we wish to predict user a's rating for film 01 in the table below, we might look at their similarity to other users, and identify user b as a close neighbour in terms of preferences.

|User|01|02|03|04|05|06|
|a|?|---|5|4|---|---|1|
|b|1|---|4|4|---|---|2|
|c|5|5|5|5|5|5|

From this, we might infer a likelihood for a to give film 01 a low rating.

In reality, we would not want to base the prediction on just one neighbour, but rather take an average from an aggregate of neighbours.

ŷ<sub>ai</sub> = predicted y for user a and film i

We proceed through all users b, our k-nearest neighbours, who did watch film i.

ŷ<sub>ai</sub> = (Σ<sub>b ∈ KNN (a, i)</sub> y<sub>bi</sub>) / K

With Σ<sub>b ∈ KNN (a, i)</sub> we denote all users b similar to a, who did watch film i.

We take their score for that film, y<sub>bi</sub>, then divide by K.

**Defining similarity**

There are several ways that similarity could be defined, for example:

- cosine similarity: cosθ = (x<sub>a</sub> • x<sub>b</sub>) / ∥ x<sub>a</sub> ∥ ∥ x<sub>b</sub> ∥
- Euclidian distance: ∥ x<sub>a</sub> - x<sub>b</sub> ∥

Since users are represented by vectors, any method that measures similarity between vectors could be applied.

**Refining KNN**

From the starting point of:

ŷ<sub>ai</sub> = (Σ<sub>b ∈ KNN (a, i)</sub> y<sub>bi</sub>) / K

we might want to not just take the score of the user, but weight the score based on how similar the user is to user a.

ŷ<sub>ai</sub> = (Σ<sub>b ∈ KNN (a, i)</sub> sim(a, b) y<sub>bi</sub>) / Σ<sub>b ∈ KNN (a, i)</sub> |sim(a, b)|

There is also the problem of each user applying a different internal logic to their ratings: one user may give a 3/5 to films they enjoy, and reserve 5/5 for only those they regard as exceptional films, whereas another user might apply 5/5 in general, and deduct stars for films they dislike.

This issue can be mitigated by comparing not the score itself, but how a user has deviated from the average score they apply.

**Drawback**

Even with refinements, the KNN method is still far behind the state-of-the-art methods in use today.

A drawback of KNN is that its success depends heavily on the choice of the similarity measure.

KNN does not enable use to detect hidden structures within the data.
