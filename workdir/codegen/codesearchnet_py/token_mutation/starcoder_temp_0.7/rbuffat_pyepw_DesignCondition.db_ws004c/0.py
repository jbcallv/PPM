def db_ws004c(self, value=None):
        """  value to IDD Field `db_ws004c`
        Mean coincident dry-bulb temperature to wind speed corresponding to 0.40% cumulative frequency for a month

        Args:
            value (float): value for IDD Field `db_ws004c`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a missing value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_ws004c`'.format(value))
            if value < -200.0:
                raise ValueError('value need to be greater or equal to -200.0 '
                                 'for field `db_ws004c`')
            if value > 200.0:
                raise ValueError('value need to be smaller 200.0 '
                                 'for field `db_ws004c`')

        self._db_ws004c = value

    @property
    def db_ws005c(self):
        """field `db_ws005c`

        |  Mean coincident dry-bulb temperature to wind speed corresponding to 0.50% cumulative frequency for a month

        Args:
            value (float): value for IDD Field `db_ws005c`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `db_ws005c` or None if not set
        """
        return self["db_ws005c"]

    @db_ws005c.setter
    def db_ws005c(self, value=None):
        """  Corresponds to IDD field `db_ws005c`

        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `db_ws005c`'.format(value))
            if value < -200.0:
                raise ValueError('value need to be greater or equal to -200.0 '
                                 'for field `db_ws005c`')
            if value > 200.0:
                raise ValueError('value need to be smaller 200.0 '
                                 'for field `db_ws005c`')

        self._db_ws005c = value

    @property
    def db_ws0
