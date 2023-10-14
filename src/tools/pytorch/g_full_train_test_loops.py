# -*- coding: utf-8 -*-
from torchvision import datasets, transforms
import torch
import torch.nn.functional as F
import torch.optim as optim
import tqdm


############################################################
# Layers
############################################################

# Before we manually defined our linear layers.
# PyTorch has them for you as sub-classes of nn.Module.

import torch.nn as nn

# Linear layer: in_features, out_features
linear = nn.Linear(10, 10)
print(linear)

# Convolution layer: in_channels, out_channels, kernel_size, stride
conv = nn.Conv2d(1, 20, 5, 1)
print(conv)

# RNN: num_inputs, num_hidden, num_layers
rnn = nn.RNN(10, 10, 1)
print(rnn)

print(linear.weight)
print([k for k, v in conv.named_parameters()])

# Make our own model!


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 1 input channel to 20 feature maps of 5x5 kernel. Stride 1.
        self.conv1 = nn.Conv2d(1, 20, 5, 1)

        # 20 input channels to 50 feature maps of 5x5 kernel. Stride 1.
        self.conv2 = nn.Conv2d(20, 50, 5, 1)

        # Full connected of final 4x4 image to 500 features
        self.fc1 = nn.Linear(4*4*50, 500)

        # From 500 to 10 classes
        self.fc2 = nn.Linear(500, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 4*4*50)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


# Initialize it
model = Net()

# A note on convolution sizes:

# Running a kernel over the image reduces the image height/length by kernel_size - 1.

# Running a max pooling over the image reduces the image height/length by a factor of the kernel size.

# So starting from a 28 x 28 image:

# Run 5x5 conv --> 24 x 24
# Apply 2x2 max pool --> 12 x 12
# Run 5x5 conv --> 8 x 8
# Apply 2x2 max pool --> 4 x 4

############################################################
# Optimizers
############################################################

# PyTorch handles all the optimizing too.
# There are several algorithms you can learn about later.
#
# Here's SGD:

# Initialize with model parameters
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Updating is now as easy as:
# loss = loss_fn()
# optimizer.zero_grad()
# loss.backward()
# optimizer.step()

############################################################
# Training loop
############################################################


def train(model, train_loader, optimizer, epoch):
    # For things like dropout
    model.train()

    # Avg loss
    total_loss = 0

    # Iterate through dataset
    for data, target in tqdm.tqdm(train_loader):
        # Zero grad
        optimizer.zero_grad()

        # Forward pass
        output = model(data)

        # Negative log likelihood loss function
        loss = F.nll_loss(output, target)

        # Backward pass
        loss.backward()
        total_loss += loss.item()

        # Update
        optimizer.step()

    # Print average loss
    print("Train Epoch: {}\t Loss: {:.6f}".format(
        epoch, total_loss / len(train_loader)))


############################################################
# Testing loops are similar.
############################################################

def test(model, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            # sum up batch loss
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            # get the index of the max log-probability
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


############################################################
# MNIST
############################################################

# See the torch DataLoader for more details.
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    batch_size=32, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=False,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    batch_size=32, shuffle=True)


for epoch in range(1, 10 + 1):
    train(model, train_loader, optimizer, epoch)
    test(model, test_loader)
