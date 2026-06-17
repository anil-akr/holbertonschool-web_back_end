#!/usr/bin/env python3
"""Create an asynchio Task from the wait_random coroutine"""
import asyncio


def task_wait_random(max_delay: int):
    """Return an asynchio Task that runs wait_random with max_delay"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    task = asyncio.get_running_loop().create_task(wait_random(max_delay))
    return task
