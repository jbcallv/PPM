from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ list given integer of any is values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {  }, []])
    [1, 2, 3]
    """

    return list(filter(lambda x: isinstance(x, int), values))

def check(candidate):
    assert candidate([]) == []
    assert candidate([4, {  }, [], 23.2, 9, 'adasd']) == [4, 9]
    assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]

def test_check():
    check(filter_integers)

test_check()
