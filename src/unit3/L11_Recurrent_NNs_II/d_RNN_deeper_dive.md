# RNN Deeper Dive

The problem with the previous first- and second-order Markov model formulations, and their FNN equivalents, is that they look at a fixed history to predict what happens next.

We want the history to be variable, and learnable, so the model can decide what part of what it has seen so far, it should pay attention to for the purpose of predicting what comes next.

We therefore want to reconstruct the model as a recurrent NN.

**RNNs for sequences**

"This couse has been a tremendous | ..."

We feed into the vector, a one-hot model of the previous word:

$\phi(tremendous) [0, ⋯, 1, 0]$

Where $tremendous = w_{t-1}$

With $t$ referring to the time or position in the sentence when we are trying to make a prediction.

When we want to predict $w_t$, we feed in a one-hot vector of $w_{t-1}$.

We call that vector $x_t$, and the length of that vector is the number of words that can precede.

We map this into a hidden state of length m hidden units, and call the vector of activations of those hidden units, $s_t$.

So $s_t$ is an $m$-dimensional vector of the activations of the hidden units.

The parameter matrix that mediates these interactions is $W^{s,x}$.

We map those hidden state activations into output unit activations, that are now the probabilities of the word we wish to predict.

$W^o$ denotes the parameters for the matrix that transforms the $s_t$ vector into probabilities.

As a result, we get a vector of values $P_t$, where each coordinate of this vector is the value of the output unit, the probability of a particular word that would come next at time $t$.

**Recurrence**

We make this into a recurrent NN model, by feeding in the previous hidden state activation.

We introduce $s_{t-1}$ as a further input - what we had computed previously.

The state we have at time $t$, is the only information that we make a prediction about the next word.

So what is inside that state description?

- The one-hot vector representation of the preceding word.
- The preceding state is also affecting how the new state is calculated.
- The preceding state was calculated on the basis of the word two steps behind, so that information is retained in $s_t$.
- The preceding state was influenced by the word a step before that state, and so on.

$s_t$ therefore carries information from the beginning of the sentence.

We have the encoder RNN state update of the basic RNN model, with an input vector transformed by a weight matrix as an input to the state calculation, and a weight applied to the previous state:

- $state = s_t = tanh(W^{s,s}s_{t-1} + W^{s,x} x_t)$

In addition, at each timepoint we derive from the state an output distribution, of what happens next:

- output distribution = $p_t = softmax(W^o s_t)$

The difference with the previous model is therefore that now we use the current state of the encoding process along the sequence, to derive the distribution over what happens next.

For the more complex decoding LSTM model, the variables for the forget gate, input gate, and so on, are analagous, but we now add our $p_t = softmax(W^o s_t)$ to the model.
