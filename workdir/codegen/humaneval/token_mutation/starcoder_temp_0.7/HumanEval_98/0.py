def count_upper(s: str) -> int:
    """
    for a string s, count the number of the vowels in even indices.
    
    For example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    return len([c for i, c in enumerate(s) if i % 2 == 0 and c.lower() in 'aeiou'])

def check(candidate):
    assert candidate('aBCdEf') == 1
    assert candidate('abcdefg') == 0
    assert candidate('dBBE') == 0
    assert candidate('B') == 0
    assert candidate('U') == 1
    assert candidate('') == 0
    assert candidate('EEEE') == 2

def test_check():
    check(count_upper)

test_check()
