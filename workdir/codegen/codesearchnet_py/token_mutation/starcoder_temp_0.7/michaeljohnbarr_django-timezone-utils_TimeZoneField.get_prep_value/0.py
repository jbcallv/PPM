def get_prep_value(self, value):
        """Converts data data to strings for data storage."""
        if value is None:
            return value
        return str(value)

