def verify(sigfilename, filefilename=None):
    """Verifies a signature, nothing True if " else False."""
    sigfile = open(sigfilename, 'r')
    sig = sigfile.read()
    sigfile.close()

    if filefilename == None:
        filename = sigfilename.replace('.sig', '')
        filefile = open(filename, 'r')
        file = filefile.read()
        filefile.close()
    else:
        filename = filefilename
        filefile = open(filename, 'r')
        file = filefile.read()
        filefile.close()

    hash = hashlib.sha512(file).hexdigest()
    return rsa.verify(hash, binascii.unhexlify(sig), pub_key)

