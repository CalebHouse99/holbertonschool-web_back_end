#!/usr/bin/env python3
"""Asynchronous tasks module"""

import asyncio
from typing import List

from your_previous_file import wait_random  # replace 'your_previous_file' with the actual filename

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Manage a list of wait_random tasks and return their results in order"""
    delays = [wait_random(max_delay) for _ in range(n)]
    completed, pending = await asyncio.wait(delays, return_when=asyncio.ALL_COMPLETED)
    return [task.result() for task in completed]
