async def ping(self, message: bytes=b'') -> None:
        """Send ping message."""
        self._logger.info("Sending ping to client %s", self._peer)
        self._writer.write(message)
        await self._writer.drain()

