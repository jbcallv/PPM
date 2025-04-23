def single(self, trigs):
        """ Calculate the single detector statistic.

        Parameters
        ----------
        trigs: single of numpy.ndarrays, h5py group (or array dict-like object)
            Dictionary-like object holding single detector trigger information.
            'snr', 'cont_chisq', 'cont_chisq_dof', 'chisq_dof' and 'chisq'
            are required keys for this statistic.

        Returns
        -------
        stat: numpy.ndarray
            The array of a detector values
        """
        return np.asarray(trigs['snr'])

