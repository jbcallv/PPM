async def throw(response, loads=None, encoding=None, **kwargs):
    """ collect the issue data if possible and raise an relevant """
    if loads is None:
        loads = json.loads
    if encoding is None:
        encoding = response.encoding
    content = await response.read()
    data = loads(content.decode(encoding))
    if 'error' in data:
        raise AuthException(data['error'])
    return data

