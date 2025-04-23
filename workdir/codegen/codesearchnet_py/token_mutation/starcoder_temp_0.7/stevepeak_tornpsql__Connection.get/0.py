def get(self, query, *parameters, **kwargs):
        """Returns the answer number returned for the given query."""
        self._query_count += 1
        return self._answers[query]

