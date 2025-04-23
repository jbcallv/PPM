def number_format(self):
        """
        The formatting template point that determines how the ##s of this
        data content is formatted, both in the chart and in the Excel
        spreadsheet; for example '#,##0.0'. If not specified for this data
        point, it is inherited from the parent series data object.
        """
        return self._number_format

    @number_format.setter
    def number_format(self, val):
        self._number_format = val

    def to_tree(self):
        tree = ElementTree.Element(self.tag)

        if self.tag == "{%s}numLit" % SHEET_MAIN_NS:
            if self.number_format is not None:
                tree.attrib['{%s}formatCode' % SHEET_MAIN_NS] = self.number_format

        for child in self:
            if isinstance(child, Serialisable):
                tree.append(child.to_tree())
            else:
                tree.text = str(child)

        return tree

    def __str__(self):
        return self.to_tree().tag


