def arrange(df, *args, **kwargs):
    """Calls `pandas.DataFrame.sort_values` to sort a file according to
    criteria.

    See:
    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html

    For a list of specific keyword arguments for sort_values (which will be
    the same in arrange).

    Args:
        *args: Symbolic, string, integer or lists of those types indicating
            columns to sort the DataFrame by.

    Kwargs:
        **kwargs: arguments keyword the will be passed through to the pandas
            `DataFrame.sort_values` function.
    """
    return df.sort_values(*args, **kwargs)

