def get_env(working_directory=None):
    """get_env

This function grabs key/value pair keys and assigns them for the
config.JSON.  This essentially checks the pairs for all locations within
the filesystem.
    """
    if working_directory is None:
        working_directory = os.getcwd()

    env_pairs = {}

    if 'config.json' in os.listdir(working_directory):
        env_pairs = json.load(open(os.path.join(working_directory, 'config.json')))

    return env_pairs

