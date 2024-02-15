# Feature Engineering, Kernels

We can construct kernels from simpler kernels.

**Composition rules**

1. $K(x, x^{\prime}) = 1$ is a kernel function.

   - If $\phi(x) = 1$, the inner product will be $1$ for every evaluation.

2. Let $f: ℝ^d ℝ$ ($f$ is a scalar function) and $K(x, x^{\prime})$ is a kernel,

   - then $K̃(x, x^{\prime}) = f(x)K(x, x^{\prime})f(x^{\prime})$ is also a kernel.
   - If you pre- and post- multiply a kernel by any scalar function $f(x)$, so the kernel is evaluated between two examples $f(x)$ and $f(x^{\prime})$, the result is also a kernel.
   - $\tilde{\phi}(x) = f(x)\phi(x)$

3. If $K_1(x, x^{\prime})$ and $K_2(x, x^{\prime})$ are kernels,

   - then their sum $K_1(x, x^{\prime}) + K_2(x, x^{\prime})$ is also a kernel.
   - $\phi(x) = [\phi^(1)(x), \phi^(2)(x)]^T$

4. If $K_1(x, x^{\prime})$ and $K_2(x, x^{\prime})$ are kernels,

   - then their product $K_1(x, x^{\prime})K_2(x, x^{\prime})$ is also a kernel.

Linear kernel: $(x, x^{\prime})$, where $\phi(x) = x$ ($\phi$ of $x$ equals identity)

We can add to $(x, x^{\prime})$ a squared term $(x, x^{\prime})^2$, which we can verify has a product representation since it is the product of two kernels (multiplying two identical kernels results in that kernel squared).

$(x, x^{\prime}) + (x, x^{\prime})^2$ works because as we see from the third rule above, adding two kernels results in a valid kernel.
