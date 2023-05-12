#!/usr/bin/env python3
"""Async Comprehension"""

import asyncio
from typing import List

# Importing async_generator function
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return 10 random numbers using an async comprehension"""
    return [i async for i in async_generator()]
