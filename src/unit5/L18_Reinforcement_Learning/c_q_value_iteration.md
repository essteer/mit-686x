# Q Value Iteration by Sampling

This method has similar qualities to the MDP Q value iteration.

It is still an iterative algorithm, but now it is based on the samples, and we don't know the transitions and rewards ahead of times.

So, we integrate our computation of the Q values with our actions in the world.

Whatever we do and experience in the world, we want to immediately feed in to update our values.

First, we need a measure of how we are acting, and how to act, then we want to know if we have already acted, how this affects our estimation.

We begin with the assumption that we have been told how to act, and know what to try, so the goal becomes to understand how the evidence we obtain from the action should change our Qs.

**Q-value iteration for reinforcement learning**

We don't know the transition probabilities; we just begin sampling.

sample<sub>1</sub>: R(s,a,s'<sub>1</sub>) + γ max<sub>a'</sub> Q(s'<sub>1</sub>,a')

Here we just take this Q as a previous estimate.

We can continue taking samples, and now let's say we will take sample K.

sample<sub>K</sub>: R(s,a,s'<sub>K</sub>) + γ max<sub>a'</sub> Q(s'<sub>K</sub>,a')

So it is exactly the same, we will just end up in a different state.

We have collected K samples, and can just take an average over these samples to get our Q(s,a).

Q(s,a) = 1/K Σ<sub>i=1</sub><sup>K</sup> sample<sub>i</sub>

In recursive form, this becomes:

Q(s,a) = 1/K Σ<sub>i=1</sub><sup>K</sup> (R(s,a,s') + γ max<sub>a'</sub> Q(s'<sub>i</sub>,a'))

**Simple example**

Assume that when in state s, there is a 50% chance of ending up in state s'<sub>1</sub>, and a 50% chance of ending up in state s'<sub>2</sub>.

Among our K samples, we can see empirically that roughly half of the time we will be in each of the states s'<sub>1</sub> and s'<sub>2</sub>.

Therefore each will contribute to the sum roughly 1/2 of the times.

**Incremental updates**

In reality, we cannot retrace our steps as in a simple example such as a coin toss - we must continue taking actions as dictated by the algorithm.

We cannot really stay in one place and try to sample it mutliple times.

We will hopefully return to the state s at some point and then be able to improve our estimate.

But we don't want to wait until we have sampled all and then update our estimate.

What we want to do, is update our Q value incrementally each time we get our sample.

To handle this need, we implement exponential running average, a method for averaging that differs from the standard averages, because it weights the significance of samples differently.

ERA gives more weight to the current sample, than prior samples that were collected.

We will introduce the formula for ERA below, and then proceed to rewrite Q to take on ERA.

**Exponential running average**

x̄<sub>n</sub> = (x<sub>n</sub> + (1-α)x<sub>n-1</sub> + (1-α)<sup>2</sup>x<sub>n-2</sub> + ⋯) / (1 + (1-α) + (1-α)<sup>2</sup> + ⋯)

Rewritten recursively:

x̄<sub>n</sub> = αx<sub>n</sub> + (1-α)x<sub>n-1</sub>

This says that the current exponential average, is the weighting of the current sample, plus the weighting of the previous ERA.

It gives us a mechanism to take the prior estimate of the ERA, and add to it the new sample that we are taking.

So we take this ERA, and utilise it to compute differently our estimates for Q values.

**Recomputing Qs with ERA**

Q<sub>i</sub>(s,a) = α sample + (1-α)Q<sub>i</sub>(s,a)

Where the Q<sub>i</sub>(s,a) on the right-hand side is our previous estimate of the value Q for state s and action a.

We multiply by (1-α), and then the sample will be one of those.

sample = R(s,a,s') + γ max<sub>a'</sub> Q<sub>i</sub>(s',a')

**Algorithm**

We initialise everything to zero, and then iterate.

1. Initialise all Q(s,a) = 0 ∀ s,a
2. Iterate until convergence

Where convergence refers to a substantially small difference between the values of the new and prior step.

The iterative steps are as follows:

2a. Collect sample: s,a,s', R(s,a,s')
2b. Q<sub>i+1</sub>(s,a) = α • (R(s,a,s') + γ max<sub>a'</sub>Q<sub>i</sub>(s,a)) + (1-α)Q<sub>i</sub>(s,a)

This formula is complete, but we can also rewrite it into a form more familiar to other algorithms studied previously.

**Algorithm - alternative form for 2b**

2b. Q<sub>i+1</sub>(s,a) = Q<sub>i</sub>(s,a) + α • (R(s,a,s') + γ max<sub>a'</sub>Q<sub>i</sub>(s,a) - Q<sub>i</sub>(s,a))

So we have separated our the terms that are and are not guided by α.

Note that it can be shown that the same conditions on alpha that were used to demonstrate convergence with gradient descent can be applied here.

Under this condition, the algorithm is guaranteed to converge.

Once it has converged, we have our policy.
