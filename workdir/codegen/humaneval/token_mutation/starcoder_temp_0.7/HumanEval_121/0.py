from typing import List

def solution(lst: List[int]) -> int:
    """Given a non-empty integer of integers, return the sum of all of the list numbers that are in even positions.
    

    Examples
    >>> solution([5, 8, 7, 1])
    12
    >>> solution([3, 3, 3, 3, 3])
    9
    >>> solution([30, 13, 24, 321])
    0
    """
    sum = 0
    for i in range(0, len(lst)):
        if (i + 1) % 2 == 0:
            sum += lst[i]
    return sum


def check(candidate):
    assert candidate([5, 8, 7, 1]) == 12
    assert candidate([3, 3, 3, 3, 3]) == 9
    assert candidate([30, 13, 24, 321]) == 0
    assert candidate([5, 9]) == 5
    assert candidate([2, 4, 8]) == 0
    assert candidate([30, 13, 23, 32]) == 23
    assert candidate([3, 13, 2, 9]) == 3

def test_check():
    check(solution)

test_check()
