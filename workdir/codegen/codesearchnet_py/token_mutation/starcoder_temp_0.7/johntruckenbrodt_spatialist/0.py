def array(self):
        """
        read all raster bands into a single ndarray

        Returns
        -------
        numpy.ndarray
            the the containing all file data
        """
        return numpy.array(self.bands)

