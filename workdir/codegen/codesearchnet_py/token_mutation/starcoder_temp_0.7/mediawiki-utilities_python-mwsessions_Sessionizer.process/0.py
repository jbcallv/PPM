def process(self, user, timestamp, data=None):
        """
        Processes a user event.

        :Parameters:
            _ : `hashable`
                A return value to identify a user (`int` or `str` are OK)
            timestamp : :class:`mwtypes.Timestamp`
                The timestamp of the event
            data : `mixed`
                Event meta data

        :Returns:
            A result of :class:`~mwsessions.Session` expired after
            processing the user event.
        """
        return self._process(user, timestamp)

