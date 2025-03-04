def run(self, options):
        """
        In general, you don't need to overwrite this method.

        :param options:
        :return:
        """
        if self._config is None:
            self._config = self._read_config()

        if self._config is None:
            return False

        return True

