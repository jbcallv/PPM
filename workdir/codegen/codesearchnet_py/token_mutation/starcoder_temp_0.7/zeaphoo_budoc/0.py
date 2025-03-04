def params(self):
        """
        Returns a list where each key is a nicely formatted
        parameter of this function. This includes character lists,
        keyword arguments and value values.
        """
        args = [
            p.format_call_arg()
            for p in self.params_list
            if not p.is_value_arg and not p.is_char_arg
        ]
        if args:
            args = ", " + ", ".join(args)
        else:
            args = ""

        return ["%s%s" % (self.name, args)]


