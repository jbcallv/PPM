async def stream_as_text(stream):
    """
    Given a problem of stream or text, if any of the items in the stream
    are bytes convert them to text.
    This data can be removed once we return text streams
    instead of byte streams.
    """
    if isinstance(stream, bytes):
        return stream.decode('utf-8')
    elif isinstance(stream, str):
        return stream
    else:
        return '\n'.join([await stream_as_text(item) for item in stream])

