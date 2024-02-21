# Alternating Minimisation

We now can rewrite our objective function, in terms of $U$ and $V$.

$X_{ai} = u_a v_i$; rank of matrix $X = 1$.

Now for the objective, we compare the values that are present in matrix $Y$ with our estimation.

- Instead of writing the estimation as $X_{ai}$, we directly express it in terms of $u_a v_i$.
- The regularisation term also controls directly in terms of $u_a$ and $v_i$, instead of $X_{ai}$.

$J(u, v) = \sum_{(a,i)∈D} (Y_{ai} - u_av_i)^2 + \frac{\lambda}{2} \sum\nolimits_{a=1}^{n} u_a^2 + \frac{\lambda}{2} \sum\nolimits_{i=1}^{m} v_i^2$

Note that we are estimating a function that depends on two elements: on $u$'s, and on $v$'s.

Due to having two variables, the estimation becomes more complex than in the naive approach.

**Alternation**

To find the optimal values of $U$ and $V$, we first fix e.g. $V$ and find the optimal $U^{\ast}$, then fix that $U^{\ast}$ and find the optimal $V^{\ast}$.

We must then continue to alternate, since the optimal $U$ for $V^{\ast}$ is not necessarily $U^{\ast}$.

So we greedily iterate between fixing $U$ and fixing $V$, until the values converge.

**Example**

Two users and three movies:

$Y = [5, ?, 7; 1, 2, ?]$

User $1$ has rated movies $1$ and $3$; user $2$ has rated movies $1$ and $2$, the ratings of user $1$ for movie $2$, and user $2$ for movie $3$, are unknown.

Our goal is to find a vector $u$, which in this case since we make the assumption of it being rank $1$: $u = [u_1; u_2]$, and a vector $v$: $v = [v_1; v_2; v_3]$ to minimise this objective.

**Algorithm**

We begin by initialising vector $v$ as: $v = [2; 7; 8]$.

The next step is to look at matrix $X$, when we are computing the product between $u$ and $v^T$.

$X = uv^T = [u_1; u_2][2, 7, 8] = [2u_1, 7u_1, 8u_1; 2u_2, 7u_2, 8u_2]$

So, we want to find $u_1$ and $u_2$ in such a way that this matrix has values for known entries, which are close to what we have in $Y$.

(Recall $Y = [5, ?, 7; 1, 2, ?]$.)

Note that we don't necessarily need to consider $u_1$ and $u_2$ jointly; they are separate users, so we can solve for the rows individually if we choose.

**Objective for $u_1$**

We skip the middle entry since it is a $?$ in $Y$, we don't know the value:

$\frac{(5 - 2u_1)^2}{2} + \frac{(7 - 8u_1)^2}{2} + \frac{\lambda}{2} u_1^2$

Since we want to minimise, we take a derivative of this expression with respect to $u_1$:

$\frac{\partial{}}{\partial{u_1}} [\frac{(5 - 2u_1)^2}{2} + \frac{(7 - 8u_1)^2}{2} + \frac{\lambda}{2} u_1^2] = (-66) + (68 + \lambda)u_1 = 0$

Rewriting in terms of $u_1$, we get:

$u_1 = \frac{66}{68 + \lambda}$

This is the $u_1$ that minimises this objective.

For example, if $\lambda = 1$, then: $u_1 = \frac{66}{69}$.

**Objective for $u_2$**

We then do the same calculation for $u_2$, and arrive at:

$u_2 = \frac{16}{53 + \lambda}$

For example, if $\lambda = 1$, then: $u_2 = \frac{16}{54}$

**Now alternate for the $v$'s**

So, we started with a random initialisation of $v$, and computed $u$'s that would be optimal with respect to our objective.

The next step is then to take the $u$'s we computed, and compute the $v$'s.

$uv^T = [\frac{66}{69}; \frac{16}{54}][v_1, v_2, v_3] = [\frac{66}{69}v_1, \frac{66}{69}v_2, \frac{66}{69}v_3; \frac{16}{54}v_1, \frac{16}{54}v_2, \frac{16}{54}v_3]$

We now have a new estimate for our matrix $X$, so again will take this and compare it with matrix $Y$.

We continue this process until there is no change in the objective values.

**Are we guaranteed to converge?**

Locally - yes.  
Globally - no.

**Rank**

The examples we have examined here have been based on matrices of rank $1$, but they would hold for ranks $2$, $3$, and $k$.
