# -*- coding: utf-8 -*-
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# Sklearn uses a uniform and very consistent API, making it easy to switch algorithms
# For instance, training and predicting with a perceptron.
# -------------------------------------------------------------------------
X, y = make_blobs(n_samples=1000, centers=2, random_state=0)
# Partition 20% of data points into test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# -------------------------------------------------------------------------

clf = Perceptron(max_iter=40, random_state=0)
# clf = LinearSVC(max_iter=40, random_state=0)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print('Test accuracy: %.4f' % accuracy_score(y_test, y_pred))
# Test accuracy: 0.9250

theta = clf.coef_[0]
theta_0 = clf.intercept_

fig, ax = plt.subplots()
for label in [0, 1]:
    mask = (y_train == label)
    ax.scatter(X_train[mask, 0], X_train[mask, 1])
for label in [0, 1]:
    mask = (y_test == label)
    ax.scatter(X_test[mask, 0], X_test[mask, 1])

x_bnd = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1,  400)
y_bnd = - x_bnd * (theta[0] / theta[1]) - (theta_0 / theta[1])
ax.plot(x_bnd, y_bnd)
