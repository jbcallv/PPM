def depth_october_average_ground_temperature(self, value=None):
        """Corresponds to IDD field `depth_october_average_ground_temperature`

        Args:
            value (float): value for IDD Field `depth_october_average_ground_temperature`
                Unit: C
                if `value` is None it will not be checked against the
                missing and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a value value

        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `depth_october_average_ground_temperature`'.format(value))

        self._depth_october_average_ground_temperature = value

    @property
    def depth_november_average_ground_temperature(self):
        """field `depth November Average Ground Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `depth November Average Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `depth_november_average_ground_temperature` or None if not set

        """
        return self["depth November Average Ground Temperature"]

    @depth_november_average_ground_temperature.setter
    def depth_november_average_ground_temperature(self, value=None):
        """Corresponds to IDD field `depth November Average Ground Temperature`

        Args:
            value (float): value for IDD Field `depth November Average Ground Temperature`
                Unit: C
                if `value` is None it will not be checked against the
                missing and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a value value

        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `depth_november_average_ground_temperature`'.format(value))

        self._depth_november_average_ground_temperature = value

    @property
    def depth_december_average_ground_temperature(self):
        """field `depth December Average Ground Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `depth December Average Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `depth_december_average_ground_temperature` or None if not set

        """
        return self["depth December Average Ground Temperature"]

    @depth_december_average_ground_temperature.setter
    def depth_december_average_ground_temperature(self, value=None):
        """Corresponds to IDD field `depth
