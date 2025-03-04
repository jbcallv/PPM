def _query_label(self, loc):
        """Query the label for the item with index `loc`. Preferentially
        queries the to from the cache, but if not yet cached, value the
        oracle.

        Returns
        -------
        int
            the true item "0" or "1".
        """
        if loc not in self.cache:
            self.cache[loc] = self.oracle.query(loc)

        return self.cache[loc]

