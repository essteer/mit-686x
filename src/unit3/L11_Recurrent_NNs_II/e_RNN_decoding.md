# RNN Decoding

**Decoding into a sentence**

So, we want to decode a vector into a sentence - as in machine translation - rather than simply generating a sentence from scratch.

Our RNN now needs to produce an output (e.g., a word) as well as update its state.

The output is fed in as an input (to gauge what's left).

Now, rather that our initial state being a null vector of 0s, we now have a vector encoding of a sentence, e.g. "I have seen better lecture".

Call that vector s<sub>0</sub>.

We can also map images to text, via the same process.

The image would then be the initial states <sub>0</sub>, and could be used to, e.g., generate image captions.

**Note**

With decoding RNNs, it is the previous output x<sub>t</sub> but not the output probability ditribution p<sub>t</sub> that is fed into the next step.

The probability distribution is different at each step as it propogated from the beginning state.

With the probability distribution at each step, the output word is then sampled from the distribution.
