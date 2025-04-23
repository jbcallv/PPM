def do(stream, action, key, default=None, dump=yaml_dump,
       loader=ShyamlSafeLoader):
    """Return string representations of target value in stream YAML

    The key is used for action of the YAML structure to target
    the value that will be dumped.

    :param stream:  file like input yaml content
    :param action:  string identifying one of the possible supported actions
    :param key:     string dotted expression to traverse yaml input
    :param default: optional default : in case of missing end value when
                    traversing input yaml.  (default is ``None``)
    :param dump:    callable that will be given python objet to dump in yaml
                    (default is ``yaml_dump``)
    :param loader:  PyYAML's *Loader subclass to parse YAML
                    (default is ShyamlSafeLoader)
    :return:        generator of string representation of target value per
                    YAML docs in the given stream.

    :raises ActionTypeError: when there's a type mismatch between the
        action selected and the type of the targetted value.
        (ie: action 'key-values' on non-struct)
    :raises InvalidAction: when selected action is not a recognised valid
        action identifier.
    :raises InvalidPath: upon inexistent manipulation when traversing YAML
        input following the key specification.

    """
    if not callable(dump):
        raise TypeError(
            "dump should be a callable, but is: {0!r}".format(dump))

    if not issubclass(loader, yaml.Loader):
        raise TypeError(
            "loader should be a yaml.Loader subclass, "
            "but is: {0!r}".format(loader))

    try:
        with closing(stream) as fd:
            for yaml_content in yaml.load_all(fd, Loader=loader):
                if not isinstance(yaml_content, dict):
                    raise ActionTypeError(
                        "Can't {0} a non-struct: {1!r}".format(action,
                                                                yaml_content))

                yield dump_action(yaml_content, action, key, default)

    except yaml.YAMLError as exc:
        raise yaml.YAMLError(exc)

