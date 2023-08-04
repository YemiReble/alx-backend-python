#!/usr/bin/env python3
""" Type Annotation Function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function multiplies floats """
    def mult_float(f: float) -> float:
        return multiplier * f
    return mult_float
