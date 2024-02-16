# Encoding with RNN

We can transform a sequence into a vector using a parametric transformation.

This transformation is undertaken in such a way that it can later be adjusted to suit the application we want to use the vector for.

We attempt this by turning a sequence piecemeal (e.g., one word at a time) into a vector, with "lego bricks" that are adjustable and can later be optimised for end-to-end performance.

To do this:

1. Take what we have already, **context or state**;
2. Add **new information**; and
3. Apply a box or function that takes what we already have, introduces the new information, and outputs our **new context or state**.

We can adjust the parameters to change the behaviour of this transformation.

This type of transformation, that has an evolving state, is called a **Recurrent Neural Network**.

$s_t = tanh(W^{s,s}s_{t-1} + W^{s,x}x_t)$

Where:

- $s_t =$ new context or state, an $m \times 1$ dimensional vector

- $s_{t-1} =$ previous context or state, an $m \times 1$ dimensional vector

- $W^{s,s} =$ a transformation that tells us how the state would evolve in the absence of information, an $m \times m$ dimensional parameter matrix

- $x_t =$ new information, a $d \times 1$ dimensional vector

- $W^{s,x} =$ a transformation from the word $x_t$ to the state, an $m \times d$ dimensional parameter matrix

We therefore have an $m$-dimensional vector within the tanh function (the result of the addition of $m \times 1$ and $m \times 1$ vectors).

We apply the tanh transformation element-wise, to turn it into a new representation of a state.

The two parameters $W^{s,s}$ and $W^{s,x}$ therefore determine the $θ$ parameters in our box or function, representing the transition from the previous to the new state (or context).

We can adjust the $θ$ parameters so that the function / box behaves as we want it to.

**Sentence example**

"Efforts and courage are not..."

We start with a null (empty) matrix, $s_0$, which has not yet "seen" any words.

We get a new word ("Efforts"), $x_1$, and apply the box / function to this single word based on the current state, to get a summary of what the model thinks the word "Efforts" is.

This then outputs our vector $s_1$, a summary of "Efforts", and the model continues on to $x_2$ ("and"), and on through the sentence.

**Differences between the encoder and feed-forward NN**

1. Input is received at each layer (per word), not just at the beginning as in a typical feed-forward NN.
2. The number of layers varies, and depends on the length of the sentence.
3. The parameters of each layer (representing an application of an RNN) are shared (same RNN at each step).
