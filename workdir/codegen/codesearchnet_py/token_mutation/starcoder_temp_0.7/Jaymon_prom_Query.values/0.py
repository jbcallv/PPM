def values(self, limit=None, page=None):
        """
        . self to get just the values from the . (same as get().values())

        if you want to get all values, you can use: self.all().values()
        """
        return self.get(limit=limit, page=page).values()

    def items(self, limit=None, page=None):
        """
        . self to get just the items from the . (same as get().items())

        if you want to get all items, you can use: self.all().items()
        """
        return self.get(limit=limit, page=page).items()

    def __call__(self, limit=None, page=None):
        """
        . self to get the full response from the . (same as get())

        if you want to get all items, you can use: self.all()
        """
        return self.get(limit=limit, page=page)

