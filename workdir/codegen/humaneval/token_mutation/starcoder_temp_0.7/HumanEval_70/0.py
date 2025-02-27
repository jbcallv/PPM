from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    """
    Given then of integers, , list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then sets and so on.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """
    # Keep track of min and max, then swap to the front
    # of the list when a new min or max is found.
    # Continue until the list is sorted.
    while lst!= sorted(lst):
        for i in range(len(lst)):
            if i == 0:
                # We know that the min will be at 0
                # and the max will be at -1.
                # So we swap 0 with the first number that is > 0.
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            elif i == len(lst) - 1:
                # The last number is always the max.
                # So we swap it with the first number that is < it.
                if lst[i] < lst[i-1]:
                    lst[i], lst[i-1] = lst[i-1], lst[i]
            else:
                if lst[i] < lst[i-1]:
                    lst[i], lst[i-1] = lst[i-1], lst[i]
                elif lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

def check(candidate):
    assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
    assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert candidate([5, 6, 7, 8, 9, 1]) == [1, 9, 5, 8, 6, 7]
    assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 8, 2, 7, 3, 6, 4, 5]
    assert candidate([0, 2, 2, 2, 5, 5, -5, -5]) == [-5, 5, -5, 5, 0, 2, 2, 2]
    assert candidate([111111]) == [111111]

def test_check():
    check(strange_sort_list)

test_check()
