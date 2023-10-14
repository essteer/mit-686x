# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.datasets import make_classification
import torch

# Before we move on to the full PyTorch wrapper library,
# let's do a simple NN SGD example by hand.
# We'll train a one hidden layer feed forward NN on a toy dataset.

# Set our random seeds


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)


# Get ourselves a simple dataset
set_seed(7)
X, Y = make_classification(n_features=2, n_redundant=0,
                           n_informative=1, n_clusters_per_class=1)
print('Number of examples: %d' % X.shape[0])
print('Number of features: %d' % X.shape[1])

# Take a peak
plt.scatter(X[:, 0], X[:, 1], marker='o', c=Y, s=25, edgecolor='k')
plt.show()

# Convert data to PyTorch
X, Y = torch.from_numpy(X), torch.from_numpy(Y)

# Gotcha: "Expected object of scalar type Float but got scalar type Double"
# If you see this it's because numpy defaults to Doubles whereas pytorch has floats.
X, Y = X.float(), Y.float()

# We'll train a one layer neural net to classify this dataset.
# Let's define the parameter sizes:

# Define dimensions
num_feats = 2
hidden_size = 100
num_outputs = 1

# Learning rate
eta = 0.1
num_steps = 1000

# And now run a few steps of SGD!

# Input to hidden weights
W1 = torch.randn(hidden_size, num_feats, requires_grad=True)
b1 = torch.zeros(hidden_size, requires_grad=True)

# Hidden to output
W2 = torch.randn(num_outputs, hidden_size, requires_grad=True)
b2 = torch.zeros(num_outputs, requires_grad=True)

# Group parameters
parameters = [W1, b1, W2, b2]

# Get random order
indices = torch.randperm(X.size(0))

# Keep running average losses for a learning curve?
avg_loss = []

# Run!
for step in range(num_steps):
    # Get example
    i = indices[step % indices.size(0)]
    x_i, y_i = X[i], Y[i]

    # Run example
    hidden = torch.relu(W1.matmul(x_i) + b1)
    y_hat = torch.sigmoid(W2.matmul(hidden) + b2)

    # Compute loss binary cross entropy: -(y_i * log(y_hat) + (1 - y_i) * log(1 - y_hat))
    # Epsilon for numerical stability
    eps = 1e-6
    loss = -(y_i * (y_hat + eps).log() + (1 - y_i) * (1 - y_hat + eps).log())

    # Add to our running average learning curve. Don't forget .item()!
    if step == 0:
        avg_loss.append(loss.item())
    else:
        old_avg = avg_loss[-1]
        new_avg = (loss.item() + old_avg * len(avg_loss)) / (len(avg_loss) + 1)
        avg_loss.append(new_avg)

    # Zero out all previous gradients
    for param in parameters:
        # It might start out as None
        if param.grad is not None:
            # In place
            param.grad.zero_()

    # Backward pass
    loss.backward()

    # Update parameters
    for param in parameters:
        # In place!
        param.data = param.data - eta * param.grad


plt.plot(range(num_steps), avg_loss)
plt.ylabel('Loss')
plt.xlabel('Step')
plt.show()
