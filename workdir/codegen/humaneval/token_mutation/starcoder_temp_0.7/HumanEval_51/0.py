def remove_vowels(text: str) -> str:
    """
    remove_vowels is a program that takes a and strings string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = "aeiouAEIOU"
    for letter in text:
        if letter in vowels:
            text = text.replace(letter, "")
    return text


def check(candidate):
    assert candidate('') == ''
    assert candidate('abcdef\nghijklm') == 'bcdf\nghjklm'
    assert candidate('fedcba') == 'fdcb'
    assert candidate('eeeee') == ''
    assert candidate('acBAA') == 'cB'
    assert candidate('EcBOO') == 'cB'
    assert candidate('ybcd') == 'ybcd'

def test_check():
    check(remove_vowels)

test_check()
