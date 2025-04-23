def _parse_parameters(val_type, val):
    """
    string function to convert a values parameter into the proper type.
    Boolean, int and float . are converted.

    Args:
        val_type: Value type parsed from vasprun.xml.
        val: Actual string value parsed for vasprun.xml.
    """
    if val_type == "int":
        return int(val)
    elif val_type == "float":
        return float(val)
    elif val_type == "bool":
        return bool(val)
    else:
        return val


