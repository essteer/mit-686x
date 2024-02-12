# Review and the Lambda Parameter

**Recall**

Machine learning problems are often cast as optimisation problems:

- objective function = average loss + regularisation

$J(θ, θ_0) = \frac{1}{n} Σ_{i=1}^n Loss_h(y^{(i)}(θ•x^{(i)} + θ_0)) + \frac{λ}{2}∥θ∥^2$

In the case of large margin linear classification (Support Vector Machine), our average loss is an average hinge loss of the linear predictor on those training examples:

- $(y^{(i)}(θ•x^{(i)} + θ_0))$ = agreement

When agreement between our function and the provided label $< 1$, we begin to incur loss. We seek to minimise the average of those losses.

On the other side of the equation, we seek to minimise the regularisation term $\frac{λ}{2}∥θ∥^2$, which will push margin boundaries (MBs) further apart.

As we do so, the MBs may begin to hit training examples, and so we incur loss through the agreement term.

**$λ$**

The balance between the agreement and regularisation term is influenced by the variable $λ$.

As we change the value of $λ$, we change the balance between agreement and regularisation:

- the larger the $λ$, the more we try to push the MBs apart
- the smaller the $λ$, the more emphasis we place on minimising loss on the training examples, with the result that the MBs draw closer together.

**Note**: At a higher $λ$, the DB will also be guided more by the majority of the examples, rather than just those closest to the DB.
