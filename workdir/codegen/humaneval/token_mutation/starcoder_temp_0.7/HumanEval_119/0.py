from typing import List

def match_parens(lst: List[str]) -> str:
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two that in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    >>> match_parens(['()(', ')'])
    'Yes'
    >>> match_parens([')', ')'])
    'No'
    """
    # 这种做法是不行的，(())()这种情况是可以匹配的
    # for p in lst:
    #     if p == '(':
    #         lst.remove(')')
    #     elif p == ')':
    #         lst.remove('(')
    # if len(lst) == 0:
    #     return 'Yes'
    # return 'No'

    # 这个做法是正解，我觉得和那种做法的区别是：
    # 前一种做法是从左往右，右往左，去匹配
    # 后一种做法是从右往左，左往右，去匹配
    stack = []
    for p in lst:
        if p == '(':
            stack.append(')')
        elif len(stack) == 0 or stack.pop()!= '(':
            return 'No'
    return 'Yes'

def check(candidate):
    assert candidate(['()(', ')']) == 'Yes'
    assert candidate([')', ')']) == 'No'
    assert candidate(['(()(())', '())())']) == 'No'
    assert candidate([')())', '(()()(']) == 'Yes'
    assert candidate(['(())))', '(()())((']) == 'Yes'
    assert candidate(['()', '())']) == 'No'
    assert candidate(['(()(', '()))()']) == 'Yes'
    assert candidate(['((((', '((())']) == 'No'
    assert candidate([')(()', '(()(']) == 'No'
    assert candidate([')(', ')(']) == 'No'
    assert candidate(['(', ')']) == 'Yes'
    assert candidate([')', '(']) == 'Yes'

def test_check():
    check(match_parens)

test_check()
