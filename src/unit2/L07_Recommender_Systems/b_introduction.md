# Introduction

Recommender problems, are those such as Netflix's recommendations of a film a user may like to watch.

The problem can be defined in several ways, one of which is K-Nearest Neighbours.

Matrix factorisation, or collaborative filtering, is another.

Imagine a large matrix, $Y$, with n possible users of the system, and m movies; it is an $n \times m$ matrix.

Then we may examine a particular element y\_{ai}, which denotes the $a$-th user's preference for the $i$-th film.

(This preference might be represented in different ways: some websites use five-star ratings, others use thumbs-up or thumbs-down, and so on.)

**Netflix challenge**

The goal of the "Netflix challenge" (which first raised this machine learning problem) is to predict a user's preference for a film, based on prior choices made by the user.

The Netflix challenge involved 0.5 million users ($n = 500,000$), and 18,000 movies ($m = 18,000$).

Most of the matrix $Y$ is in fact empty, since any given user will have viewed only a small fraction of the 18,000 films.

On average, each film was rated by only 5,000 users, or around 1% of the total number of users.

The goal of the algorithm is then to fill out the entire matrix.

**Linear regression**

On the surface, this problem might appear to lend itself to linear regression, and therefore the solution might involve determining feature vectors for films based on details such as the genre, lead actor, director, and so on.

A regression model might take these feature vectors and use regression to predict the scoring of the film.

However, there are several reasons that regression may not be suitable:

- Selecting features makes the assumption that we know which features determined the ranking of a film.
- Translating to a different platform, such as Amazon, with a much large range of more disparate products, it becomes even less clear which features to record as indicators of possible preference for another product, and the size of the feature vectors would be enormous.

- Then, there may be too few ratings for a given user to be able to extrapolate to other movies they might enjoy.

**K Nearest Neighbours**

The KNN approach, instead of trying to identify similarity between films, or products, and so on, instead seeks to identify similarity between different users.
