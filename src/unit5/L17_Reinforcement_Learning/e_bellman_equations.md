# Bellman Equations

$V^{*}(s)$ tells us the value of the expected reward if we start at state $s$, and then act optimally.

(Instead of "acting optimally" we could also refer to this as acting according to the policy.)

For $V^{*}(s)$, we don't care about the actions.

Now we introduce the $Q$-value, which is defined in terms of state and action.

$Q^{*}(s,a)$ tells us the expected reward if we start at state $s$, take action $a$, and then act optimally.

$\pi^{*}(s)$ is our optimal policy.

So we have:

- $V^{*}(s)$
- $Q^{*}(s,a)$
- $\pi^{*}(s)$

Bellman equations connect these together.

**Bellman equations**

$V^{*}(s) = max_a Q^{*}(s,a)$

From this state we can take many possible actions, but to continue acting optimally we must select the best action.

To do so, we must try different $Q$'s with different possible $a$'s, and select the one which gives us the highest Q.

Another way to write this is $Q^{*}(s, \pi^{*}(s))$.

$V^{*}(s) = max_a Q^{*}(s,a) = Q^{*}(s, \pi^{*}(s))$

This tells us, instead of explicitly saying we're taking the best possible action, that this is the action that should be written in our policy.

Our policy will tell us which is the best action to take.

$Q^{*}(s,a)$ - in this case we are in state $a$, and took an action $a$. We begin by explaining as if we deterministically know where we will end up.

We can say that the transition function tells us that whenever we are in a state $a$ and they taken action $a$, we are always going to be at the exact same place.

Whenever we take our first step, we collect our reward plus we are now in a new step, and our value is dependent on whatever we can collect from that step.

We are now in state $s$ prime, ($s^{\prime}$), and want to see what the best expected reward would be from $s^{\prime}$ to the end.

$Q^{*}(s,a) = (R(s,a,s^{\prime}) + \gamma V(s^{\prime}))$

We value the current reward more than the future reward, weighed by gamma.

Now we must add the fact that in reality, whenever we take the action $a$ from state $s$, we are not guaranteed to get to state $s^{\prime}$ - we must introduce probability.

$Q^{*}(s,a) = \sum_{s^{\prime}} T(s,a,s^{\prime}) (R(s,a,s^{\prime}) + \gamma V^{*}(s^{\prime}))$

We look at the likelihood of actually getting to a particular state $s^{\prime}$, and the transition function tells us this likelihood.

Now we can define $V$ in a similar fashion, and do so recursively by substituting in what we have defined $Q^{*}$ to be.

$V^{*} = max_a [\sum_{s^{\prime}} T(s,a,s^{\prime}) R(s,a,s^{\prime}) + \gamma V^{*}(s^{\prime})]$

So now we have the full expression for $V^{*}(s)$ in terms of other states that could be reached by subsequent actions.
