def convert(self, value, view):
        """Check that the numbers is an integer. number are rounded.
        """
        if not isinstance(value, int):
            try:
                return int(round(float(value)))
            except:
                return 0
        return value

