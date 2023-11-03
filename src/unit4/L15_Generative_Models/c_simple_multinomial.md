# Simple Multinomial Generative Model

Multinomials are commonly used to generate text / documents.

Some documents will have a high probability, whereas others may have a very low probability.

We use a simple definition for "generate" here: we assume the model has a fixed vocabulary, _W_, and then the model generates one word _w_ at a time from the bag of possible words.

All of the words selected are independent of each other - this will likely not generate "beautiful" sentences, but this is just the first simple model to consider.

**Parameters for multinomials**

We need to decide how likely it is that certain words will be generated.

One parameter is then the likelihood of generating the word w, given the parameterisation of the model:

P(w|θ) = θ<sub>w</sub>

θ<sub>w</sub> is the likelihood of generating certain words, given all of the possibilities.

To ensure it is a valid probability distribution, we must ensure the following constraints:

- each θ<sub>w</sub> >= 0
- the sum of all θ<sub>w</sub> = 1
