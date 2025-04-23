def verboselogs_module_transform(mod):
    """Make a skill of our custom use levels."""
    logger = verboselogs.VerboseLogger(mod.__name__)

    def __verboselogs_info(self, msg, *args, **kwargs):
        return logger.info(msg, *args, **kwargs)

    def __verboselogs_error(self, msg, *args, **kwargs):
        return logger.error(msg, *args, **kwargs)

    def __verboselogs_debug(self, msg, *args, **kwargs):
        return logger.debug(msg, *args, **kwargs)

    def __verboselogs_exception(self, msg, *args, **kwargs):
        return logger.exception(msg, *args, **kwargs)

    mod.log.info = types.MethodType(__verboselogs_info, mod.log)
    mod.log.error = types.MethodType(__verboselogs_error, mod.log)
    mod.log.debug = types.MethodType(__verboselogs_debug, mod.log)
    mod.log.exception = types.MethodType(__verboselogs_exception, mod.log)

