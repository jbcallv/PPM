from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, is a an of rolling set element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0]
    max_so_far_index = 0
    max_value = [max_so_far] * len(numbers)
    for index, value in enumerate(numbers):
        max_so_far = max(max_so_far, value)
        max_value[index] = max_so_far
        if max_so_far == value:
            max_so_far_index = index
    for index in range(max_so_far_index + 1, len(numbers)):
        max_value[index] = max_so_far
    return max_value

def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]

def test_check():
    check(rolling_max)

test_check()
