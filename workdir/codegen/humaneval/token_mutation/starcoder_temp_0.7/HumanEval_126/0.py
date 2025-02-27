from typing import List

def is_sorted(lst: List[int]) -> bool:
    """
    Given a list of numbers, check whether or not they are sorted
    in ascending order. If real has more than 1 duplicate of the same
    number, return False. Assume no one numbers and only integers.

    Examples
    >>> is_sorted([5])
    True
    >>> is_sorted([1, 2, 3, 4, 5])
    True
    >>> is_sorted([1, 3, 2, 4, 5])
    False
    >>> is_sorted([1, 2, 3, 4, 5, 6])
    True
    >>> is_sorted([1, 2, 3, 4, 5, 6, 7])
    True
    >>> is_sorted([1, 3, 2, 4, 5, 6, 7])
    False
    >>> is_sorted([1, 2, 2, 3, 3, 4])
    True
    >>> is_sorted([1, 2, 2, 2, 3, 4])
    False
    """
    # TODO: Implement me!
    pass

def check(candidate):
    assert candidate([5]) == True
    assert candidate([1, 2, 3, 4, 5]) == True
    assert candidate([1, 3, 2, 4, 5]) == False
    assert candidate([1, 2, 3, 4, 5, 6]) == True
    assert candidate([1, 2, 3, 4, 5, 6, 7]) == True
    assert candidate([1, 3, 2, 4, 5, 6, 7]) == False
    assert candidate([]) == True
    assert candidate([1]) == True
    assert candidate([3, 2, 1]) == False
    assert candidate([1, 2, 2, 2, 3, 4]) == False
    assert candidate([1, 2, 3, 3, 3, 4]) == False
    assert candidate([1, 2, 2, 3, 3, 4]) == True
    assert candidate([1, 2, 3, 4]) == True

def test_check():
    check(is_sorted)

test_check()
