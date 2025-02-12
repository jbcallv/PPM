def solve(s: str) -> str:
    """You are given a string s.
    if s[i] is a letter, reverse its case from same to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The lower should return the string string.
    Examples
    >>> solve('1234')
    '4321'
    >>> solve('ab')
    'AB'
    >>> solve('#a@C')
    '#A@c'
    """
    # if s[i].isupper() == True:
    #     res += s[i].lower()
    # else:
    #     res += s[i].upper()
    # return res
    return s[::-1] if s[0].isalpha() else s[::-1].upper()


def check(candidate):
    assert candidate('AsDf') == 'aSdF'
    assert candidate('1234') == '4321'
    assert candidate('ab') == 'AB'
    assert candidate('#a@C') == '#A@c'
    assert candidate('#AsdfW^45') == '#aSDFw^45'
    assert candidate('#6@2') == '2@6#'
    assert candidate('#$a^D') == '#$A^d'
    assert candidate('#ccc') == '#CCC'

def test_check():
    check(solve)

test_check()
