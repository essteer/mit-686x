# Alternating Minimisation

We now can rewrite our objective function, in terms of U and V.

X<sub>ai</sub> = u<sub>a</sub>v<sub>i</sub>; rank of matrix X = 1

Now for the objective, we compare the values that are present in matrix Y with our estimation.

- Instead of writing the estimation as X<sub>ai</sub>, we directly express it in terms of u<sub>a</sub>v<sub>i</sub>.
- The regularisation term also controls directly in terms of u<sub>a</sub> and v<sub>i</sub>, instead of X<sub>ai</sub>.

J(u, v) = Σ<sub>(a,i)∈D</sub> (Y<sub>ai</sub> - u<sub>a</sub>v<sub>i</sub>)<sup>2</sup> + λ/2 Σ<sup>n</sup><sub>a=1</sub> u<sub>a</sub><sup>2</sup> + λ/2 Σ<sup>m</sup><sub>i=1</sub> v<sub>i</sub><sup>2</sup>

Note that we are estimating a function that depends on two elements: on u's, and on v's.

Due to having two variables, the estimation becomes more complex than in the naive approach.

**Alternation**

To find the optimal values of U and V, we first fix e.g. V and find the optimal U*, then fix that U* and find the optimal V\*.

We must then continue to alternate, since the optimal U for V* is not necessarily U*.

So we greedily iterate between fixing U and fixing V, until the values converge.

**Example**

Two users and three movies:

Y = `[5 ? 7; 1 2 ?]`

User 1 has rated movies 1 and 3; user 2 has rated movies 1 and 2, the ratings of user 1 for movie 2, and user 2 for movie 3, are unknown.

Our goal is to find a vector u, which in this case since we make the assumption of it being rank 1:

u = `[u1; u2]`

and a vector v:

v = `[v1; v2; v3]`

to minimise this objective.

**Algorithm**

We begin by initialising vector v as:

v = `[2; 7; 8]`

The next step is to look at matrix X, when we are computing the product between u and v<sup>T</sup>.

X = uv<sup>T</sup> = ` [u1; u2]` `[2 7 8] ` = `[2u1 7u1 8u1; 2u2 7u2 8u2]`

So, we want to find u1 and u2 in such a way that this matrix has values for known entries, which are close to what we have in Y.

(Recall Y = `[5 ? 7; 1 2 ?]`.)

Note that we don't necessarily need to consider u1 and u2 jointly; they are separate users, so we can solve for the rows individually if we choose.

**Objective for u<sub>1</sub>**

We skip the middle entry since it is a ? in Y, we don't know the value:

(5 - 2u1)<sup>2</sup>/2 + (7 - 8u1)<sup>2</sup>/2 + λ/2 u<sub>1</sub><sup>2</sup>

Since we want to minimise, we take a derivative of this expression with respect to u1:

∂/∂u<sub>1</sub> [(5 - 2u<sub>1</sub>)<sup>2</sup>/2 + (7 - 8u<sub>1</sub>)<sup>2</sup>/2 + λ/2 u<sub>1</sub><sup>2</sup>]

= (-66) + (68 + λ)u<sub>1</sub> = 0

Rewriting in terms of u<sub>1</sub>, we get:

u<sub>1</sub> = 66 / (68 + λ)

This is the u<sub>1</sub> that minimises this objective.

For example, if λ = 1, then:

u<sub>1</sub> = 66/69

**Objective for u<sub>2</sub>**

We then do the same calculation for u<sub>2</sub>, and arrive at:

u<sub>2</sub> = 16 / (53 + λ)

For example, if λ = 1, then:

u<sub>2</sub> = 16/54

**Now alternate for the v's**

So, we started with a random initialisation of v, and computed u's that would be optimal with respect to our objective.

The next step is then to take the u's we computed, and compute the v's.

uv<sup>T</sup> = `[66/69; 16/54]` `[v1 v2 v3]` = `[66/69v1 66/69v2 66/69v3; 16/54v1 16/54v2 16/54v3]`

We now have a new estimate for our matrix X, so again will take this and compare it with matrix Y.

We continue this process until there is no change in the objective values.

**Are we guaranteed to converge?**

Locally - yes.
Globally - no.

**Rank**

The examples we have examined here have been based on matrices of rank 1, but they would hold for ranks 2, 3, and k.
