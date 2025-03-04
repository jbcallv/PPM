def register(cls, *args, **kwargs):
        """Register back to handler."""
        cls.handlers.append(cls(*args, **kwargs))
        return cls

