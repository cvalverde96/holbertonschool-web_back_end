#!/usr/bin/env python3

"""
async routine called wait_n that takes in 2 int arguments(in this order):
n and max_delay. You will spawn wait_random n
times with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays is in ascending order without using sort()
because of concurrency.
"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): the amount of time wait_random is spawned
        max_delay (int): the amount of time is delayed

    Returns:
        List: return the list of delays
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
