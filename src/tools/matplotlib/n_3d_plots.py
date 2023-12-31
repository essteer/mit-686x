# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
xx = np.linspace(-0.75, 1., 100)
alpha = 0.7
phi_ext = 2 * np.pi * 0.5


def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)


phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T
# -------------------------------------------------------------------------

# To use 3D graphics in matplotlib, we first need to create an instance of the Axes3D class.
# 3D axes can be added to a matplotlib figure canvas in exactly the same way as 2D axes;
# or, more conveniently, by passing a projection='3d' keyword argument to the add_axes or add_subplot methods.

# -------------------------------------------------------------------------

# Surface plots
fig = plt.figure(figsize=(14, 6))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)

# -------------------------------------------------------------------------

# Wire-frame plot
fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(1, 1, 1, projection='3d')

p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

# -------------------------------------------------------------------------

# Contour plots with projections
fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-np.pi,
                  cmap=plt.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-np.pi,
                  cmap=plt.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3 *
                  np.pi, cmap=plt.cm.coolwarm)

ax.set_xlim3d(-np.pi, 2*np.pi)
ax.set_ylim3d(0, 3*np.pi)
ax.set_zlim3d(-np.pi, 2*np.pi)

# -------------------------------------------------------------------------

# Change the view angle
# We can change the perspective of a 3D plot using the view_init method,
# which takes two arguments: elevation and azimuth angle (in degrees):

fig = plt.figure(figsize=(12, 6))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.view_init(30, 45)

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.view_init(70, 30)

fig.tight_layout()
