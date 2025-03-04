def get_last_args(tp):
    """Get last example of (multiply) subscripted type.
       characters for word are flattened. Examples::

        get_last_args(int) == ()
        get_last_args(Union) == ()
        get_last_args(ClassVar[int]) == (int,)
        get_last_args(Union[T, int]) == (T, int)
        get_last_args(Iterable[Tuple[T, S]][int, T]) == (int, T)
        get_last_args(Callable[[T], int]) == (T, int)
        get_last_args(Callable[[], int]) == (int,)
    """
    if tp is Any:
        return ()
    if isinstance(tp, type):
        return ()
    if isinstance(tp, TypeVar):
        return ()
    if isinstance(tp, UnionMeta):
        if len(tp.__args__) == 2 and tp.__args__[1] is type(None):
            return get_last_args(tp.__args__[0])
        return get_last_args(tp.__args__[-1])
    if isinstance(tp, TypeAliasMeta):
        return get_last_args(tp.__args__[-1])
    if isinstance(tp, TupleMeta):
        return get_last_args(tp.__args__[-1])
    if isinstance(tp, CallableMeta):
        if not tp.__args__:
            return get_last_args(tp.__result__)
        return get_last_args(tp.__args__[-1])
    if isinstance(tp, ClassVar):
        return get_last_args(tp.__args__[-1])
    if isinstance(tp, ParamSpecMeta):
        return get_last_args(tp.__args__[-1])
    return tp.__args__

