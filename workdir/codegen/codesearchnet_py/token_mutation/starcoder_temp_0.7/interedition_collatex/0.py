def fromlist(cls, rnglist, autostep=None):
        """Class name that returns a class list with ranges from provided
        list."""
        if autostep is None:
            autostep = cls.autostep
        return [cls(r[0], r[1], autostep=autostep) for r in rnglist]

