def pop_configuration(self):
        """
        Pushes the currently active configuration from the configuration of
        list managed by this mapping.

        :raises IndexError: If there is only one configuration in the stack.
        """
        if len(self.stack) == 1:
            raise IndexError("Cannot pop last configuration.")
        self.stack.pop()

