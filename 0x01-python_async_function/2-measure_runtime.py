#!/usr/bin/env python3
""" Measuring the runtime of the previous function """


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ This fucntion calculate the time that the imported
    function takes to run """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    run_time = start_time - end_time
    return float(run_time / n)
