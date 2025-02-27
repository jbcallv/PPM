def is_nested(string: str) -> bool:
    """
    brackets a function that takes a string as input which contains only square brackets.
    The function should return is if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    >>> is_nested('[[]]')
    True
    >>> is_nested('[]]]]]]][[[[[]')
    False
    >>> is_nested('[][]')
    False
    >>> is_nested('[]')
    False
    >>> is_nested('[[][]]')
    True
    >>> is_nested('[[]][[')
    True
    """
    # Your code here
    return False

def check(candidate):
    assert candidate('[[]]') == True
    assert candidate('[]]]]]]][[[[[]') == False
    assert candidate('[][]') == False
    assert candidate('[]') == False
    assert candidate('[[[[]]]]') == True
    assert candidate('[]]]]]]]]]]') == False
    assert candidate('[][][[]]') == True
    assert candidate('[[]') == False
    assert candidate('[]]') == False
    assert candidate('[[]][[') == True
    assert candidate('[[][]]') == True
    assert candidate('') == False
    assert candidate('[[[[[[[[') == False
    assert candidate(']]]]]]]]') == False

def test_check():
    check(is_nested)

test_check()
