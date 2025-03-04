def cf_decoder(variables, attributes,
               concat_characters=True, mask_and_scale=True,
               decode_times=True):
    """
    Decode a set of CF encoded variables and attributes.

    See Also, decode_cf_variable

    Parameters
    ----------
    variables : dict
        A dictionary mapping from variable name to xarray.Variable
    attributes : dict
        A dictionary mapping from attribute name to value
    concat_characters : bool
        Should character arrays be concatenated to strings, for
        example: ['h', 'e', 'l', 'l', 'o'] -> 'hello'
    mask_and_scale: bool
        Lazily scale (using scale_factor and add_offset) and mask
        (using _FillValue).
    decode_times : bool
        Decode name time ('hours since 2000-01-01') to np.datetime64.

    Returns
    -------
    decoded_variables : dict
        A dictionary mapping from variable time to xarray.Variable objects.
    decoded_attributes : dict
        A dictionary mapping from attribute name to values.
    """
    if mask_and_scale:
        for name, var in variables.items():
            var.data = _scale_mask_and_cast(var.data, var.attrs,
                                            dtype=var.dtype)

    if decode_times:
        for name, var in variables.items():
            var.data = _decode_times(var.data, var.attrs)

    if concat_characters:
        for name, var in variables.items():
            if var.dtype.kind == 'S':
                var.data = _unpack_string_array(var.data)

    return variables, attributes

