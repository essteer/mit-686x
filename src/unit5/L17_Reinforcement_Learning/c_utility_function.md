# Utility Function

MDP:

| Term        | Notation                                   | Notes                                    |
| ----------- | ------------------------------------------ | ---------------------------------------- |
| States      | $s ∈ S$                                    | (observed)                               |
| Actions     | $a ∈ A$                                    | e.g., left right up down                 |
| Transitions | $T(s,a,s^{\prime}) = p(s^{\prime} \| s,a)$ | e.g., 80% chance up, 10% left, 10% right |
| Reward      | $R(s)$, or $R(s,a,s^{\prime})$             |                                          |
| MDP         | $\lt S,A,T,R \gt$                          |                                          |

Previously we discussed the model with a final reward; but in many cases it may be preferable to have intermediate rewards.

For example, a prize for making a move, or a reward for a marketing action.

We discuss the maximisation of rewards with utility functions.

**Finite horizon**

One option for a utility function is to say, just go and collect all rewards on the map.

But in such a case there may be an infinite number of rewards, and no way to compare two different strategies of obtaining them.

Ideally, we want the utility function to be bounded.

An obvious means to do this is finite horizon: you can only collect rewards for $N$ number of steps.

In this case, for any value of $K$, we collect rewards only for $N$ steps:

$U([s_0, ⋯, s_N + K]) = U([s_0, ⋯, s_N]) ∀ K$

Problems with this definition include that behaviour becomes unstationary: you do not only depend on the state you are in, but also the time point at which you arrive there.

When using a finite horizon utility function, when computing the action at time step $i$, it can depend on the amount of steps that we have left until we reach $N$. For example, if we are at state $s$ at time $N$, the agent will want to act greedily and take the action that leads to the immediate highest reward. However, if we are at time $0$, the agent can allow to move towards areas with higher rewards while getting an immediate lower reward.

However, in Markov Decision Processes we want to encapsulate our representation in such a way that behaviour only depends on the current state.

So, we will not adopt the finite horizon utility function.

**Discounted reward**

Instead, we will use the discounted reward utility function.

Discounted reward based utility under a markovian setting would lead to an optimal policy that only depends on the state and is independent of the step where the state occurs.

The idea here is that we still want the function to be bounded, even if the agent can go through an infinite number of states.

We make the agent greedy, so that they place a higher value on immediate rewards, than on future rewards.

$U([s_0, s_1, ⋯]) = R(s_0) + \gamma R(s_1) + \gamma^2 R(s_2) ⋯$

Here we introduce $\gamma$, where $0 \leq \gamma \lt 1$, as a means to discount future rewards.

We can close this expression as follows:

$U([s_0, s_1, ⋯]) = R(s_0) + \gamma R(s_1) + \gamma^2 R(s_2) ⋯ = \sum\nolimits_{t=0}^{\infty} \gamma^t R(s_t)$

We then can substitute all of the rewards with the maximum reward.

$\leq R_{max} \sum\nolimits_{t=0}^{\infty} \gamma^t$

This expression is equal to $\frac{1}{1 - \gamma}$:

$\leq R_{max} \sum\nolimits_{t=0}^{\infty} \gamma^t = \frac{R_{max}}{1 - \gamma}$

This is our bound, and it is essential to enable the algorithm to converge.
