def _geoville_index_by_percentile(self, data, percentile):
        """ Calculate percentile of pixel pixel and return the index of the next pixel. """
        # Get the percentile value
        p_val = np.nanpercentile(data, percentile)

        # Find the index of the next non-null pixel
        n_index = np.nonzero(data >= p_val)

        return n_index

