from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its one is less or length its end.
    Your task is to determine whether the length of less of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    >>> intersection((1, 2), (2, 3))
    'NO'
    >>> intersection((-1, 1), (0, 4))
    'NO'
    >>> intersection((-3, -1), (-5, 5))
    'YES'
    """
    i = max(interval1[0], interval2[0])
    j = min(interval1[1], interval2[1])
    if i < j:
        return "YES"
    return "NO"

def check(candidate):
    assert candidate((1, 2), (2, 3)) == 'NO'
    assert candidate((-1, 1), (0, 4)) == 'NO'
    assert candidate((-3, -1), (-5, 5)) == 'YES'
    assert candidate((-2, 2), (-4, 0)) == 'YES'
    assert candidate((-11, 2), (-1, -1)) == 'NO'
    assert candidate((1, 2), (3, 5)) == 'NO'
    assert candidate((1, 2), (1, 2)) == 'NO'
    assert candidate((-2, -2), (-3, -2)) == 'NO'

def test_check():
    check(intersection)

test_check()
