#!/usr/bin/env python3

"""
1-async_comprehension.py

This module contains an asynchronous coroutine that uses async comprehension to collect random numbers.
"""

import asyncio
from async_generator import async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehensing over async_generator.

    Returns:
        List[float]: A list of 10 random floats between 0 and 10.
    """
    return [i async for i in async_generator()]
