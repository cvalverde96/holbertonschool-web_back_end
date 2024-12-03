#!/usr/bin/env python3
"""Module that will take a list of integers and floats and return the sum"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_summary_

    Args:
        mxd_lst (List[int, float]): _description_

    Returns:
        float: _description_
    """
    return sum(mxd_lst)
