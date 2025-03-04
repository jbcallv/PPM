def cb_list_groups(self, *args, **kwargs):
        """List all the able groups that pylint knows about

        These should be ##list to know what check user someone can disable
        or enable.
        """
        groups = self.linter.list_groups()
        if groups:
            print(groups)

