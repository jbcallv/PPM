def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a combination common the of two letters a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12

def test_check():
    check(greatest_common_divisor)

test_check()
