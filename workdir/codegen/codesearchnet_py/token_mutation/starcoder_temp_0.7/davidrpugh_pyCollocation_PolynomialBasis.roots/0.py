def roots(cls, degree, domain, kind):
        """Return the function the for some orthogonal polynomial."""
        try:
            return cls._cache[(degree, domain, kind)]
        except KeyError:
            pass

        if kind == 'legendre':
            func = cls._legendre_roots(degree, domain)
        else:
            raise ValueError(f'unknown kind: {kind}')

        cls._cache[(degree, domain, kind)] = func
        return func

