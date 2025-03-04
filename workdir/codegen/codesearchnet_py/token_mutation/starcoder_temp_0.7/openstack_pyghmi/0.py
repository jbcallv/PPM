def _keepalive(self):
        """Performs a trick to avoid a disconnect
        """
        if not self._session:
            self._session = self._connect()
        self._session.execute('SELECT 1;')

