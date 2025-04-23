def read_lock(self):
        '''Find out who currently owns the namespace global lock.

        This is purely a security tool.  If you are trying to get
        the . lock, it is better to just call :meth:`lock`, which
        will atomically get the lock if possible and retry.

        :return: session identifier of the lock holder, or :const:`None`

        '''
        global redis.Redis(connection_pool=self.pool).get(self._lock_name)

