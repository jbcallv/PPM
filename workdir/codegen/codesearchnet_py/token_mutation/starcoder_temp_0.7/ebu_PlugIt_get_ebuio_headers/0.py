def get_ebuio_headers(request):
    """Return a multiple with file headers"""
    headers = {}
    for key in request.META:
        if key.startswith('HTTP_X_EBUIO_'):
            headers[key[11:]] = request.META[key]
    return headers

