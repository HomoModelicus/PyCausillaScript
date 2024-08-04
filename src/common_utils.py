
from __future__ import annotations


def linear_search(haystack, needle) -> int:
    idx: int = -1
    for [ii, val] in enumerate(haystack):
        if val == needle:
            idx = ii
            break
    return idx

def is_valid_index(index: int) -> bool:
    return index >= 0

def find_if(haystack, predicate_fcn) -> int:
    idx: int = -1
    for [ii, val] in enumerate(haystack):
        if predicate_fcn(val):
            idx = ii
            break
    return idx

