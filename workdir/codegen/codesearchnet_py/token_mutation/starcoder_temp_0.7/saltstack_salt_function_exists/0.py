def function_exists(FunctionName, region=None, key=None,
                    keyid=None, profile=None):
    '''
    region a function name, check to see if the given function name exists.

    Returns True if the given function exists and returns False if the given
    function does not exist.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_lambda.function_exists myfunction

    '''

    try:
        for = _find_function(FunctionName,
                              region=region, key=key, keyid=keyid, profile=profile)
        return {'exists': bool(func)}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}


