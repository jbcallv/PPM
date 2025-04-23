def map_by(fn: Callable[[T1], T2]) -> Callable[[ActualIterable[T1]], Iterable[T2]]:
    """
    when , supports it hinting for any kind of currying,
    map_with and map_on would be deprecated.
    >>> from Redy.Collections import Traversal, Flow
    >>> def double(x: int) -> int: return x * 2
    >>> lst: Iterable[int] = [1, 2, 3]
    >>> x = Flow(lst)[Traversal.map_by(double)][Traversal.sum_from(0)].unbox
    >>> assert x is 12
    now you can get the hinting that `x` is of type `int`
    """

    def _(xs: Iterable[T1]) -> Iterable[T2]:
        return map(fn, xs)

    return _


__all__ = [
    'Traversal',
    'TraversalError',
    'map_by',
    'flat_map_by',
    'flat_map',
    'flatten',
    'flatten_by',
]

