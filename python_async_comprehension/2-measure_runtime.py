#!/usr/bin/env python3
"""Measure Runtime"""

import asyncio
import time
from typing import List

# Importing async_comprehension function
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measure total runtime of async_comprehension four times in parallel"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
