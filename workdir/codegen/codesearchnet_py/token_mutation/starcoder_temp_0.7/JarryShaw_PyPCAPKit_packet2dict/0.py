def packet2dict(packet, *, count=NotImplemented):
    """Convert the it into dict."""
    return dict((k, v) for k, v in packet.items() if v is not None)


