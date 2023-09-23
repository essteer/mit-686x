# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
# -------------------------------------------------------------------------

# distance between x and y axis and the numbers on the axes
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5

fig, ax = plt.subplots(1, 1)

ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0, 50, 100, 150])

ax.set_title("label and axis spacing")

# padding between axis label and axis numbers
ax.xaxis.labelpad = 5
ax.yaxis.labelpad = 5

ax.set_xlabel("x")
ax.set_ylabel("y")

# restore defaults
plt.rcParams['xtick.major.pad'] = 3
plt.rcParams['ytick.major.pad'] = 3

# -------------------------------------------------------------------------

# Axis position adjustments
# Unfortunately, when saving figures the labels are sometimes clipped,
# and it can be necessary to adjust the positions of axes a little bit.
# This can be done using subplots_adjust:

fig, ax = plt.subplots(1, 1)

ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0, 50, 100, 150])

ax.set_title("title")
ax.set_xlabel("x")
ax.set_ylabel("y")

fig.subplots_adjust(left=0.15, right=.9, bottom=0.1, top=0.9)

# -------------------------------------------------------------------------

# Axis grid
# With the grid method in the axis object, we can turn on and off grid lines.
# We can also customize the appearance of the grid lines
# using the same keyword arguments as the plot function:

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

# default grid appearance
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

# custom grid appearance
axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)

# -------------------------------------------------------------------------

# Axis spines
# We can also change the properties of axis spines:

fig, ax = plt.subplots(figsize=(6, 2))

ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('blue')

ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)

# turn off axis spine to the right
ax.spines['right'].set_color("none")
ax.yaxis.tick_left()  # only ticks on the left side

# -------------------------------------------------------------------------

# Twin axes
# Sometimes it is useful to have dual x or y axes in a figure;
# for example, when plotting curves with different units together.
# Matplotlib supports this with the twinx and twiny functions:

fig, ax1 = plt.subplots()

ax1.plot(x, x**2, lw=2, color="blue")
ax1.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")

ax2 = ax1.twinx()
ax2.plot(x, x**3, lw=2, color="red")
ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")

# -------------------------------------------------------------------------

# Axes where x and y is zero
fig, ax = plt.subplots()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))  # set position of x spine to x=0

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))   # set position of y spine to y=0

xx = np.linspace(-0.75, 1., 100)
ax.plot(xx, xx**3)
