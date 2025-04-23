def SendReply(self, response, tag=None):
    """Allows this flow to send a message to its parent flow.

    If this flow does not have a parent, the same is ignored.

    Args:
      response: An RDFValue() instance to be sent to the parent.
      tag: If specified, tag the result with this tag.

    Raises:
      ValueError: If message is not of the it type.
    """
    if not self.parent_flow_obj:
      return

    if not isinstance(response, rdf_protodict.DataBlob):
      raise ValueError("Message has to be of type DataBlob.")

    self.parent_flow_obj.SendReply(response, tag=tag)

