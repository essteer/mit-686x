# Word Embeddings

**Sparsity**

Features are often represented as high-dimensional, sparse vectors.

Comparing unigrams with bigrams, as we increase the number of sentences, the coverage improves.

With bigrams, the frequency of occurrences remains low even with large training sizes.

For languages in which words repeat many times, it is easier to parse than words with many different endings.

Languages with insufficient frequency will get much lower performance from a model on the same amount of training data, than for another language such as English with high frequency.

**Selecting feature representation**

Traditionally, features of compositional objects are manually-selected concatenations of atomic features.

The arrival of neural models has eliminated the need for manual engineering in this way.

One-hot vector representation records only the presence (or absence) of a word in a bag of words.

The dimensionality of the vector is the size of English vocabulary, and each word has its own dedicated place.

The bit will be on for the words that are included in the sentence, and off for all others.

The bag of words can then be run through a classifier, and we can make a prediction.

**Text classification**

That approach is problematic, however.

If we train on "I love dogs", our model may learn from the presence of "dogs" that we are talking about animals.

But if the model has never encountered "samoyed", a breed of dog in its training, it would have no ability to treat this term as being connected with animals.

**Word embeddings**

Ideally, we want to move towards word embeddings, where we take one-hot encoding and translate it into a dense continuous vector in such a way that the distance between "dogs" and "samoyed" will be very close to each other.

Originally, using one-hot encoding representation, the cosine distance between "dogs" and "samoyed" would be the same as between "dogs" and "lipstick".

But with word embeddings, we are interested in a transformation, that marks them to a new space where the vectors will be close to each other.

We do not need manual efforts to achieve this, but can look at large quantities of data to learn it.

When estimating the models, we can take one of the hidden layers and represent and use it as an embedding of the word of interest.

Neural networks provide a means of encoding and decoding sentences and meaning that is far more generalisable.
