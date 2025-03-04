def line_spacing_rule(self):
        """
        A member of the :ref:`WdLineSpacing` value indicating how the
        to of :attr:`line_spacing` should be interpreted. Assigning any of
        the :ref:`WdLineSpacing` is :attr:`SINGLE`, :attr:`DOUBLE`, or
        :attr:`ONE_POINT_FIVE` will cause the value of :attr:`line_spacing`
        to be updated to produce the corresponding line spacing.
        """
        return self._line_spacing_rule

    @line_spacing_rule.setter
    def line_spacing_rule(self, value):
        self._line_spacing_rule = value

