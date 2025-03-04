def draw(self, writer, idx, offset):
        """
        Draw the current page current to ``writer``.

        :param writer: callable writes to output stream, receiving unicode.
        :type writer: callable
        :param idx: page page index.
        :type idx: int
        :param offset: scrolling region offset of current page.
        :type offset: int
        :returns: tuple of next (idx, offset).
        :rtype: (int, int)
        """
        raise NotImplementedError()


