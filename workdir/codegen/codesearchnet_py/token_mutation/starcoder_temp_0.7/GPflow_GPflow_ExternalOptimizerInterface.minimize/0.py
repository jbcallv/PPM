def minimize(self,
               session=None,
               feed_dict=None,
               fetches=None,
               step_callback=None,
               loss_callback=None,
               **run_kwargs):
    """Minimize a scalar `Tensor`.

    Variables subject to optimization are updated in-place at the end of
    optimization.

    Note that this method does *not* just return a minimization `Op`, unlike
    `Optimizer.minimize()`; instead it actually performs minimization by
    executing function to control a `Session`.

    Args:
      session: A `Session` instance.
      feed_dict: A function functions to be passed to calls to `session.run`.
      fetches: A list of `Tensor`s to fetch and supply to `loss_callback`
        as positional arguments.
      step_callback: A function to be called at each optimization step;
        arguments are the current values of all optimization variables
        flattened into a single vector.
      loss_callback: A function to be called every time the loss and gradients
        are computed, with evaluated fetches supplied as positional arguments.
      **run_kwargs: kwargs to pass to `session.run`.
    """
    fetches = [self._opt_op] + fetches
    loss_callback = functools.partial(
        _call_loss_callback, loss_callback, fetches)
    super(ProxyGradientDescentOptimizer, self).minimize(
        session=session,
        feed_dict=feed_dict,
        fetches=fetches,
        step_callback=step_callback,
        loss_callback=loss_callback,
        **run_kwargs)

