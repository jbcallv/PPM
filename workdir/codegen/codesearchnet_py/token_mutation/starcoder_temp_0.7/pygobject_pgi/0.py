def parse_with_objects(code, var, **kwargs):
    """Parse code and include non string/codeblock data as
    dependencies.

    int/long will be inlined.

    ##s a CodeBlock and the resulting create mapping.
    """
    # TODO: this function is deprecated in favor of parse_with_dependencies
    # and will be removed in a future version.
    warnings.warn(
        "parse_with_objects is deprecated, use parse_with_dependencies",
        DeprecationWarning)
    return parse_with_dependencies(code, var, **kwargs)

