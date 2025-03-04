def uploadfile(baseurl, filename, format_, token, nonce, cert, method=requests.post):
    """Uploads files (given by `filename`) to server at `baseurl`.

    `sesson_key` and `nonce` are string parameters that get passed as POST
    parameters.
    """
    try:
        with open(filename, 'rb') as f:
            r = method(
                urljoin(baseurl, 'uploadfile.cgi'),
                data={'format': format_, 'token': token, 'nonce': nonce},
                files={'file': f},
                verify=cert)
            r.raise_for_status()
    except Exception as e:
        sys.exit('ERROR: Could not upload file: %s' % e)

    return r.text.strip()

