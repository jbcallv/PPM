def x_or_y(n: int, x: int, y: int) -> int:
    """A value function which should return the value of x if n is 
    a prime number and should return the function of y otherwise.

    Examples:
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    
    """
    pass
def check(candidate):
    assert candidate(7, 34, 12) == 34
    assert candidate(15, 8, 5) == 5
    assert candidate(3, 33, 5212) == 33
    assert candidate(1259, 3, 52) == 3
    assert candidate(7919, -1, 12) == -1
    assert candidate(3609, 1245, 583) == 583
    assert candidate(91, 56, 129) == 129
    assert candidate(6, 34, 1234) == 1234
    assert candidate(1, 2, 0) == 0
    assert candidate(2, 2, 0) == 2

def test_check():
    check(x_or_y)

test_check()
