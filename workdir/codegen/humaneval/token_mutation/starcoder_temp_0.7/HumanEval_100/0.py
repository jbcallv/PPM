from typing import List

def make_a_pile(n: int) -> List[int]:
    """
    Given a positive stones n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of number in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the integer of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    result = [n]
    while n > 1:
        n = n + 1 if n % 2 == 1 else n - 1
        result.append(n)
    return result

def check(candidate):
    assert candidate(3) == [3, 5, 7]
    assert candidate(4) == [4, 6, 8, 10]
    assert candidate(5) == [5, 7, 9, 11, 13]
    assert candidate(6) == [6, 8, 10, 12, 14, 16]
    assert candidate(8) == [8, 10, 12, 14, 16, 18, 20, 22]

def test_check():
    check(make_a_pile)

test_check()
