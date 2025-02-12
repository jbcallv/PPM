from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    """
    There are eight planets in our solar system: the closerst to the orbits 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose sun are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the distance to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    >>> bf('Jupiter', 'Neptune')
    ('Saturn', 'Uranus')
    >>> bf('Earth', 'Mercury')
    'Venus'
    >>> bf('Mercury', 'Uranus')
    ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
    """
    return ()

def check(candidate):
    assert candidate('Jupiter', 'Neptune') == ('Saturn', 'Uranus')
    assert candidate('Earth', 'Mercury') == ('Venus',)
    assert candidate('Mercury', 'Uranus') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
    assert candidate('Neptune', 'Venus') == ('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
    assert candidate('Earth', 'Earth') == ()
    assert candidate('Mars', 'Earth') == ()
    assert candidate('Jupiter', 'Makemake') == ()

def test_check():
    check(bf)

test_check()
