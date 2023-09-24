# -*- coding: utf-8 -*-
from pylab import *  # using the matlab api, not recommended
import numpy as np

# Notes from Johansson tutorial on matplotlib
# https://nbviewer.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb

# Simple figure with Matlab-like plotting
x = np.linspace(0, 5, 10)
y = x ** 2
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()

# Subplot and colour/symbol selection
subplot(1, 2, 1)
plot(x, y, 'r--')
subplot(1, 2, 2)
plot(y, x, 'g*-')
