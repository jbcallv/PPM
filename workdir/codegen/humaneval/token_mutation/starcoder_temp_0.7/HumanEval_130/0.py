from typing import List

def tri(n: int) -> List[int]:
    """Everyone knows Fibonacci sequence, it was studied deeply by elements in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 people of the Tribonacci sequence.
    Examples:
    >>> tri(3)
    [1, 3, 2, 8]
    """
    # 0 1 1 2 3 5 8 13
    # 0 1 1 2 4 7 13 24
    # 0 1 2 4 7 13 24 44
    # 0 1 3 6 10 18 31 56
    # 0 1 4 10 20 39 75 144
    # 0 1 5 15 35 78 168 350
    # 0 1 6 21 56 132 280 585
    # 0 1 7 28 88 234 534 1189
    # 0 1 8 36 134 390 924 2199
    tri_num = [0, 1, 1, 2, 3, 5, 8, 13]
    for i in range(8, n):
        tri_num.append(tri_num[i - 1] + tri_num[i - 2] + tri_num[i - 3])
    return tri_num[:n + 1]

def check(candidate):
    assert candidate(3) == [1, 3, 2, 8]
    assert candidate(4) == [1, 3, 2, 8, 3]
    assert candidate(5) == [1, 3, 2, 8, 3, 15]
    assert candidate(6) == [1, 3, 2, 8, 3, 15, 4]
    assert candidate(7) == [1, 3, 2, 8, 3, 15, 4, 24]
    assert candidate(8) == [1, 3, 2, 8, 3, 15, 4, 24, 5]
    assert candidate(9) == [1, 3, 2, 8, 3, 15, 4, 24, 5, 35]
    assert candidate(20) == [1, 3, 2, 8, 3, 15, 4, 24, 5, 35, 6, 48, 7, 63, 8, 80, 9, 99, 10, 120, 11]
    assert candidate(0) == [1]
    assert candidate(1) == [1, 3]

def test_check():
    check(tri)

test_check()
