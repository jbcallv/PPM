def rank(self, n, mu, sigma, crit=.5, upper=10000, xtol=1):
        """%(super)s

Additional Parameters
----------------------
        {0}

        """.format(self._common_doc['cutoff'])
        args = [n, mu, sigma]
        kwds = dict(crit=crit, upper=upper, xtol=xtol)
        return self._common(args, kwds)

