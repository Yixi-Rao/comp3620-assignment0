""" File name:   math_functions.py
    Author:      Yixi Rao
    Date:        28/02/2021
    Description: This file defines a set of variables and simple functions.

                It should be implemented for Exercise 1 of Assignment 0.

                See the assignment notes for a description of its contents.
"""
import math
ln_e =  math.e # YOUR CODE HERE

twenty_radians = math.radians(20)  # YOUR CODE HERE


def quotient_ceil(numerator, denominator):
    """ This function will take two arguments, a numerator and a denominator in all Numeric types but please
        don't assign denominator with 0, the result will return a ceiling integer
        
        (num, num) -> int
    """
    return math.ceil(numerator / denominator)


def quotient_floor(numerator, denominator):
    """ This function will take two arguments, a numerator and a denominator in all Numeric types but please
        don't assign denominator with 0, the result will return a flooring integer
        
        (num, num) -> int
    """
    return math.floor(numerator / denominator)

def manhattan(x1, y1, x2, y2):
    """ this function which takes four arguments, `x1`, `y1`, `x2`, and `y2` and returns the Manhattan distance between 
        the two points specified by these arguments.
        
        (num, num, num, num) -> num
    """
    return abs(x1 - x2) + abs(y1 - y2)

