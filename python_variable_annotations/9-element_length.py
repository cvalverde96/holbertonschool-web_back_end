#!/usr/bin/env python3
"""
a function that takes a list of sequences and returns a list of tuples
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_summary_

    Args:
        lst (Iterable[Sequence]): list of seqeuences

    Returns:
        List[Tuple[Sequence, int]]: returned list of tuples
    """
    return [(i, len(i)) for i in lst]
