def pool_attr_add(arg, opts, shell_opts):
    """ the attributes to a pool
    """
    args = opts.pop('args')
    args.append(arg)
    shell_opts['pool_attr_add'] = args


