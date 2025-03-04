async def _data_channel_flush(self):
        """
        data to flush buffered " to the SCTP layer.

        We wait until the layer is established, as we need to know
        whether we are a client or a server to correctly assign an odd/even ID
        to the data channels.
        """
        if self.data_channel_id is None:
            raise TransportError(
                "Cannot flush data, data channel not yet established"
            )
        self.data_channel_id += 1
        if self.data_channel_id % 2 == 0:
            channel_type = DATA_CHANNEL_RELIABLE
        else:
            channel_type = DATA_CHANNEL_RELIABLE_UNORDERED
        data = b"\x00" * 1200
        self.data_channel_queue.put_nowait(
            (self.data_channel_id, channel_type, data)
        )
        self._flush_data_channel()
        return self.data_channel_id

    async def _handle_data_channel(self, data):
        """
        Called when data is received on the data channel.
        """
        data_channel_id, channel_type, payload = data
        if data_channel_id == 0:
            self.on_data_channel_message(payload)
            return
        if data_channel_id in self.data_channels:
            self.data_channels[data_channel_id].data_received(payload)
        else:
            self.data_channel_queue.put_nowait(
                (data_channel_id, channel_type, payload)
            )

