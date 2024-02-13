# Softmax Overview and Layman Perspective

**In layman terms: softmax is how we pick the best answer, while being fair about ties.**

Softmax is useful throughout ML, to make models able to handle uncertainty, including being able to express lack of understanding.

This has applications for calibrating confidences.

We can calibrate uncertainty scores for linear classification, as well as in deep learning.

**Featurisation**

Taking the raw input, say, a bird to be classified as either a roc or an ostrich, and conveying its features in some form (e.g., height and weight) that we deem to be relevant to its classification.

**Learned weight matrix**

In this 2D (height - weight) example, we convert our features into a 1D axis, a line, with one side of the axis for points deemed more likely to be a roc, and another side for points more likely to be an ostrich.

We can write this as a $w$ matrix with three components, $[x~x~x]$, one for each of height and weight, plus a third - we concatenate a $1$ to enable us to transmit into 3-dimensional vectors.

This bias also enables us to have decision boundaries that don't necessarily go through the origin.

Applying this $1$ x $3$ matrix to our data resolves to number on our line, the learned weight matrix.

Depending on whether the number is +ve or -ve, we can decide whether it is likely to be a roc or an ostrich.

**Sigmoid**

However, we might not only be interested in the classification, but also how likely the classification is to be correct.

So, we want to turn values from the learned weight matrix, an infinite real line, into values between $0$ and $1$. To do this, we use a sigmoid function.

There are in fact many functions that could be chosen for this purpose, but sigmoid generalises well to softmax.

In the straight example above however, the sigmoid is asymmetric, because we have selected e.g. the ostrich to be $0$, and the roc to be $1$.

**Softmax**

With softmax, we want to reintroduce symmetry.

This time, to create our learned weight matrix, instead of one weight $w = [x~x~x]$, instead we pretend that we have two different $w$'s, where each row corresponds to one class: the top row says how ostrich-y it is, the bottom row how roc-y it is:

$w = [x~x~x; x~x~x]$.

This is a redundant parameterisation: for example, if we add a bias term of $1$ to each row, we have increased both the ostrich and the roc quality of the points, so the difference - which is what we care about - remains the same.

The cost of introducing symmetry is to incorporate some redundancy.

So, we have converted our features into a 2-dimensional plane that depicts ostrich-ness and roc-ness.

If we chose to, we could recover the original 1-D formulation by projecting a $[-1~1]$ matrix onto the learned weight matrix.

However, we can achieve the same result without needing to project.

We can define the map from the learned weight matrix space to the $0-1$ space, taking an $[o~r]$ (ostrich-ness and roc-ness) vector, which maps to our softmax:

- $[\frac{e^o}{e^o + e^r}; \frac{e^r}{e^o + e^r}]$

Where the denominator is the normalisation, while the numerator ensures a positive value (taking exponentials makes everythin positive).

We then can simply take the argmax and whichever is the highest (ostrich or roc) is our classification.

**Utility of the symmetric approach**

The symmetric approach is useful because we can generalise it to more than two classes.

E.g. if we now have ostrich, roc, and emu classifications, and thus a $3$ x $3$ matrix $w = [x~x~x; x~x~x; x~x~x]$.

Our features are then conveyed into a 3D learned weight matrix space, instead of a 2D space.

Then, taking a vector of $[o~r~u]$ ($u$ for emu to avoid conflict with $e$ exponent), we have a softmax function of:

- $[\frac{e^o}{e^o + e^r + e^u}; \frac{e^r}{e^o + e^r + e^u}; \frac{e^u}{e^o + e^r + e^u}]$

Essentially, softmax helps us turn scores into probabilities.

**Summary**

In layman terms: softmax is how we pick the best answer, while being fair about ties.

Softmax enables the ML model to say "I don't know", and so it can learn step-by-step.

From this, we can also calibrate confidences about the certainty of our outcomes.
