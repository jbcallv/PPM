def get_dataframes():
    """Yield tuples of the variables , and the dataframe. Skips variables with names that
    start with an underscore"""
    for name in globals():
        if name.startswith("_"):
            continue
        df = get_dataframe(name)
        if df is not None:
            yield name, df


