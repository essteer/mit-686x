# -*- coding: utf-8 -*-
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=1000, centers=2, random_state=0)
# X[:5], y[:5]
# (array([[0.4666179 , 3.86571303],
#     [2.84382807, 3.32650945],
#     [0.61121486, 2.51245978],
#     [3.81653365, 1.65175932],
#     [1.28097244, 0.62827388]]), array([0, 0, 0, 1, 1]))

fig, ax = plt.subplots()
for label in [0, 1]:
    # Give mask boolean value based on whether y == label
    mask = (y == label)
    # Plot points based on True / False mask value
    ax.scatter(X[mask, 0], X[mask, 1])
