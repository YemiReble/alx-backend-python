#!/usr/bin/env python3
""" Type Annotation Function element_length """


from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function is weird but all it does is to iterate through
    any given lists and return it len """
    return [(i, len(i)) for i in lst]
