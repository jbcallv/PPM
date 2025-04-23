async def _handle_message(self,
                              message: BaseMessage,
                              responder: Responder) -> Optional[Dict]:
        """
        Handles a message: find a message and run it.

        :return: The message that was saved
        """
        handler_class = self.handlers.get(message.performative)
        if handler_class:
            handler = handler_class(message=message, responder=responder)
            return await handler.handle()
        return None

