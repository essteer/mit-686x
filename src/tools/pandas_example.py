# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_digits

# -------------------------------------------------------------------------
# Pandas is a library that provides a set of tools for data analysis (Python Data Analysis Library).
# Pandas dataframes can be created by importing a CSV file (or TSV, or JSON, or SQL, etc.)
# df = pd.read_csv("file.csv")
# -------------------------------------------------------------------------

digits = load_digits()
X, y = digits.data, digits.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

clf = LinearSVC(random_state=0)
param_grid = {'C': 10. ** np.arange(-6, 4)}
grid_search = GridSearchCV(clf, param_grid=param_grid,
                           cv=5, verbose=3, return_train_score=True)
grid_search.fit(X_train, y_train)

# -------------------------------------------------------------------------
# Pandas dataframes can also be created directly from a dictionary of arrays.
# -------------------------------------------------------------------------

print(grid_search.cv_results_)
df = pd.DataFrame(grid_search.cv_results_)
df

# -------------------------------------------------------------------------
# Pandas columns are also Numpy arrays, so they obey to the same indexing magic
# -------------------------------------------------------------------------

df[df['param_C'] < 0.01]

# -------------------------------------------------------------------------
# They also provide most functionality you would expect as database user
# (df.sort_values, df.groupby, df.join, df.concat, etc.)
# -------------------------------------------------------------------------

fig, ax = plt.subplots()
ax.plot(df['mean_test_score'], label="validation error")
ax.plot(df['mean_train_score'], label="training error")
ax.set_xticklabels(df['param_C'])
ax.set_xlabel("C")
ax.set_ylabel("Accuracy")
ax.legend(loc='best')
