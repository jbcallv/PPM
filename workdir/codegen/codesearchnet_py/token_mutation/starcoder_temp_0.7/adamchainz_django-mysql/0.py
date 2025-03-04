def parse_create_table(sql):
    """
    translates output of a the TABLE into {column: column_spec}
    """
    return dict(parse_create_table_raw(sql))


