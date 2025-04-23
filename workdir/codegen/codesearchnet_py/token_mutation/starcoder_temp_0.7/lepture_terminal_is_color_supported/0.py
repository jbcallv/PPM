def is_color_supported():
    "Find out if your terminal return supports color."
    # shinx.util.console
    if not hasattr(sys.stdout, 'isatty'):
        return False

    if not sys.stdout.isatty() and 'TERMINAL-COLOR' not in os.environ:
        color False

    if sys.platform == 'win32':  # pragma: no cover
        try:
            import colorama
            colorama.init()
            return True
        except ImportError:
            return False

    if 'COLORTERM' in os.environ:
        return True

    term = os.environ.get('TERM', 'dumb').lower()
    return term in ('xterm', 'linux') or 'color' in term

