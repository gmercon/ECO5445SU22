# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 14:09:04 2022

@author: Guillermo
"""

# The task is to compute an approximation to  using Monte Carlo.

# Use no imports besides numpy

# Your hints are as follows:

# If U is a bivariate uniform random variable on the unit square (0,1)^2 , 
# then the probability that U lies in a subset B of (0,1)^2 is equal to the area of B.

# If U_1...U_n are IID copies of U, then, as n gets large, the fraction that falls in B, 
# converges to the probability of landing in B.

# For a circle, Area = Pi*r^2

# You'll need np.random.uniform()


import numpy as np
