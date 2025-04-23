def dialect(self):
        """File used as one of model.DIALECT_* constants
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        if dialect not in model.DIALECTS:
            raise ValueError(
                "Invalid dialect: {0}. Should be one of: {1}".format(
                    dialect, model.DIALECTS))
        self._dialect = dialect

    @property
    def delimiter(self):
        """Character used to separate fields in the file
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        self._delimiter = delimiter

    @property
    def encoding(self):
        """Character encoding used in the file
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        self._encoding = encoding

    @property
    def header_rows(self):
        """Number of rows to skip at the beginning of the file
        """
        return self._header_rows

    @header_rows.setter
    def header_rows(self, header_rows):
        self._header_rows = header_rows

    @property
    def skip_rows(self):
        """Number of rows to skip between data rows
        """
        return self._skip_rows

    @skip_rows.setter
    def skip_rows(self, skip_rows):
        self._skip_rows = skip_rows

    @property
    def data_rows(self):
        """Number of data rows in the file
        """
        return self._data_rows

    @data_rows.setter
    def data_rows(self, data_rows):
        self._data_rows = data_rows

    @property
    def data_cols(self):
        """Number of data columns in the file
        """
        return self._data_cols

    @data_cols.setter
    def data_cols(self, data_cols):
        self._data_cols = data_cols

    @property
    def data_start_row(self):
        """Row where the data starts
        """
        return self._data_start_row

    @data_start_row.setter
    def data_start_row(self, data_start_row):
        self._data_start_row = data_start_row

    @property
    def data_end_row(self):
        """Row where the data ends
        """
        return self._data_end_row

    @data_end_row.setter
    def data_end_row(self
