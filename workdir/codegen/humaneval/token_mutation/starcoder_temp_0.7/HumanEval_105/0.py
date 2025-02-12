from typing import List

def by_length(arr: List[int]) -> List[str]:
    """
    Given an array of integers, sort the numbers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each number by its corresponding number from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    
      If the array is empty, return an empty array:
    >>> by_length([])
    []
    
      If the array has any strange number ignore it:
    >>> by_length([1, -1, 55])
    ['One']
    """
    if len(arr) == 0:
        return []
    else:
        array = []
        for num in arr:
            if 1 <= num <= 9:
                array.append(str(num))
        array = sorted(array, reverse=True)
        new_array = []
        for num in array:
            if num == "1":
                new_array.append("One")
            elif num == "2":
                new_array.append("Two")
            elif num == "3":
                new_array.append("Three")
            elif num == "4":
                new_array.append("Four")
            elif num == "5":
                new_array.append("Five")
            elif num == "6":
                new_array.append("Six")
            elif num == "7":
                new_array.append("Seven")
            elif num == "8":
                new_array.append("Eight")
            elif num == "9":
                new_array.append("Nine")
        return new_array

def check(candidate):
    assert candidate([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    assert candidate([]) == []
    assert candidate([1, -1, 55]) == ['One']
    assert candidate([1, -1, 3, 2]) == ['Three', 'Two', 'One']
    assert candidate([9, 4, 8]) == ['Nine', 'Eight', 'Four']

def test_check():
    check(by_length)

test_check()
