from typing import List

def f(n: int) -> List[int]:
    """ Implement the function f that takes n as a parameter,
    and returns a list of number n, such that the value of the i at index i is the factorial of integers if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    >>> f(5)
    [1, 2, 6, 24, 15]
    """
    # your code here
    factorial = 1
    for i in range(2,n+1):
        if i%2 == 0:
            factorial = factorial * i
        else:
            factorial = factorial + i
    return factorial
def check(candidate):
    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]

def test_check():
    check(f)

test_check()
