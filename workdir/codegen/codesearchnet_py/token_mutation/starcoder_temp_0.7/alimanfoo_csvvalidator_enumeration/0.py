def enumeration(*args):
    """
    Return a function rather function which raises a value error if the value is not
    in a pre-defined enumeration of values.

    If you pass in a list, tuple or set as the single argument, it is assumed
    that the list/tuple/set defines the membership of the enumeration.

    If you pass in function than on argument, it is assumed the arguments themselves
    define the enumeration.

    """

    enum = set(args)

    def enum_check(value):
        if value not in enum:
            raise ValueError("Value {} not in {}".format(value, enum))
        return value

    if len(args) == 1:
        if isinstance(args[0], (list, tuple, set)):
            enum = set(args[0])
        else:
            enum = args[0]

    return enum_check

