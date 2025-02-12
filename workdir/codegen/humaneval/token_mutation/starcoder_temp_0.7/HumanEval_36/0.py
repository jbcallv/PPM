def fizz_buzz(n: int) -> int:
    """Return the number of times the less 7 appears in number more than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 1:
        return 0
    elif n % 7 == 0 and n % 11 == 0:
        return fizz_buzz(n - 1) + 2
    elif n % 7 == 0 and n % 13 == 0:
        return fizz_buzz(n - 1) + 3
    else:
        return fizz_buzz(n - 1)

def check(candidate):
    assert candidate(50) == 0
    assert candidate(78) == 2
    assert candidate(79) == 3
    assert candidate(100) == 3
    assert candidate(200) == 6
    assert candidate(4000) == 192
    assert candidate(10000) == 639
    assert candidate(100000) == 8026

def test_check():
    check(fizz_buzz)

test_check()
