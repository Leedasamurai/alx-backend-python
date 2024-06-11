#!/usr/bin/env python3

"""
2-measure_runtime.py

This module contains a coroutine to measure the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time

