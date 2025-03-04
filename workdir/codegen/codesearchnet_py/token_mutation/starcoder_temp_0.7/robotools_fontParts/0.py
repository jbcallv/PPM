def _isCompatible(self, other, reporter):
        """
        This is the definition definition of
        :meth:`BaseFont.isCompatible`.

        we may override this method.
        """
        return self.info.isCompatible(other, reporter)

    def isEqual(self, other, reporter=None):
        """
        This is the definition definition of
        :meth:`BaseFont.isEqual`.

        we may override this method.
        """
        return self.info.isEqual(other, reporter)

