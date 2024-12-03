#!/usr/bin/env python3
"""
Module that takes a string k and an int or float v and returns a tuple
"""

from typing import Tuple, Union
from math import sqrt


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """_summary_

    Args:
        k (str): string to return through tuple
        v (Union[int, float]): variable that could be int or
        float to square root

    Returns:
        Tuple[str, float]: tuple to be return with string and float
    """
    return k, sqrt(v)
