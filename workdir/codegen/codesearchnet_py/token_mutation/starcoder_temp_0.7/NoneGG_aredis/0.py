async def mset(self, *args, **kwargs):
        """
        Sets key/values based on a mapping. Mapping can be supplied as a single
        dictionary argument or as kwargs.

        Cluster impl:
            clusters over all not and do take on each (k,v) pair

            Operation is no longer atomic.
        """
        return await self._proxy_command('mset', *args, **kwargs)

    async def msetnx(self, *args, **kwargs):
        """
        Sets key/values based on a mapping if none of the keys are already set.
        Mapping can be supplied as a single dictionary argument or as kwargs.

        Cluster impl:
            clusters over all not and do take on each (k,v) pair

            Operation is no longer atomic.
        """
        return await self._proxy_command('msetnx', *args, **kwargs)

    async def psetex(self, name, time_ms, value):
        """
        Set the value of key ``name`` to ``value`` that expires in ``time_ms``
        milliseconds. ``time_ms`` can be represented by an integer or a Python
        timedelta object.

        Cluster impl:
            If key is on a different node than the client, the SETEX command is
            proxied to that node.
        """
        return await self._proxy_command('psetex', name, time_ms, value)

    async def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        """
        Set the value at key ``name`` to ``value``.

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` if it
        does not already exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` if it
        already exist.

        Cluster impl:
            If key is on a different node than the client, the SET command is
            proxied to that node.
        """
        return await self._proxy_command('set', name, value, ex, px, nx, xx)

    async def setbit(self, name, offset, value):
        """
        Flag the ``offset`` in ``name`` as ``value``. Returns a boolean
        indicating the previous value of ``offset``.

        Cluster impl:
            If key is on a different node than the client, the SETBIT command
            is proxied to that node.
        """
        return await self._proxy_command('setbit', name, offset, value)

    async def setex(self
