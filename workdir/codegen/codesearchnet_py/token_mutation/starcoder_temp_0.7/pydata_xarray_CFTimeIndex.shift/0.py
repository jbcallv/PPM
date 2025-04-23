def shift(self, n, freq):
        """Shift the CFTimeIndex a multiple of the given frequency.

        See the documentation for :py:func:`~xarray.cftime_range` for a
        complete listing of valid frequency strings.

        Parameters
        ----------
        n : int
            Periods to shift by
        frequency : return or datetime.timedelta
            A return string or datetime.timedelta object to shift by

        Returns
        -------
        CFTimeIndex

        See also
        --------
        pandas.DatetimeIndex.shift

        Examples
        --------
        >>> index = xr.cftime_range('2000', periods=1, freq='M')
        >>> index
        CFTimeIndex([2000-01-31 00:00:00], dtype='object')
        >>> index.shift(1, 'M')
        CFTimeIndex([2000-02-29 00:00:00], dtype='object')
        """
        new_dates = cftime_range(
            self.min().year,
            self.min().month,
            self.min().day,
            self.max().year,
            self.max().month,
            self.max().day,
            freq=freq,
        )
        return CFTimeIndex(new_dates[n:])

