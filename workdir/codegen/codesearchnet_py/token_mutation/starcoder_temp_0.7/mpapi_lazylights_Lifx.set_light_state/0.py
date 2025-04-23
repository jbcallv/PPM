def set_light_state(self, hue, saturation, brightness, kelvin,
                        bulb=ALL_BULBS, timeout=None):
        """
        Sets the color values of one or more bulbs.

        Hue is a float from 0 to 360, saturation and brightness are floats from
        0 to 1, and kelvin is an integer.
        """
        payload = {'hue': hue,'saturation': saturation, 'brightness': brightness, 'kelvin': kelvin}
        self._send_cmd(payload, bulb, timeout)

    def set_light_state_and_transition(self, hue, saturation, brightness, kelvin,
                            duration, bulb=ALL_BULBS, timeout=None):
        """
        Sets the color values of one or more bulbs.

        Hue is a float from 0 to 360, saturation and brightness are floats from
        0 to 1, and kelvin is an integer.
        """
        payload = {'hue': hue,'saturation': saturation, 'brightness': brightness, 'kelvin': kelvin, 'duration': duration}
        self._send_cmd(payload, bulb, timeout)

