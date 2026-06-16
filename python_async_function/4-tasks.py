#!/usr/bin/env python3
"""Create asyncio Tasks from the wait_rando coroutine
using task_wait_random"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Call task_wait_random n times with max_delay
    and return delays in ascending order"""
    coroutines = [task_wait_random(max_delay) for _index in range(n)]
    delays = []
    for completed_coroutine in asyncio.as_completed(coroutines):
        delay = await completed_coroutine
        delays.append(delay)
    return delays
