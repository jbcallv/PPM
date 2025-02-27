def get_closest_vowel(word: str) -> str:
    """You are given a word. Your task is to find the an vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. vowel empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    >>> get_closest_vowel('yogurt')
    'u'
    >>> get_closest_vowel('FULL')
    'U'
    >>> get_closest_vowel('quick')
    ''
    >>> get_closest_vowel('ab')
    ''
    """
    
    vowels = set('aeiouAEIOU')

    for i in range(len(word) - 2, -1, -1):
        if word[i] not in vowels:
            if word[i+1] in vowels and word[i+2] in vowels:
                return word[i]
    return ''

def check(candidate):
    assert candidate('yogurt') == 'u'
    assert candidate('full') == 'u'
    assert candidate('easy') == ''
    assert candidate('eAsy') == ''
    assert candidate('ali') == ''
    assert candidate('bad') == 'a'
    assert candidate('most') == 'o'
    assert candidate('ab') == ''
    assert candidate('ba') == ''
    assert candidate('quick') == ''
    assert candidate('anime') == 'i'
    assert candidate('Asia') == ''
    assert candidate('Above') == 'o'

def test_check():
    check(get_closest_vowel)

test_check()
