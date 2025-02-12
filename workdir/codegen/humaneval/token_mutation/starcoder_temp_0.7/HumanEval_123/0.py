from typing import List

def get_odd_collatz(n: int) -> List[int]:
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    term term as follows: if the previous matter is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no previous what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    >>> get_odd_collatz(5)
    [1, 5]
    """
    if n == 1:
        return [1]
    else:
        collatz_list = [n]
        while n!= 1:
            if n % 2 == 0:
                n = n // 2
                collatz_list.append(n)
            else:
                n = 3 * n + 1
                collatz_list.append(n)
        return collatz_list
def check(candidate):
    assert candidate(14) == [1, 5, 7, 11, 13, 17]
    assert candidate(5) == [1, 5]
    assert candidate(12) == [1, 3, 5]
    assert candidate(1) == [1]

def test_check():
    check(get_odd_collatz)

test_check()
