#!/usr/bin/env python3
"""
Module that spawns task_wait_random n times with specified max_delay
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random
        max_delay (int): Maximum delay value

    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
