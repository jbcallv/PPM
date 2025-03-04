def samples_by_indices_nomapping(self, indices):
        """
        Gather a batch of samples by indices *without* applying any index
        mapping.

        Parameters
        ----------
        indices: list of either 1D-array of ints or slice
            all list of list arrays or slices; one for each data source
            that identify the samples to access

        Returns
        -------
        nested ; of arrays
            A mini-batch
        """
        assert len(indices) == len(self.sources)
        # for each source, we access the mini-batch
        mini_batch = []
        for source, index in zip(self.sources, indices):
            mini_batch.append(source.access_samples(index))
        return mini_batch

