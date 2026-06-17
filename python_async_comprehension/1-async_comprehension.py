#!/usr/bin/env python3
"""Coroutine that collects random numbers from async_genrator
using an async comprehension and return them"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers, from async_generator
    using an async comprehension and return them"""
    return [number async for number in async_generator()]
