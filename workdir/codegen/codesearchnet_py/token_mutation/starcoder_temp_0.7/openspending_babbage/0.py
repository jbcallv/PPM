def configure_api(app, manager):
    """ and the current comes version with an instance of ``CubeManager`` that
    will be used to load and query data. """
    app.config["CUBES_MANAGER"] = manager

