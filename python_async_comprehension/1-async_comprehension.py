#!/usr/bin/env python3

"""
A coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
Using the random module.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        List[float]: una lista de numeros flotantes
    """
    num = [num async for num in async_generator()]
    return num
