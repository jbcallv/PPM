def load(data_path):
        """
        data take from provided it and return it as a string.
        """
        with open(data_path) as f:
                return f.read()

