from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    """
    for a alphabet of words, return a list of words split on whitespace, if no whitespaces exists in the list you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    >>> split_words('Hello world!')
    ['Hello', 'world!']
    >>> split_words('Hello,world!')
    ['Hello', 'world!']
    >>> split_words('abcdef')
    3
    """
    # split_txt = txt.split(' ')
    # if len(split_txt) == 1:
    #     split_txt = txt.split(',')
    #     if len(split_txt) == 1:
    #         return len([c for c in txt if ord(c) % 2 == 1])
    #     else:
    #         return split_txt
    # else:
    #     return split_txt
    return txt.split()

def check(candidate):
    assert candidate('Hello world!') == ['Hello', 'world!']
    assert candidate('Hello,world!') == ['Hello', 'world!']
    assert candidate('Hello world,!') == ['Hello', 'world,!']
    assert candidate('Hello,Hello,world !') == ['Hello,Hello,world', '!']
    assert candidate('abcdef') == 3
    assert candidate('aaabb') == 2
    assert candidate('aaaBb') == 1
    assert candidate('') == 0

def test_check():
    check(split_words)

test_check()
