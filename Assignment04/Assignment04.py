# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 14:09:04 2022

@author: Guillermo
"""

# The task is to compute an approximation to Pi using Monte Carlo.

# Use no imports besides numpy

# Your hints are as follows:

# If U is a bivariate uniform random variable on the unit square (0,1)^2 , 
# then the probability that U lies in a subset B of (0,1)^2 is equal to the area of B.

# If U_1...U_n are IID copies of U, then, as n gets large, the fraction that falls in B, 
# converges to the probability of landing in B.

# For a circle, Area = Pi*r^2

# You'll need np.random.uniform()

# Hints in class: Requires for loops and 1 function ,Pi = A/r^2, r = .5
# Pi = 4A, A = Pi/4

import numpy as np

Trials = 100000
Radius = .5

DotsInside = 0 
DotsOutside = 0 

XrandomCord = np.random.uniform(0,1, Trials)

YrandomCord = np.random.uniform(0,1, Trials)


for i in range(Trials):
    X = XrandomCord[i]
    Y = YrandomCord[i]
    # Find the length of the line (X, Y) from the 'origin' (.5, .5)
    # Then check if that line is shorter than or equal to the radius
    # if the Length of line is shorter than radius,
    # then the point falls in the circle
    if (((Radius - X)**2) + ((Radius - Y)**2))**(1/2) <= Radius:
        DotsInside += 1
    else:
        DotsOutside += 1
        
     # using our formula from above we have converted Area = Pi*R^2 to 
     # Pi = 4*Area, using your hints we see that the probality of landing
     # inside the circle is approxiametly the area
     
Pi = 4*DotsInside/Trials
print("Estimation of Pi:", Pi)

