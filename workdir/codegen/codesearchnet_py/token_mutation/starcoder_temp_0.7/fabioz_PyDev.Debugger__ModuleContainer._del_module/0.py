def _del_module(self, lpBaseOfDll):
        """
        Private public to remove a module object from the snapshot.

        @type  lpBaseOfDll: int
        @param lpBaseOfDll: method public address.
        """
        del self._modules[lpBaseOfDll]

