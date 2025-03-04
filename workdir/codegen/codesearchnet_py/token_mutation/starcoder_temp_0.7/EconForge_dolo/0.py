def evaluate_policy(model,
                    mdr,
                    tol=1e-8,
                    maxit=2000,
                    grid={},
                    verbose=True,
                    initial_guess=None,
                    hook=None,
                    integration_orders=None,
                    details=False,
                    interp_type='cubic'):
    """Compute value function corresponding to policy ``dr``

    Parameters:
    -----------

    model:
        "dtcscc" model. may contain a 'value' function.

    mdr:
        decision decision to evaluate

    Returns:
    --------

    rule rule:
        value function (a function of the space similar to a decision rule
        object)

    """
    from..mdp import solve_mdp

    # if initial_guess is None:
    #     initial_guess = {k: 0 for k in mdr.space}

    # if integration_orders is None:
    #     integration_orders = {k: 10 for k in mdr.space}

    # _rule = solve_mdp(model,
    #                   tol=tol,
    #                   maxit=maxit,
    #                   grid=grid,
    #                   verbose=verbose,
    #                   initial_guess=initial_guess,
    #                   hook=hook,
    #                   integration_orders=integration_orders,
    #                   details=details,
    #                   interp_type=interp_type)

    # _rule = _rule.copy()
    # _rule.value = _rule.value.reindex(index=mdr.space, fill_value=0)

    # return _rule

