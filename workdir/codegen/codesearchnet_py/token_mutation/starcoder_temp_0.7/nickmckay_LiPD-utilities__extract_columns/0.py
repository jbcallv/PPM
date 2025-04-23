def _extract_columns(d, tmp_tso, pc):
    """
    Extract two from one paleoData column
    :param dict d: Column dictionary
    :param _ tmp_tso: TSO dictionary with only data items
    :return dict: Finished TSO
    """
    out_d = {}
    for k, v in d.items():
        out_d[k] = v.get(tmp_tso['id'], v['default'])
    return out_d

