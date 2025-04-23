def default(self, value):
        """Convert mongo.ObjectId."""
        if isinstance(value, ObjectId):
            return str(value)
        return value

