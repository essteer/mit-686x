# -*- coding: utf-8 -*-
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
# from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

# -------------------------------------------------------------------------
# breast_cancer = load_breast_cancer()
# X, y = breast_cancer.data, breast_cancer.target
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=0)
# -------------------------------------------------------------------------

digits = load_digits()
X, y = digits.data, digits.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)
fig, ax = plt.subplots()
ax.matshow(digits.images[0])

X_train.shape
# (1437, 64)

clf = Perceptron(max_iter=40, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print('Accuracy: %.4f' % accuracy_score(y_test, y_pred))
# Accuracy: 0.9389

clf = LinearSVC(C=1, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print('Accuracy: %.4f' % accuracy_score(y_test, y_pred))
# Accuracy: 0.9361

confusion_matrix(y_test, clf.predict(X_test))
# array([[27,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#        [ 0, 29,  0,  0,  0,  0,  1,  0,  5,  0],
#        [ 0,  1, 33,  2,  0,  0,  0,  0,  0,  0],
#        [ 0,  0,  0, 29,  0,  0,  0,  0,  0,  0],
#        [ 0,  0,  0,  0, 30,  0,  0,  0,  0,  0],
#        [ 0,  1,  0,  0,  0, 38,  1,  0,  0,  0],
#        [ 0,  1,  0,  0,  0,  0, 43,  0,  0,  0],
#        [ 0,  2,  0,  0,  0,  0,  0, 37,  0,  0],
#        [ 0,  2,  1,  0,  0,  0,  0,  0, 35,  1],
#        [ 0,  0,  0,  2,  0,  1,  0,  0,  2, 36]])

# -------------------------------------------------------------------------
# Scikit-learn also includes utilities to quickly compute a cross validation score...
# -------------------------------------------------------------------------

clf = LinearSVC(C=1, random_state=0)
scores = cross_val_score(clf, X_train, y_train, cv=5)
print("Mean: %.4f, Std: %.4f" % (np.mean(scores), np.std(scores)))
# Mean: 0.9443, Std: 0.0127

clf = LinearSVC(C=0.1, random_state=0)
scores = cross_val_score(clf, X_train, y_train, cv=5)
print("Mean: %.4f, Std: %.4f" % (np.mean(scores), np.std(scores)))
# Mean: 0.9555, Std: 0.0101

# -------------------------------------------------------------------------
# ... or to perform a grid search
# -------------------------------------------------------------------------

clf = LinearSVC(random_state=0)
param_grid = {'C': 10. ** np.arange(-6, 4)}
grid_search = GridSearchCV(clf, param_grid=param_grid,
                           cv=5, verbose=3, return_train_score=True)
grid_search.fit(X_train, y_train)

print(grid_search.best_params_)
# {'C': 0.001}
print(grid_search.best_score_)
# 0.9665970772442589
y_pred = grid_search.predict(X_test)
print('Accuracy: %.4f' % accuracy_score(y_test, y_pred))
# Accuracy: 0.9639
