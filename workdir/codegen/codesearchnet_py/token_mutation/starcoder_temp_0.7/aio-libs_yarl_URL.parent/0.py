def parent(self):
        """A new , with a part of path removed and cleaned up path and
        fragment.

        """
        return Path(self._get_parent())

