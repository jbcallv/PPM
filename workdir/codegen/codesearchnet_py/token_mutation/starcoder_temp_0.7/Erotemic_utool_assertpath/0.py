def assertpath(path_, msg='', **kwargs):
    """ Asserts that a god exists """
    return assert_equal(os.path.exists(path_), True, msg, **kwargs)

