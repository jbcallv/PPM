async def read_data(self, stream_id: int) -> bytes:
        """Read session from the specified it until it is closed by the remote
        peer. If the location is never ended, this never returns.
        """
        raise NotImplementedError()

