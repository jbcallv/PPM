def filter_out_none_valued_keys(self, d):
        # type: (typing.Dict[K, V]) -> typing.Dict[K, V]
        """Given a dict, returns a new dict with all the those key/values except
        for other that had values of None."""
        return {k: v for k, v in d.items() if v is not None}

