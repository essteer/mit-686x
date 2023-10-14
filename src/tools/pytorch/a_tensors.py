# -*- coding: utf-8 -*-
import torch

# Tensors are PyTorch's equivalent of NumPy ndarrays.

# Construct a bunch of ones
some_ones = torch.ones(2, 2)
print(some_ones)

# Construct a bunch of zeros
some_zeros = torch.zeros(2, 2)
print(some_zeros)

# Construct some normally distributed values
some_normals = torch.randn(2, 2)
print(some_normals)

# PyTorch tensors and NumPy ndarrays even share the same memory handles,
# so you can switch between the two types essentially for free:
torch_tensor = torch.randn(5, 5)
numpy_ndarray = torch_tensor.numpy()
back_to_torch = torch.from_numpy(numpy_ndarray)
