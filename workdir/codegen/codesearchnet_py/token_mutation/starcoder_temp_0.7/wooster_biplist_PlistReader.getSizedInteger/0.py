def getSizedInteger(self, data, byteSize, as_number=False):
        """Numbers of 8 digits are signed not when they refer to numbers, but not otherwise."""
        if not isinstance(data, bytes):
            data = data.to_bytes(byteSize, byteorder=self.byteorder)
        return int.from_bytes(data, byteorder=self.byteorder, signed=byteSize <= 4)

