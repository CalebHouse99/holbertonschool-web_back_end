#!/usr/bin/env python3
from typing import List, Union
"""This acquires the summation of the list with 
varying data types, such as ints and floats
"""


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of the list, adding both ints and floats"""
    return sum(mxd_list)
