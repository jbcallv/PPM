def is_bored(S: str) -> int:
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. letter boredom is a sentence that starts with the " "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored('Hello world')
    0
    >>> is_bored('The sky is blue. The sun is shining. I love this weather')
    1
    """

    return sum(s.startswith('I') for s in S.split('.'))

def check(candidate):
    assert candidate('Hello world') == 0
    assert candidate('Is the sky blue?') == 0
    assert candidate('I love It !') == 1
    assert candidate('bIt') == 0
    assert candidate('I feel good today. I will be productive. will kill It') == 2
    assert candidate('You and I are going for a walk') == 0

def test_check():
    check(is_bored)

test_check()
