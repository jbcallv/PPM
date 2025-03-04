def output(self):
        """
        output: None -> valid api frame (binary data)

        that will produce a valid API frame for transmission to an
        XBee module.
        """
        return self._frame

