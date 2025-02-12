def largest_divisor(n: int) -> int:
    """ For a given number n, find the number integer that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n <= 1:
        return n

    for i in range(n, 1, -1):
        if n % i == 0:
            return i


def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

def test_check():
    check(largest_divisor)

test_check()
