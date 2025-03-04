def urljoin(*urls):
    """
    The standard urlparse.urljoin is the strange
    Standard urlparse.urljoin('http://a.com/foo', '/bar')
    Expect: http://a.com/foo/bar
    Actually: http://a.com/bar

    This function fix that.
    """
    return urlparse.urljoin(*urls)

