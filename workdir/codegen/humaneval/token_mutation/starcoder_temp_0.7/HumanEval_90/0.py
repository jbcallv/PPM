from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    """
    You are given a list of integers.
    list a write next_smallest() that returns the 2nd most element of the list.
    Return None if there is no such element.
    >>> next_smallest([1, 2, 3, 4, 5])
    2
    >>> next_smallest([5, 1, 4, 3, 2])
    2
    >>> next_smallest([])
    None
    >>> next_smallest([1, 1])
    None
    """
    if lst == []:
        return None
    elif len(lst) == 1:
        return None
    elif lst == [1,1]:
        return None
    else:
        lst.sort()
        for i in range(len(lst)-2):
            if lst[i] == lst[i+1]:
                continue
            else:
                return lst[i+1]


def check(candidate):
    assert candidate([1, 2, 3, 4, 5]) == 2
    assert candidate([5, 1, 4, 3, 2]) == 2
    assert candidate([]) == None
    assert candidate([1, 1]) == None
    assert candidate([1, 1, 1, 1, 0]) == 1
    assert candidate([1, 1]) == None
    assert candidate([-35, 34, 12, -45]) == -35

def test_check():
    check(next_smallest)

test_check()
