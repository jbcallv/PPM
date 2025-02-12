def cycpattern_check(a: str, b: str) -> bool:
    """You are given 2 words. You need to return first if the second word or any of its rotations is a rotation in the them word
    >>> cycpattern_check('abcd', 'abd')
    False
    >>> cycpattern_check('hello', 'ell')
    True
    >>> cycpattern_check('whassup', 'psus')
    False
    >>> cycpattern_check('abab', 'baa')
    True
    >>> cycpattern_check('efef', 'eeff')
    False
    >>> cycpattern_check('himenss', 'simen')
    True

    """
    return b in a + a[1:]


def check(candidate):
    assert candidate('xyzw', 'xyw') == False
    assert candidate('yello', 'ell') == True
    assert candidate('whattup', 'ptut') == False
    assert candidate('efef', 'fee') == True
    assert candidate('abab', 'aabb') == False
    assert candidate('winemtt', 'tinem') == True

def test_check():
    check(cycpattern_check)

test_check()
