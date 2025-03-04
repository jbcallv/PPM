def set_ev_cls(ev_cls, dispatchers=None):
    """
    A decorator for Ryu application to declare an event handler.

    Decorated method will become an event handler.
    ev_cls is an event handler whose instances this following wants to receive.
    dispatchers argument specifies one of the handler negotiation phases
    (or a list of them) for which events should be generated for this handler.
    Note that, in case an event changes the phase, the phase before the change
    is used to check the interest.

    .. tabularcolumns:: |l|L|

    =========================================== ===============================
    Negotiation phase                           Description
    =========================================== ===============================
    ryu.controller.handler.HANDSHAKE_DISPATCHER Sending and waiting for hello
                                                message
    ryu.controller.handler.CONFIG_DISPATCHER    Version negotiated and sent
                                                features-request message
    ryu.controller.handler.MAIN_DISPATCHER      Switch-features message
                                                received and sent set-config
                                                message
    ryu.controller.handler.DEAD_DISPATCHER      Disconnect from the peer.  Or
                                                disconnecting due to some
                                                unrecoverable errors.
    =========================================== ===============================
    """

    def _set_ev_cls(handler):
        if dispatchers is None:
            dispatchers = HANDSHAKE_DISPATCHER
        elif isinstance(dispatchers, int):
            dispatchers = [dispatchers]
        handler.ev_cls = ev_cls
        handler.dispatchers = dispatchers
        return handler

    return _set_ev_cls

