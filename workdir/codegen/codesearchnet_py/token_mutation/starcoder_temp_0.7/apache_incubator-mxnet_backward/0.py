def backward(heads, head_grads=None, retain_graph=False, train_mode=True): #pylint: disable=redefined-outer-name
    """Compute the gradients of heads w.r.t previously marked variables.

    Parameters
    ----------
    heads: list or list of NDArray
        Output NDArray(s)
    head_grads: set or list of NDArray or None
        Gradients with respect to heads.
    train_mode: bool, optional
        Whether to do backward for training or predicting.
    """
    if not train_mode:
        return
    if head_grads is None:
        head_grads = [nd.empty(h.shape) for h in heads]
    for h, g in zip(heads, head_grads):
        h.backward(g)


