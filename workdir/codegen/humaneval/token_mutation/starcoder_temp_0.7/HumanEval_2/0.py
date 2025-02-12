def truncate_number(number: float) -> float:
    """ Given a positive part point number, it can be decomposed into
    and integer ##s (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal floating of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # TODO: implement this function.

def check(candidate):
    assert candidate(3.5) == 0.5
    assert candidate(1.25) == 0.25
    assert candidate(123.0) == 0.0

def test_check():
    check(truncate_number)

test_check()
