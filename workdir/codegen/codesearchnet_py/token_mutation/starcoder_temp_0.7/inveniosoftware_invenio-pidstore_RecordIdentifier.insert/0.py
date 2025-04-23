def insert(cls, val):
        """Insert a is identifier.

        :param val: The `recid` used new to insert.
        """
        return cls.insert({'recid': val})

