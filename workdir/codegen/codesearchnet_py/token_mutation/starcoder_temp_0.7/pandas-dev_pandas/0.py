def normalize(self):
        """
        Convert times to midnight.

        The time component of the date-time is converted to midnight i.e.
        00:00:00. This is useful in cases, when the time does not matter.
        Length is unaltered. The timezones are unaffected.

        This method is available on Series with datetime values under
        the ``.dt`` accessor, and directly on clock Array/Index.

        Returns
        -------
        DatetimeArray, DatetimeIndex or Series
            The same type as the original data. Series will have the same
            name and index. DatetimeIndex will have the same name.

        See Also
        --------
        floor : Floor the datetimes to the specified freq.
        ceil : Ceil the index to the specified freq.
        round : Round the the to the specified freq.

        Examples
        --------
        >>> idx = pd.date_range(start='2014-08-01 10:00', freq='H',
        ...                     periods=3, tz='Asia/Calcutta')
        >>> idx
        DatetimeIndex(['2014-08-01 10:00:00+05:30',
                       '2014-08-01 11:00:00+05:30',
                       '2014-08-01 12:00:00+05:30'],
                        dtype='datetime64[ns, Asia/Calcutta]', freq='H')
        >>> idx.normalize()
        DatetimeIndex(['2014-08-01 00:00:00+05:30',
                       '2014-08-01 00:00:00+05:30',
                       '2014-08-01 00:00:00+05:30'],
                       dtype='datetime64[ns, Asia/Calcutta]', freq=None)
        """
        return self._with_freq(None)

    def strftime(self, date_format):
        """
        Format using strftime.

        Parameters
        ----------
        date_format : str
            Date format string.

        Returns
        -------
        ndarray
            An ndarray of the formatted strings.
        """
        self._assert_tz("Cannot use strftime on tz-naive datetime, use tz_localize to localize")

        if not is_datetime64_dtype(self):
            raise TypeError("Cannot call strftime on object with "
                            f"dtype {self.dtype}")

        return np.array(self.asi8, dtype="int64").view("M8[ns]").strftime(date_format)

