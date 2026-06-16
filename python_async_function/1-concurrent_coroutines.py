#!/usr/bin/env python3
"""write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay."""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function wait_n call wait_random, n times with max_delay
    and return the list of delays in ascending order"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    wait_time = await asyncio.gather(*coroutines)
    return sorted(wait_time)
