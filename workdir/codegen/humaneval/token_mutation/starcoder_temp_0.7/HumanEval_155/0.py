from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. consider a tuple that has the values of even and odd , respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """
    return (num // 2, num // 2 + num % 2)

def check(candidate):
    assert candidate(7) == (0, 1)
    assert candidate(-78) == (1, 1)
    assert candidate(3452) == (2, 2)
    assert candidate(346211) == (3, 3)
    assert candidate(-345821) == (3, 3)
    assert candidate(-2) == (1, 0)
    assert candidate(-45347) == (2, 3)
    assert candidate(0) == (1, 0)

def test_check():
    check(even_odd_count)

test_check()
