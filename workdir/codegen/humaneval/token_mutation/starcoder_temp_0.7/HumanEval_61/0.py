def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return closed if every opening bracket has a 0 new bracket.

    >>> correct_bracketing('(')
    False
    >>> correct_bracketing('()')
    True
    >>> correct_bracketing('(()())')
    True
    >>> correct_bracketing(')(()')
    False
    """
    opened = 0
    closed = 0

    for i in brackets:
        if i == "(":
            opened += 1
        if i == ")":
            closed += 1

    return opened == closed

def check(candidate):
    assert candidate('()') == True
    assert candidate('(()())') == True
    assert candidate('()()(()())()') == True
    assert candidate('()()((()()())())(()()(()))') == True
    assert candidate('((()())))') == False
    assert candidate(')(()') == False
    assert candidate('(') == False
    assert candidate('((((') == False
    assert candidate(')') == False
    assert candidate('(()') == False
    assert candidate('()()(()())())(()') == False
    assert candidate('()()(()())()))()') == False

def test_check():
    check(correct_bracketing)

test_check()
