from typing import List

def specialFilter(nums: List[int]) -> int:
    """Write a function that takes an array of numbers as input and counts 
    the number of elements in the array that are less than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    >>> specialFilter([15, -73, 14, -15])
    1
    >>> specialFilter([33, -2, -3, 45, 21, 109])
    2
    """
    count = 0
    for i in nums:
        if i < 10 and i % 2 == 1 and i % 10 == 1:
            count += 1
    return count

def check(candidate):
    assert candidate([5, -2, 1, -5]) == 0
    assert candidate([15, -73, 14, -15]) == 1
    assert candidate([33, -2, -3, 45, 21, 109]) == 2
    assert candidate([43, -12, 93, 125, 121, 109]) == 4
    assert candidate([71, -2, -33, 75, 21, 19]) == 3
    assert candidate([1]) == 0
    assert candidate([]) == 0

def test_check():
    check(specialFilter)

test_check()
