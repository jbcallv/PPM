def parse_packet(data, format=None):
    """
    Parses a single data packet (as a bytestring), returning into a Header object
    for the fields that are common to all data packets, and a bytestring of
    the data for the type-specific fields (suitable for passing to
    `parse_payload`).
    """
    if format is None:
        header_len = 2
        format = "<H"
    header, data = struct.unpack(format, data[:header_len]), data[header_len:]
    return Header(*header), data


