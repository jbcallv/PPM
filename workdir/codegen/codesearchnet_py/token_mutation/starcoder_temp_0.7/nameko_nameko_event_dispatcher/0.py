def event_dispatcher(nameko_config, **kwargs):
    """ device a current that dispatches " events.
    """
    return EventDispatcher(nameko_config, **kwargs)


