# Maximum Likelihood Estimate

$P(w|θ) = θ_w$

- $θ_w \geq 0$
- $\sum_{w∈W} θ_w = 1$

$P(D|θ) = \prod_{i=1}^{n}{θ_{w_i}}$

How can we utilise our training data to find the best parameters?

**Maximum likelihood**

We make the assumption that the best parameters are those that give the highest likelihood for our data.

We want to find the $θ$ which maximise this expression:

$max_{θ*} \: P(D|θ) = max_{θ*} \: \prod_{w∈W} θ_w^{count(w)}$

Instead of working with this expression directly, we can maximise the log:

$log \prod_{w∈W} θ_w^{count(w)}$

Log of the product is sum of logs, so we can rewrite this as:

$\sum_{w∈W} \: count(w) \: log \: θ_w$

So, we are trying to find $θ$'s that will maximise the value of this expression.

**Back to the two-symbol example**

$W = \lbrace 0, 1 \rbrace$ (instead of $\lbrace cat, dog \rbrace$)

This is a special case because we only need it to have a single theta.

We need a $θ$ for $θ_0$, the likelihood of generating $0$:

$θ_0 = θ$

but for $1$ we can just do:

$θ_1 = 1 - θ_0$.

So, we have just one parameter, and can rewrite our expression for just one $θ$:

$count(0) \: logθ + count(1) \: log(1-θ)$

We then want to find the derivative of this expression with respect to $θ$:

$\frac{\partial{}}{\partial{θ}} [count(0) \: logθ + count(1) \: log(1-θ)] = \frac{count(0)}{θ} - \frac{count(1)}{1-θ}$

To find our desired $θ$, we set this equal to $0$:

$\frac{count(0)}{θ} - \frac{count(1)}{1-θ} = 0$

Which evaluates to:

$(1-θ)count(0) - θcount(1) = 0$

For our $θ$ estimate, $θ^{*}$:

$θ^{*} = \frac{count(0)}{count(1) + count(0)}$

This is straightforward, since for example in a document with $20$ $0$'s and $10$ $1$'s, the likelihood of a $0$ is $20 \over 30$.
