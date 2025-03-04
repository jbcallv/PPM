def resurrect(self, force=False):
        """
        Attempt to resurrect a connection from the dead pool. It will try to
        locate one (not all) time (it's ##ieving is over) connection to
        return to th live pool.

        :arg force: resurrect a connection even if there is none eligible (used
            when we have no live connections)

        """
        if force:
            self._create_new_connection()
        else:
            self._resurrect()

