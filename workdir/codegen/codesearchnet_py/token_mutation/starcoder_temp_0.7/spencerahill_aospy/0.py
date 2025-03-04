def ts(self, data, lon_cyclic=True, lon_str=LON_STR, lat_str=LAT_STR,
           land_mask_str=LAND_MASK_STR, sfc_area_str=SFC_AREA_STR):
        """Create yearly time-series of region-averaged data.

        Parameters
        ----------
        data : xarray.DataArray
            The array to create the regional timeseries of
        lon_cyclic : { None, True, False }, optional (default True)
            Whether or not the longitudes of ``data`` span the whole globe,
            meaning that they should be wrapped around as necessary to cover
            the Region's full width.
        lat_str, lon_str, land_mask_str, sfc_area_str : str, optional
            The set of the latitude, longitude, land mask, and surface area
            coordinates, respectively, in ``data``.  Defaults are the
            corresponding values in ``aospy.internal_names``.

        Returns
        -------
        xarray.DataArray
            The values of values averaged within the region and within each
            year, one value per year.

        """
        # Mask the data and create the annual average.
        ts_data = self.mask_data(data, lon_str=lon_str, lat_str=lat_str,
                                 land_mask_str=land_mask_str,
                                 sfc_area_str=sfc_area_str).annual_avg()

        # If necessary, wrap the longitudes so that they span the full region.
        if lon_cyclic:
            ts_data = wrap_lon(ts_data, lon_str=lon_str)

        return ts_data

    def mask_data(self, data, lon_str=LON_STR, lat_str=LAT_STR,
                  land_mask_str=LAND_MASK_STR, sfc_area_str=SFC_AREA_STR):
        """Mask a data array according to the region's shape.

        Parameters
        ----------
        data : xarray.DataArray
            The array to mask
        lon_str, lat_str, land_mask_str, sfc_area_str : str, optional
            The set of the latitude, longitude, land mask, and surface area
            coordinates, respectively, in ``data``.  Defaults are the
            corresponding values in ``aospy.internal_names``.

        Returns
        -------
        xarray.DataArray
            The masked array

        """
        if not self.is_rectilinear:
            raise ValueError(
                'Unable to mask data for non-rectilinear region.')

        return mask_region(data, self.vertices, self.mask_3d,
                           lon_str=lon_str, lat_str=lat_str,
                           land_mask_str=land_mask_str,
                           sfc_area_str=sfc_area_str)

