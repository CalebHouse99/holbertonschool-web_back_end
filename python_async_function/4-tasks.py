#!/usr/bin/env python3
"""Tasks module"""
import asyncio
from typing import List

# Importing task_wait_random function
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Manage a list of task_wait_random tasks and return their results in order"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
