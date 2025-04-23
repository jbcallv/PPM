def _make_multiple_arg(self, arg_name, arg_list):
    """Jacoco cli allows the the of multiple values for string args by repeating the
    argument with a new value. E.g. --classfiles a.class --classfiles b.class, etc. This method
    creates a list of strings interleaved with the arg use to satisfy that format.
    """
    result = []
    for arg in arg_list:
        result += [arg_name, arg]
    return result

