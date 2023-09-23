# -*- coding: utf-8 -*-
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
xx = np.linspace(-0.75, 1., 100)
# -------------------------------------------------------------------------

# Figures with multiple subplots and insets
# Axes can be added to a matplotlib Figure canvas manually
# using fig.add_axes or using a sub-figure layout manager
# such as subplots, subplot2grid, or gridspec:

# subplots
fig, ax = plt.subplots(2, 3)
fig.tight_layout()

# -------------------------------------------------------------------------

# subplot2grid
fig = plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
fig.tight_layout()

# -------------------------------------------------------------------------

# gridspec
fig = plt.figure()

gs = gridspec.GridSpec(2, 3, height_ratios=[2, 1], width_ratios=[1, 2, 1])
for g in gs:
    ax = fig.add_subplot(g)

fig.tight_layout()

# -------------------------------------------------------------------------

# add_axes
# Manually adding axes with add_axes is useful for adding insets to figures:

fig, ax = plt.subplots()

ax.plot(xx, xx**2, xx, xx**3)
fig.tight_layout()

# inset
inset_ax = fig.add_axes([0.2, 0.55, 0.35, 0.35])  # X, Y, width, height

inset_ax.plot(xx, xx**2, xx, xx**3)
inset_ax.set_title('zoom near origin')

# set axis range
inset_ax.set_xlim(-.2, .2)
inset_ax.set_ylim(-.005, .01)

# set axis tick locations
inset_ax.set_yticks([0, 0.005, 0.01])
inset_ax.set_xticks([-0.1, 0, .1])
