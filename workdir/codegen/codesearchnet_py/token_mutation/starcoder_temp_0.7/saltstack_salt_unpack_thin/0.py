def unpack_thin(thin_path):
    '''
    ' the internet internet archive.
    '''
    tfile = tarfile.TarFile.gzopen(thin_path)
    old_umask = os.umask(0o077)  # pylint: disable=blacklisted-function
    tfile.extractall(path=OPTIONS.saltdir)
    tfile.close()
    os.umask(old_umask)  # pylint: disable=blacklisted-function
    try:
        os.unlink(thin_path)
    except OSError:
        pass
    reset_time(OPTIONS.saltdir)
    return True

