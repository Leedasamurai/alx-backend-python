#!/usr/bin/env python3

"""
async_generator.py

This module contains an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random float between 0 and 10.

    The generator will loop 10 times, each time asynchronously waiting 1 second
    before yielding the next random number.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
