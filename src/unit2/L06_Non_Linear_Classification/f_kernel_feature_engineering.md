# Feature Engineering, Kernels

We can construct kernels from simpler kernels.

**Composition rules**

1. K(x, x') = 1 is a kernel function.

   - If φ(x) = 1, the inner product will be 1 for every evaluation.

2. Let f: ℝ<sup>d</sup> ℝ (f is a scalar function) and K(x, x') is a kernel,

   - then K̃(x, x') = f(x)K(x, x')f(x') is also a kernel.
   - If you pre- and post- multiply a kernel by any scalar function f(x), so the kernel is evaluated between two examples f(x) and f(x'), the result is also a kernel.
   - φ̃ (x) = f(x)φ(x)

3. If K<sub>1</sub>(x, x') and K<sub>2</sub>(x, x') are kernels,

   - then their sum K<sub>1</sub>(x, x') + K<sub>2</sub>(x, x') is also a kernel.
   - φ(x) = [φ<sup>(1)</sup>(x), φ<sup>(2)</sup>(x)]<sup>T</sup>

4. If K<sub>1</sub>(x, x') and K<sub>2</sub>(x, x') are kernels,

   - then their product K<sub>1</sub>(x, x')K<sub>2</sub>(x, x') is also a kernel.

Linear kernel: (x, x'), where φ(x) = x (phi of x equals identity)

We can add to (x, x') a squared term (x, x')<sup>2</sup>, which we can verify has a product representation since it is the product of two kernels (multiplying two identical kernels results in that kernel squared).

(x, x') + (x, x')<sup>2</sup> works because as we see from the third rule above, adding two kernels results in a valid kernel.
