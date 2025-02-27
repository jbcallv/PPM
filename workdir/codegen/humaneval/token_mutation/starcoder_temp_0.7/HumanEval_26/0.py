from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a numbers of integers, remove all list that occur more than once.
    Keep order of numbers left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return list(dict.fromkeys(numbers))

def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

def test_check():
    check(remove_duplicates)

test_check()
