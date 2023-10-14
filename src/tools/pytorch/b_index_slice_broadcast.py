# -*- coding: utf-8 -*-
import torch

# Create two tensors
a = torch.randn(5, 5)
b = torch.randn(5, 5)
print(a)
print(b)

# Indexing by i,j
another_tensor = a[2, 2]
print(another_tensor)

# The above returns a tensor type! To get the python value:
python_value = a[2, 2].item()
print(python_value)

# Getting a whole row or column or range
first_row = a[0, :]
first_column = a[:, 0]
combo = a[2:4, 2:4]
print(combo)

# Addition
c = a + b

# Elementwise multiplication: c_ij = a_ij * b_ij
c = a * b

# Matrix multiplication: c_ik = a_ij * b_jk
c = a.mm(b)

# Matrix vector multiplication
c = a.matmul(b[:, 0])

a = torch.randn(5, 5)
print(a.size())

vec = a[:, 0]
print(vec.size())

# Matrix multiple 5x5 * 5x5 --> 5x5
aa = a.mm(a)

# matrix vector 5x5 * 5 --> 5
v1 = a.matmul(vec)
print(v1)


vec_as_matrix = vec.view(5, 1)
v2 = a.mm(vec_as_matrix)
print(v2)

# torch.Size([5, 5])
# torch.Size([5])
# tensor([3.8873,  2.8224,  0.5655, -1.8550,  3.2441])
# tensor([[3.8873],
#         [2.8224],
#         [0.5655],
#         [-1.8550],
#         [3.2441]])

# In-place operations exist too,
# generally denoted by a trailing '_' (e.g. my_tensor.my_inplace_function).

# Add one to all elements
a.add_(1)

# Divide all elements by 2
a.div_(2)

# Set all elements to 0
a.zero_()

# Manipulate dimensions...

# Add a dummy dimension, e.g. (n, m) --> (n, m, 1)
a = torch.randn(10, 10)

# At the end
print(a.unsqueeze(-1).size())

# At the beginning
print(a.unsqueeze(0).size())

# In the middle
print(a.unsqueeze(1).size())

# What you give you can take away
print(a.unsqueeze(0).squeeze(0).size())

# View things differently, i.e. flat
print(a.view(100, 1).size())

# Or not flat
print(a.view(50, 2).size())

# Copy data across a new dummy dimension!
a = torch.randn(2)
a = a.unsqueeze(-1)
print(a)
print(a.expand(2, 3))

# If you have a GPU...

# Check if you have it
do_i_have_cuda = torch.cuda.is_available()

if do_i_have_cuda:
    print('Using fancy GPUs')
    # One way
    a = a.cuda()
    a = a.cpu()

    # Another way
    device = torch.device('cuda')
    a = a.to(device)

    device = torch.device('cpu')
    a = a.to(device)
else:
    print('CPU it is!')
