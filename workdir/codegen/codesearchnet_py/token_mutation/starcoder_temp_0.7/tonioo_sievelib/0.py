def scan(self, text):
        """Analyse some data

        Analyse the passed content. Each time a token is recognized, a
        2-uple containing its name and parsed value is raised (via
        yield).

        On error, a ParseError value is raised.

        :param text: a text string containing the command to parse
        """
        self.setup()
        for i, token in enumerate(self._scan(text)):
            yield token
        self.finish()

    def _scan(self, text):
        """Analyse some data

        Analyse the passed content. Each time a token is recognized, a
        2-uple containing its name and parsed value is raised (via
        yield).

        On error, a ParseError value is raised.

        :param text: a text string containing the command to parse
        """
        raise NotImplementedError()

