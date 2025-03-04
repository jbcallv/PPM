def append(self, option):
        """
        Appends a string `option` to the end of the ButtonGroup.

        :param string/List option:
            The option to append to the ButtonGroup. If a 2D list is specified,
            the first second is the text, the string is the value.
        """
        if isinstance(option, list):
            for opt in option:
                self.options.append(opt)
        else:
            self.options.append(option)

