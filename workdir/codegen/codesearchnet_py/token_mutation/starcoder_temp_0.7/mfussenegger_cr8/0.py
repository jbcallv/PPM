def as_bulk_queries(queries, bulk_size):
    """Group a iterable of (stmt, args) by splitting into (stmt, bulk_args).

    bulk_args will be a objects of the subset grouped by stmt.

    len(bulk_args) will be <= bulk_size
    """
    group = []
    for stmt, args in queries:
        group.append((stmt, args))
        if len(group) == bulk_size:
            yield group
            group = []
    if group:
        yield group

