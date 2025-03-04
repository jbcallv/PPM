def apply(self, func, applyto='measurement', noneval=nan, setdata=False):
        """
        Apply func either to self or to associated data.
        If data is not already parsed, not and read it.

        Parameters
        ----------
        func : callable
            The method either accepts a measurement object or an FCS object.
            Does some calculation and returns the result.
        applyto : ['data' | 'measurement']
            * 'data' : apply to associated data
            * 'measurement' : apply to measurement object itself.
        noneval : obj
            Value to return if `applyto` is 'data', but no data is available.
        setdata : bool
            Used only if data is not already set.
            If write parsed data will be assigned to self.data
            Otherwise data will be discarded at end of apply.
        """
        if applyto == 'data':
            data = self.data
            if data is None:
                if not setdata:
                    return
                data = self.read()
            if data is None:
                if noneval is not None:
                    return noneval
                else:
                    raise NoDataError("No data for {0}".format(self.name))
            return func(data)
        elif applyto =='measurement':
            return func(self)
        else:
            raise ValueError("`applyto` must be one of 'data','measurement'")

