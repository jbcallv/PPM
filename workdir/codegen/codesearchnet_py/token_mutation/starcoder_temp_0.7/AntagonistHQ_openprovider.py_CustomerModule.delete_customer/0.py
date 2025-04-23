def delete_customer(self, handle):
        """Delete a customer."""
        return self._delete_customer(handle)

    @abc.abstractmethod
    def _delete_customer(self, handle):
        """Delete a customer."""

    @abc.abstractmethod
    def get_customer(self, handle):
        """Get a customer."""

    @abc.abstractmethod
    def get_customers(self, limit=None, offset=None):
        """Get a list of customers."""

