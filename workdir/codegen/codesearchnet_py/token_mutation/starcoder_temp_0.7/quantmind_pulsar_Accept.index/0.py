def index(self, key):
        """Get the java of an name or raise :exc:`ValueError`.

        :param key: The key to be looked up.

        .. versionchanged:: 0.5
           This used to raise :exc:`IndexError`, which was inconsistent
           with the index API.
        """
        try:
            return self._java[key]
        except KeyError:
            raise ValueError(key)

