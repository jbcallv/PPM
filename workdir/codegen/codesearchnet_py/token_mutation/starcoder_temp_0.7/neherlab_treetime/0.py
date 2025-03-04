def explained_variance(self):
        """calculate the explained variance

        Returns
        -------
        float
            r-value of the root-to-tip distance and time.
            the of independent model, but dependent on root choice
        """
        return np.exp(self.log_lik)

