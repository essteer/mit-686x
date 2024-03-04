# $Q$-Value Iteration by Sampling

This method has similar qualities to the MDP $Q$-value iteration.

It is still an iterative algorithm, but now it is based on the samples, and we don't know the transitions and rewards ahead of times.

So, we integrate our computation of the $Q$-values with our actions in the world.

Whatever we do and experience in the world, we want to immediately feed in to update our values.

First, we need a measure of how we are acting, and how to act, then we want to know if we have already acted, how this affects our estimation.

We begin with the assumption that we have been told how to act, and know what to try, so the goal becomes to understand how the evidence we obtain from the action should change our $Q$'s.

**$Q$-value iteration for reinforcement learning**

We don't know the transition probabilities; we just begin sampling.

$sample_1: R(s,a,s_{1}^{\prime}) + \gamma \: max_{a^{\prime}} Q(s_{1}^{\prime},a^{\prime})$

Here we just take this $Q$ as a previous estimate.

We can continue taking samples, and now let's say we will take sample $K$.

$sample_K: R(s,a,s_{K}^{\prime}) + \gamma \: max_{a^{\prime}} Q(s_{K}^{\prime},a^{\prime})$

So it is exactly the same, we will just end up in a different state.

We have collected $K$ samples, and can just take an average over these samples to get our $Q(s,a)$.

$Q(s,a) = \frac{1}{K} \sum\nolimits_{i=1}^{K} sample_i$

In recursive form, this becomes:

$Q(s,a) = \frac{1}{K} \sum\nolimits_{i=1}^{K} (R(s,a,s^{\prime}) + \gamma \: max_{a^{\prime}} Q(s_i^{\prime},a^{\prime}))$

**Simple example**

Assume that when in state $s$, there is a 50% chance of ending up in state $s_{1}^{\prime}$, and a 50% chance of ending up in state $s_{2}^{\prime}$.

Among our $K$ samples, we can see empirically that roughly half of the time we will be in each of the states $s_{1}^{\prime}$ and $s_{2}^{\prime}$.

Therefore each will contribute to the sum roughly $\frac{1}{2}$ of the times.

**Incremental updates**

In reality, we cannot retrace our steps as in a simple example such as a coin toss - we must continue taking actions as dictated by the algorithm.

We cannot really stay in one place and try to sample it mutliple times.

We will hopefully return to the state $s$ at some point and then be able to improve our estimate.

But we don't want to wait until we have sampled all and then update our estimate.

What we want to do, is update our $Q$-value incrementally each time we get our sample.

To handle this need, we implement exponential running average, a method for averaging that differs from the standard averages, because it weights the significance of samples differently.

ERA gives more weight to the current sample, than prior samples that were collected.

We will introduce the formula for ERA below, and then proceed to rewrite $Q$ to take on ERA.

**Exponential running average**

$x̄_{n} = \frac{x_n + (1 - \alpha) x_{n-1} + (1-\alpha)^2 x_{n-2} + ⋯}{1 + (1-\alpha) + (1-\alpha)^2 + ⋯}$

Rewritten recursively:

$x̄_{n} = \alpha x_n + (1 - \alpha) x_{n-1}$

This says that the current exponential average, is the weighting of the current sample, plus the weighting of the previous ERA.

It gives us a mechanism to take the prior estimate of the ERA, and add to it the new sample that we are taking.

So we take this ERA, and utilise it to compute differently our estimates for $Q$-values.

**Recomputing Qs with ERA**

$Q_{i}(s,a) = \alpha sample + (1 - \alpha) \: Q_{i}(s,a)$

Where the $Q_{i}(s,a)$ on the right-hand side is our previous estimate of the value $Q$ for state $s$ and action $a$.

We multiply by $(1 - \alpha)$, and then the sample will be one of those.

$sample = R(s,a,s^{\prime}) + \gamma \max_{a^{\prime}} Q_i(s^{\prime},a^{\prime})$

**Algorithm**

We initialise everything to zero, and then iterate.

1. Initialise all $Q(s,a) = 0 ∀ s,a$
2. Iterate until convergence

Where convergence refers to a substantially small difference between the values of the new and prior step.

The iterative steps are as follows:

2a. Collect sample: $s,a,s^{\prime}, R(s,a,s^{\prime})$
2b. $Q_{i+1}(s,a) = \alpha • (R(s,a,s^{\prime}) + \gamma \max_{a^{\prime}} \: Q_{i}(s,a)) + (1-\alpha) \: Q_{i}(s,a)$

This formula is complete, but we can also rewrite it into a form more familiar to other algorithms studied previously.

**Algorithm - alternative form for 2b**

2b. $Q_{i+1}(s,a) = Q_{i}(s,a) + \alpha • (R(s,a,s^{\prime}) + \gamma \max_{a^{\prime}} \: Q_{i}(s,a) - Q_{i}(s,a))$

So we have separated our the terms that are and are not guided by $\alpha$.

Note that it can be shown that the same conditions on alpha that were used to demonstrate convergence with gradient descent can be applied here.

Under this condition, the algorithm is guaranteed to converge.

Once it has converged, we have our policy.
