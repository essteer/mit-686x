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

# Use dollar signs to encapsulate LaTeX in any text
# (legend, title, label, etc.). For example, "$y=x^3$".

# But here we can run into a slightly subtle problem with LaTeX code and Python text strings.
# In LaTeX, we frequently use the backslash in commands, for example \alpha to produce the symbol α.
# But the backslash already has a meaning in Python strings (the escape code character).
# To avoid Python messing up our latex code, we need to use "raw" text strings.
# Raw text strings are prepended with an 'r', like r"\alpha" or r'\alpha' instead of "\alpha" or '\alpha':

fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2)  # upper left corner
ax.set_xlabel(r'$\alpha$', fontsize=18)
ax.set_ylabel(r'$y$', fontsize=18)
ax.set_title('title')

# -------------------------------------------------------------------------

# We can also change the global font size and font family,
# which applies to all text elements in a figure
# (tick labels, axis labels and titles, legends, etc.):

# Update the matplotlib configuration parameters:
plt.rcParams.update({'font.size': 18, 'font.family': 'serif'})
fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2)  # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title')

# -------------------------------------------------------------------------

# A good choice of global fonts are the STIX fonts:

# Update the matplotlib configuration parameters:
plt.rcParams.update(
    {'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2)  # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title')

# -------------------------------------------------------------------------

# Text annotation
# Annotating text in matplotlib figures can be done using the text function.
# It supports LaTeX formatting just like axis label texts and titles:

fig, ax = plt.subplots()

ax.plot(xx, xx**2, xx, xx**3)

ax.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
ax.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green")
