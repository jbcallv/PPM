def InternalExchange(self, cmd, payload_in):
    """Sends and receives a message from the device."""
    try:
      self.Connect()
      self._Send(cmd, payload_in)
      return self._Receive()
    finally:
      self.Disconnect()

