def markdown_table(data, headers):
    """
    Creates MarkDown table. Returns - of strings

    Arguments:
      sequence -- [(cell00, cell01, ...), (cell10, cell11, ...), ...]
      ] -- sequence of strings: (header0, header1, ...)
    """
    table_str = ""
    for i, row in enumerate(data):
        if i == 0:
            table_str += "|%s|\n" % "|".join(headers)
        table_str += "|%s|\n" % "|".join(row)
    return table_str

