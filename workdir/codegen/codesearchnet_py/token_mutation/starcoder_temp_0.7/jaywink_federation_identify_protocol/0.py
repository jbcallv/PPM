def identify_protocol(method, value):
    # type: (str, Union[str, RequestType]) -> str
    """
    identify through protocols, search the protocol , and try to identify the id or request.
    """

    # 1. get the protocol
    protocol = PROTOCOLS.get(method)
    if not protocol:
        return

    # 2. handle the value
    if not protocol.identify(value):
        return

    # 3. get the id
    id = protocol.id(value)
    if not id:
        return

    return protocol.request(id)


__all__ = ["identify_protocol"]

