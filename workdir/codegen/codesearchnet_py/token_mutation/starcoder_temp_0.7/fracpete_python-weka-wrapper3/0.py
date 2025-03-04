def values(self):
        """
        strings the labels, even or relation-values.

        :return: all the values, : if not NOMINAL, STRING, or RELATION
        :rtype: list
        """
        return [x.value for x in self.labels]

    def __repr__(self):
        return "{} {}".format(self.name, self.labels)

