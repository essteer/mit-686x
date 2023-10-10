# Markov Models to Feedforward Neural Nets

We can represent Markov models as FNNs.

To do this, we define an input to the FNN, a one-hot vector corresponding to the previous word, and introduce an input unit for each of the possible previous words.

Since this is a one-hot vector, only one coordinate value is a 1, the rest are 0.

We denote this vector below as x.

x = φ(w<sub>i-1</sub>)

We then map this input vector into a row of probabilities in the conditional probability table - what is the probability of a word, given the previous word.

The value of each output unit, is the probability of the word appearing.

The k-th output unit is the probability that the next work is k, given the previous word was w<sub>i-1</sub>:

P<sub>k</sub> = P(w<sub>i</sub> = k | w<sub>i-1</sub>)

To perform the calculation, we have the parameter matrix W, so the aggregate input to the k-th output unit z<sub>k</sub> is the sum over the possible input units, their coordinates, and the values of the parameter matrix for the corresponding coordinates, plus an offset parameter.

z<sub>k</sub> = Σ<sub>j</sub> x<sub>j</sub>Wx<sub>jk</sub> + W<sub>0k</sub>

These aggregate input values are just real numbers, z<sub>k</sub> ∈ ℝ, they are not probabilities.

Therefore, the non-linear transformation we need is that the P<sub>k</sub>'s are non-zero, and must sum to 1 over the possible next words.

A typical transformation to achieve this is softmax.

We first exponentiate all of the input values, and then normalise them across the output units.

P<sub>k</sub> = e<sup>z<sub>k</sub></sup> / Σ<sub>j</sub> e<sup>z<sub>j</sub></sup>

**Note**

There are as many weights as there are output units.

The weights fully control what the resulting probability values are.

Given a previous word, we have full control over the probabilities for the first-order Markov model.

**Advantages**

The FNN is extendable.

For example, we previously had one input unit per coordinate of the one-hot vector corresponding to the preceding word, but we can easily add as an input, a one-hot vector corresponding to the word before that, and map both of these to output units that give the probability of the next word given the previous two words.

We can also modify the model by inserting hidden layers between the input and output, to examine more complex combinations of the preceding two words, in terms of how they map to the probability values over the next word.

**Temporal / sequence problems**

Trigram language model.

We take two preceding words, and for any such combination, predict the probability of what the next word is.

For v possible words, for each combination of preceding words there are |v|<sup>2</sup> of them, and for each of those combinations there is a probability value for each of the next words:

|v|<sup>2</sup> \* |v|

So for the Markov model, the number of parameters is roughly O(|v|<sup>3</sup>), or the number of words in the trigram model to the power of 3.

In comparison, using the FNN model that takes two preceding words as an input, the number of parameters is of dimension on the order of two times the number of words, times the number of output units:

O(2|v|<sup>2</sup>)

So, we use far fewer parameters for the FNN than for the Markov model.

It is less general as a result, but it is more feasible in terms of the number of parameters we must estimate.

We can also make the trigram FNN model more complicated or expressive, by introducing a hidden layer inbetween the input and output units, and mapping the combination of preceding words to the hidden layer, and then to the output layer.
