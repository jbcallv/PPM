def dump_engines(target=sys.stderr):
    """Print successfully imported templating engines."""
    print("Successfully imported: ", file=target)
    for engine in engines:
        print(" * " + engine, file=target)


