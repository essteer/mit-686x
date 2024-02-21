# Estimating Inputs for RL Algorithm

Starting from $\lt S A \gt$ we may consider why we cannot simply iterate through possible $T$'s and $R$'s to find the optimal representations for the model.

For instance, to calculate the transition probabilities, we may count how many times we actually visit $s^{\prime}$, and divide this by all of the possible $s^{\prime}$:

$\hat{T} = \frac{count(s,a,s^{\prime})}{\sum_{s^{\prime}}(s,a,s^{\prime})}$

This would obtain an estimation, and a similar effort could be made for the rewards. In real life rewards may vary for the same state, or there may be no reward at all, so we may decide to take an average of the rewards we do receive:

$\hat{R} = \frac{\sum\nolimits_{t=1}^{count(s,a,s^{\prime})} R_{t}(s,a,s^{\prime})}{count(s,a,s^{\prime})}$

The main problem with this approach is that in the real world, every step we take puts us in a new step, and we are then going to go somewhere else - but unless we get to a specific state $s$, we cannot collect information about that state $s$.

For a complex navigation task, for example, the robot may never arrive at the end point because it doesn't know where it is supposed to go.

So in order to get reliable estimates, we do need to get to state $s$, and cannot rely on random trials to guarantee this.

We need some way to inform the robot which way it should go, to collect measurements.

**Model-based reasoning**

The above has been an example of model-based reasoning - all of the parameters are explicitly estimated, and the model is estimated through these parameters.

Then, you act in accordance with that model to act in the world.

**Model-free reasoning**

Another way is to approach the problem without the need for full estimates.

We can explore the world and collect some measurements, and as more samples are collected, the model becomes more and more intelligent (or accurate) to the real-world situation, and guides us towards where to collect further samples.

**Example of the difference**

First, with model-based learning, imagine we have a random variable $x$, and we are trying to estimate the expected value.

Our goal is to estimate:

$E[f(x)] = \sum_{x}{p(x) • f(x)}$

Let's say we have $K$ trials.

We can sample our random variables $K$ times (throwing a coin, collecting numbers, etc):

$x_i$ ~ $p(x), i=1,⋯,K$

We then want to get an estimate of $p(x)$.

$\hat{p}(x) = \frac{count(x)}{K}

That is, $\hat{p}$ is our estimated probability, calculated as the count of $x$'s observed, divided by the number of trials $K$.

Then, we can say that our estimate of the expected value is:

$E[f(x)] ≈ \sum_{x}{\hat{p}(x) • f(x)}$

This is model-based estimation.

Now we see how we can make this estimation without ever explicitly estimating the value of $\hat{p}(x)$.

For model-free estimation, the first step is the same:

$x_i$ ~ $p(x), i=1,⋯,K$

But now we don't want to estimate $\hat{p}(x)$. Model-based estimation was capturing how prevalent a certain value is, for example if a value was present 90% of the time, that is how it would contribute to the final estimate.

Here, instead of explicitly encapsulating it as 90%, for the model-free method we sum them up.

Each time we get a sample, we compute $f(x)$, sum from $1$ to $K$, and divide all by $K$.

$E[f(x)] ≈ \frac{1}{K} \sum\nolimits_{i=1}^{K}{f(x_i)}$

Values of $x$ which were much more prevalent appear a lot, and contribute via the number of times they appear; those which are less prevalent, appear less.

We then take the sum, and divide by $K$.

Although this may end up with the same outcome as the model-based approach, this way of thinking is useful for estimating the value of $Q$.
