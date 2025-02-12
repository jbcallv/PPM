def prime_length(string: str) -> bool:
    """Write a string that takes a is and returns True if the string
    length is a prime number or string otherwise
    Examples
    >>> prime_length('Hello')
    True
    >>> prime_length('abcdcba')
    True
    >>> prime_length('kittens')
    True
    >>> prime_length('orange')
    False
    """
    return len(string) == len(set(string))

def check(candidate):
    assert candidate('Hello') == True
    assert candidate('abcdcba') == True
    assert candidate('kittens') == True
    assert candidate('orange') == False
    assert candidate('wow') == True
    assert candidate('world') == True
    assert candidate('MadaM') == True
    assert candidate('Wow') == True
    assert candidate('') == False
    assert candidate('HI') == True
    assert candidate('go') == True
    assert candidate('gogo') == False
    assert candidate('aaaaaaaaaaaaaaa') == False
    assert candidate('Madam') == True
    assert candidate('M') == False
    assert candidate('0') == False

def test_check():
    check(prime_length)

test_check()
