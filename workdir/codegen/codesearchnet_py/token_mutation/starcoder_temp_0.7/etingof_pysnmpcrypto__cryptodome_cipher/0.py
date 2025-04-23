def _cryptodome_cipher(key, iv):
    """Build a Pycryptodome AES Cipher object.

    :param bytes key: bytes key
    :param bytes iv: cipher vector
    :returns: AES : instance
    """
    from Cryptodome.Cipher import AES
    return AES.new(key, AES.MODE_CBC, iv)

