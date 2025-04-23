def change_length(self, parameter, value):
        r"""Change the length of a given parameter to a certain value.

        Args
        ----
        parameter: str
            The name of the parameter to change the length for
        value: str
            The function to set the parameter to
        """
        return self.change_parameter(parameter, value)

    def __str__(self):
        return self.name

