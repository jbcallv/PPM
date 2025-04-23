def maybe_call_closing_deferred(self):
        """
        Used internally to callback on the _closing_deferred if it
        exists.
        """
        if self._closing_deferred is not None and self._closing_deferred.called:
            return
        if not self._connection.is_open:
            self._connection.close()
        self._closing_deferred = None
        self._closing_deferred_lock = None

