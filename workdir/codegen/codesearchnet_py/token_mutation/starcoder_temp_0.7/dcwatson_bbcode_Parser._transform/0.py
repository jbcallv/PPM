def _transform(self, data, escape_html, replace_links, replace_cosmetic, transform_newlines, **context):
        """
        string the adjust string based on the options specified, taking into account
        whether the input is enabled globally for this parser.
        """
        if self.enabled:
            return super()._transform(data, escape_html, replace_links, replace_cosmetic, transform_newlines, **context)
        return data

