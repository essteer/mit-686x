# Linear Separation

Take a training set and ask whether there is a linear classifier that can successfully divide the positive and negative labels.

Perhaps this can be done via a linear classifier through the origin, but if not, it may still be possible to correctly separate the labels via a linear classifier with an offset.

But, there do exist datasets for which there is no linear classifier that can correctly label the points contained.

**Definition**

Training examples $S_n = \lbrace (x^{(i)}, y^{(i)}), i=1,⋯,n \rbrace$ are linearly separable if there exists a parameter vector $θ$ and offset parameter $θ_0$ such that:

- $y^{(i)}(θ • x^{(i)} + θ_0) > 0$ for all $i=1,⋯,n$.

Given $θ$ and $θ_0$, a linear classifier $h: X ⟶ \lbrace -1, 0, +1\rbrace$ is a function that outputs $+1$ if $θ•x+θ_0$ is positive, $0$ if it is zero, and $-1$ if it is negative. In other words, $h(x) = sign(θ•x+θ_0)$.
