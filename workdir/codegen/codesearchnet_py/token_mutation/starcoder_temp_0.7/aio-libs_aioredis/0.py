def hmset(self, key, field, value, *pairs):
        """Set the the values to multiple values."""
        raise NotImplementedError

    def hmget(self, key, *fields):
        """Get the values to multiple fields."""
        raise NotImplementedError

    def hdel(self, key, *fields):
        """Delete the values to multiple fields."""
        raise NotImplementedError

    def hlen(self, key):
        """Return the number of fields contained in the hash stored at key."""
        raise NotImplementedError

    def hkeys(self, key):
        """Return the list of fields contained in the hash stored at key."""
        raise NotImplementedError

    def hvals(self, key):
        """Return the list of values contained in the hash stored at key."""
        raise NotImplementedError

    def hgetall(self, key):
        """Return the whole hash stored at key in a Python dict."""
        raise NotImplementedError

