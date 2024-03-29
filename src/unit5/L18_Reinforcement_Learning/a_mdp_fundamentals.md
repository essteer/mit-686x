# Revisiting MDP Fundamentals

This is our high-level model for the Markov Decision Process:

**$\lt S, A, T, R \gt$**

- $S$ is the set of states that represent our world.
- $A$ is the set of actions the agent can take in that world.
- $T$ is the transition probabilities, that represent the - fact that the world is not deterministic - intended actions may lead to unintended results.
- $R$ is the reward for taking an action from a given state, and ending up in a subsequent state.

**Solving MDPs**

First, we assume that all of the sets $\lt S, A, T, R \gt$ are provided to us.

We want to find a policy $\pi(s)$ that tells us the best actions to take, those that result in the highest expected utility.

$Q(s,a)$ is the value of the state and a specific action, and tells us what the best expected value is if we start in state $s$, take action $a$, and then act optimally from then on.

The algorithm propagates information derived about the rewards to the rest of the grid.

MDP: $\lt S, A, T, R \gt$

$\pi^{\ast} (s) = argmax_{a} Q^{\ast}(s,a)$

We don't know which state we will end up, even for a given action due to the non-deterministic feature of the world, and so we must compute probabilities with $T$.

Then, we want to express the relationship using $Q$ instead of $V$, and do so as follows:

$Q^{\ast}(s,a) = \sum_{s^{\prime}} T(s,a,s^{\prime}) (R(s,a,s^{\prime}) + \gamma max_a^{\prime}Q(s^{\prime},a^{\prime}))$

From this, if we take the maximum ($a^{\prime}$) over all possible actions that could be taken, this actually gives us the value of the state. (Note that $\max_{a^{\prime}}Q(s^{\prime},a^{\prime})$ is equivalent to $V^{\ast}(s^{\prime})$.)

Since we don't know in which state $s^{\prime}$ we will end up, we average across all possible states, multiplied by our likelihood weighting that we will end up in a particular $s^{\prime}$.

**Reinforcement learning**

Clearly, in the real world we never know all of the values of $\lt S, A, T, R \gt$.

We may know the states $S$ and the actions that our agent can take, $A$.

In terms of transition, $T$, we cannot know the transition ahead of time - the only way to know is to try an action.

We also don't know what the reward function $R$, is - we don't know a priori which states are the good states in which we can get rewards.

So here, we have a tuple of state and action:

$\lt S, A \gt$

We can experience different transitions by trying them in the world and seeing where we end up, and what rewards we receive.

So, we need a new version of our algorithm, whereby experimentation with different actions is part of the computation.
