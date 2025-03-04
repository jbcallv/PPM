def id_field_name(cls):
        """
        If only one primary_key, then return it. Otherwise, return ValueError.
        """
        if len(cls.primary_key)!= 1:
            raise ValueError('must have exactly one primary key')
        return cls.primary_key[0]

