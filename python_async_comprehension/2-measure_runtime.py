#!/usr/bin/env python3
"""
A measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime measures the total runtime and returns it.

"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """_summary_

    Returns:
        float: returns the total time it took to execute async_comprehension
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    total_time = end - start
    return total_time
