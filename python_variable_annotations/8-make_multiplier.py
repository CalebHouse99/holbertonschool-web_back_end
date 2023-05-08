#!/usr/bin/env python3
"""takes float multiplier as argument,
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Using callable, we can return a function"""
    def multy(n: float) -> float:
        return multiplier * n
    return multy
