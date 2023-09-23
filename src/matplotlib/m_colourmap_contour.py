# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
xx = np.linspace(-0.75, 1., 100)
# -------------------------------------------------------------------------

# Colormap and contour figures
# Colormaps and contour figures are useful for plotting functions of two variables.
# In most of these functions we will use a colormap to encode one dimension of the data.
# There are a number of predefined colormaps.
# It is relatively straightforward to define custom colormaps.
# For a list of pre-defined colormaps, see:
# http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps

alpha = 0.7
phi_ext = 2 * np.pi * 0.5


def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)


phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

# -------------------------------------------------------------------------

# pcolor
fig, ax = plt.subplots()

p = ax.pcolor(X/(2*np.pi), Y/(2*np.pi), Z, cmap=plt.cm.RdBu,
              vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)

# -------------------------------------------------------------------------

# imshow
fig, ax = plt.subplots()

im = ax.imshow(Z, cmap=plt.cm.RdBu, vmin=abs(Z).min(),
               vmax=abs(Z).max(), extent=[0, 1, 0, 1])
im.set_interpolation('bilinear')

cb = fig.colorbar(im, ax=ax)

# -------------------------------------------------------------------------

# contour
fig, ax = plt.subplots()

cnt = ax.contour(Z, cmap=plt.cm.RdBu, vmin=abs(
    Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
