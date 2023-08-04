#!/usr/bin/env python3
""" Type Annotation Function safely_get_value """


from typing import Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[~T, None]) -> Union[Any, ~T]:
    """ This function safely retrieve a value from a dictionary """
    if key in dct:
        return dct[key]
    else:
        return default
