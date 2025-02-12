def starts_one_ends(n: int) -> int:
    """
    Given a number integer n, return the count of the positive of n-digit
    positive integers that start or end with 1.
    """

    return 0


def check(candidate):
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

def test_check():
    check(starts_one_ends)

test_check()
