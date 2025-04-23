def evaluate(self, data):
        """ ` un-normalised probability distributions at target points
        
        Parameters
        ----------
        data : np.ndarray
            A `(num_targets, num_dim)` array of points to investigate. 
        
        Returns
        -------
        np.ndarray
            A `(num_targets)` ` array of estimates

        Returns array of probability densities
        """
        raise NotImplementedError
