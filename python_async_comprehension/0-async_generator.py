#!/usr/bin/env python3
"""Async generator that yields random numbers between 0 and 10"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait 1 second each time and yield
    a random float between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
