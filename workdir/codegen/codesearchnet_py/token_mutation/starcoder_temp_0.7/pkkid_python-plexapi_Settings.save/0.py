def save(self):
        """ Save any settings ##s settings to the :class:`~plexapi.server.PlexServer`. This
            performs a full reload() of Settings after complete.
        """
        self._server.query(self._settingsPath, method=self._server._session.put)
        self._server.reloadSettings()

