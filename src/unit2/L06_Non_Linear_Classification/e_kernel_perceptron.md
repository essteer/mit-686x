# Kernel Perceptron Algorithm

Recall that with perceptron (for one cycle):

`θ = 0`
`run through i = 1, ⋯, n`
`   if y^(i) θ • φ(x^(i)) <= 0`
`       θ ← θ + y^(i)φ(x^(i))`

After these updates, we can summarise what θ is as a result.

Every time we make a mistake, we add the label multiplied by the feature vector:

θ = Σ<sup>n</sup><sub>j=1</sub> α<sub>j</sub> y<sup>(i)</sup> φ(x<sup>(i)</sup>)

We can summarise by taking a sum over the training examples, of how many times we performed an update on the i-th training example.

α<sub>j</sub> = number of mistakes

Every time we make a mistake, we add the corresponding label times the feature vector, to the parameter vector θ.

We no longer look at the algorithm in terms of coordinates of θ, but in terms of the importance of training examples to the final predictor.

θ • φ(x<sup>(i)</sup>) = Σ<sup>n</sup><sub>j=1</sub> α<sub>j</sub> y<sup>(j)</sup> φ(x<sup>(j)</sup>) • φ(x<sup>(i)</sup>)

Predictions can thereby be expressed simply in terms of the kernel produced by the j-th training example and the i-th training example.

K(x<sup>(j)</sup>, x<sup>(i)</sup>) = φ(x<sup>(j)</sup>) • φ(x<sup>(i)</sup>)

If we evaluate the inner product, we can run the algorithm only in terms of the kernel functions, without the need to explicitly construct feature vectors.

`θ = 0`
`run through i = 1, ⋯, n`
`   if y^(i) θ • φ(x^(i)) <= 0`
`       θ ← θ + y^(i)φ(x^(i))`

θ • φ(x<sup>(i)</sup>) = Σ<sup>n</sup><sub>j=1</sub> α<sub>j</sub> y<sup>(j)</sup> K(x<sup>(j)</sup>, x<sup>(i)</sup>)

Just as θ would be initialised to 0, so all α - one per training example - are set to 0.

We then ask whether the i-th label y<sup>(i)</sup>, multiplied by the sum over the training examples of how many mistakes we have made on the j-th example, its label times the kernel evaluated between the j-th and i-th example.

y<sup>(i)</sup> Σ<sup>n</sup><sub>j=1</sub> α<sub>j</sub> y<sup>(j)</sup> K(x<sup>(j)</sup>, x<sup>(i)</sup>) <= 0

If this expression is less than or equal to 0, <= 0, then a mistake was made and an update will be performed.

0 ← θ + y<sup>(i)</sup> φ(x<sup>(i)</sup>)

The update is simple, because the α count how many times we've made this particular update.

α<sub>i</sub> ← α<sub>i</sub> + 1

We simply increment α by 1.

Combining this factors, the kernel perceptron algorithm enables us to implicitly run higher-dimensional feature representations, while running the algorithm only in terms of the scalar-valued kernel evaluations between two examples.

K(x<sup>(j)</sup>, x<sup>(i)</sup>) can be seen as a similarity measure, how similar the j-th example is to the i-th example.

So, our predicted value is now, how important the j-th example is, multiplied by how similar the example we wish to make a prediction about (the i-th example) is to the j-th example.
