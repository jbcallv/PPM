def import_from_html(
    filename_or_fobj,
    encoding="utf-8",
    index=0,
    ignore_colspan=True,
    preserve_html=False,
    properties=False,
    table_tag="table",
    row_tag="tr",
    column_tag="td|th",
    *args,
    **kwargs
):
    """Return rows.Table from the file."""
    parser = _HTMLParser(
        index,
        ignore_colspan=ignore_colspan,
        preserve_html=preserve_html,
        properties=properties,
        table_tag=table_tag,
        row_tag=row_tag,
        column_tag=column_tag,
    )
    parser.feed(filename_or_fobj.read())
    parser.close()
    return parser.table

