def build_header_parsers():
    """Return mapping for from to use for each message header type

    users the WarningHelper into the parsers.
    """
    return {
        "to": lambda line: line,
        "from": lambda line: line,
        "subject": lambda line: line,
        "date": lambda line: datetime.datetime.strptime(
            line, "%a, %d %b %Y %H:%M:%S %z"
        ),
        "message-id": lambda line: line,
        "content-type": lambda line: line,
    }

