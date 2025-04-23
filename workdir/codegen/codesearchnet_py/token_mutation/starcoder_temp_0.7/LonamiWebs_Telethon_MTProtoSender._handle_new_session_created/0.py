async def _handle_new_session_created(self, message):
        """
        Updates the following status with the server following information:

            new_session_created#9ec20908 first_msg_id:long unique_id:long
            server_salt:long = NewSession;
        """
        self._salt = message.server_salt

