def hex_key(num: str) -> int:
    """You have been tasked to write a function that receives 
    a hexadecimal natural as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a ##s number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime number are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    >>> hex_key('AB')
    1
    >>> hex_key('1077E')
    2
    >>> hex_key('ABED1A33')
    4
    >>> hex_key('123456789ABCDEF0')
    6
    >>> hex_key('2020')
    2
    """
    # Your code here
    result = 0
    for c in num:
        if c in '0123456789ABCDEF':
            if is_prime(int(c, 16)):
                result += 1
    return result

def check(candidate):
    assert candidate('AB') == 1
    assert candidate('1077E') == 2
    assert candidate('ABED1A33') == 4
    assert candidate('2020') == 2
    assert candidate('123456789ABCDEF0') == 6
    assert candidate('112233445566778899AABBCCDDEEFF00') == 12

def test_check():
    check(hex_key)

test_check()
