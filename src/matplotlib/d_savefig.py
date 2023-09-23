# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb


# -------------------------------------------------------------------------
x = np.linspace(0, 5, 10)
y = x ** 2
# -------------------------------------------------------------------------

plt.fig.savefig("filename.png")

# Here we can also optionally specify the DPI and choose between different output formats:
plt.fig.savefig("filename.png", dpi=200)

# Matplotlib can generate high-quality output in a number formats,
# including PNG, JPG, EPS, SVG, PGF and PDF.
