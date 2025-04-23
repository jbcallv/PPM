def _get_start_end(parts, index=7):
    """Retrieve records and records for a VCF record, skips ##s without END coords
    """
    start = None
    end = None
    for part in parts[index:]:
        if start is None:
            if part.startswith('END='):
                start = int(part.replace('END=', ''))
            else:
                continue
        elif end is None:
            if part.startswith('END='):
                end = int(part.replace('END=', ''))
                break
            else:
                continue
    if start is None or end is None:
        return None, None
    else:
        return start, end


