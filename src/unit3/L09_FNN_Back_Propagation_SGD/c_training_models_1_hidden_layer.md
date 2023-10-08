# Training Models with 1 Hidden Layer

With 10 hidden units in the layer instead of 2, we get 10-dimensions, and many decision boundary classifiers.

Several of those DB classifiers are doing something useful, but many are not in themselves able to solve the task - this is known as over-capacity.

Over-capacity is useful, because for complex problems, we do not need any individual units to be able to solve the task, just for them to be able to solve it collectively.

**Initialisation**

Initialisation is important, because for example, always initialising at the origin can lead to implicit bias in the model, with phantom results even if the examples are correctly classified.

We can randomise initialisation to mitigate this.

**Summary**

- NNs can be learned with SGD similarlry to linear classifiers.
- The derivatives necessary for SGD can be evaluated effectively via back-propagation.
- Multi-layer NN models are complicated... we are no longer guaranteed to reach global (only local) optimum with SGD.
- Larger models tend to be easier to learn... units only need to be adjusted so that they are collectively sufficient to solve the task.
