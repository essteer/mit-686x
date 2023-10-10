# Markov Models

The next word in a sentence depends on previous symbols already written (history = one, two, or more words).

Similarly, the next character in a word depends on previous characters already written.

We can model k-th order dependencies between symbols with Markov models.

In simple terms:

- we can predict the next word in a sentence based on the preceding words, and
- we can predict the next letter in a word based on the preceding letters.

The Markov model gives a distribution on what comes next, based on k-steps backwards.

**Markov language models**

Let w ∈ V (a word in a limited Vocabulary) denote the set of possible words and symbols that includes:

- an `UNK` symbol for any unknown word (out of Vocabulary), a catch-all
- `<beg>` symbol for specifying the start of a sentence
- `<end>` symbol for specifying the end of the sentence

`<beg> The lecture leaves me UNK <end>`
Consisting of w<sub>0</sub>, w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub>, w<sub>4</sub>, w<sub>5</sub>, w<sub>6</sub>.

Once the `<end>` symbol is predicted by the model, it stops generating words.

The first order Markov model defines a conditional probability of what comes next, based, only on the previous word.

P(w<sub>1</sub>, ⋯, w<sub>6</sub>) = P(w<sub>1</sub> | w<sub>0</sub>) ⋯ P(w<sub>6</sub> | w<sub>5</sub>)

Where w<sub>0</sub> = `<beg>` and w<sub>6</sub> = `<end>`

|wi-1|ML|course|is|UNK|<end>|
|<beg>|0.7|0.1|0.1|0.1|0.0|
|ML|0.1|0.5|0.2|0.1|0.1|
|course|0.0|0.0|0.7|0.1|0.2|
|is|0.1|0.3|0.0|0.6|0.0|
|UNK|0.1|0.2|0.2|0.3|0.2|

Each symbol (except `<beg>`) in the sequence is predicted using the same conditional probability table until an `<end>` symbol is seen.

Note that the probabilities in the rows sum to 1, since they are a distribution.

**Example**

The probability of generating "course is great":

- course is great -> course is UNK
- `<beg>` course is UNK `<end>`

P(course|`<beg>`)P(is|course)P(UNK|is)P(`<end>`|UNK)

= 0.1 \* 0.7 \* 0.6 \* 0.2

**Maximum likelihood estimation**

To use the Markov model, we must estimate it from data.

Seek to maximise the probability that the model can generate all the observed sentences (corpus S).

S is a collection of sentences, of varying length.

s ∈ S, s = {w<sup>s</sup><sub>1</sub>, w<sup>s</sup><sub>2</sub>, ⋯, w<sup>s</sup><sub>|s|</sub>}

For a particular sentence, s:

Π<sup>|s|</sup><sub>i=1</sub> P(w<sup>s</sup><sub>i</sub> | w<sup>s</sup><sub>i-1</sub>)

The product of these probabilities is what the Markov model defines as the probability of generating this sentence.

To generate all sentences, we take the product of those individual sentence proabilities.

Π<sub>s∈S</sub> [Π<sup>|s|</sup><sub>i=1</sub> P(w<sup>s</sup><sub>i</sub> | w<sup>s</sup><sub>i-1</sub>)]

We may then take a log of this, so that the products become sums.

The maximum likelihood estimate is obtained as normalised counts of successive word occurrences (matching statistics).

count(w, w')

P̂(w'|w) = count(w, w') / Σ<sub>w̃</sub> count(w, w̃)

So, we some over possible words that can come after w.
