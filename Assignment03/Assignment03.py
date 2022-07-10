# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:37:45 2022

@author: Guillermo
"""
import os 
import numpy as np 

os.getcwd()
os.chdir('C:\\Users\\Guillermo\\Documents\\GitHub\\ECO5445SU22\\Assignment03')


# 2. Construct the following array "A" with i = 3 rows and j = 4 columns: 

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

A

# 3. From array A show how to extract each of the following by scalar selection or slicing:
# - number 7
# - row 1
# - column 2
# - rows 2 and 3
# - values 7, 8, 11, and 12

A[1][2]

A[0]

A[:,1]

A[1:3]

A[1, 2], A[1, 3], A[2, 2], A[2, 3]

# 4. Create the array B = 2*A - 8. From B, determine the following:
  
B = 2 * A - 8

B
    
# - the sum of the row values

np.sum(B, axis = 1)

# - the sum of the column values

np.sum(B, axis = 0)

# - the cumulative sum of row values

np.cumsum(B, axis = 1)

# - the cumulative sum of column values

np.cumsum(B,axis=0)

# 5. From array B, create new arrays containing the element-by-element:
# - natural logarithm

C = np.log(B)

C = np.nan_to_num(C, copy=True, nan=0.0, posinf=None, neginf=None)

C

# - square root

D = np.sqrt(B) 

D = np.nan_to_num(D, copy=True, nan=0.0, posinf=None, neginf=None)

D

# - square

E = np.square(B)

E

# - absolute value

F = np.absolute(B)

F

# 6. In 1992, Giancarlo Moschini and Karl Meilke published a paper to the/
# Journal of Agricultural Economics. In this paper,/
# they estimated linear demand and supply functions of pork in Canada./ 
# I have simplified the equations into the following format:
#        (Demand) Q = 286 - 20p
#        (Supply)    Q = 88 + 40p

# - We can write this in matrix notation as:
#       [1 20      [Q    [286
#        1 -40] X    P] =  88]

# Using the tools provided in the lecture, solve for the equilibrium price and quantity.

X = np.array([[1, 20], [1, -40]])

Y = np.array([[286], [88]]) 

X_inv = np.linalg.inv(X)

Z_soln = X_inv.dot(Y)

print(Z_soln)

# Equilibrium price and quantity are as follows

Price = 3.3

Quantity = 220 


