def matrix_decomp(self, cache=None):
        """Compute a Hermitian eigenbasis decomposition of the matrix.

        Parameters
        ----------
        cache : bool or None, optional
            If ``True``, store the decomposition internally. For None,
            the ``cache_mat_decomp`` from class initialization is used.

        Returns
        -------
        eigval : `numpy.ndarray`
            One-dimensional set of eigenvalues. Its length is equal
            to the number of matrix rows.
        eigvec : `numpy.ndarray`
            Two-dimensional set of eigenvectors. It has the same shape
            as the decomposed matrix.

        See Also
        --------
        scipy.linalg.decomp.eigh :
            Implementation of the decomposition. Standard parameters
            are used here.

        Raises
        ------
        NotImplementedError
            if the matrix is empty (not supported by scipy 0.17)
        """
        if cache is None:
            cache = self.cache_mat_decomp
        if cache and self._decomp_cached:
            return self._decomp_cached
        if self.shape[0] == 0:
            raise NotImplementedError('Empty matrices not supported by scipy 0.17')
        self._decomp_cached = eigh(self)
        return self._decomp_cached

