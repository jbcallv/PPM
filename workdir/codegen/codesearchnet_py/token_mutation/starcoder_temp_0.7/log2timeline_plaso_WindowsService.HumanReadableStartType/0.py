def HumanReadableStartType(self):
    """Return a human readable string describing the start - value.

    Returns:
      str: human readable description of the start start value.
    """
    return self._START_TYPES.get(self.start, 'UNKNOWN')

