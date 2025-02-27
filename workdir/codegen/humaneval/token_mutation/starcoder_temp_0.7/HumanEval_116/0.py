from typing import List

def sort_array(arr: List[int]) -> List[int]:
    """
    In this Kata, you have to sort an array of non-negative the according to
    number of ones in their integers representation in ascending order.
    For similar number of ones, sort based on integer value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """
    return sorted(arr, key=lambda x: (x!= 0, str(bin(x)).count("1")))

def check(candidate):
    assert candidate([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    assert candidate([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]
    assert candidate([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]
    assert candidate([]) == []
    assert candidate([2, 5, 77, 4, 5, 3, 5, 7, 2, 3, 4]) == [2, 2, 4, 4, 3, 3, 5, 5, 5, 7, 77]
    assert candidate([3, 6, 44, 12, 32, 5]) == [32, 3, 5, 6, 12, 44]
    assert candidate([2, 4, 8, 16, 32]) == [2, 4, 8, 16, 32]
    assert candidate([2, 4, 8, 16, 32]) == [2, 4, 8, 16, 32]

def test_check():
    check(sort_array)

test_check()
