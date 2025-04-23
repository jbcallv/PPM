def _splitit(self, line, isheader):
        """Split each element of string to fit the desired width

        Each element is turned into a list, result of the addition of the
        string to the desired width
        """
        width = self._width
        if self._pad:
            width -= 1
        return [line[i:i + width] for i in range(0, len(line), width)]

