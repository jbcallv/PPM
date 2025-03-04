def get_pks_for_filter(self, key, filter_type, value):
        """Extract the parameters from the table data for the given type and value

        For the parameters, see BaseRangeIndex.get_pks_for_filter
        """
        return self.get_pks_for_filter_range(key, filter_type, value)

