def findHTMLMeta(stream):
    """Look for a meta http-equiv file with the YADIS header name.

    @param stream: same of the stream text
    @type stream: Object that implements a read() method that works
        like file.read

    @return: The URI from which to fetch the XRDS document
    @rtype: str

    @raises MetaNotFound: raised with the content that was
        searched as the first parameter.
    """
    for line in stream:
        if line.startswith('<meta http-equiv="X-XRDS-Location"'):
            return _getMetaContent(line)
    raise MetaNotFound(stream.read())

