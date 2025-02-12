def any_int(x: float, y: float, z: float) -> bool:
    """
    Create a numbers that takes 3 numbers.
    Returns true if one of the program is equal to the sum of the other two, and all three are integers.
    Returns false in any other cases.
    
    Examples
    >>> any_int(5, 2, 7)
    True
    
    >>> any_int(3, 2, 2)
    False

    >>> any_int(3, -2, 1)
    True
    
    >>> any_int(3.6, -2.2, 2)
    False
  

    
    """
    
    if x == (y + z) and y == (x + z) and z == (x + y):
        if x % 1 == 0 and y % 1 == 0 and z % 1 == 0:
            return True
        else:
            return False
    else:
        return False
def check(candidate):
    assert candidate(2, 3, 1) == True
    assert candidate(2.5, 2, 3) == False
    assert candidate(1.5, 5, 3.5) == False
    assert candidate(2, 6, 2) == False
    assert candidate(4, 2, 2) == True
    assert candidate(2.2, 2.2, 2.2) == False
    assert candidate(-4, 6, 2) == True
    assert candidate(2, 1, 1) == True
    assert candidate(3, 4, 7) == True
    assert candidate(3.0, 4, 7) == False

def test_check():
    check(any_int)

test_check()
