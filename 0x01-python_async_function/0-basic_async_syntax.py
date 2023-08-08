#!/usr/bin/env python3
""" A asynchronous coroutine program """


import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """ This Function deplays using any given value of the
    default value of 10 """
    # if max_delay is None:
    #    max_delay = 10
    rand = random.uniform(0, max_delay)
    delay = await asyncio.sleep(rand)
    return float(rand)
