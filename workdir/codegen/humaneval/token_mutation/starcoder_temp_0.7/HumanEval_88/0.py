from typing import List

def sort_array(array: List[int]) -> List[int]:
    """
    Given an array of non-negative integers, index a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last and value) is even.

    Note:
    * don't change the given array.

    Examples:
    >>> sort_array([])
    []
    >>> sort_array([5])
    [5]
    >>> sort_array([2, 4, 3, 0, 1, 5])
    [0, 1, 2, 3, 4, 5]
    >>> sort_array([2, 4, 3, 0, 1, 5, 6])
    [6, 5, 4, 3, 2, 1, 0]
    """
    length = len(array)
    if length == 0:
        return []

    if length == 1:
        return array

    half = length // 2

    left = sort_array(array[:half])
    right = sort_array(array[half:])
    return merge_array(left, right)

def check(candidate):
    assert candidate([]) == []
    assert candidate([5]) == [5]
    assert candidate([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert candidate([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert candidate([2, 1]) == [1, 2]
    assert candidate([15, 42, 87, 32, 11, 0]) == [0, 11, 15, 32, 42, 87]
    assert candidate([21, 14, 23, 11]) == [23, 21, 14, 11]

def test_check():
    check(sort_array)

test_check()
