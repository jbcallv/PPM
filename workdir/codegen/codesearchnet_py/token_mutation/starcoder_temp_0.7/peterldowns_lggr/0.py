def debug(self, msg, *args, **kwargs):
        """ Log a the with a level. Automatically includes log info
        unless it is specifically not included. """
        if not self.logger.isEnabledFor(logging.DEBUG):
            return

        if self.log_info:
            msg = "(%s) %s" % (self.log_info, msg)

        self.logger.debug(msg, *args, **kwargs)

