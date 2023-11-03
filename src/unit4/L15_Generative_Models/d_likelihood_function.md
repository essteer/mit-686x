# Likelihood Function

P(w|θ) = θ<sub>w</sub>

- θ<sub>w</sub> >= 0
- Σ<sub>w∈W</sub> θ<sub>w</sub> = 1

Given the above formulation, how do we compute the likelihood of generating a document?

Assume we have our document, _D_, given particular θs:

P(D|θ) = Π<sub>i=1</sub><sup>n</sup> θ<sub>w<sub>i</sub></sub>

So, we take every word in our document, and multiply the probabilities together.

We then amend this expression, to account for the fact that the same word may appear multiple times in the document, and so instead of multiplying the probability of the same word, say, 5 times, instead make this probability in the 5th degree.

P(D|θ) = Π<sub>i=1</sub><sup>n</sup> θ<sub>w<sub>i</sub></sub> = Π<sub>w∈W</sub> θ<sub>w</sub><sup>count(w)</sup>

Instead of taking the product of the probability of all of the words, we go over each word, take the probability and put it in count(w) for each word in the document.

**Example**

An example of how this simple model can be used to evaluate a document: imagine a vocabulary of just two words, "cat" and "dog".

W = {cat, dog}

Model 1 θ: θ<sub>cat</sub> = 0.3, θ<sub>dog</sub> = 0.7

Model 2 θ': θ'<sub>cat</sub> = 0.9, θ'<sub>dog</sub> = 0.1

These two models will generate different types of documents; the first prefers "dog", the second prefers "cat".

For a document _D_ with two "cat", then "dog":

D = {cat, cat, dog}

We can compute the likelihood of this document _D_ being generated by either the first or the second model.

What is the probability of this document _D_, given parameter θ (Model 1)?

P(D|θ) = 0.3<sup>2</sup>•0.7

For parameter θ' (Model 2):

P(D|θ') = 0.9<sup>2</sup>•0.1