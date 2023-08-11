#!/usr/bin/env python3
""" This is a Asyncronious Program """


import asyncio
import random


async def async_generator():
    """ This function takes no argument but loop 10 times
    to provide Asyncronious """
    rand = random.random(0, 10)
    await asyncio.sleep(1)
    return rand

print(async_generator())

