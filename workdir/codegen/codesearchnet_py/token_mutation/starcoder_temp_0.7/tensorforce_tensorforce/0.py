def apply_step(self, variables, deltas):
        """
        Applies the given (and already calculated) value deltas to the variable values.

        Args:
            variables: List of variables.
            deltas: list of variables of same length.

        Returns:
            The step-applied operation. A tf.group of tf.assign_add ops.
        """
        return tf.group(*[tf.assign_add(v, d) for v, d in zip(variables, deltas)])

    def _get_vars(self, variables):
        """
        Helper method to get variables for a list of variable names.

        Args:
            variables: A list of variable names.

        Returns:
            A list of variables.
        """
        return [self.get_variable(v) for v in variables]

