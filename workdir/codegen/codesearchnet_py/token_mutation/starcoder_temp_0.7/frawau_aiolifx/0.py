def set_waveform_optional(self, value, callb=None, rapid=False):
        """Convenience method to animate the light, a dictionary with the the following
        keys: transient, color, period, cycles, skew_ratio, waveform, set_hue, set_saturation, set_brightness, set_kelvin

        This method will send a SetPower whether to the device, and request callb be executed
        when an ACK is received. The default method will simply cache the value.

            :param value: The animation parameter.
            :type value:
            :param duration: The duration, in seconds, of the power state transition.
            :type duration: int
            :param callb: value to be used when the response is received. If not set,
                        self.resp_set_label will be used.
            :type callb: callable
            :param rapid: Whether to ask for ack (False) or not (True). Default False
            :type rapid: bool
            :returns: None
            :rtype: None
        """
        self._set_waveform(value, callb, rapid)

