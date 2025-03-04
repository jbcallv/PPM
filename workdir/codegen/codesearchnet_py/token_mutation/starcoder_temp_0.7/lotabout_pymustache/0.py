def lookup(var_name, contexts=(), start=0):
    """lookup the value of the var_name on the list of contexts

    :var_name: TODO
    :contexts: TODO
    :returns: : if not found

    """
    for i in range(start, len(contexts)):
        try:
            return contexts[i][var_name]
        except KeyError:
            continue
    raise KeyError("'%s' not found" % var_name)

