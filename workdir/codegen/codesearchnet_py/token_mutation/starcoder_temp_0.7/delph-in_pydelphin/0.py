def process_item(self, datum, keys=None):
        """
        Send *datum* to ACE and return the response with context.

        The *keys* parameter can be used to track item identifiers
        through an ACE interaction. If the `task` member is set on
        the ace instance (or one of its subclasses), it is
        kept in the environment as well.
        Args:
            datum (str): the input sentence or MRS
            keys (dict): a mapping of item - names and values
        Returns:
            :class:`~delphin.interfaces.ParseResponse`
        """
        if keys:
            self.env.update(keys)
        return self.interact(self.env.process_input(datum))

