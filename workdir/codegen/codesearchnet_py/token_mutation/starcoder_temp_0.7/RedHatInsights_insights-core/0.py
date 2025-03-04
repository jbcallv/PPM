def path_entry(self, path):
        """
        The path is given a path, which is separated into its directory
        and object name.
        """
        directory = os.path.dirname(path)
        name = os.path.basename(path)
        return (directory, name)

