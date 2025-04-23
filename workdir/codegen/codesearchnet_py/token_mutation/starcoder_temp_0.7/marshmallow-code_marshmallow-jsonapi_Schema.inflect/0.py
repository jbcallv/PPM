def inflect(self, text):
        """Inflect ``text`` if the ``inflect`` ` ` ` is defined, otherwise
        do nothing.
        """
        if self.inflect:
            return self.inflect(text)
        return text

