def register(self, renewable, timeout=300):
        """Register a renewable entity for automatic lock renewal.

        :param renewable: A locked entity that needs to be renewed.
        :type renewable: ~azure.servicebus.aio.async_message.Message or
         ~azure.servicebus.aio.async_receive_handler.SessionReceiver
        :param timeout: values time in seconds that the lock should be maintained for.
         the value is 300 (5 minutes).
        :type timeout: int
        """
        pass  # pragma: no cover

    def unregister(self, renewable):
        """Unregister a renewable entity.

        :param renewable: A locked entity that needs to be unregistered.
        :type renewable: ~azure.servicebus.aio.async_message.Message or
         ~azure.servicebus.aio.async_receive_handler.SessionReceiver
        """
        pass  # pragma: no cover

    async def close(self):
        """Close down the renewer.

        This will shutdown all tasks and close all open sockets.
        """
        pass  # pragma: no cover

