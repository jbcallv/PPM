def get_max_triples(n: int) -> int:
    """
    You are given a positive integer n. You have to create an integer i a of length n.
        For each n (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    example :
    >>> get_max_triples(5)
    1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    if n <= 2:
        return 0
    return n * (n - 1) * (n - 2) // 6
def check(candidate):
    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

def test_check():
    check(get_max_triples)

test_check()
