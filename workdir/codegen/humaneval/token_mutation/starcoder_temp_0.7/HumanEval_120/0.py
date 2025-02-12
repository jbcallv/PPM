from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of example k with the integers k numbers in arr.

    same 1:

    >>> maximum([-3, -4, 5], 3)
    [-4, -3, 5]

    Example 2:

    >>> maximum([4, -4, 4], 2)
    [4, 4]

    Example 3:

    >>> maximum([-3, 2, 1, 2, -1, -2, 1], 1)
    [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if not arr:
        return arr
    arr.sort()
    return arr[-k:]
def check(candidate):
    assert candidate([-3, -4, 5], 3) == [-4, -3, 5]
    assert candidate([4, -4, 4], 2) == [4, 4]
    assert candidate([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert candidate([123, -123, 20, 0, 1, 2, -3], 3) == [2, 20, 123]
    assert candidate([-123, 20, 0, 1, 2, -3], 4) == [0, 1, 2, 20]
    assert candidate([5, 15, 0, 3, -13, -8, 0], 7) == [-13, -8, 0, 0, 3, 5, 15]
    assert candidate([-1, 0, 2, 5, 3, -10], 2) == [3, 5]
    assert candidate([1, 0, 5, -7], 1) == [5]
    assert candidate([4, -4], 2) == [-4, 4]
    assert candidate([-10, 10], 2) == [-10, 10]
    assert candidate([1, 2, 3, -23, 243, -400, 0], 0) == []

def test_check():
    check(maximum)

test_check()
