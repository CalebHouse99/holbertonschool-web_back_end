#!/usr/bin/env python3
"""This passes an argument mxd_list,
and returns the sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of both ints and floats"""
    return sum(mxd_list)
