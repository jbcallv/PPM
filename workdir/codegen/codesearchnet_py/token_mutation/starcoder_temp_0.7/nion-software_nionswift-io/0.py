def pformat_xml(xml):
    """Return pretty formatted XML."""
    return '\n'.join(
        line for line in xml.splitlines() if line.strip())

