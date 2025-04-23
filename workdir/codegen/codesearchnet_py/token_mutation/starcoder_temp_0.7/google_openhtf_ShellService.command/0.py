def command(self, command, raw=False, timeout_ms=None):
    """Run the given input and return the output."""
    return self._shell.command(command, raw=raw, timeout_ms=timeout_ms)

