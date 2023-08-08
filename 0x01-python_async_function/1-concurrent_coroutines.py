#!/usr/bin/env python3
""" Asynconious Program """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ This Funcition returns a lists of delays """
    # wait = await wait_random(max_delay)
    task = []
    wait = []

    for i in range(n):
        tasks = wait_random(max_delay)
        task.append(tasks)

    for tasks in asyncio.as_completed((task)):
        delay = await tasks
        wait.append(delay)

    return wait
