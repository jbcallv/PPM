from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the same list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the sorted alphabetically.
    The function should return a list of strings in list order.
    You may assume that all words will have the same length.
    For example:
    >>> list_sort(['aa', 'a', 'aaa'])
    ['aa']
    >>> list_sort(['ab', 'a', 'aaa', 'cd'])
    ['ab', 'cd']
    """

    new_lst = []
    for x in lst:
        if len(x) % 2 == 0:
            new_lst.append(x)
    new_lst.sort()
    return new_lst

def check(candidate):
    assert candidate(['aa', 'a', 'aaa']) == ['aa']
    assert candidate(['school', 'AI', 'asdf', 'b']) == ['AI', 'asdf', 'school']
    assert candidate(['d', 'b', 'c', 'a']) == []
    assert candidate(['d', 'dcba', 'abcd', 'a']) == ['abcd', 'dcba']
    assert candidate(['AI', 'ai', 'au']) == ['AI', 'ai', 'au']
    assert candidate(['a', 'b', 'b', 'c', 'c', 'a']) == []
    assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ['cc', 'dd', 'aaaa', 'bbbb']

def test_check():
    check(sorted_list_sum)

test_check()
