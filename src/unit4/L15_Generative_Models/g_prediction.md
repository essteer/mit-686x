# Prediction

Take a classification problem for linearly separable +ve and -ve points.

If we receive a new document, how do we know to which class it belongs?

We can look at the likelihood that the document was generated by the +ve class and the -ve class, and take the log of this:

log P(D|θ<sup>+</sup>) / P(D|θ<sup>-</sup>)

We want to assign the document to the class that gives it the highest likelihood.

For now, we make the simplifying assumption that the likelihood of being in either the +ve class or the -ve class is the same.

log P(D|θ<sup>+</sup>) / P(D|θ<sup>-</sup>) = { >= 0, +ve; < 0, -ve }

These are known as class-conditional distributions.

Our expression can be rewritten as:

log P(D|θ<sup>+</sup>) - log P(D|θ<sup>-</sup>)

and then as:

log Π<sub>w∈W</sub> θ<sub>w</sub><sup>+ count(w)</sup> - log Π<sub>w∈W</sub> θ<sub>w</sub><sup>- count(w)</sup>

Recall that log of the product is the sum of logs.

Σ<sub>w∈W</sub> count(w) • logθ<sub>w</sub><sup>+</sup> - Σ<sub>w∈W</sub> count(w) • logθ<sub>w</sub><sup>-</sup>

= Σ<sub>w∈W</sub> count(w) • log(θ<sub>w</sub><sup>+</sup>/θ<sub>w</sub><sup>-</sup>)

Here we introduce new notation as a stand-in for log (θ<sub>w</sub><sup>+</sup>/θ<sub>w</sub><sup>-</sup>), as follows:

θ^<sub>w</sub><sup> = log(θ<sub>w</sub><sup>+</sup>/θ<sub>w</sub><sup>-</sup>)

Our expression then becomes:

Σ<sub>w∈W</sub> count(w) • θ'<sub>w</sub><sup>

This final form resembles the linear classifier, but is applicable to our generative model.
