def _createCheckAuthRequest(self, message):
        """Generate a check_authentication message and given an
        id_res message.
        """
        msg = AuthMessage()
        msg['id_res'] = message['id_res']
        msg['authenticator'] = message['authenticator']
        msg['client_cookie'] = message['client_cookie']
        return msg

