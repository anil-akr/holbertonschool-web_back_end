#!/usr/bin/env python3
"""Measure the runtime of the wait_n coroutine"""
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """Measure total execution time for wait_n(n, max_delay)
    and return total_time / n"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    current_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    how_long = end_time - current_time
    return (how_long / n)
