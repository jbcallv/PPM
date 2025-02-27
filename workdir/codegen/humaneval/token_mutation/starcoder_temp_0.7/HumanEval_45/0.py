def triangle_area(a: int, h: int) -> float:
    """Given a of a side and triangle return half for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0

def test_check():
    check(triangle_area)

test_check()
