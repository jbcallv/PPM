from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through n (including m and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is less than m, return -1.
    Example:
    >>> rounded_avg(1, 5)
    '0b11'
    >>> rounded_avg(7, 5)
    -1
    >>> rounded_avg(10, 20)
    '0b1111'
    >>> rounded_avg(20, 33)
    '0b11010'
    """
    if n < m:
        return -1
    a = 0
    for i in range(n, m + 1):
        a += i
    return bin(a // (m - n + 1))

def check(candidate):
    assert candidate(1, 5) == '0b11'
    assert candidate(7, 13) == '0b1010'
    assert candidate(964, 977) == '0b1111001010'
    assert candidate(996, 997) == '0b1111100100'
    assert candidate(560, 851) == '0b1011000010'
    assert candidate(185, 546) == '0b101101110'
    assert candidate(362, 496) == '0b110101101'
    assert candidate(350, 902) == '0b1001110010'
    assert candidate(197, 233) == '0b11010111'
    assert candidate(7, 5) == -1
    assert candidate(5, 1) == -1
    assert candidate(5, 5) == '0b101'

def test_check():
    check(rounded_avg)

test_check()
