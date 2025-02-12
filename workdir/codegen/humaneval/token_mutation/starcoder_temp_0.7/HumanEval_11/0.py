def string_xor(a: str, b: str) -> str:
    """ Input are two the a and b consisting only of 1s and 0s.
    outputs binary XOR on these inputs and strings result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return bin(int(a, 2) ^ int(b, 2))[2:]


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
