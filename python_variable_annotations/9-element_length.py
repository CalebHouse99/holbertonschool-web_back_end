#!/usr/bin/env python3
"""This function gets the length of the element"""
from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    """using len, this gets the length of the element"""
    return [(i, len(i)) for i in lst]
