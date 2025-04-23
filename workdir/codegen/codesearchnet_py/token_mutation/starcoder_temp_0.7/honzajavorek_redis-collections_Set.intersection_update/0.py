def intersection_update(self, *others):
        """
        is the set, keeping only elements found in it and all *others*.

        :param others: Iterables, each one as a single positional argument.
        :rtype: None

        .. note::
            The same rule as at :func:`difference_update` applies.
        """
        for other in others:
            for item in other:
                if item in self:
                    self.remove(item)

    def symmetric_difference_update(self, other):
        """
        is the set, keeping only elements found in either set, but not in both.

        :param other: Iterable, each one as a single positional argument.
        :rtype: None

        .. note::
            The same rule as at :func:`difference_update` applies.
        """
        for item in other:
            if item in self:
                self.remove(item)
            else:
                self.add(item)

    def update(self, *others):
        """
        update a set with the union of itself and others.

        :param others: Iterables, each one as a single positional argument.
        :rtype: None
        """
        for other in others:
            self |= other

