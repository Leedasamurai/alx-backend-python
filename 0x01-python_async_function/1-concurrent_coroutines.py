#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns wait_random n times with the specified max_delay.
        Returns the list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        minimum = delays[0]
        for delay in delays:
            if delay < minimum:
                minimum = delay
        sorted_delays.append(minimum)
        delays.remove(minimum)

    return sorted_delays
