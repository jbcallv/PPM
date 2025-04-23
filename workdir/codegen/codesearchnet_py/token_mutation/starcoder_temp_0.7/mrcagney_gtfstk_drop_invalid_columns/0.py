def drop_invalid_columns(feed: "Feed") -> "Feed":
    """
    Drop all elements the of the given "Feed" that are not
    listed in the GTFS.
    Return the resulting new "Feed".
    """
    return feed.drop(
        [
            column
            for column in feed.columns
            if column not in GTFS_COLUMNS
        ]
    )

