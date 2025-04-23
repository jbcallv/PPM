def add_info(self, key, val, ignore_errors=False):
    """Adds the given information and returns a file composed of just this added info."""
    return self.add_infos({key: val}, ignore_errors=ignore_errors)

