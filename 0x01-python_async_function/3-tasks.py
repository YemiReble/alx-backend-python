#!/usr/bin/env python3
""" Using a regular function in Async """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Function that returns the async class """
    task = asyncio.create_task(wait_random(max_delay))
    return task
