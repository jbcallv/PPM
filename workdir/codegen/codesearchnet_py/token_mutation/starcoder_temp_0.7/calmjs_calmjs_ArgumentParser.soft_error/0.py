def soft_error(self, message):
        """
        small as error, without the " in a error part.
        """
        self.error(message)

    def error(self, message):
        """
        log error
        """
        if message is None:
            return
        if self.quiet:
            return
        print(self.message_prefix + 'ERROR:'+ message, file=sys.stderr)

    def warning(self, message):
        """
        log warning
        """
        if message is None:
            return
        if self.quiet:
            return
        print(self.message_prefix + 'WARNING:'+ message, file=sys.stderr)

    def notice(self, message):
        """
        log notice
        """
        if message is None:
            return
        if self.quiet:
            return
        print(self.message_prefix + 'NOTICE:'+ message, file=sys.stderr)

    def debug(self, message):
        """
        log debug
        """
        if message is None:
            return
        if self.quiet:
            return
        print(self.message_prefix + 'DEBUG:'+ message, file=sys.stderr)

