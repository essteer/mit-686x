# -*- coding: utf-8 -*-
from matplotlib import ticker
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
# -------------------------------------------------------------------------

# We can explicitly determine where we want the axis ticks with set_xticks and set_yticks,
# which both take a list of values for where on the axis the ticks are to be placed.
# We can also use the set_xticklabels and set_yticklabels methods
# to provide a list of custom text labels for each tick location:

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(x, x**2, x, x**3, lw=2)

ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$',
                   r'$\delta$', r'$\epsilon$'], fontsize=18)

yticks = [0, 50, 100, 150]
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks],
                   fontsize=18)  # use LaTeX formatted labels


# There are a number of more advanced methods for controlling
# major and minor tick placement in matplotlib figures,
# such as automatic placement according to different policies.
# https://matplotlib.org/stable/api/ticker_api.html

# -------------------------------------------------------------------------

# Scientific notation
# With large numbers on axes, it is often better use scientific notation:

fig, ax = plt.subplots(1, 1)

ax.plot(x, x**2, x, np.exp(x))
ax.set_title("scientific notation")

ax.set_yticks([0, 50, 100, 150])

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1, 1))
ax.yaxis.set_major_formatter(formatter)
