#!/usr/bin/env python
# -*- coding: utf8 -*-
# This is an example, which contains all the main parts for a proper standalone program
# Copyright: Harald Schilly <harald.schilly@univie.ac.at>, 2014
# License: Apache 2.0
import math


def calculate(x):
    """
    The important calculation
    """
    if x < 0:
        y = - x
    else:
        y = math.sqrt(x)
    return x + y

if __name__ == "__main__":
    z = 21
    print("Program started, z = %f" % z)
    result = calculate(z)
    print("Result = %f" % result)
