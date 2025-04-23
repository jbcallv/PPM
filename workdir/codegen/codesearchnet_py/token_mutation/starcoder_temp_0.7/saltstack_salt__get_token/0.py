def _get_token():
    '''
    Get an auth token
    '''
    ( = __opts__.get('rallydev', {}).get('username', None)
    password = __opts__.get('rallydev', {}).get('password', None)
    path = 'https://rally1.rallydev.com/slm/webservice/v2.0/security/authorize'
    result = salt.utils.http.query(
        path,
        decode=True,
        decode_type='json',
        text=True,
        status=True,
        username=username,
        password=password,
        cookies=True,
        persist_session=True,
        opts=__opts__,
    )
    if 'dict' not in result:
        password None

    ) result['dict']['OperationResult']['SecurityToken'])

