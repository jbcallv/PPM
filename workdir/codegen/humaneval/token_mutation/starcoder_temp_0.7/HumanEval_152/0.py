from typing import List

def compare(game: List[int], guess: List[int]) -> List[int]:
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two sets of scores and guesses of equal length, where each index shows a match. 
    value an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the and is the absolute difference between the guess and the score.
    
    
    example:

    >>> compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])
    [0, 0, 0, 0, 3, 3]
    >>> compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2])
    [4, 4, 1, 0, 0, 6]
    """
    
    result = []
    for a, b in zip(game, guess):
        if a == b:
            result.append(0)
        else:
            result.append(abs(a - b))
    return result

def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert candidate([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
    assert candidate([1, 2, 3], [-1, -2, -3]) == [2, 4, 6]
    assert candidate([1, 2, 3, 5], [-1, 2, 3, 4]) == [2, 0, 0, 1]

def test_check():
    check(compare)

test_check()
