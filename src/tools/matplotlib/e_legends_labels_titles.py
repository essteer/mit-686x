# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
# -------------------------------------------------------------------------

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

fig.tight_layout()

ax.set_title("title")
ax.set_xlabel("x")
ax.set_ylabel("y")

# -------------------------------------------------------------------------

# This method is error-prone, if individual curves are added or removed
# it will disrupt the ordering
# ax.legend(["curve1", "curve2", "curve3"])

# This method applies labels at the time of creation
# so the legend is updated automatically if curves are added or removed
ax.plot(x, x**2, label="curve1")
ax.plot(x, x**3, label="curve2")
ax.legend()

# -------------------------------------------------------------------------

ax.legend(loc=0)  # let matplotlib decide the optimal location
ax.legend(loc=1)  # upper right corner
ax.legend(loc=2)  # upper left corner
ax.legend(loc=3)  # lower left corner
ax.legend(loc=4)  # lower right corner
# .. many more options are available
# http://matplotlib.org/users/legend_guide.html#legend-location

# -------------------------------------------------------------------------

# Example plot
fig, ax = plt.subplots()

ax.plot(x, x**2, label="y = x**2")
ax.plot(x, x**3, label="y = x**3")
ax.legend(loc=2)  # upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
