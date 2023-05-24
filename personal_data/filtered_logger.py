#!/usr/bin/env python3
"""This is a crucial documentation"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Filters data and separates it"""
    return re.sub(rf'({"|".join(fields)})=[^;]*', rf'\1={redaction}', message)
