# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
# -------------------------------------------------------------------------

# Matplotlib allows the aspect ratio, DPI and figure size to be specified when the Figure object is created,
# using the figsize and dpi keyword arguments.
# figsize is a tuple of the width and height of the figure in inches,
# and dpi is the dots-per-inch (pixel per inch).
# To create an 800x400 pixel, 100 dots-per-inch figure, we can do:

fig = plt.figure(figsize=(8, 4), dpi=100)

# The same arguments can also be passed to layout managers, such as the subplots function:
fig, axes = plt.subplots(figsize=(12, 3))

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
