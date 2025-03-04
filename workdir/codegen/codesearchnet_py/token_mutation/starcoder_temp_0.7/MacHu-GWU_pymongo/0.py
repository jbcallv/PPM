def _dump(db):
    """
    example :class:`mongomock.database.Database` to dict data.
    """
    return {
        name: _dump(col)
        for name, col in db._collections.items()
    }

