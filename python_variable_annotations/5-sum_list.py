#!/usr/bin/env python3
"""Module that contains a function that takes a list of floats and sums them"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """_summary_

    Args:
        input_list (List[float]): list of floats to be summed

    Returns:
        float: sum of floats
    """
    return sum(input_list)
