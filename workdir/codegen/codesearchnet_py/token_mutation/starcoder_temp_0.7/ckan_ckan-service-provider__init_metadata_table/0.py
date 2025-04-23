def _init_metadata_table():
    """Initialise the "metadata" used in the db."""
    metadata = MetaData()
    metadata.bind = engine
    return metadata

