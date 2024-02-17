# Policy and Value Functions

**Policy**

Policy is an optimal action that you can take in a state.

$\pi^{*}: S ⟶ A$

The idea is to maximise expected reward.

When taking an action or a sequence of actions, we don't know exactly which rewards we will receive, because the world is non-deterministic; the agent may have the intention to move forwards, but end up moving sideways, for example.

In every state, we want to select an action that optimises the expected maximum utility.

**Structure**

Policy very much depends on the structure of the reward.

The optimal policy assigns an action at every state that maximises the expected utility.

Returning to the $3 \times 3$ grid with blocked centre square example, a $+1$ top-right and a $-1$ middle-right.

Imagine that there is a cost associated with each transition, so that there is a small price, $-0.01$ for each action.

Beginning bottom-right, the agent may proceed clockwise to reach $+1$ (avoiding the $-1$ directly above the start).

Since it takes $6$ actions to get to $+1$ in this way, the final reward would be $6 \times (-0.01) + 1 = 0.94$.

If instead the cost was very high, $-10$ for every step, it would become optimal to pass directly through $-1$ to $+1$, for a total reward of $-20$.

Each time the agent arrives at a state, the policy tells it where to go.

When we refer to solving MDPs, we refer to finding the optimal policy, which maximises the expected reward.

**Connection with reinforcement learning**

In principle, the general idea is the same.

The difference is that with a reinforcement learning problem, we are not provided with a transition function or with a reward function.

We must go out and experience, to collect these functions.

**Bellman equations**

We need to derive a mechanism to propagate the reward.

We assume for now that the living reward is zero - we have only $+1$ and $-1$ in the $3 \times 3$ grid.

We know the top-right space (with $+1$) is a great place to be, since we get the reward there.

We also know that top-middle, just before the $+1$, is also good because it is just before the reward.

And so on.

We need to provide the agent with a quantification of how good a state is, so that it can orient itself in terms of what is a promising way to proceed.

Bellman equations connect the notion of the value of the state and the notion of policy.
