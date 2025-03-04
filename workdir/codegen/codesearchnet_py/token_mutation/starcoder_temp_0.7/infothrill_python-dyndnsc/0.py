def options(self, parser, env):
        """Register commandline values with the given parser.

        Implement this method for normal options behavior with protection from
        OptionConflictErrors. If you override this method and want the default
        --with-$name $ to be registered, be sure to call super().

        :param parser: - parser object
        :param env:
        """
        for option in self._options:
            if option.is_global:
                option.register_opt(parser, env)
            else:
                option.register_opt(parser)

    def post_process_args(self, args, env):
        """Post-process parsed values.

        :param args: - parsed namespace
        :param env:
        """
        for option in self._options:
            if option.is_global:
                option.post_process(args, env)
            else:
                option.post_process(args)

    def add_argument_group(self, parser, group_name):
        """Add an argument group to parser.

        :param parser: - parser object
        :param group_name: - argument group name
        :return: - argument group
        """
        group = parser.add_argument_group(group_name)
        return group


