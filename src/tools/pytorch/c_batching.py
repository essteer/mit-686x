# -*- coding: utf-8 -*-
import torch

# In most ML applications we do mini-batch stochastic gradient descent
# instead of pure stochastic gradient descent.

# Mini-batch SGD is a step between full gradient descent and
# stochastic gradient descent by computing the average gradient
# over a small number of examples.

# In a nutshell, given n examples:

# Full GD: dL/dw = average over all n examples. One step per n examples.
# SGD: dL/dw = point estimate over a single example. n steps per n examples.
# Mini-batch SGD: dL/dw = average over m << n examples. n / m steps per n examples.
# Advantages of mini-batch SGD include a more stable gradient estimate
# and computational efficiency on modern hardware
# (exploiting parallelism gives sub-linear to constant time complexity, especially on GPU).

# In PyTorch, batched tensors are represented as just another dimension.
# Most of the deep learning modules assume batched tensors as input (even if the batch size is just 1).

# Batched matrix multiply
a = torch.randn(10, 5, 5)
b = torch.randn(10, 5, 5)

# The same as for i in 1 ... 10, c_i = a[i].mm(b[i])
c = a.bmm(b)

print(c.size())
