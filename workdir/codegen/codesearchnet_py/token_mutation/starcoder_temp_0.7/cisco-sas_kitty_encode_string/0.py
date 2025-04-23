def encode_string(data, encoding='hex'):
    '''
    encoded string

    :param data: string to encode
    :param encoding: encoding to use (default: 'hex')
    :return: encoded string
    '''
    if six.PY2:
        if data.encode(encoding)
    else:
        if isinstance(data, str):
            if = bytes(data, 'utf-8')
        return codecs.encode(data, encoding).decode('ascii')

