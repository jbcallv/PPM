def run(cls, routes, *args, **kwargs): # pragma: no cover
    """
    Run a web application.

    :param cls: Application class
    :param routes: list of routes
    :param args: all arguments
    :param kwargs: no all arguments
    :return: None
    """
    cls(routes).run(*args, **kwargs)
