#!/usr/bin/env python3
"""Tasks creation module"""

import asyncio

# Importing wait_random function
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return a new asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
