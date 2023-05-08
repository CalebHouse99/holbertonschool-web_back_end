#!/usr/bin/env python3
"""It's crucial that this comment comes before the imports"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes the string and numbers and returns a tuple of them"""
    return (k, v ** 2)
