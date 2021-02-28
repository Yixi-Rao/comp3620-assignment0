""" File name:   truth_tables.py
    Author:      Yixi Rao
    Date:        25/02/2021
    Description: This file defines a number of functions which implement Boolean
                expressions.

                It also defines a function to generate and print truth tables
                using these functions.

                It should be implemented for Exercise 2 of Assignment 0.

                See the assignment notes for a description of its contents.
"""


def boolean_fn1(a, b, c):
    """ Return the truth value of (a ∨ b) → (-a ∧ -b) 
    
        (bool, bool, bool) -> bool
    """
    return (not (a or b)) or ((not a) and (not b))


def boolean_fn2(a, b, c):
    """ Return the truth value of (a ∧ b) ∨ (-a ∧ -b)
    
        (bool, bool, bool) -> bool 
    """
    return (a and b) or ((not a) and (not b))


def boolean_fn3(a, b, c):
    """ Return the truth value of ((c → a) ∧ (a ∧ -b)) ∨ (-a ∧ b) 
    
        (bool, bool, bool) -> bool
    """
    return ((not c or a) and (a and (not b))) or ((not a) and b)


def draw_truth_table(boolean_fn):
    """ This function prints a truth table for the given boolean function.
        It is assumed that the supplied function has three arguments.

        ((bool, bool, bool) -> bool) -> None

        If your function is working correctly, your console output should look
        like this:

        >>> from truth_tables import *
        >>> draw_truth_table(boolean_fn1)
        a     b     c     res
        -----------------------
        False False False True
        False False True  True
        False True  False False
        False True  True  False
        True  False False False
        True  False True  False
        True  True  False False
        True  True  True  False
    """
    print("a     b     c     res")
    print("-----------------------")
    a = 0
    b = 0
    c = 0
    while a != 2:
        while b != 2:
            while c != 2:
                if a != 0:
                    va = str(a != 0) + " "
                else:
                    va = str(a != 0)
                if b != 0:
                    vb = str(b != 0) + " "
                else:
                    vb = str(b != 0)
                if c != 0:
                    vc = str(c != 0) + " "
                else:
                    vc = str(c != 0)
                print(va + " " + vb + " " + vc + " " + str(boolean_fn(a != 0, b != 0, c != 0)))
                c = c + 1
            c = 0
            b = b + 1
        b = 0
        a = a + 1



