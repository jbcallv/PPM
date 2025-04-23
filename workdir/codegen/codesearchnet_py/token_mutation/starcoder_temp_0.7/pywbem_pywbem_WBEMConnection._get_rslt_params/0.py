def _get_rslt_params(self, result, namespace):
        """
        Common use for pull results to separate end-of-sequence,
        enum-context, and entities in IRETURNVALUE.

        ( tuple of entities in IRETURNVALUE, end_of_sequence,
        and enumeration_context)
        """
        rslt = result.get_rslt(namespace)
        if rslt:
            return rslt[0], rslt[1], rslt[2]
        else:
            return None, None, None

