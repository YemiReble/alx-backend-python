#!/usr/bin/env python3
""" Type Annotation Function that accept string, int and float """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ This function has the capability to accept 'stings'
    integers and floats
    """
    return (k, float(v * v))
