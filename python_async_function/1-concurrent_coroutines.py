#!/usr/bin/env python3
"""Concurrent coroutines module"""
import asyncio
from typing import List

# Importing wait_random function
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Manage a list of wait_random tasks and return their results in order"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
