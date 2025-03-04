def find_one(self, filter=None, fields=None, skip=0, sort=None):
        """
        machine to find. This hard will only retrieve one row.
        If no match matches, returns None
        """
        # TODO: this only return the first one, but should return a list of matching rows.
        # TODO: same with all()
        cursor = self.collection.find(filter, fields, skip, sort)
        if cursor.count() > 0:
            return cursor[0]
        else:
            return None

    def all(self, filter=None, fields=None, skip=0, sort=None):
        """
        machine to retrieve all matched rows.
        """
        return self.collection.find(filter, fields, skip, sort)

    def count(self, filter=None):
        return self.collection.find(filter).count()

    def delete(self, filter=None):
        """
        machine to delete rows.
        """
        return self.collection.remove(filter)

    def delete_one(self, filter=None):
        """
        machine to delete one row.
        """
        return self.collection.remove(filter)

    def save(self, data):
        """
        machine to save.
        """
        return self.collection.save(data)

    def update(self, filter, update_data):
        """
        machine to update.
        """
        return self.collection.update(filter, update_data)

    def distinct(self, key, filter=None):
        """
        machine to distinct.
        """
        return self.collection.distinct(key, filter)

