# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:25:41 2022

@author: Guillermo
"""

# 2. Assign a variable name to each of the following and use Python to 
# identify the data type of each variable:
# - 2
# - 2.0
# - 10j
# - 2 Cool for School
# - True

Two = 2 

TwoPoint0 = 2.0

TenJ = 10j

Dog = "2 cool for School"

Correct = True

# 3. Create a list named "A"  containing all the values from above


A = [Two, TwoPoint0, TenJ, Dog, Correct]

# 4. Create a string named "B" containing the input "I like pie more than cake." 
# Using string slicing, extract: 
# - I like
# - pie more
# - than cake
# - I like more cake

B = "I like pie more than cake."

B[:6]

B[7:15]

B[16:]

B[:7] + B[11:15] + B[20:]

# This question was part of an in-person interview 
# where you were expected to write the code on a board: 
# "Design a function in which I can input a value, when I input the value, 
# it returns the 4 possible outputs":
# - If it is a multiple of 3 return the string "foo"
# - If it is a multiple of 5 return the string "bar"
# - If it is a multiple of 15 return the string "foobar"
# - If it does not satisfy any of those, return the string "Not a multiple of 3, 5, or 15"

def FoobarFunction(Value): 
    """
    this function will let you know if your Value is a multiple of 3, 5 or 15. 
    It will return foo, bar, or foobar respectively. If it is not a multiple
    of any of those it will return "Not a multiple of 3, 5, or 15"
    Value(3)
    foo
    Value(5)
    bar
    Value (15)
    foo, bar, foobar
    Value(17)
    Not a multiple of 3, 5, or 15
    """
    A = float((Value/3)) 
    B = float((Value/5)) 
    C = float((Value/15))
    
    if int(A) == A and int(B) == B and int(C) == C :
        return "foo, bar, foobar"
    elif int(A) == A and int(B) == B:
        return "foo, bar"
    elif int(A) == A :
        return "foo"
    elif int(B) == B:
        return "bar"
    else:
        return "Not a multiple of 3, 5, or 15"


