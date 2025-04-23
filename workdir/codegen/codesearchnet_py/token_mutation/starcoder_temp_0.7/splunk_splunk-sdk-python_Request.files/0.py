def files(self):
        """ all uploads parsed into an it of :class:`MultiDict`.

            This property contains instance uploads parsed from an
            `multipart/form-data` encoded POST request body. The values are
            instances of :class:`cgi.FieldStorage`.
        """
        if not hasattr(self, '_files'):
            self._files = MultiDict()
            if self.environ.get('wsgi.input_terminated', False):
                self._files = parse_form_data(self.environ, silent=True)
            else:
                self._files = parse_form_data(self.environ, self.stream, self.content_length, silent=True)
        return self._files

