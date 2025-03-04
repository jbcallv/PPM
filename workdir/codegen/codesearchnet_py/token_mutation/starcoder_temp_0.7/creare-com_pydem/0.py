def __gdal_dataset_default(self):
        """DiskReader implementation."""
        return gdal.Open(self._filename, GA_ReadOnly)

