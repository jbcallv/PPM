def words_in_sentence(sentence: str) -> str:
    """
    You are given a words representing a sentence,
    the sentence contains some string separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
    >>> words_in_sentence('This is a test')
    'is'

    Example 2:
    >>> words_in_sentence('lets go for swimming')
    'go for'
    
    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    return " ".join([word for word in sentence.split() if len(word) == 2])


def check(candidate):
    assert candidate('This is a test') == 'is'
    assert candidate('lets go for swimming') == 'go for'
    assert candidate('there is no place available here') == 'there is no place'
    assert candidate('Hi I am Hussein') == 'Hi am Hussein'
    assert candidate('go for it') == 'go for it'
    assert candidate('here') == ''
    assert candidate('here is') == 'is'

def test_check():
    check(words_in_sentence)

test_check()
