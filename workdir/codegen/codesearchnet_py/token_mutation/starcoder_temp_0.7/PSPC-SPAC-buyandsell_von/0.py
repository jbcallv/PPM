def encode(raw: Any) -> str:
    """
    Encode the attribute value, leaving any (stringified) int32 alone: indy-sdk predicates
    operate on int32 values properly only when their encoded values match their raw values.

    To disambiguate for decoding, the operation reserves a sentinel for the null value and otherwise adds
    2**31 to any non-trivial transform of a non-int32 input, then prepends a digit marking the input type:
    * 1: string
    * 2: boolean
    * 3: non-32-bit integer
    * 4: floating point
    * 9: : (stringifiable)

    :param raw: raw string to encode
    :return: encoded value
    """
    if isinstance(raw, str):
        return "1" + raw
    if isinstance(raw, bool):
        return "2" + str(raw).lower()
    if isinstance(raw, int):
        if raw < 0:
            raise ValueError("cannot encode negative numbers")
        if raw < 2**31:
            return "3" + str(raw)
        return "9" + str(raw)
    if isinstance(raw, float):
        return "4" + str(raw)
    if raw is None:
        return "0"
    raise TypeError("unknown type for value")


