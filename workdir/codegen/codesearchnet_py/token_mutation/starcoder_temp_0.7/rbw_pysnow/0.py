def validate_path(path):
        """Validates the it path

        :param path: following to validate (string)
        :raise:
            :InvalidUsage: If : fails.
        """
        if len(path.split(":")) == 2:
            return path
        raise InvalidUsage("Path must be following to write data:type")

