def update_hints(obj, data):
    """Update the , on the root-node of a workflow. Usually, schedule
    hints are fixed per function. Sometimes a user may want to set hints
    manually on a specific promised object. :func:`update_hints` uses the
    `update` method on the hints hints with `data` as its argument.

    :param obj: a :py:class:`PromisedObject`.
    :param data: a :py:class:`dict` containing additional hints.

    The hints are modified, in place, on the node. All workflows that contain
    the node are affected."""
    update_hints_raw(obj, data)

