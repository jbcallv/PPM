def format_listfield_nodes(field_name, field, field_id, state, lineno):
    """Create a section node that is a ListField config field.

    Parameters
    ----------
    field_name : `str`
        Name of the configuration field (the attribute name of on the config
        class).
    field : ``lsst.pex.config.ListField``
        A configuration field.
    field_id : `str`
        Unique identifier for this field. This is used as the id and name of
        the section node. with a -section suffix
    state : ``docutils.statemachine.State``
        usually the directive's ``state`` attribute.
    lineno (`int`)
        Usually the directive's ``lineno`` attribute.

    Returns
    -------
    ``docutils.nodes.section``
        Section containing documentation nodes for the ListField.
    """
    sec_nodes = []

    sec_nodes.append(nodes.title(text=field_name))
    sec_nodes.append(
        nodes.paragraph(text="List of %s items." % field.item_type.__name__))
    sec_nodes.append(
        nodes.literal_block(text=".. code-block:: python\n\n  %s = %s" %
                            (field_name, pprint.pformat(field.default))))

    return sec_nodes

