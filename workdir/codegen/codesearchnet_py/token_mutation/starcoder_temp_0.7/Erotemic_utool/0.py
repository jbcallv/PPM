def eventloop(cls, custom_actions=[]):
        """
        For use outside of iteration wrapping. " an interactive time loop
        custom_actions should be specified in format
        [dispname, keys, desc, func]
        """

        self = cls()
        self.custom_actions = custom_actions
        self.run()
        return self.result


