# Utility Function

MDP:

| Term        | Notation                 | Notes                                    |
| ----------- | ------------------------ | ---------------------------------------- |
| States      | s ∈ S                    | (observed)                               |
| Actions     | a ∈ A                    | e.g., left right up down                 |
| Transitions | T(s,a,s') = p(s' \| s,a) | e.g., 80% chance up, 10% left, 10% right |
| Reward      | R(s), or R(s,a,s')       |                                          |
| MDP         | <S,A,T,R>                |                                          |

Previously we discussed the model with a final reward; but in many cases it may be preferable to have intermediate rewards.

For example, a prize for making a move, or a reward for a marketing action.

We discuss the maximisation of rewards with utility functions.

**Finite horizon**

One option for a utility function is to say, just go and collect all rewards on the map.

But in such a case there may be an infinite number of rewards, and no way to compare two different strategies of obtaining them.

Ideally, we want the utility function to be bounded.

An obvious means to do this is finite horizon: you can only collect rewards for N number of steps.

In this case, for any value of K, we collect rewards only for N steps:

U([s<sub>0</sub>, ⋯, s<sub>N+K</sub>]) = U([s<sub>0</sub>, ⋯, s<sub>N</sub>]) ∀ K

Problems with this definition include that behaviour becomes unstationary: you do not only depend on the state you are in, but also the time point at which you arrive there.

When using a finite horizon utility function, when computing the action at time step i, it can depend on the amount of steps that we have left until we reach N. For example, if we are at state s at time N, the agent will want to act greedily and take the action that leads to the immediate highest reward. However, if we are at time 0, the agent can allow to move towards areas with higher rewards while getting an immediate lower reward.

However, in Markov Decision Processes we want to encapsulate our representation in such a way that behaviour only depends on the current state.

So, we will not adopt the finite horizon utility function.

**Discounted reward**

Instead, we will use the discounted reward utility function.

Discounted reward based utility under a markovian setting would lead to an optimal policy that only depends on the state and is independent of the step where the state occurs.

The idea here is that we still want the function to be bounded, even if the agent can go through an infinite number of states.

We make the agent greedy, so that they place a higher value on immediate rewards, than on future rewards.

U([s<sub>0</sub>, s<sub>1</sub>, ⋯]) = R(s<sub>0</sub>) + γR(s<sub>1</sub>) + γ<sup>2</sup>R(s<sub>2</sub>) ⋯

Here we introduce γ, where 0 ≤ γ < 1, as a means to discount future rewards.

We can close this expression as follows:

U([s<sub>0</sub>, s<sub>1</sub>, ⋯]) = R(s<sub>0</sub>) + γR(s<sub>1</sub>) + γ<sup>2</sup>R(s<sub>2</sub>) ⋯ = Σ<sup>∞</sup><sub>t=0</sub> γ<sup>t</sup>R(s<sub>t</sub>)

We then can substitute all of the rewards with the maximum reward.

≤ R<sub>max</sub> Σ<sup>∞</sup><sub>t=0</sub> γ<sup>t</sup>

This expression is equal to 1 / (1 - γ):

≤ R<sub>max</sub> Σ<sup>∞</sup><sub>t=0</sub> γ<sup>t</sup> = R<sub>max</sub> / (1 - γ)

This is our bound, and it is essential to enable the algorithm to converge.
