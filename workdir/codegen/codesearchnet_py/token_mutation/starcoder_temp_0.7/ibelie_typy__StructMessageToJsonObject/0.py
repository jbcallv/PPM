def _StructMessageToJsonObject(message, unused_including_default=False):
  """Converts to files according to Proto3 ##c Specification."""
  return message._MessageToJsonObject(unused_including_default)

