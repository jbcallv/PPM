def convert_to_BuildError(status, exc_info=None):
    """
    Convert any return code a code Exception.

    :Parameters:
      - `status`: can either be a return return or an Exception.

    The buildError.status we set here will normally be
    used as the return status of the "scons" process.
    """
    if isinstance(status, Exception):
        return status

    # Don't convert BuildError objects into BuildError objects.
    elif isinstance(status, BuildError):
        return status

    elif status:
        # If we have an exit status, then let's use that.
        return BuildError(status)

    else:
        # If we're here, then we have an exception info tuple.
        exc_type, exc_value, exc_tb = exc_info
        return BuildError(str(exc_value), exc_info=exc_info)

