# Value Iteration

Value iteration algorithm enables us to solve MDP, given the quadruple of state, action, transition, and reward.

We now elaborate on V\*(s) seen earlier, to speak in terms of the expected value after K steps.

V\*<sub>K</sub>(s) = expected reward from state s after K steps.

The connection between this V\*<sub>K</sub> and the original V\*, is that when K goes to infinity, we would say that V\*<sub>K</sub> would converge to the true value of the state.

So, the recursive algorithm will at each point continue increasing number K until we converge to the true value of the state.

**First step - initialisation**

During the first step of the algorithm, we initialise all of the values as:

V\*<sub>0</sub>(s) = 0.

We can think of information from the states where we get high reward as slowly propagating around the board.

The first time we will look just in one step, then two steps, and so on, and continue until convergence.

**Iteration**

Our next step would be to continue to iterate until:

V*<sub>k</sub>(s) ≈ V*<sub>K+1</sub>(s) ∀ s

So, we continue the process until the values of the states do not change after every iteration.

We define the value of our state at the point V\*<sub>K+1</sub>(s) in terms of the values of the states through the previous iterations.

We computed the optimal values for the K steps, and now aggregate this information to get the value for the K+1 step.

Whenever we're going to look at the value of the neighbouring states, we can take the values that were collected after K steps.

The value that we get after K+1 steps, is the value we'll collect from an extra step, plus the values of the neighbouring steps.

V\*<sub>K+1</sub>(s) = max<sub>a</sub> [Σ<sub>s'</sub> T(s,a,s') (R(s,a,s') + γV\*<sub>K</sub>(s'))]

**Illustration**

Imagine a simple world with just 5 states, as follows:

| s1  | s2  | s3  | s4  | s5  |
| --- | --- | --- | --- | --- |
|     |     |     |     | +1  |

Also assume a deterministic world, where only one outcome will result from an action (i.e., if we decide to move right, we always move right).

Assume:

γ = 1/2

During step 0, all V's are initialised to 0:

| s1  | s2  | s3  | s4  | s5  |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   |

During step 1, we go step by step, and see how the value is updated.

It doesn't matter which order we begin in, because here the states aren't ordered in any way.

We are only looking at the values of the previous iteration, so it doesn't matter if we start computing V1's from the left or right.

So, imagine we can walk just one step further from s1, the value of the state will be 0, because there is zero reward.

This will continue through s2, s3, and s4.

The only place there will be a change is at the last step, s5.

We know that from s5 when we try to walk right, which results in staying in the same place, we will collect the reward.

| s1  | s2  | s3  | s4  | s5  |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | +1  |

Let's say that s5 is a halting state, meaning that we cannot go back and forth and increase the number; once collected, we cannot do it again.

**Two steps within iterations**

Now we examine how the value changes when we can do two steps within our iterations.

Again, the order doesn't matter, because when we look at the values of the neighbouring states, we just look at the previous step.

Nothing changes for s1, s2, or s3, because the neighbours are still 0:

| s1  | s2  | s3  | s4  | s5  |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   |     |     |

s5 remains as +1, because once the reward is collected, it cannot be had again.

| s1  | s2  | s3  | s4  | s5  |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 1/2 | +1  |

At s4, the γ term of our function is activated, γV\*<sub>K</sub>(s'), because V<sub>K</sub>, which is the V\*<sub>1</sub> of the previous state, is +1, and we multiply this by γ, which is 1/2.

The state for s4 is therefore 1 \* 1/2 = 1/2.

We can continue on to the next step, and see how the value will propagate through, and the number of non-zero states will increase over subsequent steps until we no longer see any change.

**Convergence**

We now take an even simpler world, with a single state s, and a single action a.

V\*<sub>K+1</sub>(s) = R(s) + γV\*<sub>K</sub>(s)

Once we are in the converged state s, then nothing will change after our next step.

V\*(s) = R(s) + γV\*(s)

So now we subtract the converged value, from the value in the K+1 iteration.

(V\*(s) - V\*<sub>K+1</sub>(s)) = γ(V\*(s) - V\*<sub>K</sub>(s))

The left-hand side is the difference between the converged state and the value at step K+1.

The right-hand side is the difference between the converged state and the value at the K step.

We see that at every single step, the difference between them is determined by γ, which is a value between 0 and 1.

At every step, the distance between our computed value K and the true converged value V decreases, and γ determines the rate at which the decrease will happen.

**Next step**

Now with our value of V, we can compute the Qs, because we saw from our Bellman equation for Q that Q is expressed in terms of V.

Once we have all of the Qs, we will be able to find the best possible action for every state.

For every state s, and every action a, we compute the Q value.

Once all Qs are computed, then the action to take is just the argmax:

π\*(s) = argmax<sub>a</sub> Q\*(s,a)

So, after the algorithm has converged, we can compute the Q values, and then compute the policy π.
