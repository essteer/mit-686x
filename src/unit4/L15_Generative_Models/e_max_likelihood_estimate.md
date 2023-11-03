# Maximum Likelihood Estimate

P(w|θ) = θ<sub>w</sub>

- θ<sub>w</sub> >= 0
- Σ<sub>w∈W</sub> θ<sub>w</sub> = 1

P(D|θ) = Π<sub>i=1</sub><sup>n</sup> θ<sub>w<sub>i</sub></sub>

How can we utilise our training data to find the best parameters?

**Maximum likelihood**

We make the assumption that the best parameters are those that give the highest likelihood for our data.

We want to find the θ which maximise this expression:

max<sub>θ</sub> P(D|θ) = max<sub>θ</sub> Π<sub>w∈W</sub> θ<sub>w</sub><sup>count(w)</sup>

Instead of working with this expression directly, we can maximise the log:

log Π<sub>w∈W</sub> θ<sub>w</sub><sup>count(w)</sup>

Log of the product is sum of logs, so we can rewrite this as:

Σ<sub>w∈W</sub> count(w) log θ<sub>w</sub>

So, we are trying to find θ's that will maximise the value of this expression.

**Back to the two-symbol example**

W = {0, 1} (instead of {cat, dog})

This is a special case because we only need it to have a single theta.

We need a θ for θ<sub>0</sub>, the likelihood of generating 0:

θ<sub>0</sub> = θ

but for 1 we can just do:

θ<sub>1</sub> = 1 - θ<sub>0</sub>.

So, we have just one parameter, and can rewrite our expression for just one θ:

count(0) logθ + count(1) log(1-θ)

We then want to find the derivative of this expression with respect to θ:

d/dθ [count(0) logθ + count(1) log(1-θ)] = count(0)/θ - count(1)/(1-θ)

To find our desired θ, we set this equal to 0:

count(0)/θ - count(1)/(1-θ) = 0

Which evaluates to:

(1-θ)count(0) - θcount(1) = 0

For our θ estimate, θ\*:

θ\* = count(0) / (count(1) + count(0))

This is straightforward, since for example in a document with 20 0's and 10 1's, the likelihood of a 0 is 20/30.
