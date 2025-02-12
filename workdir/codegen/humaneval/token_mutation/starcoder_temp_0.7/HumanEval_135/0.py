from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a list which returns the largest index of an list which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given element will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """

    seen = {}

    for i, v in enumerate(arr):
        if v in seen:
            return seen[v]
        else:
            seen[v - min(arr)] = i

    return -1

def check(candidate):
    assert candidate([1, 2, 4, 3, 5]) == 3
    assert candidate([1, 2, 4, 5]) == -1
    assert candidate([1, 4, 2, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate([4, 8, 5, 7, 3]) == 4
    assert candidate([]) == -1

def test_check():
    check(can_arrange)

test_check()
