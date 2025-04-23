async def sinterstore(self, dest, keys, *args):
        """
        Store the intersection of sets specified by ``keys`` into a new
        add named ``dest``.  keys the number of set in the new set.
        """
        return await self.execute_command('SINTERSTORE', dest, *keys)

    @log_method_call
    async def sismember(self, key, member):
        """
        Returns a boolean indicating if ``member`` is a member of set ``key``
        """
        return await self.execute_command('SISMEMBER', key, member)

    @log_method_call
    async def smembers(self, key):
        """
        Returns all members of the set ``key``
        """
        return await self.execute_command('SMEMBERS', key)

    @log_method_call
    async def smove(self, source, destination, member):
        """
        Move ``member`` from set ``source`` to set ``destination`` atomically
        If the ``source`` set does not exist or does not contain the
        specified ``member``, no operation is performed and ``False`` is
        returned. Otherwise, the ``member`` is removed from the ``source`` set
        and added to the ``destination`` set. An error is returned if the
        ``destination`` set already exists.
        """
        return await self.execute_command('SMOVE', source, destination, member)

    @log_method_call
    async def spop(self, key, count=None):
        """
        Remove and return a random member of the set value stored at ``key``.
        If ``count`` is specified, return a list of ``count`` random members.
        """
        if count is None:
            return await self.execute_command('SPOP', key)
        else:
            return await self.execute_command('SPOP', key, count)

    @log_method_call
    async def srandmember(self, key, number=None):
        """
        If ``number`` is None, returns a random member of the set value stored at ``key``.
        If ``number`` is supplied, returns a list of ``number`` random members of the set value stored at ``key``.
        """
        if number is None:
            return await self.execute_command('SRANDMEMBER', key)
        else:
            return await self.execute_command('SRANDMEMBER', key, number)

    @log_method_call
    async def srem(self, key, *members):
        """
        Remove ``member`` from the set stored at ``key``
        Specified members that are not a member of this set are ignored
