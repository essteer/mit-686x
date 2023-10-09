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

- s<sub>t</sub> = tanh(W<sup>s,s</sup>s<sub>t-1</sub> + W<sup>s,x</sup>x<sub>t</sub>)

Where:

- s<sub>t</sub> = new context or state, an (m x 1) dimensional vector

- s<sub>t-1</sub> = previous context or state, an (m x 1) dimensional vector

- W<sup>s,s</sup> = a transformation that tells us how the state would evolve in the absence of information, an (m x m) dimensional parameter matrix

- x<sub>t</sub> = new information, a (d x 1) dimensional vector

- W<sup>s,x</sup> = a transformation from the word x<sub>t</sub> to the state, an (m x d) dimensional parameter matrix

We therefore have an m-dimensional vector within the tanh function (the result of the addition of (m x 1) and (m x 1) vectors).

We apply the tanh transformation element-wise, to turn it into a new representation of a state.

The two parameters W<sup>s,s</sup> and W<sup>s,x</sup> therefore determine the θ parameters in our box or function, representing the transition from the previous to the new state (or context).

We can adjust the θ parameters so that the function / box behaves as we want it to.

**Sentence example**

"Efforts and courage are not..."

We start with a null (empty) matrix, s<sub>0</sub>, which has not yet "seen" any words.

We get a new word ("Efforts"), x<sub>1</sub>, and apply the box / function to this single word based on the current state, to get a summary of what the model thinks the word "Efforts" is.

This then outputs our vector s<sub>1</sub>, a summary of "Efforts", and the model continues on to x<sub>2</sub> ("and"), and on through the sentence.

**Differences between the encoder and feed-forward NN**

1. Input is received at each layer (per word), not just at the beginning as in a typical feed-forward NN.
2. The number of layers varies, and depends on the length of the sentence.
3. The parameters of each layer (representing an application of an RNN) are shared (same RNN at each step).
