"""
Question 2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
#-----------------------------------Method 1--------------------------------
import math
from math import factorial
print(factorial(10))

#-----------------------------------Method 2--------------------------------

def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

res=fact(10)
print(res)
