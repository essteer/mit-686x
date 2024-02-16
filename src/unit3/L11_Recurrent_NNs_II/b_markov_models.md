# Markov Models

The next word in a sentence depends on previous symbols already written (history = one, two, or more words).

Similarly, the next character in a word depends on previous characters already written.

We can model $k$-th order dependencies between symbols with Markov models.

In simple terms:

- we can predict the next word in a sentence based on the preceding words, and
- we can predict the next letter in a word based on the preceding letters.

The Markov model gives a distribution on what comes next, based on $k$-steps backwards.

**Markov language models**

Let $w ∈ V$ (a word in a limited Vocabulary) denote the set of possible words and symbols that includes:

- an $UNK$ symbol for any unknown word (out of Vocabulary), a catch-all
- \<beg\> symbol for specifying the start of a sentence
- \<end\> symbol for specifying the end of the sentence

- \<beg\> The lecture leaves me UNK \<end\>

Consisting of $w_0, w_1, w_2, w_3, w_4, w_5, w_6$.

Once the \<end\> symbol is predicted by the model, it stops generating words.

The first order Markov model defines a conditional probability of what comes next, based, only on the previous word.

$P(w_1, ⋯, w_6) = P(w_1 | w_0) ⋯ P(w_6 | w_5)$

Where $w_0 =$ \<beg\> and $w_6 =$ \<end\>

| wi-1    | ML  | course | is  | UNK | \<end\> |
| ------- | --- | ------ | --- | --- | ------- |
| \<beg\> | 0.7 | 0.1    | 0.1 | 0.1 | 0.0     |
| ML      | 0.1 | 0.5    | 0.2 | 0.1 | 0.1     |
| course  | 0.0 | 0.0    | 0.7 | 0.1 | 0.2     |
| is      | 0.1 | 0.3    | 0.0 | 0.6 | 0.0     |
| UNK     | 0.1 | 0.2    | 0.2 | 0.3 | 0.2     |

Each symbol (except \<beg\>) in the sequence is predicted using the same conditional probability table until an \<end\> symbol is seen.

Note that the probabilities in the rows sum to $1$, since they are a distribution.

**Example**

The probability of generating "course is great":

- course is great -> course is UNK
- \<beg\> course is UNK \<end\>

$P(course|\lt beg \gt)P(is|course)P(UNK|is)P(\lt end \gt |UNK) = 0.1 \times 0.7 \times 0.6 \times 0.2$

**Maximum likelihood estimation**

To use the Markov model, we must estimate it from data.

Seek to maximise the probability that the model can generate all the observed sentences (corpus $S$).

$S$ is a collection of sentences, of varying length.

$s ∈ S, s = {w_1^s, w_2^s, ⋯, w_{|s|}^s}$

For a particular sentence, $s$:

$\prod_{i=1}^{|s|} P(w_i^s | w_{i-1}^s)$

The product of these probabilities is what the Markov model defines as the probability of generating this sentence.

To generate all sentences, we take the product of those individual sentence proabilities.

$\prod_{s∈S} [\Pi_{i=1}^{|s|} P(w_i^s | w_{i-1}^s)]$

We may then take a log of this, so that the products become sums.

The maximum likelihood estimate is obtained as normalised counts of successive word occurrences (matching statistics).

$count(w, w^{\prime})$

$\hat{P}(w^{\prime}|w) = \frac{count(w, w^{\prime})}{\sum_{\tilde{w}} count(w, \tilde{w})}$

So, we sum over possible words that can come after $w$.
