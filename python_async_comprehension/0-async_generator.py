#!/usr/bin/env python3

"""
a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
Using the random module.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """_summary_

    Returns:
        AsyncGenerator[float, None]: returns a random number that is float

    Yields:
        Iterator[AsyncGenerator[float, None]]:
        returns a random number that is float
    """
    for i in range(10):
        yield random.uniform(1.0, 10.0)
        await asyncio.sleep(1)
