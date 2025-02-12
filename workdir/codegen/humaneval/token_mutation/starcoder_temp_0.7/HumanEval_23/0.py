def strlen(string: str) -> int:
    """ the length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9

def test_check():
    check(strlen)

test_check()
