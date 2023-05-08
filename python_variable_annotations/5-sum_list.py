#!/usr/bin/env python3
"""
This module contains a single function, sum_list, that sums a list of floats.

Functions:
    sum_list(input_list: List[float]) -> float:
        Given a list of floats, returns the sum of the list elements.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Given a list of floats, returns the sum of the list elements.

    Args:
        input_list (List[float]): A list of floats to be summed.

    Returns:
        float: The sum of the input list.

    Example:
        >>> sum_list([1.0, 2.0, 3.0])
        6.0
    """
    return sum(input_list)
