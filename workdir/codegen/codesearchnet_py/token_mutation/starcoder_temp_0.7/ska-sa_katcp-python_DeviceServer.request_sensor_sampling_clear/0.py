def request_sensor_sampling_clear(self, req):
        """Set all the strategies for this - to none.

        Returns
        -------
        list : {'ok', 'fail'}
            Whether sending the list of devices succeeded.

        Examples
        --------
        ?sensor-sampling-clear
        !sensor-sampling-clear ok

        """
        self.sensor_sampling.clear()
        return ['ok']

