# Objective Function

Combining the hinge loss and regularisation terms (see d_hinge_loss.md), we arrive at an objective function that guides our selection of the parameter vectors $θ$ and $θ_0$.

**Objective function**

$J(θ, θ_0) = \frac{1}{n} \sum\nolimits_{i=1}^{n} Loss_h(y^{(i)}(θ•x^{(i)} + θ_0)) + \frac{λ}{2}∥θ∥^2$

The two parts are:

- average loss, where each loss term measures how much an example violates the margin boundary (MB)
- regularisation, which tries to push the MBs further and further apart.

The objective function (OF) is a balance between the two parts.

We set the balance by defining a new parameter $λ$, the regularisation parameter.

- $λ$ weighs how the two terms should affect the solution.
- $λ$ is always $> 0$.

For large values of $λ$, we will favour large-margin solutions, but potentially at a cost of incurring further loss as the MBs push past the examples.

If $λ$ is small, we favour correctly keeping examples beyond the MBs, potentially at a cost of keeping the MBs closer to the decision boundary (DB).

**The optimal value of $θ$ and $θ_0$ is obtained by minimising the OF.**

The learning problem is now an optimisation problem.

**Examples**

1. Point A, a positive point exactly on the positive MB (+MB):

   - $Loss_h(1) = 1 - (1•1) = 0$.
   - As expected, since a point on the correct MB should have no loss.

2. Point B, a +ve point halfway between +MB and the DB:

   - First calculate by supposing B was instead exactly on the DB.
   - At that point, $Loss_h(0) = 1 - 0 = 1$.
   - The loss is a linear function of how much the point violates the MB.
   - At MB, loss = $0$; at DB, loss = $1$; so the loss for a point between the MB and DB is between $0$ and $1$.
   - Point B is halfway between +MB and DB, so the loss = $Loss_h(0.5) = \frac{1}{2}$.
   - $Loss_h(0.5) = 1 - (1•0.5) = 0.5$.

3. Point C, a -ve point exactly on the DB:

   - Points exactly on the DB incur hinge loss of $1$.
   - $Loss_h(0) = 1 - (1•0) = 1$.

4. Point D, a -ve point exactly on the **+MB**:

   - We have seen that a point on its own MB incurs no loss;
   - A point exactly on the DB incurs loss = $1$.
   - A point exactly on the opposite MB incurs loss = $2$.
   - $Loss_h(-1) = 1 - (1•-1) = 2$.

5. Point E, a -ve point beyond the +MB:
   - This will have a loss > $2$.
   - E.g., at $-6$:
   - $Loss_h(-6) = 1 - (1•-6) = 7$.
