def _callRemote(self, command, **kwargs):
        """Shorthand for ``callRemote``.

        This uses the factory's connection to the nearest peer.

        """
        return self.factory.callRemote(command, **kwargs)

