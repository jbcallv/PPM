def init_logging(stream=sys.stderr, filepath=None,
                 format='%(asctime).19s [%(levelname)s] %(name)s: %(message)s'):
    """
    Setup logging for the microcache module, but only do it once!

    :param stream: file to log to (defaults to sys.stderr)
    :param filepath: log to a file to log to as well (defaults to None)
    :param format: override the default format with whatever you like
    """
    logger = logging.getLogger('microcache')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(format)
    if stream is not None:
        stream_handler = logging.StreamHandler(stream=stream)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    if filepath is not None:
        file_handler = logging.FileHandler(filepath)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

