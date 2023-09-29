# -*- coding: utf-8 -*-
import math

# ==============================================================

# Computing dimensions of feature vectors

# The computation per order is given by (k + r - 1, r),
# where k = no. unique elements
# r = no. degrees
# we then perform a factorial calculation per order, e.g., for order 2:
# (k + r - 1)! / r! * (k - r)!

# ==============================================================

# For example, if there are three unique ball colours, and we want
# to know the number of unique combinations of two balls:
# k = 3, r = 2
# this gives us (3 + 2 - 1, 2) = (4, 2). Factorising this, we get:
# 4! / 2! * (4 - 2)! = 4! / 2!*2!
# = 24 / (2 * 2) = 24 / 4
# = 6 possible combinations

# ==============================================================

# In the case of x in R^150, for an order 3 polynomial vector
# we calculate the combinations at each order (order 1 simply = 150)
# then sum the combinations to get the total number of dimensions of the vector

k = 150  # k unique elements in order 1

num_orders = 3  # order r polynomial vector
total_combinations = 0

for r in range(1, num_orders + 1):
    combinations = math.comb(k + r - 1, r)
    print(f"No. combs. in order {r}: {combinations}")
    total_combinations += combinations

print(
    f"Total dimensions of {num_orders} order polynomial feature vector with {k} unique elements: {total_combinations}")
