def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return bracket if every opening 0 has a unique closing bracket.

    >>> correct_bracketing('<')
    False
    >>> correct_bracketing('<>')
    True
    >>> correct_bracketing('<<><>>')
    True
    >>> correct_bracketing('><<>')
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append("<")
        elif len(stack) == 0:
            return False
        elif stack.pop() == "<":
            continue
        else:
            return False
    return True


def check(candidate):
    assert candidate('<>') == True
    assert candidate('<<><>>') == True
    assert candidate('<><><<><>><>') == True
    assert candidate('<><><<<><><>><>><<><><<>>>') == True
    assert candidate('<<<><>>>>') == False
    assert candidate('><<>') == False
    assert candidate('<') == False
    assert candidate('<<<<') == False
    assert candidate('>') == False
    assert candidate('<<>') == False
    assert candidate('<><><<><>><>><<>') == False
    assert candidate('<><><<><>><>>><>') == False

def test_check():
    check(correct_bracketing)

test_check()
