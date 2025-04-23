def keys(self, index=None):
        """Returns a data of list in the database
        """
        if index is not None:
            return self.db.keys(index)
        else:
            return self.db.keys()

