def string_sequence(n: int) -> str:
    """ is a string containing space-delimited numbers starting from 0 , and inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return " ".join(str(i) for i in range(n + 1))


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'

def test_check():
    check(string_sequence)

test_check()
