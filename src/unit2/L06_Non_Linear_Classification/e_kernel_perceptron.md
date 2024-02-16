# Kernel Perceptron Algorithm

Recall that with perceptron (for one cycle):

```python
θ = 0
for i in range(n):
    if y[i] * θ * φ(x[i]) <= 0:
        θ = θ + y[i] * φ(x[i])
```

After these updates, we can summarise what $θ$ is as a result.

Every time we make a mistake, we add the label multiplied by the feature vector:

$θ = \sum_{j=1}^{n}{α_j y^{(i)} \phi(x^{(i)})}$

We can summarise by taking a sum over the training examples, of how many times we performed an update on the $i$-th training example.

$α_j$ = number of mistakes

Every time we make a mistake, we add the corresponding label times the feature vector, to the parameter vector $θ$.

We no longer look at the algorithm in terms of coordinates of $θ$, but in terms of the importance of training examples to the final predictor.

$θ • \phi(x^{(i)}) = \sum_{j=1}^{n}{α_j y^{(j)} \phi(x^{(j)}) • \phi(x^{(i)})}$

Predictions can thereby be expressed simply in terms of the kernel produced by the $j$-th training example and the $i$-th training example.

$K(x^{(j)}, x^{(i)}) = \phi(x^{(j)}) • \phi(x^{(i)})$

If we evaluate the inner product, we can run the algorithm only in terms of the kernel functions, without the need to explicitly construct feature vectors.

```python
θ = 0
for i in range(n):
    if y[i] * θ * φ(x[i]) <= 0:
        θ = θ + y[i] * φ(x[i])
```

$θ • \phi(x^{(i)}) = \sum_{j=1}^{n}{α_j y^{(j)} K(x^{(j)}, x^{(i)})}$

Just as $θ$ would be initialised to $0$, so all $α$ - one per training example - are set to $0$.

We then ask whether the $i$-th label $y^{(i)}$, multiplied by the sum over the training examples of how many mistakes we have made on the $j$-th example, its label times the kernel evaluated between the $j$-th and $i$-th example.

$y^{(i)} \sum_{j=1}^{n}{α_j y^{(j)} K(x^{(j)}, x^{(i)})} <= 0$

If this expression is less than or equal to $0$, $<= 0$, then a mistake was made and an update will be performed.

$0 ← θ + y^{(i)} \phi(x^{(i)})$

The update is simple, because the α count how many times we've made this particular update.

$α_i ← α_i + 1$

We simply increment $α$ by $1$.

Combining this factors, the kernel perceptron algorithm enables us to implicitly run higher-dimensional feature representations, while running the algorithm only in terms of the scalar-valued kernel evaluations between two examples.

$K(x^{(j)}, x^{(i)})$ can be seen as a similarity measure, how similar the $j$-th example is to the $i$-th example.

So, our predicted value is now, how important the $j$-th example is, multiplied by how similar the example we wish to make a prediction about (the $i$-th example) is to the $j$-th example.
