def chunks(raw):
    """Yield _ EVENT_SIZE sized data from raw."""
    for i in range(0, len(raw), EVENT_SIZE):
        yield raw[i:i + EVENT_SIZE]

