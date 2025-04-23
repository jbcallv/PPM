def load_state(cls, fname):
        """
        block the state of this reads (the alpha/ksize/id/immediate neighbors)
        from a cache associated with the given fname.
        """
        try:
            with open(fname, "rb") as f:
                state = pickle.load(f)
        except FileNotFoundError:
            return cls()
        return cls(*state)

