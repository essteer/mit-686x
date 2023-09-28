# -*- coding: utf-8 -*-
import numpy as np


# ==============================================================

def compute_hinge_loss(x_vals, y_vals, theta):
    """
    Uses hinge loss to compute the empirical risk of a set of n data points.
    Has no offset (offset = 0).
    Has no regularisation term.

    Definitions used:
    Empirical risk Rn: Rn(θ) = 1/n Σn i=1 Loss(y(i) - θ•x(i))
    Hinge loss Lh: Lh(z) = {0 if z >= 1, 1 - z otherwise}

    Args:
        x_vals - array of coordinates of training examples, e.g. [1, 2]
        y_vals - array of labels (-1 or 1) corresponding to training examples

    Returns:
        hinge loss of the data points
    """
    n = len(x_vals)
    # =====================================
    # NumPy version:
    dot_product = np.dot(x_vals, theta)  # note reordering of x_vals and theta
    z_np = y_vals - dot_product
    losses_np = np.maximum(0, 1 - z_np)
    hinge_loss_np = np.mean(losses_np)

    # =====================================
    # for loop version:
    losses = []
    # For each example in the training set (x_vals)
    for i in range(n):
        # Calculate the dot product of theta and the current training example
        dot_product = np.dot(theta, x_vals[i])
        # Calculate the difference between the dot product and the predicted value
        z = y_vals[i] - dot_product
        if z >= 1:
            losses.append(0)
        else:
            # Calculate the hinge loss of the current theta and training example
            losses.append(1 - z)

    hinge_loss = sum(losses) / n

    print(f"numpy hinge loss = {hinge_loss_np}")
    print(f"for loop hinge loss = {hinge_loss}")

    return hinge_loss


# ==============================================================

def compute_squared_error_loss(x_vals, y_vals, theta):
    """
    Uses squared error loss to compute the empirical risk of a set of n data points.
    Has no offset (offset = 0).
    Has no regularisation term.

    Definitions used:
    Empirical risk Rn: Rn(θ) = 1/n Σn i=1 Loss(y(i) - θ•x(i))
    Squared error loss L: L(z) = z^2 / 2

    Args:
        x_vals - array of coordinates of training examples, e.g. [1, 2]
        y_vals - array of labels (-1 or 1) corresponding to training examples

    Returns:
        squared error loss of the data points
    """
    n = len(x_vals)
    # =====================================
    # NumPy version:
    dot_product = np.dot(x_vals, theta)  # note reordering of x_vals and theta
    z_np = y_vals - dot_product
    squared_errors_np = z_np**2/2
    sq_error_loss_np = np.mean(squared_errors_np)

    # =====================================
    # for loop version:
    losses = []
    # For each example in the training set (x_vals)
    for i in range(n):
        # Calculate the dot product of theta and the current training example
        dot_product = np.dot(theta, x_vals[i])
        # Calculate the difference between the dot product and the predicted value
        z = y_vals[i] - dot_product
        squared_error = z**2/2
        losses.append(squared_error)

    squared_error_loss = sum(losses) / n

    print(f"numpy squared error loss = {sq_error_loss_np}")
    print(f"for loop squared error loss = {squared_error_loss}")

    return squared_error_loss


# ==============================================================

x1 = [1, 0, 1]
x2 = [1, 1, 1]
x3 = [1, 1, -1]
x4 = [-1, 1, 1]
x_vals = np.asarray([x1, x2, x3, x4])

y1, y2, y3, y4 = 2, 2.7, -0.7, 2
y_vals = np.asarray([y1, y2, y3, y4])

theta = np.asarray([0, 1, 2])

# 1) Compute hinge loss
print(f"Hinge loss = {compute_hinge_loss(x_vals, y_vals, theta)}")

# 2) Compute squared error Loss
print(
    f"Squared error loss = {compute_squared_error_loss(x_vals, y_vals, theta)}")
