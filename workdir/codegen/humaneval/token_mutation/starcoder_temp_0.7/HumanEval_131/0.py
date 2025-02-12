def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    return 0 if all digits are even.
    For example:
    >>> digits(1)
    1
    >>> digits(4)
    0
    >>> digits(235)
    15
    """
    if n == 0:
        return 0
    else:
        if n % 2!= 0:
            return n % 10 + digits(n // 10)
        else:
            return digits(n // 10)

def check(candidate):
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) == 1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625
    assert candidate(2468) == 0

def test_check():
    check(digits)

test_check()
