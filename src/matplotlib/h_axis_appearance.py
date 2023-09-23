# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
# -------------------------------------------------------------------------

# Plot range
# The first thing we might want to configure is the ranges of the axes.
# We can do this using the set_ylim and set_xlim methods in the axis object,
# or axis('tight') for automatrically getting "tightly fitted" axes ranges:

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range")

# -------------------------------------------------------------------------

# Logarithmic scale
# It is also possible to set a logarithmic scale for one or both axes.
# This functionality is in fact only one application of a more general
# transformation system in Matplotlib.
# Each of the axes' scales are set seperately using set_xscale
# and set_yscale methods which accept one parameter (with the value "log" in this case):

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, x**2, x, np.exp(x))
axes[0].set_title("Normal scale")

axes[1].plot(x, x**2, x, np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")
