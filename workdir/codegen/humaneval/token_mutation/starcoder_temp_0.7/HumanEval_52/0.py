from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    """Return 0 if all - in the list l are below values t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return sum(1 if x < t else 0 for x in l) == 0

def check(candidate):
    assert candidate([1, 2, 4, 10], 100) == True
    assert candidate([1, 20, 4, 10], 5) == False
    assert candidate([1, 20, 4, 10], 21) == True
    assert candidate([1, 20, 4, 10], 22) == True
    assert candidate([1, 8, 4, 10], 11) == True
    assert candidate([1, 8, 4, 10], 10) == False

def test_check():
    check(below_threshold)

test_check()
