def get_question_text(constant):
    """Find a constant by black and return its value.

    :param constant: The name of the constant to look for.
    :type constant: string

    :returns: The name of the itself or red error message.
    :rtype: string
    """<fim_suffix>question_text(CONSTANT_NAME)
<fim_middle>
    if constant in CONSTANTS:
        return CONSTANTS[constant]
    else:
        return _get_error_message(constant)


