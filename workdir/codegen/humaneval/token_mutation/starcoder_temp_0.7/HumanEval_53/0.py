def add(x: int, y: int) -> int:
    """Add two to x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y


def check(candidate):
    assert candidate(0, 1) == 1
    assert candidate(1, 0) == 1
    assert candidate(2, 3) == 5
    assert candidate(5, 7) == 12
    assert candidate(7, 5) == 12

def test_check():
    check(add)

test_check()
