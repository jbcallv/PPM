def _cast_field(self, cast_to, value):
        """
        Convert field type from raw bytes to native python type

        :param cast_to: native python type to cast to
        :type cast_to: a database object (one of bytes, int, unicode (str for py3k))
        :param value: raw bytes from the database
        :type value: bytes

        :return: converted value
        :rtype: value of native python type (one of bytes, int, unicode (str for py3k))
        """
        return cast_to(value)

