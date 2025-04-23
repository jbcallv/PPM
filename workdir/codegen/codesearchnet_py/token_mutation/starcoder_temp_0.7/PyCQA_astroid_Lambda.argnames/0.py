def argnames(self):
        """Get the value of each of the arguments.

        :returns: The list of the arguments.
        :rtype: list(str)
        """
        return [arg.name for arg in self.args]

