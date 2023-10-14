# -*- coding: utf-8 -*-
import torch

# Autograd automatically computes gradients.
# All those complicated functions you might be using for your model
# need gradients for back-propagation.
# Autograd does this auto-magically!

# A tensor that will remember gradients
x = torch.randn(1, requires_grad=True)
print(x)

# At first the 'grad' parameter is None:
print(x.grad)

# Let's do an operation. Take y = e^x.
y = x.exp()

# To run the gradient computing magic, call '.backward()' on a variable.
y.backward()

# For all dependent variables {x_1, ..., x_n} that were used to compute y,
# dy/x_i is computed and stored in the x_i.grad field.
# Here dy/dx = e^x = y. Let's see!
print(x.grad, y)

# Important! Remember to zero gradients before subsequent calls to backwards.

# Compute another thing with x.
z = x * 2
z.backward()

# Should be 2! But it will be 2 + e^x.
print(x.grad)

x_a = torch.randn(1, requires_grad=True)
x_b = torch.randn(1, requires_grad=True)
x = x_a * x_b
x1 = x ** 2
x2 = 1 / x1
x3 = x2.exp()
x4 = 1 + x3
x5 = x4.log()
x6 = x5 ** (1/3)
x6.backward()
print(x_a.grad)
print(x_b.grad)


x = torch.randn(1, requires_grad=True)
y = torch.tanh(x)
y.backward()
print(x.grad)

# Also important! Under the hood PyTorch stores all the stuff required to compute gradients
# (call stack, cached values, etc).
# If you want to save a variable just to keep it around (say for logging or plotting)
# remember to call .item() to get the python value and free the PyTorch machinery memory.

# You can stop auto-grad from running in the background by using the torch.no_grad() context manager.

# with torch.no_grad():
#     do_all_my_things()
