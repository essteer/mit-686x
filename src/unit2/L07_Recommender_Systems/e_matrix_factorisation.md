# Collaborative Filtering with Matrix Factorisation

A key problem with the naive approach was that we treated each entry as independent, thus preventing the algorithm from being able to learn any underlying structure or grouping between the elements. This therefore obstructed the goal of being able to recommend movies based on other movies a user liked.

Another problem was that we knew very few values in the training set, only that small fraction of films viewed by each user.

**Decrease parameters**

To improve our algorithm, we want to decrease the number of parameters involved.

**Matrix rank**

To do this, we make the assumption that matrix $X$ is of low rank - recall from linear algebra that rank captures how much dependence there is between the entries of a matrix.

For example, with a matrix of rank $1$:

$[1, 2, 3; 5, 10, 15]$

This matrix can be written as a multiplication of two vectors:

$[1, 2, 3; 5, 10, 15] = [1; 5] [1, 2, 3]$

Note that there are many ways to factorise, and this could also be written as:

$[1, 2, 3; 5, 10, 15] = [10; 50][0.1, 0.2, 0.3]$

Though there are many ways to factorise, the important point is that you can factorise - since not all matrices can be written in this form - the vast majority of matrices do not have rank $1$.

**Relation of factorisation to decrease of parameters**

This matrix has $n \times m$ parameters: $[1, 2, 3; 5, 10, 15]$ with $O(n m)$.

After factorisation, we have: $[1; 5][1, 2, 3]$ with $O(n + m)$.

Thus the complexity is drastically reduced.

Whenever we make the assumption that we are operating with a matrix of rank $1$, we are making a strong assumption of how the decision of users and their preferences for movies are related.

**Intuition**

What do the vectors capture?

$u = [1; 5]$

$v = [1, 2, 3]$

$X = UV^T$

In the case of rank $1$:

$X_{ai} = u_av_i$

I.e., a multiplication of the $a$-th coordinate of vector $U$, and the $i$-th coordinate of vector $V$.

For each user, we record their general sentiment about the movies.

**Problem: over-simplification**

This raises the question of over-simplification, since now $a$ user is represented by a single number, without distinguishing for preferences between different movies / products.

**Higher ranks**

If we want to have a feature representation of a user, we don't have to focus only on rank $1$.

We can, for example, take rank $2$ (with arbitrary numbers):

$U = [2, 3; 1, 5]$  
$V = [1, 2; 4, 5]$

The higher the rank, the more multifaceted representation of the user and the movie we can have.

The number $K$ of the ranks we should use, is typically decided on the development side.

We try various $K$'s, and select the one that gives the best value in development.

There is then the question of how to find the values of $U$ and $V$ to use.
