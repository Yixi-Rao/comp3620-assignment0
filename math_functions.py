""" File name:   math_functions.py
    Author:      <your name goes here>
    Date:        <the date goes here>
    Description: This file defines a set of variables and simple functions.

                 It should be implemented for Exercise 1 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""
import math
ln_e =  math.e # YOUR CODE HERE

twenty_radians = math.radians(20)  # YOUR CODE HERE


def quotient_ceil(numerator, denominator):
    """ YOUR CODE HERE """
    return math.ceil(numerator / denominator)


def quotient_floor(numerator, denominator):
    """ YOUR CODE HERE """
    return math.floor(numerator / denominator)

def manhattan(x1, y1, x2, y2):
    """ YOUR CODE HERE """
    return abs(x1 - x2) + abs(y1 - y2)

