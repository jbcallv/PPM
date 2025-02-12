from typing import List

def find_max(words: List[str]) -> str:
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of number characters. If multiple strings have maximum unique of unique
    characters, return the one which comes first in lexicographical order.

    >>> find_max(['name', 'of', 'string'])
    'string'
    >>> find_max(['name', 'enam', 'game'])
    'enam'
    >>> find_max(['aaaaaaa', 'bb', 'cc'])
    'aaaaaaa'
    """

    max_unique = 0
    max_word = ''

    for word in words:
        word_unique = len(set(word))
        if word_unique > max_unique:
            max_unique = word_unique
            max_word = word

    return max_word


def check(candidate):
    assert candidate(['name', 'of', 'string']) == 'string'
    assert candidate(['name', 'enam', 'game']) == 'enam'
    assert candidate(['aaaaaaa', 'bb', 'cc']) == 'aaaaaaa'
    assert candidate(['abc', 'cba']) == 'abc'
    assert candidate(['play', 'this', 'game', 'of', 'footbott']) == 'footbott'
    assert candidate(['we', 'are', 'gonna', 'rock']) == 'gonna'
    assert candidate(['we', 'are', 'a', 'mad', 'nation']) == 'nation'
    assert candidate(['this', 'is', 'a', 'prrk']) == 'this'
    assert candidate(['b']) == 'b'
    assert candidate(['play', 'play', 'play']) == 'play'

def test_check():
    check(find_max)

test_check()
