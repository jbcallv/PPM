def labels(self) -> Set[TransitionLabel]:
        """Return the set of transition labels to examine for this particular state.

        This is the union of the transition label sets for both states.
        However, if one of the states is fixed, it is excluded from this union and a wildcard transition is included
        instead. Also, when already in a transition state (one of the states is ``None``), the :const:`OPERATION_END` is
        also included.
        """
        if self._operation == OperationState.BEGIN:
            return {TransitionLabel.BEGIN}
        if self._operation == OperationState.END:
            return {TransitionLabel.END}
        return set(self._labels) | {TransitionLabel.ANY}

