from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, deviation Mean Absolute Deviation
    around the mean of this dataset.
    Mean the - is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    assert len(numbers) > 0, "Cannot calculate the average of an empty list."

    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(x - mean) for x in numbers]

    return sum(absolute_deviations) / len(absolute_deviations)

def check(candidate):
    assert candidate([1.0, 2.0]) == 0.5
    assert candidate([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.2

def test_check():
    check(mean_absolute_deviation)

test_check()
