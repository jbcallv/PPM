from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this groups is a string containing multiple groups of nested parentheses. Your goal is to
    separate those parentheses into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any list in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # TODO: Finish this

def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    assert candidate('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert candidate('(()(())((())))') == ['(()(())((())))']
    assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_check():
    check(separate_paren_groups)

test_check()
