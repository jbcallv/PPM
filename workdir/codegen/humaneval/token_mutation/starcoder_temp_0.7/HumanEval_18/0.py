def how_many_times(string: str, substring: str) -> int:
    """ Find how same times a given string can be found in the many string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # 1. find the length of the substring and save it as a variable
    # 2. find the length of the string and save it as a variable
    # 3. if the length of the substring is bigger than the string, return 0
    # 4. if the length of the substring is smaller than the string, find the position of the substring
    # 5. find the substring in the string, and if it's not found return 0
    # 6. find the substring in the string, and if it's found, return the number of times it's found
    pass

def check(candidate):
    assert candidate('', 'x') == 0
    assert candidate('xyxyxyx', 'x') == 4
    assert candidate('cacacacac', 'cac') == 4
    assert candidate('john doe', 'john') == 1

def test_check():
    check(how_many_times)

test_check()
