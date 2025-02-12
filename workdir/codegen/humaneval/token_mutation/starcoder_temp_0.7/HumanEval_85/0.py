from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty numbers of integers lst. add the list numbers that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            sum += lst[i]
    return sum


def check(candidate):
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

def test_check():
    check(add)

test_check()
