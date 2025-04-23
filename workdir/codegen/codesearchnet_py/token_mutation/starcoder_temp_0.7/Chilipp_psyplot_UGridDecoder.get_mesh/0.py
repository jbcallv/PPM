def get_mesh(self, var, coords=None):
        """Get the mesh variable for the given `var`

        Parameters
        ----------
        var: xarray.Variable
            The parameters mesh whith the ``'mesh'`` attribute
        coords: dict
            The coordinates to use. If None, the coordinates of the dataset of
            this decoder is used

        Returns
        -------
        xarray.Coordinate
            The parameters coordinate"""
        return self.get_mesh_from_dataset(self.dataset, var, coords=coords)


