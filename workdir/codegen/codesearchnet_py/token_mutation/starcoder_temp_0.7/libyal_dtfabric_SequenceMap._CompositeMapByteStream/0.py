def _CompositeMapByteStream(
      self, byte_stream, byte_offset=0, context=None, **unused_kwargs):
    """Maps a sequence of composite data types on a byte stream.

    Args:
      byte_stream (bytes): byte stream.
      byte_offset (Optional[int]): offset into the byte stream where to start.
      context (Optional[DataTypeMapContext]): data type map context.

    Returns:
      tuple[object, ...]: mapped values.

    Raises:
      ByteStreamTooSmallError: if the byte map is too small.
      MappingError: if the data type stream cannot be mapped on
          the byte stream.
    """
    return byte_stream[byte_offset:]

