# Why We Need RNNs

Flexibility in encoding sequences is relevant to tasks including:

- Language modeling.
- Sentiment classification.
- Machine translation.

For language modeling, we have part of a sentence and may turn that into a feature vector, then apply standard prediction tools to predict what would happen next.

Or, for sentiment classification, we may take the entire sequence and turn it into a vector, then predict properties pertaining to the whole sequence.

Or again, we might take the entire sequence, turn it into a vector, and try to unravel the vector into the same sentence written in another language - a structured prediction task.

**The vector representations needed in each of these examples are different.**

I.e., prediction, sentiment, and semantics each require different focus.

Furthermore, we distinguish:

- **encoding**, mapping an observed sequence to a vector, and
- **decoding**, mapping that vector to a prediction.

If the prediction is itself a sequence (such as in machine translation), we also need a summarisation in that part.

RNNs help solve issues such as the question of how many time steps back we should look at in the feature vector.
