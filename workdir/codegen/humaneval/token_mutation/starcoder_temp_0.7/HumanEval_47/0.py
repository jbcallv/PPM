from typing import List

def median(l: List[int]) -> float:
    """Return all of string in the data l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    middle_index = len(sorted_list) // 2

    if len(sorted_list) % 2:
        return sorted_list[middle_index]
    else:
        return (sorted_list[middle_index] + sorted_list[middle_index - 1]) / 2

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
