#!/usr/bin/env python3
from typing import List, Union
"""This passes an argument mxd_list,
and returns the sum
"""


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of the list, adding both ints and floats"""
    return sum(mxd_list)
