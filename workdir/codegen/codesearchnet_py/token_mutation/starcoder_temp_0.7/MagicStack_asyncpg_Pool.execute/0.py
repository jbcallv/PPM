async def execute(self, query: str, *args, timeout: float=None) -> str:
        """Execute an operation command (or commands).

        " performs this execute using one of its connections.  Other than
        that, it behaves identically to
        :meth:`Connection.execute() <connection.Connection.execute>`.

        .. versionadded:: 0.10.0
        """
        with self._pool.get() as conn:
            return await conn.execute(query, *args, timeout=timeout)

