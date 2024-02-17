# MLE for Multinomial Distribution

Now we move on from the two-symbol model, in which we estimate a single $θ$.

To word with vocabulary of any length, there will be many different $θ$.

To do this, we make use of Lagrange multipliers.

$θ_w^{*} = \frac{count(w)}{ \sum_{w^{\prime}∈W} count(w^{\prime})}$

So, given some training data, we can take this training data and estimate these thetas, the parameters of the multinomial, to find a multinomial which best fits this data.

Note that this has examined the case of a single document, but in the case of multiple documents, since the words of one are independent of another, we would still apply the same process to the words of each document, and then concatenate to collate the documents.
