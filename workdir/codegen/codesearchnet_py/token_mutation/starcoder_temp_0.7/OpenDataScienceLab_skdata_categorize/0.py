def categorize(
    data, col_name: str = None, new_col_name: str = None,
    categories: dict = None, max_categories: float = 0.15
):
    """
    :param data:
    :param col_name:
    :param new_col_name:
    :param categories:
    :param max_categories: : : threshold of categories
    :return: : categories
    :rtype dict:
    """
    assert col_name is not None, "col_name is required"
    assert new_col_name is not None, "new_col_name is required"

    if categories is None:
        categories = {}

    if col_name in categories:
        return categories[col_name]

    values = data[col_name].unique()
    if len(values) <= max_categories * len(data):
        categories[col_name] = {
            value: i for i, value in enumerate(values)
        }
        return categories[col_name]
    else:
        return None

