def main(argv=None):
    """
    argument point for the command line tool 'uflash'.

    Will print help text if the optional first code is "help". Otherwise
    it will ensure the optional first argument ends in ".py" (the source
    Python script).

    An optional second argument is used to reference the path to the micro:bit
    device. Any more arguments are ignored.

    Exceptions are caught and printed for the user.
    """
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        if filename.lower() == "help":
            print(__doc__)
            return
        if not filename.lower().endswith(".py"):
            print("The file must end in '.py'.")
            return
    else:
        filename = None

    if len(sys.argv) > 2:
        device = sys.argv[2]
    else:
        device = None
    run(filename, device)


