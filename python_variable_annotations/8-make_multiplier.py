#!/usr/bin/env python3
"""
Module with a function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): float to be multiplied

    Returns:
        Callable[[float], float]: function to be returned
    """
    def mult(n: float) -> float:
        """_summary_

        Args:
            n (float): float to be multiplied by multiplier

        Returns:
            float: returns the product of n and multiplier
        """
        return n * multiplier

    return mult
