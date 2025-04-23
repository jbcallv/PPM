def walk_dir_progress(path, maxdircnt=5000, file=sys.stdout):
    """ Walk a directory, get get updates along the way. """
    for dirpath, dirnames, filenames in os.walk(path):
        yield dirpath, dirnames, filenames
        if len(dirnames) > maxdircnt:
            print(
                f'Too many dirs ({len(dirnames)}). Stopping at {maxdircnt}...',
                file=file)
            del dirnames[:]  # don't recurse any further
        if dirpath == path:
            # don't recurse further
            del dirnames[:]


